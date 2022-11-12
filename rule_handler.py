# def get_courses_for_degree_in_college(/....):
#     pass

# def get_courses_for_degree_in_college(/....):
#     pass

# def get_courses_for_degree_in_college(/....):
#     pass


    # for sh_kw in shortlisted_keywords:
    #     for key in list(keyword_classes.keys()):
    #         if sh_kw in keyword_classes[key]:
    #             shortlisted_keyword_classes.append(key) 


from synonyms import synonyms
from rulebase import rulebase
from utils import bot_confirmation_prompt, bot_print_with_name, bot_print


def next_rule():
    pass


# def call_rulehandler(kw_c): 
#     if synonyms.quantifier in kw_c:
#         if synonyms.college in kw_c:
#             quantifier_college()

#         if synonyms.college in kw_c:
#             quantifier_
            
    


def quantifier_college(query_dict):
    # if synonyms.quantifier in kw_c:
    #     if synonyms.college in kw_c:
    #         get_number_of_colleges_in_university()
    rule_list=['quantifier', 'college']
    if all(value in query_dict.keys() for value in rule_list):
        # college = query_dict['college']
        message_for_query_to_be_searched = " number of colleges affiliated by the University " 
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_colleges_in_university()
            generated_response = "There are " + str(query_results) + " colleges affiliated by the University."  
            bot_print_with_name (generated_response)



def quantifier_faculty(query_dict):
    
    # if synonyms.quantifier in kw_c:
    #     if synonyms.faculty in kw_c:
    #         get_number_of_faculties_in_university()
    rule_list=['faculty']
    if all(value in query_dict.keys() for value in rule_list):
        # college = query_dict['college']
        message_for_query_to_be_searched = " number of faculties in the University " 
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_faculties_in_university()
            generated_response = "There are " + str(query_results) + " colleges faculties in the University"  
            bot_print_with_name (generated_response)




def quantifier_department(query_dict):
    # if synonyms.quantifier in kw_c:
    #     if synonyms.department in kw_c:
    #         get_number_of_departments_in_university()
    rule_list=['department']
    if all(value in query_dict.keys() for value in rule_list):
        # college = query_dict['college']
        message_for_query_to_be_searched = " number of departments in the University " 
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_departments_in_university()
            generated_response = "There are " + str(query_results) + " colleges departments in the University"  
            bot_print_with_name (generated_response)




def quantifier_course(query_dict):
    # if synonyms.quantifier in kw_c:
    #     if synonyms.course in kw_c:
    #         get_number_of_courses_in_university()
    rule_list=['course']
    if all(value in query_dict.keys() for value in rule_list):
        college = query_dict['course']
        message_for_query_to_be_searched = " number of courses in the University " 
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_courses_in_university()
            generated_response = "There are " + str(query_results) + " courses in the University"  
            bot_print_with_name (generated_response)


# def quantifier_faculty_college(kw_c):
#     rule_list=['faculty','college']
#     if all(value in kw_c for value in rule_list):

#         get_number_of_faculties_in_college(faculty,college)


# query should also be a parameter in the method or not?
def quantifier_faculty_college(query_dict):
    rule_list=['faculty','college']
    if all(value in query_dict.keys() for value in rule_list):
        college = query_dict['college']
        message_for_query_to_be_searched = "number of faculties in " + college
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_faculties_in_college(college)
            generated_response = "There are " + str(query_results) + " number of faulties at " + college
            bot_print_with_name (generated_response)
            # bot_print_with_name ( "There are " + str(query_result) + "number of faulties at " + college)                   #"Number of faculties in " + college + "are"
 
 



def quantifier_seats_course_college(query_dict):
    rule_list=['seats','course','college']
    if all(value in query_dict.keys() for value in rule_list):
        college = query_dict['college']
        course = query_dict['course']
        message_for_query_to_be_searched = "total number of seats in "+ course + " at " + college
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_total_number_of_seats_for_course_at_college(course,college)
            generated_response = "There are " + str(query_results) + " total seats in "+ course + " at " + college
            bot_print_with_name (generated_response)





def  quantifier_seats_category_course_college(query_dict):
    rule_list=['seats','category','course','college']
    if all(value in query_dict.keys() for value in rule_list):
        college = query_dict['college']
        course = query_dict['course']
        category = query_dict['category']
        message_for_query_to_be_searched = " number of seats for " + category + " in " + course + " at " + college
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_seats_for_category_for_course_at_college(category,course,college)
            generated_response = "There are " + str(query_results) + " seats for " + category + " in " + course + " at " + college
            bot_print_with_name (generated_response)
        # get_number_of_seats_for_category_for_course_at_college(seats,category,course,college)



def quantifier_course_college(query_dict):
    rule_list=['course','college']
    if all(value in query_dict.keys() for value in rule_list):
        college = query_dict['college']
        message_for_query_to_be_searched = " number of courses at " + college
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_courses_at_college(college)
            generated_response = "There are " + str(query_results) + " courses at " + college
            bot_print_with_name (generated_response)


def quantifier_course_faculty(query_dict):
    rule_list=['course','faculty']
    if all(value in query_dict.keys() for value in rule_list):
        faculty = query_dict['faculty']
        message_for_query_to_be_searched = " number of courses offered by " + faculty
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_courses_in_faculty(faculty)
            generated_response = "There are " + str(query_results) + " courses offered by " + faculty
            bot_print_with_name (generated_response)
        # get_number_of_courses_in_faculty(course,faculty)


def quantifier_course_department(query_dict):
    rule_list=['course','department']
    if all(value in query_dict.keys() for value in rule_list):
        department = query_dict['department']
        message_for_query_to_be_searched = " number of courses offered by " + department
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_courses_in_department(department)
            generated_response = "There are " + str(query_results) + " courses offered by " + department
            bot_print_with_name (generated_response)   



def quantifier_course_department_college(query_dict):
    rule_list=['course','department','college']
    if all(value in query_dict.keys() for value in rule_list):
        college = query_dict['college']
        department = query_dict['department']
        message_for_query_to_be_searched = " number of courses offered by " + department + " at " + college 
        if bot_confirmation_prompt(message_for_query_to_be_searched):
            query_results = get_number_of_courses_in_department_at_college(department,college)
            generated_response = "There are " + str(query_results) + " courses offered by " + department + " at " + college
            bot_print_with_name (generated_response)      
            # get_number_of_courses_in_department_at_college(department,college)


