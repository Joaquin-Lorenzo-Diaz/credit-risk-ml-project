# Modelo de Riesgo Crediticio con Machine Learning

🇬🇧 [Read in English](README.md)

Proyecto end-to-end de riesgo crediticio aplicando Machine Learning.

**Dataset:** Lending Club (préstamos de consumo reales de EEUU, 2007-2018; 1.3M+ préstamos con resultado final usados para el modelado)

## 🎯 Objetivo

Construir un pipeline completo de riesgo crediticio: desde el análisis exploratorio hasta el cálculo de pérdida esperada del portafolio y pruebas de estrés, replicando el flujo de trabajo de un analista de riesgo real.

## 📊 Resultados principales

| Métrica | Resultado |
|---|---|
| NPL Ratio | 2.36% |
| AUC-ROC (modelo PD, XGBoost) | 0.7147 |
| LGD promedio | 46.7% |
| Expected Loss del portafolio | 10.07% |
| EL en estrés (percentil 99, Monte Carlo, sensibilidad macro supuesta) | +70% vs. escenario base |

## 🛠️ Stack técnico

- **Python:** Pandas, NumPy, scikit-learn, XGBoost, Matplotlib
- **Automatización:** APIs REST (requests), n8n
- **Control de versiones:** Git/GitHub

## 📁 Estructura del proyecto

```text
notebooks/
├── 01_eda_npl_vintage.ipynb     → EDA, NPL ratio, análisis de cosechas (vintage)
├── 02_pd_model.ipynb            → Modelo de Probability of Default (XGBoost vs. Regresión Logística)
├── 03_lgd_model.ipynb           → Modelo de Loss Given Default
├── 04_expected_loss.ipynb       → Expected Loss del portafolio (PD × LGD × EAD)
├── 05_pd_model_improved.ipynb   → Feature Engineering aplicado al modelo de PD
├── 06_stress_testing.ipynb      → Stress testing con simulación Monte Carlo
└── 07_api_consumption.ipynb     → Consumo de APIs (DolarAPI) y reglas de negocio

pd_model_xgb.pkl                 → Modelo de PD entrenado (lo genera el notebook 02)
lgd_by_grade.json                → LGD por grado (lo genera el notebook 03)
fx_gap_monitor.py                → Script de automatización (consumo de API + reglas de negocio)
```

## 🔑 Conceptos aplicados

PD, LGD, EAD, Expected Loss, NPL, Vintage Analysis, Feature Engineering, AUC-ROC, Simulación Monte Carlo, Stress Testing, Automatización de procesos con APIs.

## ⚙️ Cómo reproducirlo

1. Clonar el repositorio
2. Crear y activar un entorno virtual: `python -m venv venv`
3. Instalar las dependencias: `pip install pandas numpy scikit-learn xgboost matplotlib jupyter kaggle requests`
4. Descargar el dataset de [Lending Club en Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club) en una carpeta `data/` en la raíz del proyecto (el archivo usado es `accepted_2007_to_2018Q4.csv.gz`). Con la CLI de Kaggle: `kaggle datasets download -d wordsforthewise/lending-club -p data`, y luego descomprimirlo.
5. Correr los notebooks en orden (01 a 07). El notebook 02 guarda el modelo de PD (`pd_model_xgb.pkl`) y el notebook 03 guarda el LGD por grado (`lgd_by_grade.json`); los notebooks 04 y 06 cargan ambos.
6. Opcional: ejecutar `python fx_gap_monitor.py` para correr el monitor de brecha cambiaria como script independiente.
