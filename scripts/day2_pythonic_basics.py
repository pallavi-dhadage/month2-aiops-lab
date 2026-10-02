print("=" * 40)
print("1. COMPREHENSIONS")
print("=" * 40)

squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

dict_comp = {x: x**2 for x in range(5)}
print(f"Dict Comprehension: {dict_comp}")


print("\n" + "=" * 40)
print("2. ENUMERATE")
print("=" * 40)

tasks = ["Setup repo", "Learn Python", "Push to GitHub"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")


print("\n" + "=" * 40)
print("3. ZIP")
print("=" * 40)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

name_score_dict = dict(zip(names, scores))
print(f"Dictionary from zip: {name_score_dict}")


print("\n" + "=" * 40)
print("4. UNPACKING")
print("=" * 40)

coordinates = (10, 20)
x, y = coordinates
print(f"X: {x}, Y: {y}")

first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")


print("\n" + "=" * 40)
print("5. MINI PROJECT: REFACTORED MARKS APP")
print("=" * 40)

students = ["Alice", "Bob", "Charlie", "David"]
marks = [85, 92, 78, 95]

student_data = list(zip(students, marks))
print(f"Paired data: {student_data}")

passed_students = [name for name, mark in student_data if mark >= 80]
print(f"Passed students: {passed_students}")

summary = {name: mark for name, mark in zip(students, marks)}
print(f"Summary: {summary}")

print("\n--- Student Rankings ---")
sorted_students = sorted(student_data, key=lambda item: item[1], reverse=True)

for rank, (name, mark) in enumerate(sorted_students, start=1):
    print(f"Rank {rank}: {name} ({mark})")