import requests
import pandas as pd
from datetime import datetime

def obtener_cotizaciones():
    """Consulta la API de DolarAPI y devuelve un DataFrame"""
    url = "https://dolarapi.com/v1/dolares"
    response = requests.get(url, timeout=15)
    response.raise_for_status()  # si falla la consulta, corta acá con un error claro
    return pd.DataFrame(response.json())

def calcular_brecha(df):
    """Calcula la brecha cambiaria entre oficial y blue"""
    oficial = df[df['casa'] == 'oficial']['venta'].values[0]
    blue = df[df['casa'] == 'blue']['venta'].values[0]
    brecha = (blue - oficial) / oficial * 100
    return oficial, blue, brecha

def evaluar_brecha(brecha):
    """Clasifica el nivel de alerta según la brecha"""
    if brecha < 10:
        return "NORMAL"
    elif brecha < 30:
        return "ATENCIÓN"
    else:
        return "ALERTA"

def main():
    print(f"=== Monitor de Brecha Cambiaria ===")
    print(f"Ejecutado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    df = obtener_cotizaciones()
    oficial, blue, brecha = calcular_brecha(df)
    estado = evaluar_brecha(brecha)

    print(f"Dólar oficial: ${oficial:,.2f}")
    print(f"Dólar blue: ${blue:,.2f}")
    print(f"Brecha cambiaria: {brecha:.2f}%")
    print(f"Estado: {estado}")

if __name__ == "__main__":
    main()