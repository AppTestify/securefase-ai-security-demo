import pickle
import torch


def load_weights(path: str):
    # DEMO: unsafe deserialization of model weights.
    return torch.load(path)


def load_cache(path: str):
    with open(path, "rb") as handle:
        return pickle.load(handle)
