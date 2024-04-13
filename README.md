# Abalone Age Prediction

This repository contains code and resources for training a machine learning model to predict the age of abalones based on various features. The project structure is organized as follows:

## Project Structure

+-- data/
| +-- train.csv
| +-- test.csv
+-- research/
| +-- EDA.ipynb
| +-- Regression_model.ipynb
+-- submission/
| +-- submission.csv


- **data/**: Contains the training and testing datasets in CSV format.
  - `train.csv`: Training dataset containing features and labels.
  - `test.csv`: Testing dataset containing only features (used for model evaluation).
  
- **research/**: Contains Jupyter notebooks for exploratory data analysis (EDA) and model development.
  - `EDA.ipynb`: Jupyter notebook for exploratory data analysis.
  - `Regression_model.ipynb`: Jupyter notebook for building and evaluating regression models.
  
- **submission/**: Contains the submission file for the Kaggle competition.
  - `submission.csv`: CSV file format for submitting predictions to the Kaggle competition.

## Kaggle Competition
The goal of this project is to predict the age of abalones accurately. The submission file (`submission.csv`) is formatted according to the requirements of the Kaggle competition.

## Dependencies
- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- lightGBM 

## Usage
1. Clone this repository: `git clone https://github.com/yourusername/abalone-age-prediction.git`
2. Navigate to the project directory: `cd abalone-age-prediction`
3. Install dependencies: `pip install -r requirements.txt`
4. Explore the notebooks in the `research/` directory to understand the data and model development process.
5. Train your model using `Regression_model.ipynb`.
6. Generate predictions using the trained model.
7. Create a submission file (`submission.csv`) following the Kaggle competition guidelines.
8. Submit your predictions to the Kaggle competition and evaluate your model's performance.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
