#!/bin/bash

# Start FastAPI server in the background
echo "Starting FastAPI Server on port 8000..."
python main.py &

# Start Streamlit dashboard
echo "Starting Streamlit Dashboard on port 8501..."
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
