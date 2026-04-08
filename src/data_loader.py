from typing import List, Dict

def load_data() -> List[Dict]:
    """Load sample tourist data"""
    return [
        {"name": "A", "age": 25, "location": "Beach", "spending": 200, "footfall": 120},
        {"name": "B", "age": 30, "location": "Hill", "spending": 300, "footfall": 150},
        {"name": "C", "age": 22, "location": "Beach", "spending": 150, "footfall": 180},
        {"name": "D", "age": 35, "location": "City", "spending": 400, "footfall": 200},
    ]