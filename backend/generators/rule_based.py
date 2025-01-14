import pandas as pd
import numpy as np
from typing import Dict, Optional
import random
from faker import Faker
class RuleBasedGenerator:

    def __init__(self):
        self.faker = Faker()
        self.state_data = {
        "CA": {"area_codes": ["209", "213", "310", "323", "408", "415"], "pin_ranges": [(90001, 96162)], "income_multiplier": 1.4},
        "NY": {"area_codes": ["212", "315", "516", "518", "585", "607"], "pin_ranges": [(10001, 14975)], "income_multiplier": 1.3},
        "TX": {"area_codes": ["210", "214", "254", "281", "325", "361"], "pin_ranges": [(73301, 88595)], "income_multiplier": 1.0},
        "FL": {"area_codes": ["239", "305", "321", "352", "386", "407"], "pin_ranges": [(32004, 34997)], "income_multiplier": 1.1},
        "IL": {"area_codes": ["217", "224", "309", "312", "618", "630"], "pin_ranges": [(60001, 62999)], "income_multiplier": 1.2},
        "MA": {"area_codes": ["339", "351", "413", "508", "617", "774"], "pin_ranges": [(1001, 5544)], "income_multiplier": 1.3},
        "WA": {"area_codes": ["206", "253", "360", "425", "509", "564"], "pin_ranges": [(98001, 99403)], "income_multiplier": 1.3},
        "CO": {"area_codes": ["303", "719", "720", "970"], "pin_ranges": [(80001, 81658)], "income_multiplier": 1.2},
    }

        self.occupations = {
        "Software Engineer": {"income_range": (70000, 150000), "age_range": (22, 65), "gender_prob": {"M": 0.7, "F": 0.3}},
        "Teacher": {"income_range": (35000, 75000), "age_range": (24, 65), "gender_prob": {"M": 0.3, "F": 0.7}},
        "Plumber": {"income_range": (40000, 90000), "age_range": (25, 60), "gender_prob": {"M": 0.95, "F": 0.05}},
        "Nurse": {"income_range": (45000, 95000), "age_range": (22, 65), "gender_prob": {"M": 0.15, "F": 0.85}},
        "Sales Manager": {"income_range": (60000, 120000), "age_range": (30, 65), "gender_prob": {"M": 0.55, "F": 0.45}},
        "Data Scientist": {"income_range": (75000, 160000), "age_range": (25, 65), "gender_prob": {"M": 0.65, "F": 0.35}},
        "Chef": {"income_range": (35000, 85000), "age_range": (20, 65), "gender_prob": {"M": 0.7, "F": 0.3}},
        "Financial Analyst": {"income_range": (55000, 115000), "age_range": (23, 65), "gender_prob": {"M": 0.6, "F": 0.4}},
        "Electrician": {"income_range": (45000, 95000), "age_range": (25, 60), "gender_prob": {"M": 0.9, "F": 0.1}},
        "Marketing Manager": {"income_range": (65000, 130000), "age_range": (28, 65), "gender_prob": {"M": 0.4, "F": 0.6}},
        "Doctor": {"income_range": (150000, 300000), "age_range": (30, 70), "gender_prob": {"M": 0.55, "F": 0.45}},
        "Graphic Designer": {"income_range": (40000, 90000), "age_range": (20, 65), "gender_prob": {"M": 0.4, "F": 0.6}},
        "Construction Worker": {"income_range": (35000, 75000), "age_range": (18, 60), "gender_prob": {"M": 0.95, "F": 0.05}},
        "HR Manager": {"income_range": (55000, 110000), "age_range": (28, 65), "gender_prob": {"M": 0.3, "F": 0.7}},
        "Lawyer": {"income_range": (80000, 200000), "age_range": (26, 70), "gender_prob": {"M": 0.55, "F": 0.45}}
    }
    

    def generate_name(self, sex: str) -> str:
        if sex == "M":
            return self.faker.name_male()
        return self.faker.name_female()

    def get_suitable_occupation(self, age: int, sex: str) -> str:
        suitable_jobs = []
        for job, details in self.occupations.items():
            if (details["age_range"][0] <= age <= details["age_range"][1]):
                # Weight by gender probability
                weight = details["gender_prob"][sex] * 100
                suitable_jobs.extend([job] * int(weight))
        return random.choice(suitable_jobs)

    def generate_phone(self, state: str) -> str:
        area_code = random.choice(self.state_data[state]["area_codes"])
        return f"({area_code})-{random.randint(100,999)}-{random.randint(1000,9999)}"

    def generate_pincode(self, state: str) -> str:
        pin_range = random.choice(self.state_data[state]["pin_ranges"])
        return str(random.randint(*pin_range))

    def calculate_income(self, occupation: str, state: str) -> float:
        base_range = self.occupations[occupation]["income_range"]
        state_multiplier = self.state_data[state]["income_multiplier"]
        base_income = random.uniform(*base_range)
        return round(base_income * state_multiplier, 2)

    def generate_data(self, rows: int, params: Optional[Dict] = None) -> pd.DataFrame:
        if params is None:
            params = {}
            
        # Extract parameters with defaults
        try:
            rows = int(rows)  # Ensure rows is integer
            state_filter = params.get('state')
            age_min = int(params.get('ageMin', 18))  # Default age range if not provided
            age_max = int(params.get('ageMax', 65))
        except ValueError as e:
            age_min = 18  # Default if conversion fails
            age_max = 65
        
        data = []
        for i in range(rows):
            sex = random.choice(["M", "F"])
            age = np.random.randint(age_min, age_max + 1)
            state = state_filter if state_filter else random.choice(list(self.state_data.keys()))
            occupation = self.get_suitable_occupation(age, sex)
            
            record = {
                'id': i + 1,
                'name': self.generate_name(sex),
                'age': age,
                'sex': sex,
                'state': state,
                'phone': self.generate_phone(state),
                'pin_code': self.generate_pincode(state),
                'occupation': occupation,
                'income': self.calculate_income(occupation, state)
            }
            data.append(record)
                
        return pd.DataFrame(data)