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

# ---------------- ADD ----------------
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

# ---------------- VIEW ----------------
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

# ---------------- SEARCH ----------------
def search_student():
    name = input("Enter student name to search: ")
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE name=?", (name,))
    result = cursor.fetchall()
    
    if result:
        for row in result:
            print(row)
    else:
        print("Student not found.")
    
    conn.close()

# ---------------- UPDATE ----------------
def update_student():
    student_id = input("Enter student ID to update: ")
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    data = cursor.fetchone()
    
    if not data:
        print("Student not found.")
        return
    
    print("Enter new details:")
    name = input("Name: ")
    s1 = int(input("Subject 1: "))
    s2 = int(input("Subject 2: "))
    s3 = int(input("Subject 3: "))
    
    percentage = (s1 + s2 + s3) / 3
    grade = calculate_grade(percentage)
    
    cursor.execute("""
    UPDATE students
    SET name=?, subject1=?, subject2=?, subject3=?, percentage=?, grade=?
    WHERE id=?
    """, (name, s1, s2, s3, percentage, grade, student_id))
    
    conn.commit()
    conn.close()
    
    print("✅ Student updated successfully!")

# ---------------- DELETE ----------------
def delete_student():
    student_id = input("Enter student ID to delete: ")
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    
    conn.commit()
    conn.close()
    
    print("❌ Student deleted successfully!")

# ---------------- CHART ----------------
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

# ---------------- MENU ----------------
def menu():
    create_table()
    
    while True:
        print("\n--- Student Result System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Chart")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_chart()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
