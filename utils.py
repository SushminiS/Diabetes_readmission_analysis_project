# utils.py
from datetime import datetime

def save_report(report, filename="report.txt"):
    """
    Saves dictionary report into a file with timestamp.
    """
    with open(f"reports/{filename}", "w") as f:
        f.write(f"Report generated: {datetime.now()}\n\n")
        for k, v in report.items():
            f.write(f"{k}: {v}\n")
    print(f"📄 Report saved to reports/{filename}")
