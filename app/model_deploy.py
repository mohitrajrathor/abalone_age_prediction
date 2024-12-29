# 
# model_deploy.py
#   - this file is for model deployment
# 

# imports 
import pandas as pd 
from typing import List
import numpy as np
import pickle 
from sklearn.preprocessing import StandardScaler


# const
features = ['Sex','Length', 'Diameter', 'Height', 'Whole weight', 'Whole weight.1', 'Whole weight.2', 'Shell weight']


df = pd.read_csv('data/train.csv', index_col='id')

df['Sex'] = df['Sex'].map({
    'M' : 0,
    'F' : 1,
    'I' : 2
})

scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# loading model
with open('trained_models/xgboost.pkl', 'rb') as fh:
    model = pickle.load(fh)



class PrdictModel:
	def __init__(self, model, scaler):
		self.model = model
		self.scaler = scaler

	def predict(self, sample: List[np.number])-> np.ndarray:
		assert len(sample) == 8, "Sample must have 8 features (1 int and rest float)"
		data = self.scaler.transform([sample])
		output: int = int(self.model.predict(data)[0])

		return output


# preparing model 
output_model = PrdictModel(model, scaler)