# utils.py
from datetime import datetime

def save_report(report, filename="report.txt"):
    
    with open(f"reports/{filename}", "w") as f:

        f.write(f"Report generated: {datetime.now()}\n")

        for k, v in report.items():

            f.write(f"{k}: {v}\n")
            
    print(f" Report saved to reports/{filename}")
