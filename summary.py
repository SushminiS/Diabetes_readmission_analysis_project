# summary.py

def dataset_summary(data):
    
    total_records = len(data)
    unique_patients = len(set([row["patient_nbr"] for row in data]))
    unique_hospitals = len(set([row["admission_type_id"] for row in data]))
    unique_diagnoses = len(set([row["diag_1"] for row in data]))

    return {
        "Total Records": total_records,
        "Unique Patients": unique_patients,
        "Unique Admission Types": unique_hospitals,
        "Unique Diagnoses": unique_diagnoses,
    }
