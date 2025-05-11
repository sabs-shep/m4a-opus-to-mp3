# ConvertTomp3

A lightweight tool to batch convert `.opus` and `.m4a` audio files into `.mp3`.  
Converted files are saved in a subfolder called `mp3s`, and any failed conversions are logged.

## 📦 Features

- Supports `.opus` and `.m4a` files
- Skips files already converted
- Creates a `conversion_errors.txt` log
- Requires **no installation** when compiled
- Uses local `ffmpeg.exe` (no need for PATH setup)

---

## 🔧 Setup

1. **Download `ffmpeg.exe`**  
   - From: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
   - Place `ffmpeg.exe` in the same folder as this project.

2. **Run the app**
   - If using source code:
     ```
     python main.py
     ```
   - If using the compiled `.exe`:
     Just double-click `ConvertTomp3.exe`

---

## 📝 How to Use

1. Launch the program
2. Follow the command-line instructions
3. Select the folder that contains your `.opus` or `.m4a` files
4. The app will:
   - Convert each file to `.mp3`
   - Save them to `mp3s/`
   - Log any failed conversions in `conversion_errors.txt`

---

# 📥 Download the Latest Release

You can download the latest version of the app from the [Releases Page](https://github.com/sabs-shep/m4a-opus-to-mp3/releases).

---

## 🛠 Build It Yourself

To create a standalone `.exe` (requires Python and [PyInstaller](https://pyinstaller.org)):

```bash
pip install pyinstaller
pyinstaller --onefile --add-binary "ffmpeg.exe;." main.py
