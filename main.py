from database import create_table, connect

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
    
    print("Student added successfully!")

def view_students():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()

def menu():
    create_table()
    
    while True:
        print("\n--- Student Result System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
