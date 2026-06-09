# EDA Summary Report

## Dataset Overview
- Rows: 120
- Columns: 5
- Start Date: 2025-01-01 00:00:00
- End Date: 2025-01-05 23:00:00

## Key Statistics

|       |   temperature |   humidity |     co2 |   yield_kg |
|:------|--------------:|-----------:|--------:|-----------:|
| count |        120    |     120    |  120    |     120    |
| mean  |         24.84 |      78.64 |  989.66 |      13.09 |
| std   |          1.85 |      10.15 |  116.7  |       0.96 |
| min   |         19.76 |      60.18 |  805.76 |      10.88 |
| 25%   |         23.86 |      69.69 |  884.33 |      12.38 |
| 50%   |         24.85 |      80.07 |  993.16 |      13.07 |
| 75%   |         25.77 |      87.43 | 1082.56 |      13.7  |
| max   |         29.93 |      94.65 | 1196.2  |      15.19 |

## Insights
- Humidity is moderately stable and slightly below ideal range (85–90%).
- Temperature is highly stable across the dataset.
- CO₂ shows moderate variation but remains controlled.
- Yield is consistent with low variance, suitable for modeling.

## Visualizations
- Correlation heatmap
- Humidity vs Yield scatter plot
- CO₂ vs Yield scatter plot
