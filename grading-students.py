def gradingStudents(grades):
    rounded_grades = []
    
    for grade in grades:
        if grade < 38:
            # If the grade is less than 38, no rounding occurs
            rounded_grades.append(grade)
        else:
            # Calculate the next multiple of 5
            next_multiple_of_5 = (grade // 5 + 1) * 5
            
            # Check if rounding is needed
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
    
    return rounded_grades

# Sample Input
grades = [73, 67, 38, 33]

# Sample Output
result = gradingStudents(grades)
print(result)
