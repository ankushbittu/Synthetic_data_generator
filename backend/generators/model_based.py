import torch
import pandas as pd
import pickle
from typing import Optional, Dict

class ModelBasedGenerator:
    def __init__(self, model_path="C:/Users/HP BITTU/Downloads/ctgan_model.pkl"):
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
        except Exception as e:
            print(f"Detailed error loading model: {str(e)}")
            self.model = None

    def generate_data(self, rows: int, params: Optional[Dict] = None) -> pd.DataFrame:
        if params is None:
            params = {}
            
        try:
            rows = int(rows)  # Convert rows to integer
            object_type = params.get('objectType', 'all')
            
            if self.model is None:
                raise Exception("Model not loaded properly")
                
            # Generate synthetic samples using CTGAN
            synthetic_data = self.model.sample(rows)
            
            # Filter based on object type if specified
            if object_type == 'hazardous':
                synthetic_data = synthetic_data[synthetic_data['Hazardous'] == 1]
            elif object_type == 'non-hazardous':
                synthetic_data = synthetic_data[synthetic_data['Hazardous'] == 0]
            
            # Convert hazard_status to boolean/string if needed
            synthetic_data['Hazardous'] = synthetic_data['Hazardous'].map({1: 'Hazardous', 0: 'Non-Hazardous'})
            
            return synthetic_data
            
        except Exception as e:
            raise Exception(f"Error generating data: {e}")