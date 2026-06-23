# Ask for user input
weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

# Display the BMI result rounded to two decimal places
print(f"\nYour BMI is: {bmi:.2f}")

# Determine health category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 24.9 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")