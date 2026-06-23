import csv
import os
import matplotlib.pyplot as plt

# current file ka folder path
base_path = os.path.dirname(__file__)

# input file
file_path = os.path.join(base_path, "data.csv")

# output file
output_path = os.path.join(base_path, "output.csv")

students = {}

#  CSV READ
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        name = row["Name"]
        marks = int(row["Marks"])
        students[name] = marks

#  ANALYSIS
average = sum(students.values()) / len(students)
topper = max(students, key=students.get)
lowest = min(students, key=students.get)

print(" Student Data Analysis")
print("-----------------------")
print("Total Students:", len(students))
print("Average Marks:", round(average, 2))
print("Topper:", topper, "-", students[topper])
print("Lowest Scorer:", lowest, "-", students[lowest])

difference = students[topper] - students[lowest]
print("Score Gap:", difference)

# 🎓 GRADES + STORE DATA FOR CSV
result_data = []
grades_count = {"A":0, "B":0, "C":0, "F":0}

print("\n Grades:")
for student, marks in students.items():
    if marks >= 90:
        grade = "A"
        status = "Pass"
    elif marks >= 75:
        grade = "B"
        status = "Pass"
    elif marks >= 50:
        grade = "C"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"
    
    print(student, "->", grade, "|", status)

    grades_count[grade] += 1

    result_data.append({
        "Name": student,
        "Marks": marks,
        "Grade": grade,
        "Status": status
    })

#  RANKING
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

print("\n Rankings:")
for i, (name, marks) in enumerate(sorted_students, 1):
    print(i, name, marks)

#  SEARCH
search_name = input("\nEnter student name to search: ")

if search_name in students:
    print(search_name, "marks:", students[search_name])
else:
    print("Student not found ")

#  SAVE TO NEW CSV
with open(output_path, "w", newline="") as file:
    fieldnames = ["Name", "Marks", "Grade", "Status"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(result_data)

print("\n Output saved to output.csv")

#  BAR GRAPH
names = list(students.keys())
marks = list(students.values())

plt.figure(figsize=(10, 5))

bars = plt.bar(names, marks)

# topper & fail highlight
for bar, mark in zip(bars, marks):
    if mark == students[topper]:
        bar.set_color("green")
    elif mark < 50:
        bar.set_color("red")

plt.axhline(average, linestyle="--", label=f"Average ({round(average,2)})")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title(" Student Performance Analysis")
plt.xticks(rotation=30)
plt.legend()

plt.tight_layout()
plt.show()



#  PIE CHART (based on grades distribution)

labels = list(grades_count.keys())
sizes = list(grades_count.values())

plt.figure()
colors = ["green", "blue", "orange", "red"]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title(" Grade Distribution")


plt.show()
