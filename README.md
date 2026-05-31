# Day 3 – Courses Dictionary (Lists as Nested Values)

## 📘 The Exercise Instructions

Given the following dictionary:
```python
courses = {
    "course_1": {"name": "Math", "credits": 3, "students": ["Alice", "Bob"]},
    "course_2": {"name": "Science", "credits": 4, "students": ["Charlie"]},
    "course_3": {"name": "History", "credits": 2, "students": ["David", "Eve", "Frank"]}
}
Perform these tasks:

Add a new student to Science.

Update the credits of History to 5.

Print all courses that have more than 2 students enrolled.

🧠 My Approach
Task 1: Accessed the "students" list inside "course_2" using courses["course_2"]["students"] and used .append("Innocent") to add a new student.

Task 2: Accessed "course_3" then "credits" and reassigned it to 5.

Task 3: Looped through courses.items() and checked len(value["students"]) > 2. Printed the outer key (course_1, etc.) for those matching.

🚧 Challenges I Faced
Remembering that the "students" value is a list, not a dictionary – so I use .append() not assignment.

Making sure I used the correct syntax: courses["course_2"]["students"].append(...) – double brackets and dot method.

Understanding that len(value["students"]) counts the number of students in the list.

✅ What I Learned
Dictionaries can contain lists as values, not just strings or numbers.

How to modify a list inside a nested dictionary.

How to use len() on a list that lives inside a dictionary.

Combining conditions (len() > 2) inside a loop to filter results.

🖥️ How to Run My Code
Save the code as main.py.

In terminal: python main.py

Expected output:

text
course_3
(Only History has more than 2 students – David, Eve, Frank. Science had 1, after appending becomes 2 – still not >2. So only course_3 prints.)

📅 Part of My AI/ML Learning Journey
Day 3 – now combining dictionaries with lists. This is useful for representing relational data (e.g., a course with multiple enrolled students). In ML, similar structures appear when grouping data points by category.

Another step forward. Dictionaries are becoming natural.
