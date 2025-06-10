import numpy as np
import pandas as pd

class Patient:
    def __init__(self, name, age, gender, weight, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height

patients = {
    "Patient 1": Patient("John Doe", 30, "Male", 180, 75),
    "Patient 2": Patient("Jane Smith", 28, "Female", 165, 60),
    "Patient 3": Patient("Alice Johnson", 35, "Female", 170, 65),
    "Patient 4": Patient("Bob Brown", 40, "Male", 175, 80)
}

l_patients = [p.__dict__ for p in patients.values()]

df_patients = pd.DataFrame.from_records(l_patients, index=patients.keys())

df_patients['BMI'] = df_patients.apply(
    lambda column: round(column['weight'] / ((column['height'] / 100) ** 2), 2), axis=1
)
print(df_patients)
average_bmi = df_patients['BMI'].mean()
overweight_patients = df_patients[df_patients['BMI'] > 25]
print(f"Average BMI: {average_bmi:.2f}")
print(f"Overweight Patients: {overweight_patients['name'].tolist()}")
print(f"Overweight Percentage: {len(overweight_patients) / len(df_patients) * 100:.2f}%")
