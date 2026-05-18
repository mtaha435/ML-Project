# Machine Learning for Motor Imagery Classification Using EEG Signals

## 🧠 Overview
Brain-computer interface (BCI) systems translate brain activity into machine-readable commands, enabling users to communicate or control devices without physical movement. A critical application of BCI is motor imagery classification, where a model predicts intended movement from EEG activity. 

This project implements a complete, interpretable machine learning pipeline to classify left-hand versus right-hand motor imagery from EEG recordings. By accurately decoding motor imagery, this work contributes to foundational techniques used in assistive technologies and neurorehabilitation for individuals with motor impairments.

## 📊 Dataset
This project uses the **BCI Competition IV (2008) Graz Dataset 2b**.
* **Subjects:** 9 subjects performing left-hand and right-hand motor imagery tasks.
* **Sessions:** 5 sessions per subject (screening without feedback + feedback sessions).
* **Sampling Rate:** 250 Hz.
* **Channels:** * 3 EEG channels for classification (`C3`, `Cz`, `C4`).
  * 3 EOG channels for artifact inspection and trial rejection (left, central, right).
* **Annotations:** Event markers identify trial starts, cue onsets, classification labels, rejected trials, and run boundaries.

> **Note:** The dataset can be accessed via the [UCSD Neural Data Challenge Kaggle Competition](https://www.kaggle.com/competitions/ucsd-neural-data-challenge).

## ⚙️ Pipeline Architecture
The software is designed as a modular Python-based pipeline, ensuring each step is independently executable and testable.

1. **Data Loading & Preprocessing (`src/pkl_reader.py`)**
   * Imports raw `.pkl` files and extracts valid trials based on event markers.
   * Rejects trials heavily affected by eye movements using EOG channel data.
   * Applies signal filtering and normalizes segments.
2. **Feature Extraction (`src/preprocessor.py`)**
   * Computes frequency-based spectral features (bandpower in the **mu** and **beta** bands).
   * Explores **Common Spatial Patterns (CSP)** to capture class-specific spatial activity.
3. **Model Training & Evaluation (`src/model.py`)**
   * Implements baseline classification using **Logistic Regression**.
   * Implements and compares **Support Vector Machines (SVM)**.
   * Evaluates performance using accuracy metrics, confusion matrices, and subject-level breakdowns.
4. **Visualization (`notebooks/notebook.ipynb`)**
   * Plots processed EEG signals, extracted feature distributions, and classifier evaluation results.

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.8+ installed. The primary libraries required for this project include `numpy`, `scipy`, `scikit-learn`, `mne` (for EEG processing), and `matplotlib`.
