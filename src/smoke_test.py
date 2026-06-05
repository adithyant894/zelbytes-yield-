import pandas as pd

sample_sensor_row = {
    "temperature": 24.5,
    "humidity": 88.2,
    "co2": 950,
    "yield_kg": 12.4
}

df = pd.DataFrame([sample_sensor_row])

print("Sample Polyhouse Sensor Data:")
print(df)