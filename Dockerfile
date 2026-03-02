FROM node:18-slim AS builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.10-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 -c "from huggingface_hub import hf_hub_download as hfd; hfd('srivarshini0306/body_sound_detection', 'lstm_model.h5'); hfd('srivarshini0306/body_sound_detection', 'lung_model.h5')"

COPY . .
COPY --from=builder /app/frontend/dist ./frontend/dist

# Fix potential Windows line endings and set permissions
RUN sed -i 's/\r$//' start.sh && chmod +x start.sh
EXPOSE 8000 8501
CMD ["./start.sh"]
