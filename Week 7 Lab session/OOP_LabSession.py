# Week 7 Lab 1
# Date: 02.4.2026
# Auther: Riley


import random
counter = 200
studentList = []

class Student:
    def __init__(self, student_name, attendance, course):
        self.student_id = random.randint(100, 999)
        self.student_name = student_name
        self.attendance = attendance
        self.course = course
    
    #This Function reads the student information and then stores the attendance

    def add_student_attendance(self):

        st_name = " "

        while True:
            st_name = input("Enter student name (or type done to stop): ")
            if st_name == "done":
                break
            
            self.student_name = st_name
            self.attendance = int(input("Enter attendance percentage: "))
            self.course = input("Enter course name: ")
            studentList.append((self.student_id, self.student_name, self.attendance, self.course))

    def calculate_average_attendance(self):

        total = 0
        count = 0

        for student in studentList:
            total += student[2]
            count += 1

        if count == 0:
            return 0 
        
        average = total / count
        return average
    
    def update_attendance(self):

        message = ""

        update_id = int(input("Enter Student ID to update attendance"))

        for i in range(len(studentList)):
            if studentList[i][0] == update_id:
                new_attendance = int(input("Enter the new attendance percentage: "))
                new_course = input("Enter new course name: ")

                studentList[i] = (studentList[i][0], studentList[1][1], new_attendance, new_course)
                message = "Updated successfuly"
                break
            else:
                message = "Student Not Found"

        print(message)

    
    def display_student_list(self):

        print("\n---Student Attendance Records ---")
        for student in studentList:
            print(f"Student ID: {student[0]}")
            print(f"Student Name: {student[1]}")
            print(f"Attendance: {student[2]}%")
            print(f"Course Name: {student[3]}")
            print("---------------------------")

        avg = self.calculate_average_attendance()
        print(f"\n The Average attendance is: {avg}%")

#Create a instance of the student class and display the student list
student1 = Student("",0,"")
student1.add_student_attendance()

student1.display_student_list()