from fastapi import FastAPI
import tensorflow as tf

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "TensorFlow is running",
        "version": tf.__version__
    }
