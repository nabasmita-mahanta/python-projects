# Student details Project
# CRUD Operations - create, read, update, delete
import os
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
        file.write(name + '~~~' + roll_no + '~~~' + student_class + '~~~' + fees + '~~~' + percentage + '\n')
        file.close()

    elif user_input == '2':
        print("\nAll Student Records\n")
        print("\nNAME~~~RollNo~~~Class~~~Fees~~~Percentage\n")

        file = open('student_details.txt', 'r')
        while True:
            line_content = file.readline()
            length = len(line_content)
            if length == 0:
                break
            print(line_content.strip())
        file.close()


    elif user_input == '3':
        print("\nSearching for a student record by name")
        search_string = input("\nPlease enter the student name: ")

        file = open('student_details.txt', 'r')
        while True:
            line_content = file.readline()
            length = len(line_content)
            if length == 0:
                print("Record not found")
                break

            my_list = line_content.split("~~~")
            if my_list[0] == search_string:
                print("\nRecord found")
                print("\n Student name : ", my_list[0])
                print("\n Student rollno : ", my_list[1])
                print("\n Student class : ", my_list[2])
                print("\n Student fees : ", my_list[3])
                print("\n Student percentage : ", my_list[4])
                break
        file.close()


    elif user_input == '4':
        print("\nSearching for a student record by rollno")
        search_string = input("Please enter the student roll no: ")

        file = open('student_details.txt', 'r')
        while True:
            line_content = file.readline()
            length = len(line_content)
            if length == 0:
                print("Record not found")
                break

            my_list = line_content.split("~~~")
            if my_list[1] == search_string:
                print("\nRecord found")
                print("\n Student name : ", my_list[0])
                print("\n Student rollno : ", my_list[1])
                print("\n Student class : ", my_list[2])
                print("\n Student fees : ", my_list[3])
                print("\n Student percentage : ", my_list[4])
                break

        file.close()

    elif user_input == '5':
        print("\nDeleting a student details by name")
        search_string = input("Please enter the student name: ")

        file = open('student_details.txt', 'r')
        temp_file = open('temp_file.txt', 'w')
        while True:
            line_content = file.readline()
            if len(line_content) == 0:
                break

            name = line_content.split("~~~")[0]
            if name == search_string:
                pass
            else:
                temp_file.write(line_content)

        file.close()
        temp_file.close()

        os.remove('student_details.txt')
        os.rename('temp_file.txt','student_details.txt')


