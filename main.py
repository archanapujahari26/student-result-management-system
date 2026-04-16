from database import create_table, connect
import matplotlib.pyplot as plt

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

def add_student():
    name = input("Enter student name: ")
    s1 = int(input("Enter Subject 1 marks: "))
    s2 = int(input("Enter Subject 2 marks: "))
    s3 = int(input("Enter Subject 3 marks: "))
    
    percentage = (s1 + s2 + s3) / 3
    grade = calculate_grade(percentage)
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO students (name, subject1, subject2, subject3, percentage, grade)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, s1, s2, s3, percentage, grade))
    
    conn.commit()
    conn.close()
    
    print("✅ Student added successfully!")

def view_students():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    if not rows:
        print("No records found.")
    else:
        print("\n--- Student Records ---")
        for row in rows:
            print(row)
    
    conn.close()

def show_chart():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT name, percentage FROM students")
    data = cursor.fetchall()

    if not data:
        print("No data to display!")
        return

    names = [row[0] for row in data]
    percentages = [row[1] for row in data]

    plt.bar(names, percentages)
    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.title("Student Performance Chart")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    conn.close()

def menu():
    create_table()
    
    while True:
        print("\n--- Student Result System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Show Chart")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
