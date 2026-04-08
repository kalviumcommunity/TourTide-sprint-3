def group_by_location(data):
    """Group tourists by location"""
    result = {}

    for d in data:
        loc = d["location"]

        if loc not in result:
            result[loc] = []

        result[loc].append(d)

    return result


def calculate_total_spending(data):
    """Calculate total spending"""
    return sum(d["spending"] for d in data)