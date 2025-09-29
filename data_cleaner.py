# data_cleaner.py

def clean_data(data):
    """
    Cleans dataset:
    - Strips spaces
    - Replaces missing values with 'Unknown'
    - Removes duplicates
    """
    cleaned = []

    seen = set()  

    for row in data:
        
        row = {k.strip().lower(): (v.strip() if v.strip() != "?" else "Unknown") 
               
               for k, v in row.items()}

       
        unique_key = (row.get("patient_nbr"), row.get("encounter_id"))


        if unique_key not in seen:

            cleaned.append(row)

            seen.add(unique_key)

    print(f" Cleaned dataset: {len(cleaned)} unique records")
    
    return cleaned
