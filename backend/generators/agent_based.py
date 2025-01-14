import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple

class AgentBasedGenerator:
    def __init__(self):
        self.START_DATE = datetime(2025, 1, 15)
        self.SIMULATION_DAYS = 7
        self.END_DATE = self.START_DATE + timedelta(days=self.SIMULATION_DAYS)
        
        np.random.seed(42)
        random.seed(42)
        
        self.staff_roles = ["ER Physician", "ER Nurse", "Physician Assistant"]
        self.bed_ids = [f"EDBed{i}" for i in range(1, 6)]
        self.complaints = [
            "Chest Pain", "Headache", "Abdominal Pain", 
            "Flu-like Symptoms", "Severe Trauma", "Fracture", 
            "General Weakness"
        ]
        self.comorbidities = ["None", "Hypertension", "Diabetes", "Asthma", "COPD"]

    def generate_data(self, rows: int, params: Optional[Dict] = None) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        try:
            num_patients = int(rows)  # Convert rows to integer
            staff_count = int(params.get('staffCount', 10)) if params else 10
            sim_days = int(params.get('days', 7)) if params else 7
            
            # Update simulation duration
            self.SIMULATION_DAYS = sim_days
            self.END_DATE = self.START_DATE + timedelta(days=self.SIMULATION_DAYS)
            
            # Generate staff IDs
            staff_ids = [f"S{i+1:03d}" for i in range(staff_count)]
            
            # Generate the three datasets
            df_patients = self._generate_patients(num_patients, staff_ids)
            df_staff = self._generate_staff(staff_ids)
            df_resources = self._generate_resource_usage(df_patients)
            
            return df_patients, df_staff, df_resources
            
        except Exception as e:
            raise Exception(f"Error in generate_data: {str(e)}")

    def _random_timestamp(self, start_dt, end_dt):
        delta = end_dt - start_dt
        random_sec = random.randrange(int(delta.total_seconds()))
        return start_dt + timedelta(seconds=random_sec)

    def _generate_comorbidities(self):
        if random.random() < 0.3:
            return "None"
        selected = random.sample(self.comorbidities[1:], k=random.randint(1,2))
        return ", ".join(selected)

    def _assign_triage_level(self, chief_complaint):
        if chief_complaint == "Chest Pain":
            return np.random.choice([1, 2], p=[0.3, 0.7])
        elif chief_complaint == "Severe Trauma":
            return 1
        return np.random.choice([3, 4, 5], p=[0.4, 0.4, 0.2])

    def _resource_usage_duration(self, triage_level):
        durations = {
            1: (180, 360),  # 3-6 hours
            2: (120, 240),  # 2-4 hours
            3: (90, 180),   # 1.5-3 hours
            4: (60, 120),   # 1-2 hours
            5: (30, 90)     # 0.5-1.5 hours
        }
        return np.random.randint(*durations[triage_level])

    def _generate_patients(self, num_patients, staff_ids):
        arrival_times = [
            self._random_timestamp(self.START_DATE, self.END_DATE)
            for _ in range(num_patients)
        ]
        arrival_times.sort()

        records = []
        for i in range(num_patients):
            patient_id = f"P{i+1:04d}"
            arrival_time = arrival_times[i]
            
            chief_complaint = random.choice(self.complaints)
            triage_level = self._assign_triage_level(chief_complaint)
            
            triage_delay = np.random.randint(5, 31)
            triage_time = arrival_time + timedelta(minutes=triage_delay)
            
            duration = self._resource_usage_duration(triage_level)
            discharge_time = triage_time + timedelta(minutes=duration)
            
            record = {
                "patient_id": patient_id,
                "arrival_time": arrival_time,
                "age": np.random.randint(1, 90),
                "gender": np.random.choice(["Male", "Female"], p=[0.48, 0.52]),
                "comorbidities": self._generate_comorbidities(),
                "chief_complaint": chief_complaint,
                "triage_time": triage_time,
                "triage_level": triage_level,
                "discharge_time": discharge_time,
                "disposition": "Admitted" if (triage_level <= 2 and random.random() < 0.1) else "Discharged",
                "primary_staff_id": random.choice(staff_ids),
                "length_of_stay_hours": (discharge_time - arrival_time).total_seconds() / 3600.0
            }
            records.append(record)
            
        return pd.DataFrame(records)

    def _generate_staff(self, staff_ids):
        records = []
        for s_id in staff_ids:
            staff_role = random.choice(self.staff_roles)
            for day in range(self.SIMULATION_DAYS):
                shift_date = self.START_DATE + timedelta(days=day)
                
                # Day shift: 7AM to 7PM
                shift1_start = shift_date.replace(hour=7, minute=0, second=0)
                shift1_end = shift_date.replace(hour=19, minute=0, second=0)
                records.append({
                    "staff_id": s_id,
                    "role": staff_role,
                    "shift_start": shift1_start,
                    "shift_end": shift1_end
                })
                
                # Night shift: 7PM to 7AM
                shift2_start = shift_date.replace(hour=19, minute=0, second=0)
                shift2_end = (shift_date + timedelta(days=1)).replace(hour=7, minute=0, second=0)
                records.append({
                    "staff_id": s_id,
                    "role": staff_role,
                    "shift_start": shift2_start,
                    "shift_end": shift2_end
                })
                
        return pd.DataFrame(records)

    def _generate_resource_usage(self, df_patients):
        records = []
        for _, patient in df_patients.iterrows():
            records.append({
                "patient_id": patient["patient_id"],
                "resource_id": random.choice(self.bed_ids),
                "resource_type": "ED Bed",
                "start_utilization_time": patient["triage_time"],
                "end_utilization_time": patient["discharge_time"]
            })
        return pd.DataFrame(records)