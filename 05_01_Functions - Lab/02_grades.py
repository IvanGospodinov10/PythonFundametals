grade = float(input())

def grades(grade_point: float):
    if 2 <= grade_point <= 2.99:
        return "Fail"
    elif 3 <= grade_point <= 3.49:
        return "Poor"
    elif 3.50 <= grade_point <= 4.49:
        return "Good"
    elif 4.50 <= grade_point <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_point <= 6:
        return "Excellent"


print(grades(grade))