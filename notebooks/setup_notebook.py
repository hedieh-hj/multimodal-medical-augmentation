{
 "cells": [
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import sys\n",
    "!{sys.executable} -m pip install --upgrade pip\n",
    "packages = [\"pandas\", \"numpy\", \"matplotlib\", \"scikit-learn\", \"Pillow\"]\n",
    "for pkg in packages:\n",
    "    !{sys.executable} -m pip install {pkg}\n",
    "!{sys.executable} -m pip install torch==2.0.1+cpu torchvision==0.15.2+cpu torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cpu"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from PIL import Image\n",
    "import matplotlib.pyplot as plt\n",
    "import torch\n",
    "os.environ[\"CUDA_MODULE_LOADING\"] = \"LAZY\"\n",
    "print(\"All packages imported successfully\")\n",
    "print(\"Torch version:\", torch.__version__)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "base_path = '../'\n",
    "folders = ['data/raw','data/processed','outputs','src']\n",
    "for f in folders:\n",
    "    path = os.path.join(base_path, f)\n",
    "    os.makedirs(path, exist_ok=True)\n",
    "    print(f'Folder ready: {path}')"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "preprocessing_path = os.path.join(base_path, 'src', 'preprocessing.py')\n",
    "if not os.path.exists(preprocessing_path):\n",
    "    with open(preprocessing_path, 'w', encoding='utf-8') as f:\n",
    "        f.write(\"import pandas as pd\nimport numpy as np\n\ndef load_csv(path):\n    return pd.read_csv(path)\n\ndef normalize_array(arr):\n    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))\")\n",
    "    print('Preprocessing module created at:', preprocessing_path)\n",
    "else:\n",
    "    print('Preprocessing module already exists.')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
