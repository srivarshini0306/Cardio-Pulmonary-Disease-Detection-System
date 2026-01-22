import tensorflow as tf
from tensorflow.keras.layers import LSTM
from huggingface_hub import hf_hub_download
from config import HF_REPO, HEART_MODEL_FILE

# Fix for old LSTM model
def LSTM_fixed(**kwargs):
    kwargs.pop("time_major", None)
    return LSTM(**kwargs)

def load_heart_model():
    model_path = hf_hub_download(
        repo_id=HF_REPO,
        filename=HEART_MODEL_FILE,
        repo_type="model"
    )

    model = tf.keras.models.load_model(
        model_path,
        custom_objects={"LSTM": LSTM_fixed}
    )

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

