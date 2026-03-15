import pandas as pd
import numpy as np


def process_data(text):

    words = text.split()

    df = pd.DataFrame(words, columns=["word"])

    df["length"] = df["word"].apply(len)

    avg_length = np.mean(df["length"])

    filtered = df[df["length"] > avg_length]

    return " ".join(filtered["word"].tolist())