# analysis.py
from functools import reduce

def readmission_stats(data):
    
    total = len(data)

    readmitted = len(list(filter(lambda x: x["readmitted"] != "NO", data)))

    non_readmitted = total - readmitted

    return {"Readmitted": readmitted, "Not Readmitted": non_readmitted}

def average_stay(data):
   
    stays = list(map(lambda x: int(x["time_in_hospital"]), data))

    avg_stay = reduce(lambda a, b: a + b, stays) / len(stays)

    return round(avg_stay, 2)

def filter_by_medication(data, *medications):
   
    return list(filter(lambda x: any(x.get(med, "Unknown") != "No" for med in medications), data))


def search_by_patient(data, patient_id):
    
    visits = list(filter(lambda x: x["patient_nbr"] == str(patient_id), data))

    return visits


def readmission_by_diagnosis(data, diagnosis_code):
    
    diag_patients = list(filter(lambda x: x["diag_1"] == str(diagnosis_code), data))

    total = len(diag_patients)

    readmitted = len(list(filter(lambda x: x["readmitted"] != "NO", diag_patients)))
    
    return {"Total Patients": total, "Readmitted": readmitted}


