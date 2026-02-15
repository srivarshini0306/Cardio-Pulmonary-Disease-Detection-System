🫀🫁 Cardio-Pulmonary Disease Detection System

An AI-powered medical sound analysis system that detects heart murmurs and lung diseases using deep learning models.
This application integrates multiple healthcare models into one unified Streamlit web application for real-time diagnosis from audio recordings.

It allows users to upload heart or lung sound recordings and receive instant predictions, confidence scores, and visualizations.

🚀 Project Overview

This project combines:

❤️ Heart Murmur Detection (LSTM model)

🫁 Lung Disease Classification (GRU model)

🌐 Streamlit Web App for real-time prediction

The system can analyze medical audio (.wav/.mp3) and classify:

Heart Model

Normal

Abnormal

Murmur detected

Lung Model

Healthy

COPD

Pneumonia

URTI

Bronchiolitis

🧠 Features

✔ Integrated heart + lung detection in one app
✔ Upload audio (.wav/.mp3)
✔ Real-time AI prediction
✔ Confidence score display
✔ Audio waveform visualization
✔ Clean UI using Streamlit
✔ Modular scalable code structure
✔ Separate preprocessing for heart & lung
✔ Model loading system for fast inference

🏗 Project Architecture
Cardio-Pulmonary-Disease-Detection-System/
│
├── app.py                     # Main Streamlit app
├── config.py                  # Configuration file
├── requirements.txt
├── README.md
│
├── audio/                     # Audio preprocessing
│   ├── heart_preprocessing.py
│   └── lung_preprocessing.py
│
├── model/
│   ├── heart_model_loader.py
│   └── lung_model_loader.py
│
├── model files/
│   ├── lstm_model.h5          # Heart model
│   └── lung_model.h5          # Lung model
│
├── test_files/
│   ├── heart_testfiles/
│   └── lung_testfiles/
│
├── ui/
│   └── visualizations.py      # Graphs & plots
│
└── utils/
    └── logger.py

⚙️ Tech Stack
Languages & Libraries

Python

TensorFlow / Keras

Librosa (audio processing)

NumPy, Pandas

Matplotlib

Scikit-learn

Streamlit

AI Models Used

LSTM Neural Network (Heart Murmur Detection)

GRU Neural Network (Lung Disease)

MFCC Feature Extraction

Signal Processing

🔬 How the System Works
Step 1: Upload Audio

User uploads heart or lung sound (.wav/.mp3)

Step 2: Preprocessing

Noise handling

Audio normalization

MFCC feature extraction

Reshaping for model input

Step 3: Model Prediction

Heart → LSTM model

Lung → CNN/Deep learning model

Step 4: Output

Predicted disease

Confidence score

Visualization graph

💻 Installation Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/cardio-pulmonary-detection.git
cd cardio-pulmonary-detection

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment
Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

4️⃣ Install Requirements
pip install -r requirements.txt

5️⃣ Run Application
streamlit run app.py


🖥 How to Use the App

Select diagnosis type:

Heart

Lung

Upload audio file (.wav or .mp3)

Click predict

View:

Predicted disease

Confidence score

Visualization graph

📊 Model Details
❤️ Heart Murmur Model

Model: LSTM

Input: MFCC features

Classes: Normal, Abnormal, Murmur

Accuracy: ~95–97%

🫁 Lung Disease Model

Model: GRU

Input: MFCC + audio features

Classes:

Healthy

COPD

Pneumonia

URTI

Bronchiolitis

Deep learning classification model

📈 Future Improvements

Add bowel sound detection

Add XAI (Explainable AI)

Deploy on cloud (AWS/GCP)

Add patient report generation

Mobile app integration

Real hospital dataset training

🎓 Author

Srivarshini G
BSc Data Science Student
AI & Healthcare Enthusiast

Projects:

Heart Murmur Detection

Lung Disease Detection

Breast Cancer Detection (XAI)

Integrated Medical AI System

⭐ Why This Project is Special

This is not a basic ML project.

It is a complete healthcare AI system combining:

Multiple deep learning models

Signal processing

Real-time web app

End-to-end deployment

This level of integration is internship + research level.

📜 License

This project is for educational and research purposes. Please ensure you have appropriate permissions for any audio data used.