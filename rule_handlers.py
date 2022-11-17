# from utils import invalid_query_prompt #,bot_print_with_name, bot_print
import random


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
    print("get_number_of_colleges_in_university is called")
    # confirmation_message_for_query = " number of colleges affiliated by the University "
    # if bot_confirmation_prompt(confirmation_message_for_query) == True:
    query_results = 64    # logic to count no. of colleges from the json or csv
    possible_responses = ["There are {no_of_colleges} offering Undrgraduate courses at the university", "There are {no_of_colleges} colleges affiliated by the University." ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = query_results)  
    return generated_response

    # print(query_dict)

def get_number_of_faculties_in_university (self): 
    # query_results = 
    print("s")

def get_number_of_departments_in_university(self): 

    print("z")

def get_number_of_courses_in_university(query_dict):
    print("j")


def get_number_of_faculties_in_college(college):
    print("2")


def get_total_number_of_seats_for_course_at_college(course,college):
    print("3")


def get_number_of_seats_for_category_for_course_at_college(category,course,college):
    pass 


def get_number_of_courses_at_college(college):
    pass 


def get_number_of_courses_in_faculty(faculty):
    pass 


def get_number_of_courses_in_department(department):
    pass 


def get_number_of_courses_in_department_at_college(department,college):
    pass 


def get_number_of_department_at_college(college):
    pass 


def get_number_of_department_under_faculty_at_college(faculty, department):
    pass 


def get_number_of_department_under_faculty(faculty):
    pass 


def get_number_of_colleges_offering_course(course):
    pass 


def get_list_of_faculties_in_college(college):
    pass 


def get_list_of_colleges_in_university():
    pass 


def get_list_of_faculties_in_university():
    pass 


def get_list_of_departments_in_university():
    pass 


def get_list_of_courses_in_university():
    pass 


def get_list_of_courses_at_college():
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

