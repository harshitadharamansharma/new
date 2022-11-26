import random

def format_response_number_of_colleges_in_university(response_dict):
    possible_responses = [
        "There are {no_of_colleges} offering Undergraduate courses at the university", 
        "There are {no_of_colleges} colleges affiliated by the University." 
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = response_dict["no_of_college"])  
    return generated_response


def format_response_number_of_faculties_in_university(response_dict):
    possible_responses = [
        "There are {no_of_faculties} faculties at the university", 
        "There are {no_of_faculties} faculties the University.", 
        "{no_of_faculties} faculties are there at DU." 
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_faculties = response_dict["no_of_faculties"])  
    return generated_response


def format_response_number_of_departments_in_university(response_dict):
    possible_responses = [
        "There are {no_of_departments} departments at the university", 
        "There are {no_of_departments} departments the University.", 
        "{no_of_departments} departments are there at DU." 
        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_departments = response_dict["no_of_departments"]
                                                                    )  
    return generated_response


def format_response_number_of_courses_in_university(response_dict):
    possible_responses = [
        "There are {no_of_courses} UG courses offered the university.", 
        "There are {no_of_courses} undergrad courses at the University.", 
        "{no_of_courses} UG courses are there at DU.", 
        "You can choose among {no_of_courses} for your UG degree at DU." 
        ]
    generated_response = (random.choice(possible_responses)).format(
                                        no_of_courses = response_dict["no_of_courses"]
                                        )  
    return generated_response    


def format_response_number_faculties_in_college(response_dict):
    return "No faculty exists in college"


def format_response_total_number_of_seats_for_course_at_college(response_dict):
    possible_responses = [
        "There are {total_no_of_seats} total seats in {ccourse} at {ccollege}", 
        "There are {total_no_of_seats} seats available in {ccourse} at {ccollege}", 
        "{total_no_of_seats} seats in total in {ccourse} at {ccollege}"
        ]
    generated_response = (random.choice(possible_responses)).format(total_no_of_seats = response_dict["total seats"], 
                                                                    ccollege = response_dict["college"], 
                                                                    ccourse = response_dict["course"]
                                                                    )  
    return generated_response


def format_response_number_of_seats_for_category_for_course_at_college(response_dict):
    possible_responses = [  
                            "There are {no_of_seats} seats in {ccourse} at {ccollege}", 
                            "There are {no_of_seats} seats available for {ccategory} in {ccourse} at {ccollege}", 
                            "{no_of_seats} seats for {ccategory} in {ccourse} at {ccollege}"
                            ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_seats = response_dict["seats"],
                                                                    ccollege = response_dict["college"],
                                                                    ccourse = response_dict["course"],
                                                                    ccategory = response_dict["category"],
                                                                    )
    return generated_response

def format_response_number_of_courses_at_college(response_dict):
    return "data is not available"



def format_response_number_of_courses_in_faculty(response_dict):
    possible_responses = [
                        "There are {no_of_courses} courses at {ccollege}", 
                        "{no_of_courses} courses are there at {ccollege}"]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_seats = len(response_dict["number_of_college"]),
                                                                    ccollege = response_dict["college"]
                                                                    )  
    return generated_response

def format_response_number_of_courses_in_department(response_dict):
    pass


def format_response_number_of_courses_in_department_at_college(response_dict):
    pass


def format_response_number_of_department_at_college(response_dict):
    pass


def format_response_number_of_department_under_faculty_at_college(response_dict):
    pass

def format_response_number_of_department_under_faculty(response_dict):
    possible_responses = [
                        "There are {no_of_departments} departments under {ffaculty}.", 
                        "{no_of_departments} departments are there under {ffaculty}."
                        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_departments = len(response_dict["department_under_faculty_set"]), 
                                                                    ffaculty = response_dict["faculty"]
                                                                    )  
    return generated_response



def format_response_number_of_colleges_offering_course(response_dict):
    possible_responses = ["There are {no_of_colleges} offering {ccourse}.", 
                            "There are {no_of_colleges} offering {ccourse}.", 
                            "{no_of_colleges} are there offering {ccourse}."
                        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                no_of_colleges = len(response_dict["colleges_offering_course_set"]), 
                                                                ccourse = response_dict["course"] 
                                                                )  
    return generated_response 

def format_response_list_of_faculties_in_college(response_dict):
    pass

def format_response_list_of_colleges_in_university(response_dict):

    serial_no = 1
    final_output_list = ''
    for i in response_dict["college_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = [
                        "There are {no_of_colleges} offering Undrgraduate courses at the university. Here is the list of all the colleges at DU:- \n{s}", 
                        "There are {no_of_colleges} colleges affiliated by the University. Here is the list of all the colleges at DU:- \n{s}" 
                        ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = len(response_dict["college_set"]), 
                                                                    s = final_output_list )   
    # print(str(generated_response)) 
    return generated_response 


def format_response_list_of_faculties_in_university(response_dict):

    serial_no = 1
    final_output_list = ''
    for i in response_dict["faculties_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = ["There are {no_of_faculties} faculties at the university. Here is the list:- \n{s}", "There are {no_of_faculties} faculties the University. Here is the list of all the faculties at DU:- \n{s}", "{no_of_faculties} faculties are there at DU. Here is the list of all the faculties at DU:- \n{s}" ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_faculties = len(response_dict["faculties_set"]), 
                                                                    s = final_output_list
                                                                    )  
    return generated_response


def format_response_list_of_departments_in_university(response_dict):
    serial_no = 1
    final_output_list = ''
    for i in response_dict["departments_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1
    
    possible_responses = [
                        "There are {no_of_departments} departments at the university. Here is the list of all the departments at DU:- \n{s}", 
                        "There are {no_of_departments} departments the University. Here is the list of all the departments at DU:- \n{s}", 
                        "{no_of_departments} departments are there at DU. Here is the list of all the departments at DU:- \n{s}" 
                        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_departments = len(response_dict["departments_set"]), 
                                                                    s = final_output_list
                                                                    )  
    return generated_response


def format_response_list_of_courses_in_university(response_dict):
    serial_no = 1  
    final_output_list = ''
    for i in response_dict["courses_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1
    # print(final_output_list)
    possible_responses = ["There are {no_of_courses} UG courses offered the university. Here is the list of all the courses at DU:- \n{s}", 
                        "There are {no_of_courses} undergrad courses at the University. Here is the list of all the courses at DU:- \n{s}", 
                        "{no_of_courses} UG courses are there at DU.  Here is the list of all the courses at DU:- \n{s}", 
                        "You can choose among {no_of_courses} courses for your UG degree at DU. Here is the list of all the courses at DU:- \n{s}" 
                        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_courses = len(response_dict["courses_set"]), 
                                                                    s = final_output_list)  
    return generated_response 


def format_response_list_of_courses_at_college(response_dict):
    serial_no = 1
    final_output_list = ''
    for i in response_dict["courses_at_college_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = [
        "There are {no_of_courses} courses at {ccollege}. Here is the list of courses available at {ccollege} at DU:- \n{s}", 
        "There are {no_of_courses} courses at {ccollege}. \nHere is the list of courses available at {ccollege} at DU:- \n{s}", 
        "{no_of_courses} courses are there at {ccollege}.\n Here is the list of courses available at {ccollege} at DU:- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_courses = response_dict["courses_at_college_set"], 
                                                                    ccollege = response_dict["college"], 
                                                                    s = final_output_list 
                                                                    )  
    return generated_response 


def format_response_list_of_courses_in_faculty(response_dict):
    pass

def format_response_list_of_courses_in_department(response_dict):
    pass

def format_response_list_of_courses_in_department_at_college(response_dict):
    pass

def format_response_list_of_department_at_college(response_dict):
    pass

def format_response_list_of_department_under_faculty_at_college(response_dict):
    pass

def format_response_list_of_department_under_faculty(response_dict):   
    serial_no = 1
    final_output_list = ''
    for i in response_dict["department_under_faculty_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = [
        "There are {no_of_departments} departments under {ffaculty}.\nHere is the list :- \n{s}", 
        "{no_of_departments} departments are there under {ffaculty}.\nHere is the list :- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_departments = len(response_dict["department_under_faculty_set"]), 
                                                                    ffaculty = response_dict["faculty"], 
                                                                    s = final_output_list
                                                                    )  

    return generated_response


def format_response_list_of_colleges_offering_course(response_dict):
    
    serial_no = 1
    final_output_list = ''
    for i in response_dict["colleges_offering_course_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1
    
    possible_responses = [
        "There are {no_of_colleges} offering {ccourse}.\nHere is the list :- \n{s}", 
        "There are {no_of_colleges} offering {ccourse}.\nHere is the list :- \n{s}", 
        "{no_of_colleges} are there offering {ccourse}.\nHere is the list :- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = len(response_dict["colleges_offering_course_set"]), 
                                                                    ccourse = response_dict["colleges_offering_course_set"], 
                                                                    s = final_output_list 
                                                                    )  
    return generated_response

def format_response_cutoff_for_category_for_course_college(response_dict):
    pass

def format_response_cutoff_for_course_for_college(response_dict):
    pass

def format_response_coursefee_for_category_for_course_college(response_dict):
    
    possible_responses = [
        "Course fee of {ccourse} for {ccategory} at {ccollege} is INR {coursefee_for_enquired_category} ", 
        "Students from {ccategory} need to pay INR {coursefee_for_enquired_category} for {ccourse} at {ccollege}."
        ]
    generated_response = (random.choice(possible_responses)).format(coursefee_for_enquired_category = response_dict["coursefee"], 
                                                                    ccollege = response_dict["college"], 
                                                                    ccourse = response_dict["course"], 
                                                                    ccategory = response_dict["category"] 
                                                                    )  
    return generated_response


def format_response_details_for_eligibility_of_course(response_dict):
    pass

def format_response_details_for_duration_of_course(response_dict):
    pass

def format_response_details_for_duration_of_course(response_dict):
    pass

