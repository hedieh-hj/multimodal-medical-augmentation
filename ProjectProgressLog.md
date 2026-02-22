# Project Progress Log – Multimodal Medical Data Augmentation

This document contains **daily progress updates** for the project. Each entry describes the work completed and observations for that day.

---

## [Day 1] Environment Setup

**Date:** 2026-2-22

**Tasks Completed:**

- Installed all required Python packages for the project.
- Verified that Jupyter Notebook environment works properly.
- Created the project folder structure and initialized Git repository.
- Configured `.gitignore` to exclude large raw data folders (`image` and `ecgen-radiology`).
- Prepared main Jupyter Notebook (`main.ipynb`) and environment setup notebook (`01_environment_setup.ipynb`) for the pipeline.
- **Loaded raw data:**
  - Read all X-ray images from `data/raw/image/`.
  - Parsed all XML radiology reports from `data/raw/ecgen-radiology/`.
  - Mapped each report to its corresponding image(s) according to `<parentImage>` tags in the XML files.
- Implemented preprocessing functions for images (`preprocess_image`) and report text (`preprocess_report`) and verified they run without errors.


**Observations:**

- Environment is ready for data loading and preprocessing.
- Project structure ensures modular and organized workflow.
- Raw image and XML data are ready to be processed without committing large files to Git.
