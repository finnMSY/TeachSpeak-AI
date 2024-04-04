import boto3
import time

def transcribe_audio(audio_file, output_file):
    transcribe = boto3.Session(profile_name='teachspeakais3').client('transcribe', region_name='ap-southeast-2')

    job_name = "transcribe-job-" + str(int(time.time()))
    job_uri = "s3://teachspeakai/" + audio_file

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='en-US',
        Settings={
            'ShowSpeakerLabels': True,
            'MaxSpeakerLabels': 3
        }
    )

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Transcribing...")
        time.sleep(5)

    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcription_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        transcription_result = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        print("Transcription URL:", transcription_url)
        print("Transcription Result:")
        print(transcription_result)
    else:
        print("Transcription failed.")

if __name__ == "__main__":
    audio_file = "classDemo.mp3"
    output_file = "transcription.txt"
    transcribe_audio(audio_file, output_file)
