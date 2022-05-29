import numpy as np
import pandas as pd

data = pd.read_csv("data.csv", header=None, sep="\t")
print(data.shape)
