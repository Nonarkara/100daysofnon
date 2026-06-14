#!/usr/bin/env python3
"""
Generate Chapter 1 narration using OmniVoice voice cloning.

Usage:
    python generate_ch1_voice.py --ref /path/to/your-voice.wav

The script:
  1. Loads OmniVoice on MPS (M5 Max)
  2. Clones the voice from the reference clip (auto-transcribes with Whisper)
  3. Generates each paragraph of Chapter 1 separately
  4. Concatenates all clips into one MP3

Output: site/assets/artifacts/ch1-narration-cloned.mp3
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
import numpy as np
import soundfile as sf
import torch

ROOT = Path(__file__).parent


def load_ch1_paragraphs():
    with open(ROOT / "data" / "two-layers.json", encoding="utf-8") as f:
        data = json.load(f)
    return data["chapters"][0]["simulation"]["paragraphs"]["en"]


def generate(ref_audio: str):
    print("Loading OmniVoice on MPS…")
    from omnivoice import OmniVoice

    model = OmniVoice.from_pretrained(
        "k2-fsa/OmniVoice",
        device_map="mps",
        dtype=torch.float16,
    )

    paras = load_ch1_paragraphs()
    print(f"{len(paras)} paragraphs to narrate")

    # Trim reference to 8 seconds if it's longer
    ref_path = Path(ref_audio)
    ref_wav = ROOT / ".venv-omnivoice" / "ref_trimmed.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(ref_path), "-t", "8", "-ar", "24000",
         "-ac", "1", str(ref_wav)],
        check=True, capture_output=True,
    )
    print(f"Reference clip: {ref_wav}")

    clips = []
    silence = np.zeros(int(0.45 * 24000))  # 450ms silence between paragraphs

    for i, para in enumerate(paras, 1):
        print(f"  [{i}/{len(paras)}] {para[:60]}…")
        audio = model.generate(
            text=para,
            ref_audio=str(ref_wav),
            # ref_text omitted — Whisper auto-transcribes
        )
        clips.append(audio[0])
        clips.append(silence)

    combined = np.concatenate(clips)

    wav_out = ROOT / "site" / "assets" / "artifacts" / "ch1-narration-cloned.wav"
    sf.write(str(wav_out), combined, 24000)
    print(f"WAV written: {wav_out}")

    mp3_out = wav_out.with_suffix(".mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(wav_out), "-codec:a", "libmp3lame",
         "-b:a", "128k", str(mp3_out)],
        check=True, capture_output=True,
    )
    wav_out.unlink()  # remove intermediate WAV
    print(f"\nDone → {mp3_out}")
    duration_s = len(combined) / 24000
    print(f"Duration: {duration_s/60:.1f} min")
    return mp3_out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", required=True,
                        help="Path to 5–10s reference audio of your voice (WAV/MP3/M4A)")
    args = parser.parse_args()
    generate(args.ref)
