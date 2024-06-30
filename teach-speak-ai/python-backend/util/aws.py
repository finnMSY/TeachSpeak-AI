import boto3
import time
import configparser
import os
from botocore.exceptions import NoCredentialsError
import requests

config = configparser.ConfigParser()
script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
config_file_path = os.path.join(script_dir, "awsconfig.ini")
config.read(config_file_path)

aws_access_key_id = config['teachspeakais3']['aws_access_key_id']
aws_secret_access_key = config['teachspeakais3']['aws_secret_access_key']

def transcribe_audio(audio_file: str, output_file: str) -> str:
    # load AWS credentials
    
    transcribe = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,   
    ).client('transcribe', region_name='ap-southeast-2')

    job_name = "transcribe-job-" + str(int(time.time()))
    file_name = audio_file.split("\\")[-1]
    job_uri = "s3://teachspeak/transcribed-audio-files/" + file_name

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
        # response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        # transcription_result = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        print("Transcription URL:", transcription_url)
        
        # Fetch the transcription result
        response = requests.get(transcription_url)
        transcription_result = response.json()
        # Extract the transcription text
        transcription_text = transcription_result['results']['transcripts'][0]['transcript']

        file_name = output_file.split("\\")[-1]
        upload_str_to_s3(transcription_text, "teachspeak", f"transcription-text-files/{file_name}")

        print("Transcription Result:")
        print(transcription_text)

        return transcription_text
    else:
        print("Transcription failed.")

def upload_to_s3(file_name: str, bucket: str, object_name: str = None) -> bool:
    if file_name is None:
        print("No recording found to upload.")
        return False
    
    # Set the default object_name if not provided
    if object_name is None:
        object_name = f"transcribed-audio-files/text.txt"

    s3_client = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    ).client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to s3://{bucket}/{object_name}")
        os.remove(file_name)
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except Exception as e:
        print(f"Upload failed: {e}")
        return False
    
def upload_str_to_s3(string: str, bucket: str, key: str = None) -> bool:
    if string is None:
        print("No recording found to upload.")
        return False
    
    # Set the default object_name if not provided
    if key is None:
        object_name = f"transcribed-audio-files/text.txt"

    s3_client = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    ).client('s3')
    try:
        s3_client.put_object(Body=string, Bucket=bucket, Key=key, ContentType='text/plain')
        print(f"File {string} uploaded to s3://{bucket}/{key}")
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except Exception as e:
        print(f"Upload failed: {e}")
        return False
    