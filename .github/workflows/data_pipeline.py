import pandas as pd
import requests
from pathlib import Path

# Fetch sample CSV
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
r = requests.get(url)
csv_path = Path("data/airtravel.csv")
csv_path.parent.mkdir(parents=True, exist_ok=True)
csv_path.write_bytes(r.content)

# Load & process
df = pd.read_csv(csv_path)
df["TOTAL"] = df.iloc[:, 1:].sum(axis=1)

# Save output
output_path = Path("output/processed_data.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Processed data saved to {output_path}")
