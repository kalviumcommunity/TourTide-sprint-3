#!/usr/bin/env python3
"""
Tourist Data Analyzer - Basic Data Analysis Script

This script demonstrates basic Python data operations for tourist data analysis.
It shows simple data processing, calculations, and output generation.

Author: TourTide Development Team
Date: 2026-04-06
Purpose: Demonstrate Python script creation and execution flow
"""

import datetime
from typing import List, Dict


def main():
    """Main function to execute the tourist data analysis."""
    print("=" * 60)
    print("TOURIST DATA ANALYZER - Basic Data Analysis Script")
    print("=" * 60)
    
    # Step 1: Data Initialization
    print("\n📊 Step 1: Initializing Tourist Data...")
    tourist_data = initialize_tourist_data()
    print(f"✓ Loaded {len(tourist_data)} tourist records")
    
    # Step 2: Basic Data Analysis
    print("\n🔍 Step 2: Performing Basic Data Analysis...")
    analysis_results = analyze_tourist_data(tourist_data)
    print("✓ Data analysis completed")
    
    # Step 3: Data Aggregation
    print("\n📈 Step 3: Aggregating Data by Location...")
    location_summary = aggregate_by_location(tourist_data)
    print("✓ Data aggregation completed")
    
    # Step 4: Results Display
    print("\n📋 Step 4: Displaying Analysis Results...")
    display_results(analysis_results, location_summary)
    
    # Step 5: Summary Report
    print("\n📄 Step 5: Generating Summary Report...")
    generate_summary_report(tourist_data, analysis_results)
    
    print("\n" + "=" * 60)
    print("🎉 Tourist Data Analysis Completed Successfully!")
    print("=" * 60)


def initialize_tourist_data() -> List[Dict]:
    """
    Initialize sample tourist data for demonstration.
    
    Returns:
        List[Dict]: List of tourist data records
    """
    print("  - Creating sample tourist dataset...")
    
    # Sample tourist data with various attributes
    tourist_data = [
        {
            "id": 1,
            "name": "John Smith",
            "age": 35,
            "location": "Downtown",
            "duration_days": 3,
            "spending": 450.75,
            "group_size": 2,
            "visit_date": "2023-01-15"
        },
        {
            "id": 2,
            "name": "Emily Johnson",
            "age": 28,
            "location": "Historic District",
            "duration_days": 2,
            "spending": 280.50,
            "group_size": 1,
            "visit_date": "2023-01-16"
        },
        {
            "id": 3,
            "name": "Michael Brown",
            "age": 42,
            "location": "Downtown",
            "duration_days": 5,
            "spending": 890.25,
            "group_size": 4,
            "visit_date": "2023-01-17"
        },
        {
            "id": 4,
            "name": "Sarah Davis",
            "age": 31,
            "location": "Waterfront",
            "duration_days": 2,
            "spending": 320.00,
            "group_size": 2,
            "visit_date": "2023-01-18"
        },
        {
            "id": 5,
            "name": "Robert Wilson",
            "age": 55,
            "location": "Historic District",
            "duration_days": 4,
            "spending": 675.80,
            "group_size": 2,
            "visit_date": "2023-01-19"
        },
        {
            "id": 6,
            "name": "Lisa Anderson",
            "age": 29,
            "location": "Downtown",
            "duration_days": 1,
            "spending": 125.30,
            "group_size": 1,
            "visit_date": "2023-01-20"
        },
        {
            "id": 7,
            "name": "David Martinez",
            "age": 38,
            "location": "Waterfront",
            "duration_days": 3,
            "spending": 410.60,
            "group_size": 3,
            "visit_date": "2023-01-21"
        },
        {
            "id": 8,
            "name": "Jennifer Taylor",
            "age": 26,
            "location": "Historic District",
            "duration_days": 2,
            "spending": 195.25,
            "group_size": 1,
            "visit_date": "2023-01-22"
        }
    ]
    
    print("  - Sample dataset created with 8 tourist records")
    return tourist_data


def analyze_tourist_data(data: List[Dict]) -> Dict:
    """
    Perform basic statistical analysis on tourist data.
    
    Args:
        data (List[Dict]): Tourist data records
        
    Returns:
        Dict: Analysis results with various statistics
    """
    print("  - Calculating basic statistics...")
    
    # Extract numeric data for calculations
    ages = [record["age"] for record in data]
    durations = [record["duration_days"] for record in data]
    spending = [record["spending"] for record in data]
    group_sizes = [record["group_size"] for record in data]
    
    # Calculate basic statistics
    analysis_results = {
        "total_tourists": len(data),
        "age_statistics": calculate_statistics(ages, "Age"),
        "duration_statistics": calculate_statistics(durations, "Duration (days)"),
        "spending_statistics": calculate_statistics(spending, "Spending ($)"),
        "group_size_statistics": calculate_statistics(group_sizes, "Group Size"),
        "total_spending": sum(spending),
        "average_spending_per_tourist": sum(spending) / len(spending),
        "total_visitor_days": sum(durations),
        "unique_locations": len(set(record["location"] for record in data))
    }
    
    print(f"  - Analyzed {len(data)} tourist records")
    return analysis_results


def calculate_statistics(values: List[float], metric_name: str) -> Dict:
    """
    Calculate basic statistics for a list of values.
    
    Args:
        values (List[float]): List of numeric values
        metric_name (str): Name of the metric
        
    Returns:
        Dict: Statistical measures
    """
    if not values:
        return {"name": metric_name, "count": 0}
    
    sorted_values = sorted(values)
    count = len(values)
    total = sum(values)
    average = total / count
    minimum = min(values)
    maximum = max(values)
    
    # Calculate median
    if count % 2 == 0:
        median = (sorted_values[count // 2 - 1] + sorted_values[count // 2]) / 2
    else:
        median = sorted_values[count // 2]
    
    return {
        "name": metric_name,
        "count": count,
        "total": total,
        "average": round(average, 2),
        "median": median,
        "minimum": minimum,
        "maximum": maximum,
        "range": maximum - minimum
    }


def aggregate_by_location(data: List[Dict]) -> Dict:
    """
    Aggregate tourist data by location.
    
    Args:
        data (List[Dict]): Tourist data records
        
    Returns:
        Dict: Location-wise aggregated data
    """
    print("  - Grouping data by location...")
    
    location_data = {}
    
    for record in data:
        location = record["location"]
        
        if location not in location_data:
            location_data[location] = {
                "tourists": [],
                "total_spending": 0,
                "total_duration": 0,
                "total_group_size": 0
            }
        
        location_data[location]["tourists"].append(record)
        location_data[location]["total_spending"] += record["spending"]
        location_data[location]["total_duration"] += record["duration_days"]
        location_data[location]["total_group_size"] += record["group_size"]
    
    # Calculate summary statistics for each location
    location_summary = {}
    
    for location, data in location_data.items():
        tourist_count = len(data["tourists"])
        avg_spending = data["total_spending"] / tourist_count
        avg_duration = data["total_duration"] / tourist_count
        avg_group_size = data["total_group_size"] / tourist_count
        
        location_summary[location] = {
            "tourist_count": tourist_count,
            "total_spending": round(data["total_spending"], 2),
            "average_spending": round(avg_spending, 2),
            "total_duration": data["total_duration"],
            "average_duration": round(avg_duration, 2),
            "average_group_size": round(avg_group_size, 2)
        }
    
    print(f"  - Aggregated data for {len(location_summary)} locations")
    return location_summary


def display_results(analysis_results: Dict, location_summary: Dict):
    """Display analysis results in a formatted way."""
    
    # Display overall statistics
    print("\n📊 OVERALL STATISTICS:")
    print("-" * 40)
    print(f"Total Tourists: {analysis_results['total_tourists']}")
    print(f"Unique Locations: {analysis_results['unique_locations']}")
    print(f"Total Spending: ${analysis_results['total_spending']:.2f}")
    print(f"Average Spending per Tourist: ${analysis_results['average_spending_per_tourist']:.2f}")
    print(f"Total Visitor Days: {analysis_results['total_visitor_days']}")
    
    # Display detailed statistics
    print("\n📈 DETAILED STATISTICS:")
    print("-" * 40)
    
    stats_categories = [
        analysis_results["age_statistics"],
        analysis_results["duration_statistics"],
        analysis_results["spending_statistics"],
        analysis_results["group_size_statistics"]
    ]
    
    for stats in stats_categories:
        print(f"\n{stats['name']}:")
        print(f"  Count: {stats['count']}")
        print(f"  Average: {stats['average']}")
        print(f"  Median: {stats['median']}")
        print(f"  Range: {stats['minimum']} - {stats['maximum']}")
    
    # Display location summary
    print("\n🏢 LOCATION SUMMARY:")
    print("-" * 40)
    
    for location, summary in location_summary.items():
        print(f"\n{location}:")
        print(f"  Tourists: {summary['tourist_count']}")
        print(f"  Total Spending: ${summary['total_spending']}")
        print(f"  Average Spending: ${summary['average_spending']}")
        print(f"  Average Duration: {summary['average_duration']} days")
        print(f"  Average Group Size: {summary['average_group_size']}")


def generate_summary_report(data: List[Dict], analysis_results: Dict):
    """Generate a summary report of the analysis."""
    
    print("\n📄 SUMMARY REPORT:")
    print("-" * 40)
    
    # Find top spending tourist
    top_spender = max(data, key=lambda x: x["spending"])
    
    # Find longest staying tourist
    longest_stay = max(data, key=lambda x: x["duration_days"])
    
    # Find most popular location
    location_counts = {}
    for record in data:
        location = record["location"]
        location_counts[location] = location_counts.get(location, 0) + 1
    
    most_popular = max(location_counts, key=location_counts.get)
    
    print(f"🏆 Top Spender: {top_spender['name']} (${top_spender['spending']})")
    print(f"⏰ Longest Stay: {longest_stay['name']} ({longest_stay['duration_days']} days)")
    print(f"📍 Most Popular Location: {most_popular} ({location_counts[most_popular]} tourists)")
    
    # Calculate additional insights
    weekend_tourists = sum(1 for record in data if record["group_size"] >= 3)
    solo_tourists = sum(1 for record in data if record["group_size"] == 1)
    
    print(f"👥 Group Tourists (3+ people): {weekend_tourists}")
    print(f"👤 Solo Tourists: {solo_tourists}")
    
    # Performance metrics
    print(f"\n📊 PERFORMANCE METRICS:")
    print(f"  Records Processed: {len(data)}")
    print(f"  Processing Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Script Status: SUCCESS ✅")


if __name__ == "__main__":
    """Entry point of the script."""
    print("Starting Tourist Data Analyzer...")
    print("Script execution flow: Initialization → Analysis → Aggregation → Results → Report")
    
    try:
        main()
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        exit(1)
    
    print("\nScript execution completed successfully!")
    print("This demonstrates basic Python script creation and data analysis capabilities.")
