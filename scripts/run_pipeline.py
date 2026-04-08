from src.data_loader import load_data
from src.preprocessing import group_by_location, calculate_total_spending
from src.forecasting import moving_average


def main():
    # Step 1: Load data
    data = load_data()

    # Step 2: Process data
    grouped = group_by_location(data)
    total_spending = calculate_total_spending(data)

    # Step 3: Forecast
    forecast = moving_average(data)

    # Step 4: Output
    print("\n=== RESULTS ===")
    print("Total tourists:", len(data))
    print("Total spending:", total_spending)

    print("\nGrouped Data:")
    for k, v in grouped.items():
        print(k, ":", len(v))

    print("\nForecast:", forecast)


if __name__ == "__main__":
    main()