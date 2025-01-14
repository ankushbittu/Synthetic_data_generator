import numpy as np
import pandas as pd
from typing import Dict, Optional

class StatisticalGenerator:
    def __init__(self):
        # Mean vectors for each sex [height, weight, shoe_size, pant_size]
        self.male_means = np.array([175.0, 78.0, 43.0, 34.0])
        self.female_means = np.array([162.0, 63.0, 38.0, 28.0])
        
        # Covariance matrices
        self.male_cov = np.array([
            [40.0,  30.0,  2.0,  1.5],  # height
            [30.0,  60.0,  1.8,  2.0],  # weight
            [2.0,   1.8,   2.0,  0.5],  # shoe
            [1.5,   2.0,   0.5,  2.0]   # pant
        ])
        
        self.female_cov = np.array([
            [35.0,  25.0,  1.8,  1.2],
            [25.0,  50.0,  1.5,  1.8],
            [1.8,   1.5,   1.5,  0.4],
            [1.2,   1.8,   0.4,  1.5]
        ])

    def generate_data(self, rows: int, params: Optional[Dict] = None) -> pd.DataFrame:
        if params is None:
            params = {}
            
        try:
            rows = int(rows)
            male_ratio = float(params.get('maleRatio', 0.5))
            n_males = int(rows * male_ratio)
            n_females = rows - n_males
            
            # Generate male data
            male_data = np.random.multivariate_normal(
                self.male_means, self.male_cov, n_males
            )
            
            # Generate female data
            female_data = np.random.multivariate_normal(
                self.female_means, self.female_cov, n_females
            )
            
            # Combine and create DataFrame
            all_data = np.vstack([male_data, female_data])
            sexes = ['M'] * n_males + ['F'] * n_females
            
            df = pd.DataFrame(
                all_data,
                columns=['height', 'weight', 'shoe_size', 'pant_size']
            )
            df['sex'] = sexes
            
            # Round appropriate columns
            
            df['shoe_size'] = df['shoe_size'].round()
            df['pant_size'] = df['pant_size'].round()
            df['height'] = df['height'].round(2)
            df['weight'] = df['weight'].round(2)
            
            return df
            
        except Exception as e:
            raise Exception(f"Error in generating statistical data: {str(e)}")