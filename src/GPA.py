def calculate_gpa(grades_data):
    Scale = {"A+":4.2,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.5,"D":1.0,"F":0.0}
    TCR = 0
    CGP = 0
    for item in grades_data:
        grade = item['grade']
        # Ensure credits are float, handle potential ValueError if conversion fails
        try:
            cr = float(item['credits'])
        except ValueError:
            print(f"Invalid credits format: {item['credits']}") # Optional: for logging
            continue # Skip this entry or handle as error

        try:
            gp = Scale[grade] * cr
        except KeyError:
            # Handle invalid grade, perhaps log an error or return a specific value
            print(f"Invalid grade: {grade}") # Optional: for logging
            continue # Skip this entry or handle as error

        TCR += cr
        CGP += gp

    if TCR == 0:
        return 0.0  # Avoid division by zero if no valid credits

    GPA = CGP / TCR
    return round(GPA, 2)
