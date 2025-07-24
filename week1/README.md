# Irrigation System Analysis Project - week1

This project analyzes sensor data from irrigation machines and predicts irrigation needs for different parcels using machine learning.

## Project Structure

- `irrigation_machine.csv` - Dataset containing sensor readings and parcel information
  - 20 sensor columns (sensor_0 to sensor_19) with values ranging from 0 to 10
  - 3 parcel columns (parcel_0, parcel_1, parcel_2) with binary values (0 or 1)
- `Irrigation_System.ipynb` - Jupyter notebook containing the analysis and machine learning model

## Requirements

- Python 3.x
- Required Python packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - joblib

You can install the required packages using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

## Dataset Description

The dataset contains:
- 20 sensor readings (sensor_0 through sensor_19) with values from 0 to 10
- 3 target variables (parcel_0, parcel_1, parcel_2) indicating irrigation needs for different parcels
- Each row represents a single measurement point in time

### Features
- `sensor_0` to `sensor_19`: Numerical values representing various sensor readings
  - Range: 0.0 to 10.0
  - Type: Float

### Target Variables
- `parcel_0`, `parcel_1`, `parcel_2`: Binary indicators for irrigation needs
  - Values: 0 (no irrigation needed) or 1 (irrigation needed)
  - Type: Integer

## Usage

1. Open `Irrigation_System.ipynb` in Jupyter Notebook or JupyterLab
2. Run all cells in sequence to:
   - Load and validate the data
   - Perform exploratory data analysis
   - Train the machine learning model
   - Evaluate model performance
   - Make predictions

## Model Information

The system uses a Random Forest Classifier with multi-output classification to predict irrigation needs for all three parcels simultaneously. The model:
- Takes 20 sensor readings as input
- Predicts binary outcomes for 3 parcels
- Uses feature scaling for better performance
- Includes validation and error handling

## Results

The notebook generates:
- Data visualization and analysis
- Model performance metrics
- Feature importance analysis
- Confusion matrices for each parcel

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is proprietary and contains company-specific data.
