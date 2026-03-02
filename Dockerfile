# Stage 1: Build React Frontend
FROM node:18-slim AS builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Final Python image
FROM python:3.10-slim
WORKDIR /app

# Install system dependencies and Python packages in one layer
RUN apt-get update && apt-get install -y ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bake models into the image
RUN python3 -c "from huggingface_hub import hf_hub_download as hfd; hfd('srivarshini0306/body_sound_detection', 'lstm_model.h5'); hfd('srivarshini0306/body_sound_detection', 'lung_model.h5')"

# Copy app code and built frontend
COPY . .
COPY --from=builder /app/frontend/dist ./frontend/dist

# Setup entrypoint
RUN chmod +x start.sh
EXPOSE 8000 8501
CMD ["./start.sh"]
