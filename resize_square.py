import subprocess
import shutil
import os

input_video = "resource/test.mp4"
backup_video = "resource/test_backup.mp4"

# Create a backup of the original video
shutil.copy(input_video, backup_video)

# Use ffmpeg to resize the video to a square format (e.g., 720x720)
temp_output_video = "resource/temp_test.mp4"  # Temporary file for output
ffmpeg_command = [
    "ffmpeg",
    "-i", input_video,
    "-vf", "scale=720:720:force_original_aspect_ratio=1,pad=720:720:(ow-iw)/2:(oh-ih)/2",
    "-c:a", "copy",  # Copy the audio stream without re-encoding
    temp_output_video
]

# Run the ffmpeg command
subprocess.run(ffmpeg_command, check=True)

# Replace the original file with the temporary file
os.replace(temp_output_video, input_video)
