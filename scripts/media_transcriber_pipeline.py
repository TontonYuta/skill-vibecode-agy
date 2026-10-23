#!/usr/bin/env python3
"""
scripts/media_transcriber_pipeline.py
Kịch bản Hacker Media Engineering:
1. Tải siêu tốc thông tin metadata, thumbnail và subtitle từ video YouTube qua yt-dlp.
2. Dùng ffmpeg trích xuất luồng âm thanh sạch 16kHz mono WAV (chuẩn đầu vào tối ưu cho Whisper).
3. Hỗ trợ cắt đoạn trích xuất audio (--download-sections) mà không cần tải cả video 4K nặng nề.
"""

import subprocess
import sys
import os
import json
import argparse

def get_media_info(url):
    print(f"[*] Đang bóc tách metadata từ URL: {url}...")
    cmd = ["yt-dlp", "--dump-json", "--no-playlist", url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(res.stdout)
        info = {
            "title": data.get("title"),
            "duration_seconds": data.get("duration"),
            "uploader": data.get("uploader"),
            "view_count": data.get("view_count"),
            "subtitles": list(data.get("subtitles", {}).keys()),
            "auto_subtitles": list(data.get("automatic_captions", {}).keys()),
            "formats_count": len(data.get("formats", []))
        }
        print(f"✅ [Metadata Extracted]")
        print(f"   - Tiêu đề: {info['title']}")
        print(f"   - Thời lượng: {info['duration_seconds']}s")
        print(f"   - Kênh: {info['uploader']}")
        print(f"   - Phụ đề có sẵn: {', '.join(info['subtitles'][:5]) if info['subtitles'] else 'Không có'}")
        print(f"   - Phụ đề tự sinh (Auto-cap): {', '.join(info['auto_subtitles'][:5]) if info['auto_subtitles'] else 'Không có'}")
        return data, info
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi yt-dlp: {e.stderr.strip()[:200]}")
        return None, None

def download_audio_for_whisper(url, output_wav="audio_16k.wav", section=None):
    """
    Sử dụng kết hợp yt-dlp và FFmpeg để:
    - Bóc tách đúng luồng audio tốt nhất.
    - Ép chuẩn sang 16kHz, mono, PCM s16le (chuẩn vàng để nạp vào Whisper AI).
    - Cắt đúng section mong muốn (ví dụ: '*01:00-02:30') để tiết kiệm băng thông.
    """
    print(f"[*] Đang tải và nén audio chuẩn Whisper vào: {output_wav}...")
    cmd = [
        "yt-dlp",
        "-x", # Chỉ lấy audio
        "--audio-format", "wav",
        "--postprocessor-args", "ffmpeg:-ar 16000 -ac 1 -c:a pcm_s16le", # Ép xung ffmpeg 16kHz mono
        "-o", output_wav,
        "--force-overwrites",
        "--no-playlist"
    ]
    if section:
        cmd.extend(["--download-sections", section])
        print(f"   ✂️ Chỉ tải phân đoạn: {section}")
        
    cmd.append(url)
    
    try:
        subprocess.run(cmd, check=True)
        if os.path.exists(output_wav):
            size_kb = os.path.getsize(output_wav) // 1024
            print(f"✅ Đã trích xuất audio thành công: {output_wav} ({size_kb} KB)")
            return True
        else:
            print("[-] Không tìm thấy tệp audio sau khi chạy.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi khi tải/xử lý audio: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Media Transcriber Pipeline for Vibecoding")
    parser.add_argument("url", help="URL video YouTube / TikTok / Facebook")
    parser.add_argument("--info-only", action="store_true", help="Chỉ trích xuất metadata và danh sách phụ đề")
    parser.add_argument("--section", help="Phân đoạn cần cắt (ví dụ: '*00:00-01:00')")
    parser.add_argument("--out", default="extracted_audio.wav", help="Đường dẫn lưu tệp audio WAV 16kHz")
    
    args = parser.parse_args()
    raw_data, info = get_media_info(args.url)
    
    if not args.info_only and info:
        download_audio_for_whisper(args.url, output_wav=args.out, section=args.section)
