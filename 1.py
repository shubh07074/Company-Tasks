import numpy as np

students_datatype = np.dtype([
    ('name', 'U10'),
    ('age', 'i4'),
    ('marks', 'f8'),
    ('student_enrollment', 'i8')
])

students = np.array([
    ('shubham', 20, 98.2, 210490131009),
    ('Ramesh', 22, 77.2, 210490131010),
    ('Kamlesh', 21, 82.2, 210490131011),
], dtype=students_datatype)

print(students)

print("Names:", students['name'])
print("Age:", students['age'])
print("Marks:", students['marks'])
print("Enrollment:", students['student_enrollment'])
