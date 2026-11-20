def get_grade(score):
    if score < 0 and score > 100:
        return "Yanlis bal"
    
    elif 90 < score <= 100:
        return "A"

    elif score > 80:
        return "B"

    elif score > 70:
        return "C"

    elif score > 60:
        return "D"

    elif score > 50:
        return "E"

    else:
        return "F"


def make_report(students):
    for i in students:
        students[i] = get_grade(students[i])

    return students

students = {"Aysel": 95, "Murad": 72, "Elvin": 48}

print(make_report(students))