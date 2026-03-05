# Build Stage: Frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Final Stage: Python Application
FROM python:3.10-slim

# Install system dependencies (needed for audio processing/librosa)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy built frontend from stage 1
COPY --from=frontend-builder /app/frontend/dist /app/frontend/dist

# Expose ports
# 8000: FastAPI + Static Frontend
# 8501: Streamlit Dashboard
EXPOSE 8000 8501

# Add execution permission to the start script
RUN chmod +x /app/start.sh

# Start services
CMD ["/app/start.sh"]
