FROM python:3.11.9-slim-bookworm

EXPOSE 5000/tcp

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY app.py .
COPY util/aws_transcibe_audio.py ./util
COPY util/transcribe_audio.py ./util

CMD ["python", "app.py"]

