import subprocess
import os
import glob
from pydub import AudioSegment
import sys
from pydub.utils import mediainfo

def get_bitrate(file_path):
    info = mediainfo(file_path)
    return info['bit_rate']

def find_latest_song(input_folder):
    # List all mp3 files in the input folder
    list_of_files = glob.glob(os.path.join(input_folder, '*.mp3')) 
    if not list_of_files:
        raise Exception("No MP3 files found in the input folder.")
    # Find the most recent file
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def create_nightcore_with_sox(input_file, output_file, speed_increase_factor, pitch_shift_semitones):
    # Get the bitrate of the input file
    bitrate = get_bitrate(input_file)

    # Calculate the pitch shift in cents (1 semitone = 100 cents)
    pitch_shift_cents = pitch_shift_semitones * 100

    # Build the Sox command with explicit bitrate
    sox_command = [
        'sox', input_file, '-C', bitrate, output_file,
        'speed', str(speed_increase_factor),
        'pitch', str(pitch_shift_cents)
    ]

    # Execute the Sox command
    try:
        subprocess.run(sox_command, check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while processing the audio with Sox:", e)
        sys.exit(1)

    # Load the processed file and normalize
    processed_audio = AudioSegment.from_mp3(output_file)
    normalized_audio = processed_audio.normalize()

    # Export the normalized audio with the same bitrate as the original
    normalized_audio.export(output_file, format="mp3", bitrate=bitrate)

if __name__ == "__main__":
    input_folder = 'input'  # Set the input folder path
    output_folder = 'output'  # Set the output folder path

    if len(sys.argv) < 3:
        print("Usage: python script.py <speed_increase_factor> <pitch_shift_semitones>")
        sys.exit(1)

    try:
        input_file = find_latest_song(input_folder)
    except Exception as e:
        print(e)
        sys.exit(1)

    # Extract the original song name
    song_name = os.path.splitext(os.path.basename(input_file))[0]

    # Set output file name
    output_file = os.path.join(output_folder, f"Nightcore - {song_name}.mp3")

    speed_increase_factor = float(sys.argv[1])
    pitch_shift_semitones = float(sys.argv[2])  # Accept fractional semitones

    create_nightcore_with_sox(input_file, output_file, speed_increase_factor, pitch_shift_semitones)
    print(f"Nightcore version created: {output_file}")


