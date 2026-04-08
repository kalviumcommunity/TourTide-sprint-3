def moving_average(data, window=2):
    """Simple forecast using moving average"""
    footfall = [d["footfall"] for d in data]

    forecast = []

    for i in range(len(footfall)):
        if i < window:
            forecast.append(None)
        else:
            avg = sum(footfall[i-window:i]) / window
            forecast.append(avg)

    return forecast