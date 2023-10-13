import os
from gtts import gTTS

# Define the directory containing the text files
input_directory = "chapters"

# List all the text files and sort them by filename
text_files = [filename for filename in os.listdir(input_directory) if filename.endswith(".txt")]
sorted_text_files = sorted(text_files, key=lambda x: int(x.split('.')[0]))

# Iterate through the sorted text files
for filename in sorted_text_files:
    input_file = os.path.join(input_directory, filename)
    
    # Extract the filename without the extension
    name_without_extension = os.path.splitext(filename)[0]

    print(f"Converting '{filename}' to '{name_without_extension}.mp3'")
    
    # Define the output audio file with the same name
    output_audio_file = os.path.join(input_directory, f"{name_without_extension}.mp3")
    
    # Read the text from the input file
    with open(input_file, "r") as file:
        text = file.read().replace("\n", " ")

    
    
    # Convert the text to audio using gTTS
    tts = gTTS(text, lang='en', tld='com')  # English, United States accent
    
    # Save the audio to the output file
    tts.save(output_audio_file)
    
    print(f"Converted '{filename}' to '{name_without_extension}.mp3'")
