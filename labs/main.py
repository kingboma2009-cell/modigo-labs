def bmi_report(weight_kg, height_m):
    # TODO: calculate bmi, round it to 1 decimal place, determine the category,
    # and return "BMI: {bmi}, Category: {category}"
    pass
    BMI = round(weight_kg / height_m ** 2, 1)
    if BMI < 18.5:
        Category = "Underweight"
    elif BMI <= 24.9:
        Category = "Normal weight"
    elif BMI <= 29.9:
        Category = "Overweight"
    else:
        Category = "Obese"
    return f"BMI: {BMI}, Category: {Category}"