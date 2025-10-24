students = [
    {"name": "Alice", "age": 20, "scores": {"math": 88, "english": 92, "science": 85}},
    {"name": "Bob", "age": 22, "scores": {"math": 75, "english": 78, "science": 72}},
    {"name": "Charlie", "age": 19, "scores": {"math": 95, "english": 85, "science": 91}},
    {"name": "Diana", "age": 21, "scores": {"math": 82, "english": 89, "science": 84}},
]

for student in students:
    total = student['scores']['math'] + student['scores']['english'] + student['scores']['science']
    avg = f"{total / 3:.0f}"
    student['average'] = int(avg)

print(students)

high_avg = 0

for student in students:
    if student['average'] > high_avg:
        high_avg = student['average']

for student in students:
    if high_avg == student['average']:
        print(student['name'])

print(students[0]['scores'])

students.sort(key=lambda student: student['average'], reverse=True)
print(students)

g_students = []

for s in students:
    if s['average'] > 85:
        g_students.append(s)

print(g_students)

subject_totals = {"math": 0, "english": 0, "science": 0}



for student in students:
    for subject, score in student['scores'].items():
        subject_totals[subject] += score

num_students = len(students)
subject_averages = {subject: total / num_students for subject, total in subject_totals.items()}

print(subject_averages)

best_subject = max(subject_averages, key=subject_averages.get)

print(f"The subject with the highest overall average is {best_subject} ({subject_averages[best_subject]:.2f})")