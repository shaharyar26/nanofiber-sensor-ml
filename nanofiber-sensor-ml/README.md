## Live demo
[nanofiber-sensor-app-onojwc5pdqzon9uehwqqvz.streamlit.app](https://nanofiber-sensor-app-onojwc5pdqzon9uehwqqvz.streamlit.app)
# nanofiber-sensor-ml

Machine learning analysis of flexible capacitive pressure sensors.

> **Paper:** Siddique et al. — *Electrospun Hollow Nanofiber Surfaces as Dielectric 
> Mediums for Highly Sensitive Flexible Capacitive Pressure Sensors in Low-Pressure Regimes*  
> IEEE Journal on Flexible Electronics, 2025  
> DOI: [10.1109/JFLEX.2025.3577111](https://doi.org/10.1109/JFLEX.2025.3577111)

## Projects

| # | Notebook | Method | Key result |
|---|----------|--------|------------|
| 1 | `01_gpr_prediction.ipynb` | Gaussian Process Regression | R²=0.99 control, R²=0.92 coaxial |
| 2 | `02_materials_ml.ipynb` | Random Forest + Materials Project API | pressure×hollow = 64% of model |

## Results

![GPR Uncertainty](https://raw.githubusercontent.com/shaharyar26/nanofiber-sensor-ml/main/nanofiber-sensor-ml/outputs/01_gpr_uncertainty.png)
![Feature Importance](https://raw.githubusercontent.com/shaharyar26/nanofiber-sensor-ml/main/nanofiber-sensor-ml/outputs/02_feature_importance.png)

## Key findings
- Coaxial sensor peak sensitivity: **1.086 ± 0.005 kPa⁻¹ at 1 kPa**
- Control sensor peak sensitivity: **0.544 ± 0.091 kPa⁻¹ at 5 kPa**
- Improvement: **~100% (p < 0.001)**
- Crossover pressure: **~3.8 kPa**
- GPR LOO R² control: **0.9958** — coaxial: **0.9220**
- Random Forest: hollow×pressure interaction drives **64%** of sensitivity variance

## How to run
```bash
git clone https://github.com/shaharyar26/nanofiber-sensor-ml
cd nanofiber-sensor-ml/nanofiber-sensor-ml
pip install -r requirements.txt
jupyter notebook
```

## Skills demonstrated
- Gaussian Process Regression with uncertainty quantification
- Random Forest with physics-engineered features
- Materials Project API (mp-api, pymatgen)
- Leave-one-out cross validation
- Statistical analysis from first-author IEEE publication
