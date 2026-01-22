import librosa
import numpy as np
from config import SAMPLE_RATE, N_MFCC

def extract_lung_mfcc(file):
    y, sr = librosa.load(file, sr=SAMPLE_RATE)
    y = librosa.effects.time_stretch(y, rate=1.2)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC).T, axis=0)
    mfcc = mfcc.reshape(1, 1, N_MFCC)
    return mfcc
