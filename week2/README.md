# Irrigation System Analysis Project – Week 2

This project analyzes sensor data from irrigation machines and predicts irrigation needs for different parcels using machine learning.

# Project Structure

-`irrigation_machine.csv`- – Dataset containing sensor readings and parcel information

-`Irrigation_System.ipynb`- – Jupyter notebook with the updated analysis and machine learning pipeline

# Requirements

Python 3.x

# Install dependencies:
```bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```
# Dataset Features:
```
20 sensor columns (sensor_0 to sensor_19)
Range: 0.0 – 10.0
Targets:
3 parcel columns (parcel_0, parcel_1, parcel_2)
Values: 0 (No irrigation) or 1 (Irrigation needed)
```
# Updates in Week 2
```
Removed feature scaling (model works without it)
Removed confusion matrix and feature importance visualization
Kept Random Forest inside MultiOutputClassifier
Added classification report for evaluation
Model persistence using joblib retained
Streamlined notebook structure for faster execution
```
# Usage
```
Open Irrigation_System.ipynb in Jupyter Notebook or JupyterLab.
Run all cells in sequence to:
Load and validate data
Train the multi-output model
Evaluate model with classification report
Save the trained model for later use
```
# Model Details
```
Algorithm: Random Forest Classifier (multi-output)
Inputs: 20 sensor readings
Outputs: Binary predictions for 3 parcels
Evaluation: Classification report for each parcel
```
# Results
```
Performance metrics for each target (precision, recall, F1-score)
Model saved as .joblib for reuse
```
