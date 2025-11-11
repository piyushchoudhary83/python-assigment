import csv

data = {}

#<---------Input Section--------->
try:
    choice = int(input("Enter 1 to input manually or 2 to load from CSV: "))
except ValueError:
    print("Invalid input. Please enter 1 or 2.")
    exit()

if choice == 1:
    try:
        n = int(input("Enter number of students: "))
        if n <= 0:
            print("Number of students must be positive.")
            exit()
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            marks = int(input("Enter marks: "))
            data[name] = marks
    except ValueError:
        print("Invalid input. Please enter numeric values for marks and number of students.")
        exit()

elif choice == 2:
    file = input("Enter CSV filename: ")
    try:
        with open(file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2:
                    continue  # Skip invalid rows
                try:
                    data[row[0]] = int(row[1])
                except ValueError:
                    print(f"Invalid mark for {row[0]}. Skipping entry.")
        if not data:
            print("No valid data found in CSV.")
            exit()
    except FileNotFoundError:
        print("File not found.")
        exit()
else:
    print("Invalid choice.")
    exit()

if not data:
    print("No data available.")
    exit()

#<-----------Basic Calculations----------->
marks = list(data.values())

average = sum(marks) / len(marks)

# Median calculation (works for even/odd)
sorted_marks = sorted(marks)
n = len(sorted_marks)
if n % 2 == 1:
    median = sorted_marks[n // 2]
else:
    median = (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2

max_score = max(marks)
min_score = min(marks)

#<--------Grading-------->
grades = {}
for name, score in data.items():
    if score >= 90:
        grades[name] = "A"
    elif score >= 80:
        grades[name] = "B"
    elif score >= 70:
        grades[name] = "C"
    elif score >= 60:
        grades[name] = "D"
    elif score >= 50:
        grades[name] = "E"
    else:
        grades[name] = "F"

#<--------Output------------>
print("\n----- Results Summary -----")
print(f"Average Marks: {average:.2f}")
print(f"Median Marks: {median}")
print(f"Highest Marks: {max_score}")
print(f"Lowest Marks: {min_score}")

print("\n----- Student Grades -----")
for name, grade in grades.items():
    print(f"{name}: {data[name]} -> Grade {grade}")

#<--------Optional: Save to CSV------------>
save_choice = input("\nDo you want to save the results to 'results.csv'? (y/n): ").lower()
if save_choice == 'y':
    with open('results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])
        for name, marks in data.items():
            writer.writerow([name, marks, grades[name]])
    print("Results saved to 'results.csv'.")