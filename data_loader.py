# data_loader.py
import csv

def load_csv(filepath):
    """
    Loads a CSV file and returns a list of dictionaries.
    """
    data = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        print(f"✅ Loaded {len(data)} records from {filepath}")
        return data
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return []
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return []
