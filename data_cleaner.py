# data_cleaner.py

def clean_data(data):
    """
    Cleans dataset:
    - Strips spaces
    - Replaces missing values with 'Unknown'
    - Removes duplicates
    """
    cleaned = []
    seen = set()  # to remove duplicates

    for row in data:
        # Convert values
        row = {k.strip().lower(): (v.strip() if v.strip() != "?" else "Unknown") 
               for k, v in row.items()}

        # Use patient ID + encounter ID as unique key
        unique_key = (row.get("patient_nbr"), row.get("encounter_id"))

        if unique_key not in seen:
            cleaned.append(row)
            seen.add(unique_key)

    print(f"✅ Cleaned dataset: {len(cleaned)} unique records")
    return cleaned
