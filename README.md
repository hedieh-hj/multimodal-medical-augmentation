# Multimodal Medical Data Augmentation

This repository provides a **multimodal data augmentation pipeline** for **chest X-ray images** and their corresponding **radiology reports**. It is designed to preprocess, augment, and organize medical image-text pairs for AI research or model training.

---

## Project Structure
multimodal-medical-augmentation/
├─ main.ipynb # Main Jupyter Notebook for full pipeline execution
├─ 01_environment_setup.ipynb # Notebook to install and setup dependencies
├─ data/
│ ├─ raw/
│ │ ├─ image/ # Original X-ray images (PNG)
│ │ └─ ecgen-radiology/ # Original XML reports
│ └─ processed/ # Preprocessed images and text
├─ outputs/ # Augmented data, metrics, visualizations
├─ notebooks/ # Additional experimental notebooks (optional)
├─ .gitignore
└─ README.md


---

## Environment Setup

1. Install required Python packages using `requirements.txt`.
2. Run `01_environment_setup.ipynb` to confirm that all packages are working.
3. The project is designed to run entirely in Jupyter Notebook for transparency and reproducibility.

---

## Data Details

- **Images:** Stored in `data/raw/image/`, named like `CXR1_1_IM-0001-3001.png`.
- **Reports:** Stored in `data/raw/ecgen-radiology/` as XML files. Each report specifies the images corresponding to it.
- **Mapping:** One report may correspond to one or multiple images. This mapping is defined in the XML `<parentImage>` tags.

---

## Pipeline Overview

The main steps in the pipeline are:

1. **Environment setup:** Ensure all packages are installed and the environment works correctly.
2. **Data loading:** Load XML reports and images from raw folders.
3. **Report-image mapping:** Identify which images belong to each report.
4. **Preprocessing:**
   - Resize and normalize images.
   - Clean and format report text.
5. **Optional Data Augmentation:** Apply image and text augmentation to increase dataset size.
6. **Outputs:** Save processed and augmented data for downstream tasks.

---

## Notes

- Large data folders (`raw/image` and `raw/ecgen-radiology`) are excluded from Git using `.gitignore`.
- The project is designed to work on any system without requiring a GPU.
- Each step is executed inside Jupyter Notebook for reproducibility.
- Processed and augmented data is stored separately from the raw data.

---

## Next Steps

- Implement model training using the preprocessed multimodal dataset.
- Add evaluation metrics to assess alignment between images and reports (e.g., MedCLIP, BERTScore, FID).
- Visualize sample augmented images and reports.
- Continuously document progress in the separate daily log README.
