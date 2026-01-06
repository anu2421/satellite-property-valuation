# Satellite Imagery–Based Property Valuation (Multimodal Regression)

This repository contains a multimodal regression pipeline that predicts property prices by combining tabular housing data with satellite imagery.

# Prerequisites

Python 3.9+

pip (Python package manager)

Mapbox API access token (free tier)

# Installing dependencies:

pip install pandas numpy scikit-learn torch torchvision opencv-python matplotlib seaborn requests

# API Setup (Satellite Images)

Create a free Mapbox account:
https://www.mapbox.com/

Generate a Mapbox Access Token

Add the token inside data_fetcher.py:

# Running the Project
## Step 1: Download Satellite Images

Fetch satellite images using latitude and longitude:

python data_fetcher.py

This will:

Read property coordinates from CSV files

Download satellite images

Save them in images/train/ and images/test/

## Step 2: Preprocess Data

Open and run:

preprocessing.ipynb


This notebook:

Cleans missing values

Standardizes numerical features

Applies log transformation to price

Saves processed datasets

## Step 3: Train Models

Open and run:

model_training.ipynb


This notebook:

Trains baseline, tabular-only, and multimodal models

Evaluates RMSE and R²

Saves:

Predictions (outputs/23124005_final.csv)

Trained multimodal model (outputs/multimodal_model.pth)

## Step 4: Exploratory Analysis & Explainability

Open and run:

eda_and_evaluation.ipynb


This notebook:

Performs exploratory and geospatial analysis

Generates price heatmaps and clusters

Applies Grad-CAM to visualize influential image regions

# Output Files

outputs/23124005_final.csv – Final price predictions

outputs/multimodal_model.pth – Trained multimodal model

Grad-CAM visualizations (displayed in notebook)

# Notes

Multimodal models may not always outperform tabular models in RMSE.

Satellite imagery primarily improves interpretability and contextual understanding.

Grad-CAM visualizations highlight environmental features influencing predictions.

# Troubleshooting

If training is slow, ensure GPU is enabled (optional).

Grad-CAM runs on CPU by default for stability.

Image download may take time depending on API limits.