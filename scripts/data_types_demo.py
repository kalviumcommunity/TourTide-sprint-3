#!/usr/bin/env python3
"""
Python Data Types Demonstration

This script demonstrates Python's fundamental data types including:
- Integer and floating-point numeric types
- String data type and operations
- Type conversions and mismatches
- Proper usage patterns and behavior differences

Author: TourTide Development Team
Date: 2026-04-07
Purpose: Demonstrate clear understanding of Python data types
"""

def main():
    """Main function to demonstrate Python data types."""
    print("=" * 70)
    print("PYTHON DATA TYPES DEMONSTRATION")
    print("=" * 70)
    
    # Section 1: Numeric Data Types
    print("\n1. NUMERIC DATA TYPES")
    print("-" * 40)
    demonstrate_numeric_types()
    
    # Section 2: String Data Types
    print("\n2. STRING DATA TYPES")
    print("-" * 40)
    demonstrate_string_types()
    
    # Section 3: Type Operations and Conversions
    print("\n3. TYPE OPERATIONS AND CONVERSIONS")
    print("-" * 40)
    demonstrate_type_operations()
    
    # Section 4: Type Mismatches and Solutions
    print("\n4. TYPE MISMATCHES AND SOLUTIONS")
    print("-" * 40)
    demonstrate_type_mismatches()
    
    # Section 5: Real-world Examples
    print("\n5. REAL-WORLD TOURISM EXAMPLES")
    print("-" * 40)
    demonstrate_tourism_examples()
    
    print("\n" + "=" * 70)
    print("DATA TYPES DEMONSTRATION COMPLETED!")
    print("=" * 70)


def demonstrate_numeric_types():
    """Demonstrate integer and floating-point operations."""
    print("Creating numeric variables...")
    
    # Integer variables
    tour_guide_count = 15
    visitor_capacity = 250
    tour_duration_hours = 3
    available_buses = 8
    
    # Floating-point variables
    ticket_price = 45.99
    distance_km = 12.5
    satisfaction_score = 4.7
    average_spending = 125.75
    
    print(f"\nInteger Variables:")
    print(f"  Tour Guides: {tour_guide_count} (type: {type(tour_guide_count)})")
    print(f"  Visitor Capacity: {visitor_capacity} (type: {type(visitor_capacity)})")
    print(f"  Tour Duration: {tour_duration_hours} hours (type: {type(tour_duration_hours)})")
    print(f"  Available Buses: {available_buses} (type: {type(available_buses)})")
    
    print(f"\nFloating-point Variables:")
    print(f"  Ticket Price: ${ticket_price} (type: {type(ticket_price)})")
    print(f"  Distance: {distance_km} km (type: {type(distance_km)})")
    print(f"  Satisfaction Score: {satisfaction_score} (type: {type(satisfaction_score)})")
    print(f"  Average Spending: ${average_spending} (type: {type(average_spending)})")
    
    # Arithmetic operations on integers
    print(f"\nInteger Arithmetic Operations:")
    total_capacity = visitor_capacity * available_buses
    tours_per_day = available_buses * 3  # 3 tours per bus per day
    total_guides_needed = tours_per_day // tour_guide_count  # Integer division
    
    print(f"  Total Capacity: {visitor_capacity} × {available_buses} = {total_capacity}")
    print(f"  Tours Per Day: {available_buses} × 3 = {tours_per_day}")
    print(f"  Guides Needed (floor division): {tours_per_day} // {tour_guide_count} = {total_guides_needed}")
    
    # Arithmetic operations on floats
    print(f"\nFloating-point Arithmetic Operations:")
    daily_revenue = ticket_price * visitor_capacity
    cost_per_km = average_spending / distance_km
    rounded_satisfaction = round(satisfaction_score, 1)
    
    print(f"  Daily Revenue: ${ticket_price} × {visitor_capacity} = ${daily_revenue:.2f}")
    print(f"  Cost per Km: ${average_spending} ÷ {distance_km} = ${cost_per_km:.2f}")
    print(f"  Rounded Satisfaction: round({satisfaction_score}, 1) = {rounded_satisfaction}")
    
    # Mixed operations
    print(f"\nMixed Type Operations:")
    total_daily_income = ticket_price * visitor_capacity * available_buses
    average_tour_income = total_daily_income / tours_per_day
    
    print(f"  Total Daily Income: ${ticket_price} × {visitor_capacity} × {available_buses} = ${total_daily_income:.2f}")
    print(f"  Average Tour Income: ${total_daily_income:.2f} ÷ {tours_per_day} = ${average_tour_income:.2f}")


def demonstrate_string_types():
    """Demonstrate string operations and formatting."""
    print("Creating string variables...")
    
    # String variables
    tourist_name = "Sarah Johnson"
    tour_location = "Historic Downtown"
    tour_type = "Walking Tour"
    guide_name = "Michael Chen"
    weather_condition = "Sunny and Warm"
    
    print(f"\nString Variables:")
    print(f"  Tourist Name: '{tourist_name}' (type: {type(tourist_name)})")
    print(f"  Tour Location: '{tour_location}' (type: {type(tour_location)})")
    print(f"  Tour Type: '{tour_type}' (type: {type(tour_type)})")
    print(f"  Guide Name: '{guide_name}' (type: {type(guide_name)})")
    print(f"  Weather: '{weather_condition}' (type: {type(weather_condition)})")
    
    # String concatenation
    print(f"\nString Concatenation:")
    full_description = tour_location + " - " + tour_type
    booking_reference = "TOUR-" + "2023" + "-" + "0415"
    welcome_message = "Welcome, " + tourist_name + "!"
    
    print(f"  Full Description: '{tour_location}' + ' - ' + '{tour_type}' = '{full_description}'")
    print(f"  Booking Reference: 'TOUR-' + '2023' + '-' + '0415' = '{booking_reference}'")
    print(f"  Welcome Message: 'Welcome, ' + '{tourist_name}' + '!' = '{welcome_message}'")
    
    # String formatting with f-strings
    print(f"\nString Formatting (f-strings):")
    formatted_description = f"{tour_type} of {tour_location} with guide {guide_name}"
    weather_report = f"Weather: {weather_condition} for today's {tour_type}"
    tour_summary = f"Tour: {tour_location} | Type: {tour_type} | Guide: {guide_name}"
    
    print(f"  Formatted Description: '{formatted_description}'")
    print(f"  Weather Report: '{weather_report}'")
    print(f"  Tour Summary: '{tour_summary}'")
    
    # String methods
    print(f"\nString Methods:")
    uppercase_location = tour_location.upper()
    lowercase_name = tourist_name.lower()
    title_case = tour_type.title()
    location_length = len(tour_location)
    contains_word = "Historic" in tour_location
    
    print(f"  Uppercase Location: '{tour_location}'.upper() = '{uppercase_location}'")
    print(f"  Lowercase Name: '{tourist_name}'.lower() = '{lowercase_name}'")
    print(f"  Title Case: '{tour_type}'.title() = '{title_case}'")
    print(f"  Location Length: len('{tour_location}') = {location_length}")
    print(f"  Contains 'Historic': 'Historic' in '{tour_location}' = {contains_word}")
    
    # String slicing
    print(f"\nString Slicing:")
    first_name = tourist_name[:5]  # First 5 characters
    last_name = tourist_name[6:]   # From 6th character to end
    location_code = tour_location[:8]  # First 8 characters
    
    print(f"  First Name: '{tourist_name}'[:5] = '{first_name}'")
    print(f"  Last Name: '{tourist_name}'[6:] = '{last_name}'")
    print(f"  Location Code: '{tour_location}'[:8] = '{location_code}'")


def demonstrate_type_operations():
    """Demonstrate type operations and conversions."""
    print("Exploring type operations and conversions...")
    
    # Original variables
    visitor_age = 35  # Integer
    ticket_cost = 45.99  # Float
    visitor_id = "A1234"  # String
    rating = "4.7"  # String that looks like a number
    
    print(f"\nOriginal Variables:")
    print(f"  Visitor Age: {visitor_age} (type: {type(visitor_age)})")
    print(f"  Ticket Cost: ${ticket_cost} (type: {type(ticket_cost)})")
    print(f"  Visitor ID: '{visitor_id}' (type: {type(visitor_id)})")
    print(f"  Rating: '{rating}' (type: {type(rating)})")
    
    # Type conversions
    print(f"\nType Conversions:")
    
    # Integer to string
    age_as_string = str(visitor_age)
    print(f"  Age as String: str({visitor_age}) = '{age_as_string}' (type: {type(age_as_string)})")
    
    # Float to integer
    cost_as_integer = int(ticket_cost)
    print(f"  Cost as Integer: int({ticket_cost}) = {cost_as_integer} (type: {type(cost_as_integer)})")
    
    # String to integer
    rating_as_integer = int(float(rating))  # Convert string to float first, then to int
    print(f"  Rating as Integer: int(float('{rating}')) = {rating_as_integer} (type: {type(rating_as_integer)})")
    
    # String to float
    rating_as_float = float(rating)
    print(f"  Rating as Float: float('{rating}') = {rating_as_float} (type: {type(rating_as_float)})")
    
    # Type checking
    print(f"\nType Checking:")
    print(f"  isinstance(visitor_age, int): {isinstance(visitor_age, int)}")
    print(f"  isinstance(ticket_cost, float): {isinstance(ticket_cost, float)}")
    print(f"  isinstance(visitor_id, str): {isinstance(visitor_id, str)}")
    print(f"  isinstance(rating, str): {isinstance(rating, str)}")
    
    # Dynamic typing demonstration
    print(f"\nDynamic Typing Demonstration:")
    dynamic_variable = 42
    print(f"  Initial: dynamic_variable = {dynamic_variable} (type: {type(dynamic_variable)})")
    
    dynamic_variable = "Forty-two"
    print(f"  Changed: dynamic_variable = '{dynamic_variable}' (type: {type(dynamic_variable)})")
    
    dynamic_variable = 42.0
    print(f"  Changed: dynamic_variable = {dynamic_variable} (type: {type(dynamic_variable)})")


def demonstrate_type_mismatches():
    """Demonstrate common type mismatches and their solutions."""
    print("Exploring type mismatches and solutions...")
    
    # Example 1: Trying to add string and number
    print(f"\nExample 1: String + Number Mismatch")
    visitor_count = 25
    location_name = "Downtown"
    
    try:
        # This will cause a TypeError
        result = location_name + visitor_count
        print(f"  Result: {result}")
    except TypeError as e:
        print(f"  Error: {e}")
        print(f"  Solution: Convert number to string first")
        corrected_result = location_name + str(visitor_count)
        print(f"  Corrected: '{location_name}' + str({visitor_count}) = '{corrected_result}'")
    
    # Example 2: Trying to perform arithmetic on string numbers
    print(f"\nExample 2: Arithmetic on String Numbers")
    price_string = "45.99"
    quantity = 3
    
    try:
        # This will cause a TypeError
        total = price_string * quantity
        print(f"  Result: {total}")
    except TypeError as e:
        print(f"  Error: {e}")
        print(f"  Solution: Convert string to number first")
        corrected_total = float(price_string) * quantity
        print(f"  Corrected: float('{price_string}') × {quantity} = ${corrected_total:.2f}")
    
    # Example 3: String multiplication (valid but different behavior)
    print(f"\nExample 3: String Multiplication (Valid Operation)")
    tour_name = "Tour"
    repeat_times = 3
    
    string_multiplication = tour_name * repeat_times
    print(f"  String Multiplication: '{tour_name}' × {repeat_times} = '{string_multiplication}'")
    print(f"  Note: This repeats the string, not mathematical multiplication")
    
    # Example 4: Division with integers
    print(f"\nExample 4: Integer Division Behavior")
    total_visitors = 25
    buses = 4
    
    # Regular division (produces float)
    regular_division = total_visitors / buses
    print(f"  Regular Division: {total_visitors} / {buses} = {regular_division} (type: {type(regular_division)})")
    
    # Integer division (produces integer)
    integer_division = total_visitors // buses
    print(f"  Integer Division: {total_visitors} // {buses} = {integer_division} (type: {type(integer_division)})")
    
    # Modulo operation
    remainder = total_visitors % buses
    print(f"  Remainder: {total_visitors} % {buses} = {remainder} (type: {type(remainder)})")


def demonstrate_tourism_examples():
    """Demonstrate real-world tourism data type examples."""
    print("Real-world tourism data type examples...")
    
    # Tour booking system
    print(f"\nTour Booking System Example:")
    
    booking_id = "BK2023041501"  # String
    tourist_age = 28  # Integer
    ticket_price = 75.50  # Float
    tour_name = "Sunset City Tour"  # String
    group_size = 4  # Integer
    special_requirements = "Vegetarian lunch needed"  # String
    
    print(f"  Booking ID: {booking_id} ({type(booking_id).__name__})")
    print(f"  Tourist Age: {tourist_age} years ({type(tourist_age).__name__})")
    print(f"  Ticket Price: ${ticket_price} ({type(ticket_price).__name__})")
    print(f"  Tour Name: {tour_name} ({type(tour_name).__name__})")
    print(f"  Group Size: {group_size} people ({type(group_size).__name__})")
    print(f"  Special Requirements: {special_requirements} ({type(special_requirements).__name__})")
    
    # Calculations
    total_cost = ticket_price * group_size
    age_group = "Adult" if tourist_age >= 18 else "Child"
    booking_reference = f"{booking_id}-{tourist_age}-{group_size}"
    
    print(f"\n  Calculated Values:")
    print(f"  Total Cost: ${ticket_price} × {group_size} = ${total_cost:.2f}")
    print(f"  Age Group: {'Adult' if tourist_age >= 18 else 'Child'}")
    print(f"  Booking Reference: '{booking_reference}'")
    
    # Tour rating system
    print(f"\nTour Rating System Example:")
    
    rating_count = 150  # Integer
    average_rating = 4.7  # Float
    rating_comment = "Excellent tour guide!"  # String
    recommend_percentage = 92.5  # Float
    
    print(f"  Rating Count: {rating_count} ratings")
    print(f"  Average Rating: {average_rating} stars")
    print(f"  Sample Comment: '{rating_comment}'")
    print(f"  Recommend Percentage: {recommend_percentage}%")
    
    # Formatted summary
    rating_summary = f"Tour '{tour_name}' has {rating_count} ratings with an average of {average_rating} stars. {recommend_percentage}% would recommend."
    print(f"  Summary: '{rating_summary}'")
    
    # Data validation example
    print(f"\nData Validation Example:")
    
    input_age = "25"  # String input from user
    input_price = "50.00"  # String input from user
    
    try:
        # Convert and validate
        validated_age = int(input_age)
        validated_price = float(input_price)
        
        # Validation checks
        age_valid = 0 <= validated_age <= 120
        price_valid = validated_price > 0
        
        print(f"  Input Age: '{input_age}' -> {validated_age} (Valid: {age_valid})")
        print(f"  Input Price: '${input_price}' -> ${validated_price:.2f} (Valid: {price_valid})")
        
        if age_valid and price_valid:
            print(f"  Validation: PASSED - Both inputs are valid")
        else:
            print(f"  Validation: FAILED - Invalid input detected")
            
    except ValueError as e:
        print(f"  Validation Error: {e}")


if __name__ == "__main__":
    """Entry point of the script."""
    print("Starting Python Data Types Demonstration...")
    print("This script will demonstrate numeric and string data types, operations, and conversions.")
    
    try:
        main()
    except Exception as e:
        print(f"Error occurred during demonstration: {e}")
        exit(1)
    
    print("\nData types demonstration completed successfully!")
    print("This demonstrates clear understanding of Python data types and their proper usage.")
