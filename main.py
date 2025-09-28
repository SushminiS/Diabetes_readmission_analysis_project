# main.py
from data_loader import load_csv
from data_cleaner import clean_data
from summary import dataset_summary
from analysis import readmission_stats, average_stay, filter_by_medication
from utils import save_report

def main():
    filepath = "data/diabetic_data.csv"
    
    # Step 1: Load
    data = load_csv(filepath)
    if not data:
        return
    
    # Step 2: Clean
    data = clean_data(data)

    # Step 3: Summary
    summary = dataset_summary(data)
    print("📊 Dataset Summary:", summary)

    # Step 4: Readmission Stats
    read_stats = readmission_stats(data)
    print("📊 Readmission Stats:", read_stats)

    # Step 5: Average stay
    avg_stay = average_stay(data)
    print("📊 Average Stay:", avg_stay)

    # Step 6: Patients on insulin
    insulin_patients = filter_by_medication(data, "insulin")
    print(f"📊 Patients on Insulin: {len(insulin_patients)}")

    # Save everything in report
    full_report = {**summary, **read_stats, "Average Stay": avg_stay, "Insulin Patients": len(insulin_patients)}
    save_report(full_report, "analysis_report.txt")

if __name__ == "__main__":
    main()
