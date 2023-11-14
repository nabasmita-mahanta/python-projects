# Student details Project
# CRUD Operations - create, read, update, delete

# create the file
file = open('student_details.txt', 'a')
prompt = ("\nWelcome to SMS - Student Management System."
          "\nPlease type 1, 2, 3, 4"
          "\n1 - Add Record (Create)"
          "\n2 - Display All Records (Read)"
          "\n3 - Search student record by name (Read)"
          "\n4 - Search student record by roll no (Read)"
          "\n5 - Delete student record by name (Delete)"
          "\n6 - Update student record (Update)"
          "\n7 - Exit")

while True:
    print(prompt)
    # take input from user
    user_input = input('Please give your input: ')
    print(user_input)
    if user_input == '7':
        break
    elif user_input == '1':
        print("\nEnter student details")
        name = input('\nEnter student name: ')
        roll_no = input('\nEnter student roll no: ')
        student_class = input('\nEnter student class: ')
        fees = input('\nEnter student fees: ')
        percentage = input('\nEnter student percentage: ')

        print("You have entered the following student details ...")
        print('Student Name : ', name)
        print('Student Roll No : ', roll_no)
        print('Student Class : ', student_class)
        print('Student Fees : ', fees)
        print('Student Percentage : ', percentage)

        file = open('student_details.txt', 'a')
        file.write(name+'~~~'+roll_no+'~~~'+student_class+'~~~'+fees+'~~~'+percentage)
        file.close()

    elif user_input == '2':
        print("\nAll Student Records\n")
        print("\nNAME~~~RollNo~~~Class~~~Fees~~~Percentage\n")

        file = open('student_details.txt', 'r')
        file_content = file.read()
        file.close()
        print(file_content)
