import os
import subprocess

def convert_audio_to_mp3(folder_path, ffmpeg_path):
    output_folder = os.path.join(folder_path, "mp3s")
    os.makedirs(output_folder, exist_ok=True)

    error_log = os.path.join(folder_path, "conversion_errors.txt")
    errors = []

    print(f"\n📁 Input folder: {folder_path}")
    print(f"📁 Output folder: {output_folder}\n")

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".opus", ".m4a")):
            input_path = os.path.join(folder_path, filename)
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(output_folder, output_filename)

            if os.path.exists(output_path):
                print(f"⏭️  Skipping '{filename}' (already converted)")
                continue

            print(f"🔄 Converting '{filename}'...")

            result = subprocess.run(
                [ffmpeg_path, "-i", input_path, output_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )

            if result.returncode != 0:
                print(f"❌ Failed to convert '{filename}'")
                errors.append(filename)
            else:
                print(f"✅ Converted '{filename}'")

    if errors:
        with open(error_log, "w") as log_file:
            for item in errors:
                log_file.write(f"Failed to convert: {item}\n")
        print(f"\n⚠️  Conversion completed with {len(errors)} error(s). See 'conversion_errors.txt'.")
    else:
        print("\n✅ All files converted successfully!")

def main():
    print("🎵 MP3 Converter (opus/m4a → mp3)")
    print("----------------------------------")
    print("📌 Instructions:")
    print("1. Place this program and ffmpeg.exe in the same folder.")
    print("2. Press Enter to select the folder with .opus/.m4a files.")
    input("👉 Press Enter to choose the input folder...")

    import tkinter as tk
    from tkinter import filedialog
    tk.Tk().withdraw()
    folder = filedialog.askdirectory(title="Select Folder with .opus/.m4a Files")

    if not folder:
        print("❌ No folder selected. Exiting.")
        return

    ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
    if not os.path.exists(ffmpeg_path):
        print("❌ ffmpeg.exe not found in script folder.")
        return

    convert_audio_to_mp3(folder, ffmpeg_path)

    input("\n✅ Done. Press Enter to exit...")

if __name__ == "__main__":
    main()
