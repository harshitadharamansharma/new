import random
# from utils import check_and_add_available_link_in_response

def check_and_add_available_link_in_response(response_dict,generated_response):
    if "link" in response_dict.keys():
        special_message = (random.choice("\nFor more information, we recommend you to refer these links:- \n {link}", "\nPlease check these links for details regarding this course\n:-{link}", "\nPlease refer this link to get your query resolved \n {link}","\ncheck out thids link: {link} to know more", "\nThis information may vary. Validate it from the link provided below below.\n{link}")).format(link = response_dict["link"])
        generated_response += special_message
    return generated_response


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


def format_response_number_of_programmes_in_university(response_dict):
    possible_responses = [
        "There are {no_of_courses} UG programmes / courses offered the university.", 
        "There are {no_of_courses} undergrad programme / courses at the University.", 
        "{no_of_courses} UG programme / courses are there at DU.", 
        "You can choose among {no_of_courses} for your UG degree at DU." 
        ]
    generated_response = (random.choice(possible_responses)).format(
                                        no_of_courses = response_dict["no_of_programmes"]
                                        )  
    return generated_response    


def format_response_number_faculties_in_college(response_dict):
    return "No faculty exists in college"


def format_response_total_number_of_seats_for_degree_degreetype_course_at_college(response_dict):
    generated_response = str()
    if response_dict["programme_not_available_flag"] == True:
        generated_response == "This Programme is not available in this college."
    else:
        possible_responses = [
        "There are {total_no_of_seats} total seats in {dg} {dt} {crs} at {clg}", 
        "There are {total_no_of_seats} seats available in {dg} {dt} {crs} at {clg}", 
        "{total_no_of_seats} seats in total for {dg} {dt} {crs} at {clg}"
        ]
        generated_response = (random.choice(possible_responses)).format(total_no_of_seats = response_dict["total seats"], 
                                                                    clg = response_dict["college"], 
                                                                    dg = response_dict["degree"],
                                                                    dt = response_dict["degreetype"],
                                                                    crs = response_dict["course"]
                                                                    )  
        generated_response = check_and_add_available_link_in_response(response_dict,generated_response)
    return generated_response


def format_response_number_of_seats_for_category_for_degree_degreetype_course_at_college(response_dict):
    possible_responses = [  
                            "There are {no_of_seats} seats in {dg} {dt} {crs} at {clg}", 
                            "There are {no_of_seats} seats available for {ctgry} in {dg} {dt} {crs} at {clg}", 
                            "{no_of_seats} seats for {ctgry} in {dg} {dt} {crs} at {clg}"
                            ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_seats = response_dict["seats"],
                                                                    clg = response_dict["college"].title(), 
                                                                    dg = response_dict["degree"].title(),
                                                                    dt = response_dict["degreetype"],
                                                                    crs = response_dict["course"].title(),
                                                                    ctgry = response_dict["category"].upper(),
                                                                    )
    generated_response_with_link = check_and_add_available_link_in_response(response_dict,generated_response)   
    return generated_response_with_link


def format_response_number_of_programmes_at_college(response_dict):
    possible_responses = [
                        "There are {no_of_prgms} programmes at {clg}", 
                        "{no_of_prgms} programmes are there at {clg}"]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_prgms = response_dict["no_of_programmes_at_college_set"],
                                                                    clg = response_dict["college"]
                                                                    )  
    return generated_response


def format_response_number_of_courses_in_faculty(response_dict):
    return "data is not available"


def format_response_number_of_courses_in_department(response_dict):
    return "data is not available"


def format_response_number_of_courses_in_department_at_college(response_dict):
    return "data is not available"


def format_response_number_of_department_at_college(response_dict):
    return "data is not available"


def format_response_number_of_department_under_faculty_at_college(response_dict):
    return "data is not available"

def format_response_number_of_department_under_faculty(response_dict):
    # possible_responses = [
    #                     "There are {no_of_departments} departments under {ffaculty}.", 
    #                     "{no_of_departments} departments are there under {ffaculty}."
    #                     ]
    # generated_response = (random.choice(possible_responses)).format(
    #                                                                 no_of_departments = len(response_dict["department_under_faculty_set"]), 
    #                                                                 ffaculty = response_dict["faculty"]
    #                                                                 )  
    # return generated_response
    return "not processing this query right now"


def format_response_number_of_colleges_offering_degree_degreetype_course(response_dict):
    possible_responses = ["There are {no_of_colleges} offering {prgm}.", 
                            "There are {no_of_colleges} offering {prgm}.", 
                            "{no_of_colleges} are there offering {prgm}."
                        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                no_of_colleges = len(response_dict["colleges_offering_programme_set"]), 
                                                                prgm = response_dict["programme"] 
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


def format_response_list_of_programmes_in_university(response_dict):
    serial_no = 1  
    final_output_list = ''
    for i in response_dict["programmes_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1
    # print(final_output_list)
    possible_responses = ["There are {no_of_courses} UG programmes / courses offered the university. Here is the list of all the courses at DU:- \n{s}", 
                        "There are {no_of_courses} undergrad programmes / courses at the University. Here is the list of all the courses at DU:- \n{s}", 
                        "{no_of_courses} UG programmes / courses are there at DU.  Here is the list of all the courses at DU:- \n{s}", 
                        "You can choose among {no_of_courses} programmes / courses for your UG degree at DU. Here is the list of all the courses at DU:- \n{s}" 
                        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_courses = len(response_dict["programmes_set"]), 
                                                                    s = final_output_list)  
    return generated_response 


def format_response_list_of_programmes_at_college(response_dict):
    serial_no = 1
    final_output_list = ''
    for i in response_dict["programme_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = [
        "There are {no_of_courses} programmes / courses at {clg}. Here is the list of programmes / courses available at {clg} at DU:- \n{s}", 
        "There are {no_of_courses} programmes / courses at {clg}. \nHere is the list of programmes / courses available at {clg} at DU:- \n{s}", 
        "{no_of_courses} programmes / courses are there at {clg}.\n Here is the list of programmes / courses available at {clg} at DU:- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_courses = response_dict["programme_set"], 
                                                                    clg = response_dict["college"], 
                                                                    s = final_output_list 
                                                                    )  
    return generated_response 


def format_response_list_of_programmes_in_faculty(response_dict):
    pass

def format_response_list_of_programmes_in_department(response_dict):
    pass

def format_response_list_of_programmes_in_department_at_college(response_dict):
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


def format_response_list_of_colleges_offering_degree_degreetype_course(response_dict):
    
    serial_no = 1
    final_output_list = ''
    for i in response_dict["colleges_offering_programme_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1
    
    possible_responses = [
        "There are {no_of_colleges} offering {prgm}.\nHere is the list :- \n{s}", 
        "There are {no_of_colleges} offering {prgm}.\nHere is the list :- \n{s}", 
        "{no_of_colleges} are there offering {prgm}.\nHere is the list :- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = len(response_dict["colleges_offering_programme_set"]),
                                                                    prgm = response_dict["programme"],
                                                                    s = final_output_list 
                                                                    )  
    return generated_response


def format_response_cutoff_for_category_for_degree_degreetype_course_college(response_dict):
    pass

def format_response_cutoff_for_degree_degreetype_course_for_college(response_dict):
    pass

def format_response_coursefee_for_category_for_degree_degreetype_course_college(response_dict):   
    possible_responses = [
        "Course fee of {prgm} for {ctgry} at {clg} is INR {coursefee_for_enquired_category} ", 
        "Students from {ctgry} need to pay INR {coursefee_for_enquired_category} for {prgm} at {clg}."
        ]
    generated_response = (random.choice(possible_responses)).format(coursefee_for_enquired_category = response_dict["coursefee"], 
                                                                    clg = response_dict["college"], 
                                                                    prgm = response_dict["programme"], 
                                                                    ctgry = response_dict["category"] 
                                                                    )  
    return generated_response


def format_response_details_for_eligibility_of_degree_degreetype_course(response_dict):
    possible_responses = [
        "Get details regarding eligibility for {prgm} here:-\n {link}", 
        "Find eligibility details for {prgm} here at this link:- \n{link}"
        ]
    generated_response = (random.choice(possible_responses)).format(prgm = response_dict["programme"], 
                                                                    link = response_dict["link"] 
                                                                    )  
        
    return generated_response


def format_response_details_for_duration_of_degree_degreetype_course(response_dict):
    possible_responses = [
        "Get details regarding {prgm} duration and other related details here:-\n{link}", 
        "Find duration and syllabus related details for {prgm} here at this link:- \n{link}",
        "Get duration and related information for {prgm} here at this link:- \n{link}"
        ]
    generated_response = (random.choice(possible_responses)).format(prgm = response_dict["programme"], 
                                                                    link = response_dict["link"] 
                                                                    )  
        
    return generated_response

def format_response_details_for_syllabus_of_degree_degreetype_course(response_dict):
    possible_responses = [ 
        "Get details regarding syllabus of {prgm} here:-\n{link}", 
        "Find syllabus related details for {prgm} here at this link:- \n{link}"
        ]
    generated_response = (random.choice(possible_responses)).format(prgm = response_dict["programme"], 
                                                                    link = response_dict["link"] 
                                                                    )  
        
    return generated_response

