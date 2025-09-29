# main.py
from data_loader import load_csv
from data_cleaner import clean_data
from summary import dataset_summary
from analysis import readmission_stats, average_stay, filter_by_medication
from utils import save_report



def main():
    filepath = "data/diabetic_data.csv"
    

    data = load_csv(filepath)
    if not data:
        return

    data = clean_data(data)

    
    summary = dataset_summary(data)
    print(" Dataset Summary:", summary)

    read_stats = readmission_stats(data)
    print(" Readmission Stats:", read_stats)

    
    avg_stay = average_stay(data)
    print(" Average Stay:", avg_stay)

   
    insulin_patients = filter_by_medication(data, "insulin")
    print(f" Patients on Insulin: {len(insulin_patients)}")

   
    full_report = {**summary, **read_stats, "Average Stay": avg_stay, "Insulin Patients": len(insulin_patients)}
    save_report(full_report, "analysis_report.txt")



if __name__ == "__main__":
    main()
