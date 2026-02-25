# This is the preprocessing module

import pandas as pd
import numpy as np

def load_csv(path):
    """Load CSV file"""
    return pd.read_csv(path)

def normalize_array(arr):
    """Normalize numpy array"""
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
