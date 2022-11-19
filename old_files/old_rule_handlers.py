# from utils import invalid_query_prompt #,bot_print_with_name, bot_print
import random
import csv


# def bot_confirmation_prompt(query_to_be_searched):
#     print("Are you asking for"+ query_to_be_searched +"?")
#     print("1.Yes! this what I was looking for.")
#     print("2.No! I asked something else.")
 
#     confirmation = input("Enter the you choice 1 OR 2")
#     if confirmation == "1":
#         return True
#     elif confirmation ==  "2":
#         print("OK, can you please repeat your query?")
#         # invalid_query_prompt()
#         return False
#     else :
#         #call next rule from the handler
#         print("Wrong input!!")
#         return False


def get_number_of_colleges_in_university  (query_dict): 

    path = "C:\du_chatbot_terminal\college_course_category_seats.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    colleges_set = set()
    for row in reader:
        colleges_set.add(row[0])
        # print(row[0])

    query_results = len(colleges_set)   # logic to count no. of colleges from the json or csv
    possible_responses = ["There are {no_of_colleges} offering Undrgraduate courses at the university", "There are {no_of_colleges} colleges affiliated by the University." ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = query_results)  
    return generated_response

    # print(query_dict)

def get_number_of_faculties_in_university (self): 
    
    path = "C:\du_chatbot_terminal\\faculty_department.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    faculties_set = set()
    for row in reader:
        faculties_set.add(row[0])

    query_results = len(faculties_set)    # logic to count no. of faculties from the json or csv
    possible_responses = ["There are {no_of_faculties} faculties at the university", "There are {no_of_faculties} faculties the University.", "{no_of_faculties} faculties are there at DU." ]
    generated_response = (random.choice(possible_responses)).format(no_of_faculties = query_results)  

    return generated_response


def get_number_of_departments_in_university(self): 
    
    path = "C:\du_chatbot_terminal\\faculty_department.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    departments_set = set()
    for row in reader:
        departments_set.add(row[1])
    
    query_results = len(departments_set)    # logic to count no. of departments from the json or csv
    possible_responses = ["There are {no_of_departments} departments at the university", "There are {no_of_departments} departments the University.", "{no_of_departments} departments are there at DU." ]
    generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results)  
    return generated_response


def get_number_of_courses_in_university(query_dict):

    path = "C:\du_chatbot_terminal\college_course.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    courses_set = set()
    for row in reader:
        courses_set.add(row[1])

    query_results = len(courses_set)   # logic to count no. of departments from the json or csv
    possible_responses = ["There are {no_of_courses} UG courses offered the university.", "There are {no_of_courses} undergrad courses at the University.", "{no_of_courses} UG courses are there at DU.", "You can choose among {no_of_courses} for your UG degree at DU." ]
    generated_response = (random.choice(possible_responses)).format(no_of_courses = query_results)  
    return generated_response
# other variant of this could be making set of row[1] in college_course_cat_seat or fee and then print len
# if all the departments are not getting covered then we will use this second approach


def get_number_of_faculties_in_college(query_dict):
    print("get_number_of_faculties_in_college is called")
    # college = query_dict['college']
    # message_for_query_to_be_searched = "number of faculties in " + college
    # if bot_confirmation_prompt(message_for_query_to_be_searched):
    #     query_results = 5
    #     generated_response = "There are " + str(query_results) + " faulties at " + college
    #     return generated_response
    # else:
    #      return  
    # discuss the idea;; the method is in utils


def get_total_number_of_seats_for_course_at_college(query_dict):
    college = query_dict['college']
    course = query_dict['course']

    path = "C:\du_chatbot_terminal\college_course_category_seats.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        if row[0] == college and row[1] == course:
            query_results = int(row[2])

    possible_responses = ["There are {total_no_of_seats} total seats in {ccourse} at {ccollege}", "There are {total_no_of_seats} seats available in {ccourse} at {ccollege}", "{total_no_of_seats} seats in total in {ccourse} at {ccollege}"]
    generated_response = (random.choice(possible_responses)).format(total_no_of_seats = query_results, ccollege = college, ccourse = course )  

    return generated_response
    

def get_number_of_seats_for_category_for_course_at_college(query_dict):
    college = query_dict['college']
    course = query_dict['course']
    category = query_dict['category']

    path = "C:\du_chatbot_terminal\college_course_category_seats.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)
    category_index_form_csv = header.index(category)

    for row in reader:
        if row[0] == college and row[1] == course :
            query_results = int(row[category_index_form_csv])

    # query_results = 7 #logic to count total no. of seats for a course at a college  ; form the csv, --> available doc has seat matrix for category for course at all the colleges ; category,course,college
 
    possible_responses = ["There are {no_of_seats} seats in {ccourse} at {ccollege}", "There are {no_of_seats} seats available for {ccategory} in {ccourse} at {ccollege}", "{no_of_seats} seats for {ccategory} in {ccourse} at {ccollege}"]
    generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ccollege = college, ccourse = course, ccategory = category )  

    return generated_response
    

def get_number_of_courses_at_college(query_dict):
    college = query_dict['college']

    path = "C:\du_chatbot_terminal\college_course_category_seats.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    courses_at_college_set = set()

    for row in reader:
        if row[0] == college:
            courses_at_college_set.add(row[1])

    query_results = len(courses_at_college_set)
    #pass collegename #logic to count total no. course at a college  ; form the csv, --> available doc no of courses per college with vcategoruy wise fee
 
    possible_responses = ["There are {no_of_courses} courses at {ccollege}", "There are {no_of_courses} courses at {ccollege}", "{no_of_courses} courses are there at {ccollege}"]
    generated_response = (random.choice(possible_responses)).format(no_of_courses = query_results, ccollege = college )  

    return generated_response


def get_number_of_courses_in_faculty(query_dict):
    faculty = query_dict['faculty']    

    path = "D:\\new_chat\\new_n\\faculty_department_college.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    courses_at_faculty_set = set()
    for row in reader:
        if row[0] == faculty:
            courses_at_faculty_set.add(row[2])

    
    query_results = len(courses_at_faculty_set) 
    #pass facultyname #logic to count total no. course faculty; form the csv, --> available doc ?

    possible_responses = ["There are {no_of_courses} courses at {ffaculty}", "There are {no_of_courses} courses at {ffaculty}", "{no_of_courses} courses at {ffaculty}"]
    generated_response = (random.choice(possible_responses)).format(no_of_courses = query_results, ffaculty = faculty )  

    return generated_response

def get_number_of_courses_in_department(query_dict):
    department = query_dict['department']    

    path = "D:\\new_chat\\new_n\\faculty_department_college.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    courses_in_department_set = set()
    for row in reader:
        if row[1] == department:
            courses_in_department_set.add(row[2])

    query_results = len(courses_in_department_set) #pass college name #logic to count total no. course at a college  ; form the csv, --> available doc no of courses per college with vcategoruy wise fee

    possible_responses = ["There are {no_of_courses} courses offered by {ddepartment}", "There are {no_of_courses} courses at {ddepartment}", "{no_of_courses} courses at {ddepartment}"]
    generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department )  

    return generated_response

def get_number_of_courses_in_department_at_college(query_dict):
    # to be discussed college level detail 
    college = query_dict['college']
    department = query_dict['department']    

    query_results = 11 #pass collegename and dept name #logic to count total no. course at a college  ; form the csv, --> available doc no of courses per college with vcategoruy wise fee
   
    possible_responses = ["There are {no_of_courses} courses offered by {ddepartment} at {ccollege}.", "There are {no_of_courses} courses at {ddepartment} at {ccollege}.", "{no_of_courses} courses at {ddepartment} at {ccollege}."]
    generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department, ccollege = college )  

    return generated_response


def get_number_of_department_at_college(query_dict):
    #college level detail
    # create college dept document;
    college = query_dict['college']

    query_results = 12 #pass college name #logic to count total no. departments at a college  ; form the csv, --> available doc no of courses per college with category wise fee
   
    possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    return generated_response


def get_number_of_department_under_faculty_at_college(query_dict):    
    #clear
    faculty = query_dict['faculty']
    college = query_dict['college']

    query_results = 13 #pass faculty, department name #logic to count total no. departments at a college  ; form the csv, --> available doc no of courses per college with category wise fee
   
    possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    return generated_response



def get_number_of_department_under_faculty(query_dict):
    faculty = query_dict['faculty']

    path = "D:\\new_chat\\new_n\\faculty_department_college.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    department_under_faculty_set = set()
    for row in reader:
        if row[0] == faculty:
            department_under_faculty_set.add(row[1])    

    query_results = len(department_under_faculty_set) 
    #pass faculty name #logic to count total no. departments under a faculty  ; form the csv, --> available doc no of courses per college with category wise fee
   
    possible_responses = ["There are {no_of_departments} departments under {ffaculty}.", "There are {no_of_departments} departments under {ffaculty}.", "{no_of_departments} departments are there under {ffaculty}."]
    generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ffaculty = faculty)  

    return generated_response


def get_number_of_colleges_offering_course(query_dict):
    course = query_dict['course']
    
    path = "C:\du_chatbot_terminal\college_course_category_seats.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    colleges_offering_course_set = set()

    for row in reader:
        if row[1] == course :
            colleges_offering_course_set.add(row[1])
    
    query_results = len(colleges_offering_course_set) #pass course name #logic to count no of colleges offering this course  ; form the csv
   
    possible_responses = ["There are {no_of_colleges} offering {ccourse}.", "There are {no_of_colleges} offering {ccourse}.", "{no_of_colleges} are there offering {ccourse}."]
    generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccourse = course )  

    return generated_response


def get_list_of_faculties_in_college(self):
    # faculties at college
    pass
    # return generated_response


def get_list_of_colleges_in_university(self):
    path = "C:\du_chatbot_terminal\college_course_category_seats.csv"
    file = open(path, newline = '')
    reader = csv.reader(file)
    header = next(reader)

    colleges_set = set()
    for row in reader:
        colleges_set.add(row[0])
        # print(row[0])

    query_results = len(colleges_set)
    # colleges_names_print_string = ''
    # n=1
    # for a in colleges_set:
    #     colleges_names_print_string.join(a+'\n')
            
    # print(colleges_set)
    possible_responses = ["There are {no_of_colleges} offering Undrgraduate courses at the university. Here is the list of all the colleges at DU:- \n{s}", "There are {no_of_colleges} colleges affiliated by the University. Here is the list of all the colleges at DU:- \n{s}" ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = query_results, s = colleges_set )  #colleges_names_print_string)  
    print(str(generated_response)) 
    # return generated_response 



def get_list_of_faculties_in_university():
    pass



def get_list_of_departments_in_university():
    pass 


def get_list_of_courses_in_university():
    pass 


def get_list_of_courses_in_university():
    pass


def get_list_of_courses_at_college():
    pass 


def get_list_of_courses_in_faculty(faculty):
    pass 


def get_list_of_courses_in_department(department):
    pass 


def get_list_of_courses_in_department_at_college(department,college):
    pass 


def get_list_of_department_at_college(college):
    pass 


def get_list_of_department_under_faculty_at_college(faculty, college):
    pass 


def get_list_of_department_under_faculty(faculty):
    pass 


def get_list_of_colleges_offering_course(course):
    pass 


def get_cutoff_for_category_for_course_college(category, course, college):
    pass 


def get_cutoff_for_course_for_college( course, college):
    pass 


def get_coursefee_for_category_for_course_college(course, college):
    pass 


def get_coursefee_for_category_for_course_college(course):
    pass 


def get_details_for_eligibility_of_course(course):
    pass 


def get_details_for_duration_of_course(course):
    pass 


def get_details_for_syllabus_of_course(course):
    pass 