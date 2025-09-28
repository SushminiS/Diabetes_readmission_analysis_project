# analysis.py
from functools import reduce

def readmission_stats(data):
    """
    Counts readmitted vs non-readmitted.
    """
    total = len(data)
    readmitted = len(list(filter(lambda x: x["readmitted"] != "NO", data)))
    non_readmitted = total - readmitted
    return {"Readmitted": readmitted, "Not Readmitted": non_readmitted}

def average_stay(data):
    """
    Calculates average length of stay.
    """
    stays = list(map(lambda x: int(x["time_in_hospital"]), data))
    avg_stay = reduce(lambda a, b: a + b, stays) / len(stays)
    return round(avg_stay, 2)

def filter_by_medication(data, *medications):
    """
    Filters patients who were prescribed specific medications.
    """
    return list(filter(lambda x: any(x.get(med, "Unknown") != "No" for med in medications), data))
