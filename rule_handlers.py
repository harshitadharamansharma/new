from synonyms import synonyms
from rulebase import rulebase
from utils import bot_confirmation_prompt, bot_print_with_name, bot_print
 
 
 
for n in rulebase:
    rule_format_list = list(rulebase[n]["rule_format"])
    rule_tokens_list = list(rulebase[n]["rule_tokens"])
 
 
def next_rule(query_dict):
    for n in rulebase:
        if list(query_dict.keys()) == rulebase[n]["rule_tokens"]:
            a = rulebase[n]["rule_format"]
            a(query_dict)
            if a is True:
                break
            else:
                continue
 
 
def quantifier_college(query_dict):
    message_for_query_to_be_searched = " number of colleges affiliated by the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_colleges_in_university()
        generated_response = "There are " + str(query_results) + " colleges affiliated by the University."  
        bot_print_with_name (generated_response)
        return True
    else:
        return False
 
 
def quantifier_faculty(query_dict):
    message_for_query_to_be_searched = " number of faculties in the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_faculties_in_university()
        generated_response = "There are " + str(query_results) + " faculties in the University"  
        bot_print_with_name (generated_response)
        return True
    else:
        return False
 
 
def quantifier_department(query_dict):
    message_for_query_to_be_searched = " number of departments in the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_departments_in_university()
        generated_response = "There are " + str(query_results) + " colleges departments in the University"  
        bot_print_with_name (generated_response)
        return True
    else:
        return False

 
def quantifier_course(query_dict):
    message_for_query_to_be_searched = " number of courses in the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_courses_in_university()
        generated_response = "There are " + str(query_results) + " courses in the University"  
        bot_print_with_name (generated_response)
        return True
    else:
        return False 

 
def quantifier_faculty_college(query_dict):
    message_for_query_to_be_searched = "number of faculties in " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_faculties_in_college(college)
        generated_response = "There are " + str(query_results) + " faulties at " + college
        bot_print_with_name (generated_response)
        return True
    else:
        return False 
 
 
def quantifier_seats_course_college(query_dict):
    college = query_dict['college']
    course = query_dict['course']
    message_for_query_to_be_searched = "total number of seats in "+ course + " at " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_total_number_of_seats_for_course_at_college(course,college)
        generated_response = "There are " + str(query_results) + " total seats in "+ course + " at " + college
        bot_print_with_name (generated_response)
        return True
    else:
        return False 
 

def  quantifier_seats_category_course_college(query_dict):
    college = query_dict['college']
    course = query_dict['course']
    category = query_dict['category']
    message_for_query_to_be_searched = " number of seats for " + category + " in " + course + " at " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_seats_for_category_for_course_at_college(category,course,college)
        generated_response = "There are " + str(query_results) + " seats for " + category + " in " + course + " at " + college
        bot_print_with_name (generated_response)
        return True
    else:
        return False 


def quantifier_course_college(query_dict):
    college = query_dict['college']
    message_for_query_to_be_searched = " number of courses at " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_courses_at_college(college)
        generated_response = "There are " + str(query_results) + " courses at " + college
        bot_print_with_name (generated_response)
        return True
    else:
        return False 


def quantifier_course_faculty(query_dict):
    faculty = query_dict['faculty']
    message_for_query_to_be_searched = " number of courses offered by " + faculty
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_courses_in_faculty(faculty)
        generated_response = "There are " + str(query_results) + " courses offered by " + faculty
        bot_print_with_name (generated_response)
        return True
    else:
        return False 


def quantifier_course_department(query_dict):
    department = query_dict['department']
    message_for_query_to_be_searched = " number of courses offered by " + department
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_courses_in_department(department)
        generated_response = "There are " + str(query_results) + " courses offered by " + department
        bot_print_with_name (generated_response)   
        return True
    else:
        return False 


def quantifier_course_department_college(query_dict):
    college = query_dict['college']
    department = query_dict['department']
    message_for_query_to_be_searched = " number of courses offered by " + department + " at " + college 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_courses_in_department_at_college(department,college)
        generated_response = "There are " + str(query_results) + " courses offered by " + department + " at " + college
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def quantifier_department_college(query_dict):
    college = query_dict['college']
    message_for_query_to_be_searched = " number of departments at " + college 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_department_at_college(college)
        generated_response = "There are " + str(query_results) + " departments at " + college
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def quantifier_department_faculty_college(query_dict):
    faculty = query_dict['faculty']
    department = query_dict['department']
    message_for_query_to_be_searched = " number of colleges offering course under the " + department + ", " + faculty
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_department_under_faculty_at_college(faculty, department)
        generated_response = "There are " + str(query_results) + " departments at " + college + ", " + faculty
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def quantifier_department_faculty(query_dict):
    faculty = query_dict['faculty']
    message_for_query_to_be_searched = " number of departments under" + faculty
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_department_under_faculty(faculty)
        generated_response = "There are " + str(query_results) + " departments at " + faculty
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def quantifier_college_course(query_dict):
    course = query_dict['course']
    message_for_query_to_be_searched = " number of colleges offering " + course
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_number_of_colleges_offering_course(course)
        generated_response = "There are " + str(query_results) + " colleges offering " + course
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_faculty_college(query_dict):
    college = query_dict['college']
    message_for_query_to_be_searched = " number of colleges offering " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_faculties_in_college(college)
        generated_response = "This is the list of faculty at "+ college + ":-" + str(query_results)
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_college(query_dict):
    message_for_query_to_be_searched = " list of colleges affiliated by the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_colleges_in_university()
        generated_response = "This is the list of colleges affiliated by the University:-" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_faculty(query_dict):
    message_for_query_to_be_searched = " list of faculties in the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_faculties_in_university()
        generated_response = "This is the list of faculties in the University:-" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_department(query_dict):
    message_for_query_to_be_searched = " list of departments in the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_departments_in_university()
        generated_response = "This is the list of departments in the University:-" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False

    
def show_list_course(query_dict):
    message_for_query_to_be_searched = " list of courses in the University "
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_courses_in_university()
        generated_response = "This is the list of courses in the University:-" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_course_college(query_dict):
    college = query_dict('college')
    message_for_query_to_be_searched = " list of courses at " + college 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_courses_at_college()
        generated_response = "This is the list of courses at " + college + ":-" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_course_college(query_dict):
    college = query_dict('college')
    message_for_query_to_be_searched = " list of courses at " + college 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_courses_at_college()
        generated_response = "This is the list of courses at " + college + ":-" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_course_faculty(query_dict):
    faculty = query_dict('faculty')
    message_for_query_to_be_searched = " list of courses offered by the " + faculty 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_courses_in_faculty(faculty)
        generated_response = "This is the list of courses offered by the " + faculty + ":-" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_course_department(query_dict):
    department = query_dict('department')
    message_for_query_to_be_searched = " list of courses offered by the " + department
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_courses_in_department(faculty)
        generated_response = "This is the list of courses offered by the " + department + ":-\n" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_course_department_college(query_dict):
    department = query_dict('department')
    college = query_dict('college')
    message_for_query_to_be_searched = " list of courses offered by the " + department + " at " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_courses_in_department_at_college(department,college)
        generated_response = "This is the list of courses offered by the " + department + " at " + college + ":-\n" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_department_college(query_dict):
    college = query_dict('college')
    message_for_query_to_be_searched = " list of departments at " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_department_at_college(college)
        generated_response = "This is the list of departments at " + college + ":-\n" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_department_faculty_college(query_dict):
    faculty = query_dict('faculty')
    college = query_dict('college')
    message_for_query_to_be_searched = " list of departments under " + faculty + " at " + college
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_department_under_faculty_at_college(faculty, college)
        generated_response = "This is the list of departments under " + faculty + " at " + college + ":-\n" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_department_faculty(query_dict):
    faculty = query_dict('faculty')
    message_for_query_to_be_searched = " list of departments under " + faculty 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_department_under_faculty(faculty)
        generated_response = "This is the list of departments under " + faculty + ":-\n" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_list_college_course(query_dict):
    course = query_dict('course')
    message_for_query_to_be_searched = " list of colleges offering " + course 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_list_of_colleges_offering_course(course)
        generated_response = "This is the list of colleges offering " + course + ":-\n" + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_details_cutoff_category_course_college(query_dict):
    category = query_dict('category')
    course = query_dict('course')
    college = query_dict('college')
    message_for_query_to_be_searched = " cutoff for " + category +" in "+ course + " at " + college 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_cutoff_for_category_for_course_college(category, course, college)
        generated_response = "Cutoff for " + category + " in " + course + " at " + college +  " is " + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False



def show_details_cutoff_course_college(query_dict):
    college = query_dict('college')
    course = query_dict('course')
    message_for_query_to_be_searched = " general cutoff in "+ course + " at " + college 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_cutoff_for_course_college( course, college)
        generated_response = " General Cutoff for in " + course + " at " + college +  " is " + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_details_coursefee_category_course_college(query_dict):
    college = query_dict('college')
    course = query_dict('course')
    category = query_dict('category')
    message_for_query_to_be_searched = " course fee for " + course + " for " + category + " at " + college 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_coursefee_for_category_for_course_college(course, college)
        generated_response = " Course fee for " + course + " for " + category + " at " + college + " is " + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_details_eligibility_course(query_dict):
    course = query_dict('course')
    message_for_query_to_be_searched = " eligibility for "+ course 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_coursefee_for_category_for_course_college(course)
        generated_response = " Eligibility for " + course + " is " + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_details_duration_course(query_dict):
    course = query_dict('course')
    message_for_query_to_be_searched = " duration of "+ course 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_details_for_duration_of_course(course)
        generated_response = " Duration of " + course + " is " + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False


def show_details_syllabus_course(query_dict):
    course = query_dict('course')
    message_for_query_to_be_searched = " syllabus of "+ course 
    if bot_confirmation_prompt(message_for_query_to_be_searched):
        query_results = get_details_for_duration_of_course(course)
        generated_response = "Syllabus of " + course + " is " + str(query_results) 
        bot_print_with_name (generated_response)
        return True
    else:
        return False

get_number_of_colleges_in_university = lambda a :  91
