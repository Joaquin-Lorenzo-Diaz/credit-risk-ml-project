import requests
import pandas as pd
from datetime import datetime

def get_rates():
    """Query DolarAPI and return the exchange rates as a DataFrame."""
    url = "https://dolarapi.com/v1/dolares"
    response = requests.get(url, timeout=15)
    response.raise_for_status()  # stop here with a clear error if the request failed
    return pd.DataFrame(response.json())

def compute_gap(df):
    """Compute the FX gap (%) between the blue and the official dollar."""
    official = df[df['casa'] == 'oficial']['venta'].values[0]
    blue = df[df['casa'] == 'blue']['venta'].values[0]
    gap = (blue - official) / official * 100
    return official, blue, gap

def evaluate_gap(gap):
    """Classify the alert level from the FX gap.
    The thresholds (10% / 30%) are illustrative, not calibrated on historical data."""
    if gap < 10:
        return "NORMAL"
    elif gap < 30:
        return "WARNING"
    else:
        return "ALERT"

def main():
    print("=== FX Gap Monitor ===")
    print(f"Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    df = get_rates()
    official, blue, gap = compute_gap(df)
    status = evaluate_gap(gap)

    print(f"Official USD: ${official:,.2f}")
    print(f"Blue USD: ${blue:,.2f}")
    print(f"FX gap: {gap:.2f}%")
    print(f"Status: {status}")

if __name__ == "__main__":
    main()
