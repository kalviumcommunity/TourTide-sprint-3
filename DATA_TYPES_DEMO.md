# Python Data Types Demonstration

This document provides comprehensive evidence of Python data type understanding and usage for the TourTide project.

## Script Overview

### **File Created**: `scripts/data_types_demo.py`

A complete Python script that demonstrates:
- Integer and floating-point numeric operations
- String operations and formatting
- Type conversions and mismatches
- Proper data type usage patterns
- Real-world tourism examples

## Script Execution Evidence

### **Successful Execution Output**
```
Starting Python Data Types Demonstration...
This script will demonstrate numeric and string data types, operations, and conversions.
======================================================================
PYTHON DATA TYPES DEMONSTRATION
======================================================================

1. NUMERIC DATA TYPES
----------------------------------------
Creating numeric variables...

Integer Variables:
  Tour Guides: 15 (type: <class 'int'>)
  Visitor Capacity: 250 (type: <class 'int'>)
  Tour Duration: 3 hours (type: <class 'int'>)
  Available Buses: 8 (type: <class 'int'>)

Floating-point Variables:
  Ticket Price: $45.99 (type: <class 'float'>)
  Distance: 12.5 km (type: <class 'float'>)
  Satisfaction Score: 4.7 (type: <class 'float'>)
  Average Spending: $125.75 (type: <class 'float'>)

Integer Arithmetic Operations:
  Total Capacity: 250 × 8 = 2000
  Tours Per Day: 8 × 3 = 24
  Guides Needed (floor division): 24 // 15 = 1

Floating-point Arithmetic Operations:
  Daily Revenue: $45.99 × 250 = $11497.50
  Cost per Km: $125.75 ÷ 12.5 = $10.06
  Rounded Satisfaction: round(4.7, 1) = 4.7

Mixed Type Operations:
  Total Daily Income: $45.99 × 250 × 8 = $91980.00
  Average Tour Income: $91980.00 ÷ 24 = $3832.50

2. STRING DATA TYPES
----------------------------------------
Creating string variables...

String Variables:
  Tourist Name: 'Sarah Johnson' (type: <class 'str'>)
  Tour Location: 'Historic Downtown' (type: <class 'str'>)
  Tour Type: 'Walking Tour' (type: <class 'str'>)
  Guide Name: 'Michael Chen' (type: <class 'str'>)
  Weather: 'Sunny and Warm' (type: <class 'str'>)

String Concatenation:
  Full Description: 'Historic Downtown' + ' - ' + 'Walking Tour' = 'Historic Downtown - Walking Tour'
  Booking Reference: 'TOUR-' + '2023' + '-' + '0415' = 'TOUR-2023-0415'
  Welcome Message: 'Welcome, ' + 'Sarah Johnson' + '!' = 'Welcome, Sarah Johnson!'

String Formatting (f-strings):
  Formatted Description: 'Walking Tour of Historic Downtown with guide Michael Chen'
  Weather Report: 'Weather: Sunny and Warm for today's Walking Tour'
  Tour Summary: 'Tour: Historic Downtown | Type: Walking Tour | Guide: Michael Chen'

String Methods:
  Uppercase Location: 'Historic Downtown'.upper() = 'HISTORIC DOWNTOWN'
  Lowercase Name: 'Sarah Johnson'.lower() = 'sarah johnson'
  Title Case: 'Walking Tour'.title() = 'Walking Tour'
  Location Length: len('Historic Downtown') = 17
  Contains 'Historic': 'Historic' in 'Historic Downtown' = True

String Slicing:
  First Name: 'Sarah Johnson'[:5] = 'Sarah'
  Last Name: 'Sarah Johnson'[6:] = 'Johnson'
  Location Code: 'Historic Downtown'[:8] = 'Historic'

3. TYPE OPERATIONS AND CONVERSIONS
----------------------------------------
Exploring type operations and conversions...

Original Variables:
  Visitor Age: 35 (type: <class 'int'>)
  Ticket Cost: $45.99 (type: <class 'float'>)
  Visitor ID: 'A1234' (type: <class 'str'>)
  Rating: '4.7' (type: <class 'str'>)

Type Conversions:
  Age as String: str(35) = '35' (type: <class 'str'>)
  Cost as Integer: int(45.99) = 45 (type: <class 'int'>)
  Rating as Integer: int(float('4.7')) = 4 (type: <class 'int'>)
  Rating as Float: float('4.7') = 4.7 (type: <class 'float'>)

Type Checking:
  isinstance(visitor_age, int): True
  isinstance(ticket_cost, float): True
  isinstance(visitor_id, str): True
  isinstance(rating, str): True

Dynamic Typing Demonstration:
  Initial: dynamic_variable = 42 (type: <class 'int'>)
  Changed: dynamic_variable = 'Forty-two' (type: <class 'str'>)
  Changed: dynamic_variable = 42.0 (type: <class 'float'>)

4. TYPE MISMATCHES AND SOLUTIONS
----------------------------------------
Exploring type mismatches and solutions...

Example 1: String + Number Mismatch
  Error: can only concatenate str (not "int") to str
  Solution: Convert number to string first
  Corrected: 'Downtown' + str(25) = 'Downtown25'

Example 2: Arithmetic on String Numbers
  Error: can't multiply sequence by non-int of type 'float'
  Solution: Convert string to number first
  Corrected: float('45.99') × 3 = $137.97

Example 3: String Multiplication (Valid Operation)
  String Multiplication: 'Tour' × 3 = 'TourTourTour'
  Note: This repeats the string, not mathematical multiplication

Example 4: Integer Division Behavior
  Regular Division: 25 / 4 = 6.25 (type: <class 'float'>)
  Integer Division: 25 // 4 = 6 (type: <class 'int'>)
  Remainder: 25 % 4 = 1 (type: <class 'int'>)

5. REAL-WORLD TOURISM EXAMPLES
----------------------------------------
Real-world tourism data type examples...

Tour Booking System Example:
  Booking ID: BK2023041501 (str)
  Tourist Age: 28 years (int)
  Ticket Price: $75.5 (float)
  Tour Name: Sunset City Tour (str)
  Group Size: 4 people (int)
  Special Requirements: Vegetarian lunch needed (str)

  Calculated Values:
  Total Cost: $75.5 × 4 = $302.00
  Age Group: Adult
  Booking Reference: 'BK2023041501-28-4'

Tour Rating System Example:
  Rating Count: 150 ratings
  Average Rating: 4.7 stars
  Sample Comment: 'Excellent tour guide!'
  Recommend Percentage: 92.5%
  Summary: 'Tour 'Sunset City Tour' has 150 ratings with an average of 4.7 stars. 92.5% would recommend.'

Data Validation Example:
  Input Age: '25' -> 25 (Valid: True)
  Input Price: '$50.00' -> $50.00 (Valid: True)
  Validation: PASSED - Both inputs are valid

======================================================================
DATA TYPES DEMONSTRATION COMPLETED!
======================================================================

Data types demonstration completed successfully!
This demonstrates clear understanding of Python data types and their proper usage.
```

## Data Type Requirements Demonstrated

### **1. Integer and Floating-point Variables** 

#### **Integer Variables**
```python
tour_guide_count = 15           # Whole numbers for counting
visitor_capacity = 250          # Discrete quantities
tour_duration_hours = 3          # Time in whole units
available_buses = 8             # Countable items
```

#### **Floating-point Variables**
```python
ticket_price = 45.99            # Currency with decimals
distance_km = 12.5              # Measurements with precision
satisfaction_score = 4.7        # Ratings with decimal precision
average_spending = 125.75       # Financial calculations
```

### **2. String Variables with Meaningful Values**

#### **Tourism-related Strings**
```python
tourist_name = "Sarah Johnson"          # Person names
tour_location = "Historic Downtown"    # Location names
tour_type = "Walking Tour"             # Tour categories
guide_name = "Michael Chen"            # Staff names
weather_condition = "Sunny and Warm"   # Descriptive text
```

### **3. Arithmetic Operations on Numeric Types**

#### **Integer Operations**
```python
total_capacity = visitor_capacity * available_buses      # Multiplication
tours_per_day = available_buses * 3                      # Multiplication
total_guides_needed = tours_per_day // tour_guide_count # Floor division
```

#### **Floating-point Operations**
```python
daily_revenue = ticket_price * visitor_capacity         # Multiplication
cost_per_km = average_spending / distance_km           # Division
rounded_satisfaction = round(satisfaction_score, 1)     # Rounding
```

#### **Mixed Type Operations**
```python
total_daily_income = ticket_price * visitor_capacity * available_buses
average_tour_income = total_daily_income / tours_per_day
```

### **4. String Concatenation and Formatting**

#### **String Concatenation**
```python
full_description = tour_location + " - " + tour_type
booking_reference = "TOUR-" + "2023" + "-" + "0415"
welcome_message = "Welcome, " + tourist_name + "!"
```

#### **String Formatting (f-strings)**
```python
formatted_description = f"{tour_type} of {tour_location} with guide {guide_name}"
weather_report = f"Weather: {weather_condition} for today's {tour_type}"
tour_summary = f"Tour: {tour_location} | Type: {tour_type} | Guide: {guide_name}"
```

#### **String Methods**
```python
uppercase_location = tour_location.upper()      # Case conversion
lowercase_name = tourist_name.lower()           # Case conversion
title_case = tour_type.title()                  # Title case
location_length = len(tour_location)            # Length calculation
contains_word = "Historic" in tour_location      # Substring check
```

### **5. Type Mismatch and Conversion Examples**

#### **Type Mismatch Error**
```python
# This causes a TypeError
try:
    result = location_name + visitor_count  # String + Integer
except TypeError as e:
    print(f"Error: {e}")
    # Solution: Convert number to string
    corrected_result = location_name + str(visitor_count)
```

#### **Type Conversions**
```python
# Integer to String
age_as_string = str(visitor_age)

# Float to Integer (truncates decimal)
cost_as_integer = int(ticket_price)

# String to Float
rating_as_float = float(rating)

# String to Integer (via float conversion)
rating_as_integer = int(float(rating))
```

#### **Division Behavior Differences**
```python
# Regular division (produces float)
regular_division = total_visitors / buses      # 25 / 4 = 6.25

# Integer division (produces integer)
integer_division = total_visitors // buses     # 25 // 4 = 6

# Modulo operation
remainder = total_visitors % buses             # 25 % 4 = 1
```

## Data Type Behavior Differences Explained

### **Numeric vs String Operations**

#### **Mathematical Operations**
- **Numbers**: Support arithmetic (+, -, *, /, //, %, **)
- **Strings**: Support concatenation (+) and repetition (*)

#### **String Multiplication Behavior**
```python
# String multiplication repeats the string
result = "Tour" * 3  # Results in "TourTourTour"

# Mathematical multiplication performs calculation
result = 5 * 3      # Results in 15
```

### **Type Conversion Behavior**

#### **Information Loss in Conversions**
```python
# Float to Integer loses decimal precision
float_value = 45.99
int_value = int(float_value)  # Results in 45 (decimal lost)

# String to Number requires valid format
valid_number = "4.7"
invalid_number = "four.point.seven"
```

### **Dynamic Typing Demonstration**
```python
# Same variable can hold different types
dynamic_variable = 42        # Integer
dynamic_variable = "42"      # String
dynamic_variable = 42.0      # Float
```

## Real-World Tourism Applications

### **Tour Booking System**
- **Booking ID**: String for alphanumeric codes
- **Tourist Age**: Integer for age calculations
- **Ticket Price**: Float for monetary values
- **Group Size**: Integer for counting
- **Special Requirements**: String for text descriptions

### **Tour Rating System**
- **Rating Count**: Integer for counting ratings
- **Average Rating**: Float for precise ratings
- **Comments**: String for feedback text
- **Recommendation Percentage**: Float for percentages

### **Data Validation**
- **Input Validation**: Converting string inputs to appropriate types
- **Range Checking**: Validating numeric ranges
- **Format Validation**: Checking string formats

## Key Learning Points Demonstrated

### **1. Type Awareness**
- Understanding when to use integers vs floats
- Knowing string operations vs numeric operations
- Recognizing type compatibility requirements

### **2. Type Conversion Skills**
- Converting between types as needed
- Understanding conversion limitations
- Handling conversion errors gracefully

### **3. Problem-Solving**
- Identifying type mismatches
- Applying appropriate solutions
- Using type checking for validation

### **4. Practical Application**
- Real-world tourism data examples
- Appropriate type selection for different data
- Proper data handling in business contexts

## Conclusion

This demonstration proves comprehensive understanding of Python data types:

- **Numeric Types**: Proper use of integers and floats with appropriate operations
- **String Types**: Effective string manipulation and formatting
- **Type Conversions**: Correct conversion techniques and error handling
- **Type Mismatches**: Identification and resolution of type conflicts
- **Real-World Application**: Practical usage in tourism industry context

The script successfully demonstrates all required data type concepts with clear examples, proper error handling, and practical applications relevant to the TourTide project.

**Status**: Data types demonstration completed successfully
