
import argparse
from pathlib import Path
from faster_whisper import WhisperModel
from tqdm import tqdm

def write_txt(segments, out_txt):
    with open(out_txt, "w", encoding="utf-8") as f:
        for s in segments:
            f.write(s.text.strip() + "\n")

def format_ts(seconds: float) -> str:
    # SRT timestamp format: HH:MM:SS,mmm
    ms = int((seconds - int(seconds)) * 1000)
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def write_srt(segments, out_srt):
    with open(out_srt, "w", encoding="utf-8") as f:
        for i, s in enumerate(segments, start=1):
            f.write(f"{i}\n")
            f.write(f"{format_ts(s.start)} --> {format_ts(s.end)}\n")
            f.write(s.text.strip() + "\n\n")

def main():
    ap = argparse.ArgumentParser(description="Transcribe audio/video to text & SRT")
    ap.add_argument("input", help="Path to audio/video file (mp3, m4a, wav, mp4, etc.)")
    ap.add_argument("--model", default="small", 
                    help="Whisper size: tiny | base | small | medium | large-v3 (bigger = better but slower)")
    ap.add_argument("--language", default=None, 
                    help="Force language code (e.g., 'es', 'en'). Default: auto-detect")
    ap.add_argument("--beam-size", type=int, default=5, help="Decoding beam size (quality vs speed)")
    ap.add_argument("--vad", action="store_true", help="Enable voice activity detection (can help on noisy files)")
    args = ap.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        raise FileNotFoundError(in_path)

    # Choose compute type automatically
    # Options: "int8", "int8_float16", "float16", "float32" (float16 needs GPU)
    # model = WhisperModel(args.model, compute_type="int8_float16")
    model = WhisperModel(args.model, device="cpu", compute_type="int8")  # o "float32"

    print(f"Transcribing: {in_path.name} with model '{args.model}'...")
    segments, info = model.transcribe(
        str(in_path),
        language=args.language,
        beam_size=args.beam_size,
        vad_filter=args.vad
    )

    segments = list(segments)  # exhaust generator to reuse

    # Outputs
    out_base = in_path.with_suffix("")  # remove extension
    out_txt = out_base.with_suffix(".txt")
    out_srt = out_base.with_suffix(".srt")

    # Progress (optional)
    for _ in tqdm(segments, desc="Writing output"):
        pass

    write_txt(segments, out_txt)
    write_srt(segments, out_srt)

    print(f"\nLanguage: {info.language} (prob {info.language_probability:.2f})")
    print(f"Saved: {out_txt.name} and {out_srt.name}")

if __name__ == "__main__":
    main()
