import tensorflow as tf
from tensorflow.keras.layers import GRU
from huggingface_hub import hf_hub_download
from config import HF_REPO, LUNG_MODEL_FILE

def GRU_fixed(**kwargs):
    kwargs.pop("time_major", None)
    return GRU(**kwargs)

def load_lung_model():
    model_path = hf_hub_download(
        repo_id=HF_REPO,
        filename=LUNG_MODEL_FILE,
        repo_type="model"
    )
    model = tf.keras.models.load_model(model_path, custom_objects={"GRU": GRU_fixed})
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model
