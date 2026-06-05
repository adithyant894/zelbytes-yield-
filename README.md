# Mushroom Yield Forecasting

## Environment Setup

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```
### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Smoke Test

```bash
python src/smoke_test.py
```

Expected Output:

```text
Sample Polyhouse Sensor Data:
   temperature  humidity  co2  yield_kg
0         24.5      88.2  950      12.4
```
