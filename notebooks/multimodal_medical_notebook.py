{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# Multimodal Medical Data Augmentation Project\n", "This notebook contains all preprocessing, augmentation, and utility functions."]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["# Install and import packages\n", "import sys\n", "!{sys.executable} -m pip install --upgrade pip\n", "!{sys.executable} -m pip install pandas numpy matplotlib scikit-learn Pillow\n", "!{sys.executable} -m pip install torch==2.0.1+cpu torchvision==0.15.2+cpu torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cpu\n", "import os\n", "import pandas as pd\n", "import numpy as np\n", "from PIL import Image\n", "import matplotlib.pyplot as plt\n", "import torch\n", "os.environ['CUDA_MODULE_LOADING'] = 'LAZY'\n", "print('All packages imported successfully')\n", "print('Torch version:', torch.__version__)"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["# Prepare project folders\n", "base_path = '../'\n", "folders = ['data/raw','data/processed','outputs']\n", "for f in folders:\n", "    path = os.path.join(base_path, f)\n", "    os.makedirs(path, exist_ok=True)\n", "    print(f'Folder ready: {path}')"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["# Preprocessing functions\n", "def load_csv(path):\n", "    '''Load CSV file'''\n", "    return pd.read_csv(path)\n\n", "def normalize_array(arr):\n", "    '''Normalize numpy array'''\n", "    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["# Data augmentation functions\n", "def generate_synthetic_image(image_array):\n", "    '''Simple synthetic image example (flip horizontally)'''\n", "    return np.fliplr(image_array)\n\n", "def generate_synthetic_text(text):\n", "    '''Simple synthetic text example (reverse string)'''\n", "    return text[::-1]"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["# Utility functions\n", "def save_image(array, path):\n", "    '''Save numpy array as image'''\n", "    img = Image.fromarray(array)\n", "    img.save(path)\n\n", "def save_report(text, path):\n", "    '''Save text report'''\n", "    with open(path, 'w', encoding='utf-8') as f:\n", "        f.write(text)"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["# Example pipeline\n", "# Load sample data\n", "# data = load_csv('../data/raw/sample.csv')  # Uncomment and provide your sample CSV\n", "# print('Original data head:\n', data.head())\n\n", "# Example augmentation\n", "# img = np.array(Image.open('../data/raw/sample_image.png'))  # Uncomment and provide your sample image\n", "# aug_img = generate_synthetic_image(img)\n", "# plt.imshow(aug_img)\n", "# plt.show()\n\n", "# text_sample = 'Radiology report example'\n", "# aug_text = generate_synthetic_text(text_sample)\n", "# print('Original text:', text_sample)\n", "# print('Augmented text:', aug_text)"]
  }
 ],
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.10"}
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
