# Modelo de Riesgo Crediticio con Machine Learning

Proyecto end-to-end de riesgo crediticio aplicando Machine Learning, construido como práctica para aplicar a roles de Data Science / Risk Analytics en finanzas.

**Dataset:** Lending Club (1.3M+ préstamos reales, EEUU, 2007-2018)

## 🎯 Objetivo

Construir un pipeline completo de riesgo crediticio: desde el análisis exploratorio hasta el cálculo de pérdida esperada del portafolio y pruebas de estrés, replicando el flujo de trabajo de un analista de riesgo real.

## 📊 Resultados principales

| Métrica | Resultado |
|---|---|
| NPL Ratio | 2.36% |
| AUC-ROC (modelo PD, XGBoost) | 0.7147 |
| LGD promedio | 40.4% |
| Expected Loss del portafolio | 8.71% |
| EL en estrés (percentil 99, Monte Carlo) | +70% vs. escenario base |

## 🛠️ Stack técnico

- **Python:** Pandas, NumPy, scikit-learn, XGBoost, Matplotlib
- **Automatización:** APIs REST (requests), n8n
- **Control de versiones:** Git/GitHub

## 📁 Estructura del proyecto
notebooks/
├── 01_eda_npl_vintage.ipynb → EDA, NPL ratio, Vintage analysis
├── 02_pd_model.ipynb → Modelo de Probability of Default (XGBoost vs Regresión Logística)
├── 03_lgd_model.ipynb → Modelo de Loss Given Default
├── 04_expected_loss.ipynb → Expected Loss del portafolio (PD × LGD × EAD)
├── 05_pd_model_mejorado.ipynb → Feature Engineering aplicado al modelo de PD
├── 06_stress_testing.ipynb → Stress testing con simulación Monte Carlo
└── 07_api_bcra.ipynb → Integración con APIs externas

monitor_brecha.py → Script de automatización (consumo de API + reglas de negocio)

## 🔑 Conceptos aplicados

PD, LGD, EAD, Expected Loss, NPL, Vintage Analysis, Feature Engineering, AUC-ROC, Simulación Monte Carlo, Stress Testing, Automatización de procesos con APIs.

## ⚙️ Cómo reproducirlo

1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv` y activarlo
3. Instalar dependencias: `pip install pandas numpy scikit-learn xgboost matplotlib seaborn jupyter kaggle`
4. Descargar el dataset de [Lending Club en Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)
5. Correr los notebooks en orden (01 a 07)