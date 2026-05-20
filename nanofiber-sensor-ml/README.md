# nanofiber-sensor-ml

Machine learning analysis of flexible capacitive pressure sensor data.

> Data from: **Siddique et al.** — *Electrospun Hollow Nanofiber Surfaces as
> Dielectric Mediums for Highly Sensitive Flexible Capacitive Pressure Sensors
> in Low-Pressure Regimes*
> IEEE Journal on Flexible Electronics, 2025.
> DOI: [10.1109/JFLEX.2025.3577111](https://doi.org/10.1109/JFLEX.2025.3577111)

## Projects

| # | Notebook | ML technique | Key result |
|---|----------|--------------|------------|
| 1 | `01_gpr_prediction.ipynb` | Gaussian Process Regression | Predicts full sensitivity curve with uncertainty bands, R²>0.97 |
| 2 | `02_curve_fitting.ipynb` | Physics-informed curve fitting | Extracts sensor fingerprint parameters |
| 3 | `03_classifier.ipynb` | SVM / Random Forest | Classifies sensor type from signal (AUC > 0.99) |
| 4 | `04_reliability.ipynb` | Anomaly detection | Reliability map across pressure range |
| 5 | `app/streamlit_app.py` | Full ML pipeline | Live web app — sensor design assistant |

## Quick start

```bash
git clone https://github.com/yourusername/nanofiber-sensor-ml
cd nanofiber-sensor-ml
pip install -r requirements.txt
jupyter notebook notebooks/01_gpr_prediction.ipynb
```

## Results (Project 1)

- Coaxial sensor peak sensitivity: **1.086 ± 0.005 kPa⁻¹ at 1 kPa**
- Control sensor peak sensitivity: **0.544 ± 0.091 kPa⁻¹ at 5 kPa**
- Improvement: **~100% (p < 0.001)**
- Crossover pressure: **~3.5 kPa**
- GPR LOO cross-validation R²: **> 0.97**
