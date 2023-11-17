# Nightcore Creator

This Python script automatically generates Nightcore versions of songs. It takes the most recently added song from an `/input` directory, speeds it up, adjusts its pitch, and saves the transformed song in an `/output` directory with the prefix "Nightcore - " in the filename.

## Features

- Automatically selects the latest MP3 file from the `/input` folder.
- Adjusts the speed and pitch of the selected song.
- Saves the transformed song in the `/output` folder with an updated name.
- Maintains the original song's bitrate in the Nightcore version.

## Requirements

- Python 3
- PyDub
- Sox (with MP3 support)

## Installation

### Python and PyDub

Ensure Python 3 is installed on your system. Install PyDub using pip:

```bash
pip install pydub
```
### Sox Installation

Install Sox:

- **Linux**: Use your distribution's package manager. For example, on Debian/Ubuntu-based systems:
- 
  ```bash
  sudo apt-get install sox
  sudo apt-get install libsox-fmt-mp3
  ```
- **Windows**: Download from [SoX - Sound eXchange.](https://sourceforge.net/projects/sox/)
- **MacOS**: Install using Homebrew:
- 
  ```bash
  brew install sox
  ```

## Usage

1. Place the MP3 files you want to transform into the `/input` folder.

2. Run the script from the command line with two parameters:
   - Speed increase factor (e.g., `1.25` for a 25% increase)
   - Pitch shift in semitones (can be fractional, e.g., `2.5`)

  ```bash
   python script.py 1.25 2.5
  ```

   The script will process the most recently added song in the `/input` folder. It will increase the song's speed by the specified factor and adjust the pitch by the specified number of semitones, thereby creating a Nightcore version of the track.

## Output

- The transformed song will be saved in the `/output` folder.
- The output filename will be formatted as "Nightcore - [Original Song Name].mp3", where "[Original Song Name]" is the name of the original file.

## Notes

- Ensure that the `/input` and `/output` directories are created in the same directory as the script.
- The script fetches the bitrate of the input file and applies the same bitrate to the output file to preserve the audio quality.
- Sox must be installed with MP3 support for the script to function properly.
- If an error occurs, verify that Sox is correctly installed, the `/input` folder contains MP3 files, and you have the necessary permissions to read from and write to the specified directories.
