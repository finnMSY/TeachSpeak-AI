import os
import speech_recognition as sr

def transcribe_audio(audio_file_name):
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Construct the full path to the audio file
    audio_file_path = os.path.join(current_directory, "teach-speak-ai\\python-backend\\audio_files", audio_file_name)

    # Initialize recognizer
    r = sr.Recognizer() 
    
    try:
        # Load audio file
        with sr.AudioFile(audio_file_path) as source:
            audio_data = r.record(source)
        
        # Convert audio file to text
        text = r.recognize_google(audio_data)
        return text
    
    except Exception as e:
        print("Translation failed:", e)
        return None

# Example usage
audio_file_name = "2024-04-08_23-55-38-recording.wav"
transcribed_text = transcribe_audio(audio_file_name)
if transcribed_text:
    print("Transcription result:", transcribed_text)
