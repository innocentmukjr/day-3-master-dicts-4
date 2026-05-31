
---

```python
courses = {
    "course_1": {"name": "Math", "credits": 3, "students": ["Alice", "Bob"]},
    "course_2": {"name": "Science", "credits": 4, "students": ["Charlie"]},
    "course_3": {"name": "History", "credits": 2, "students": ["David", "Eve", "Frank"]}
}

# 1. Add a new student to Science
courses["course_2"]["students"].append("Innocent")

# 2. Update the credits of History to 5
courses["course_3"]["credits"] = 5

# 3. Print all courses that have more than 2 students enrolled
for key, value in courses.items():
    if len(value["students"]) > 2:
        print(key)
