import pandas as pd
import numpy as np

def create_sample_excel():
    np.random.seed(42)
    dates = pd.date_range(start="2026-01-01", periods=10, freq="ME")
    
    data = {
        "Date": dates,
        "Revenue": np.random.randint(50000, 120000, size=10),
        "Cost": np.random.randint(30000, 90000, size=10),
        "Supply_Delay_Days": np.random.choice([0, 1, 2, 3], size=10, p=[0.6, 0.2, 0.1, 0.1])
    }
    
    df = pd.DataFrame(data)
    file_name = "company_data.xlsx"
    df.to_excel(file_name, index=False)
    print(f"[{file_name}] file generated successfully!")

if __name__ == "__main__":
    create_sample_excel()
