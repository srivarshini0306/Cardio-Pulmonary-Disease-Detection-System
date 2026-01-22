import librosa
import numpy as np
from config import SAMPLE_RATE, N_MFCC

def load_heart_audio(file):
    y, sr = librosa.load(file, sr=SAMPLE_RATE)
    return y, sr

def extract_heart_mfcc(y, sr):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
    mfcc = np.mean(mfcc.T, axis=0)
    mfcc = np.expand_dims(mfcc, axis=0)
    mfcc = np.expand_dims(mfcc, axis=2)
    return mfcc
