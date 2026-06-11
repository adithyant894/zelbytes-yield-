# Linear Regression Diagnostics

- Residuals vs Predicted plot generated.
- Residuals vs Humidity plot generated.
- Linear Regression used as baseline model.
- Further comparison with Random Forest recommended.


# Linear Regression Diagnostics

## Model Performance

* MAE: 0.978
* RMSE: 1.137
* R²: 0.01

## Diagnostic Findings

1. Residuals are distributed around the zero line without severe systematic bias.
2. The residuals versus humidity plot does not reveal a strong linear trend.
3. The low R² score indicates that the model explains only a small portion of the variability in mushroom yield.

## Recommendation

Linear Regression serves as an interpretable baseline model for yield prediction. However, the low R² score suggests that more advanced machine learning models, such as Random Forest Regression, should be explored to capture potential non-linear relationships among environmental variables and improve predictive performance.
