import random
# from utils import check_and_add_available_link_in_response

# def check_and_add_available_link_in_response(response_dict,generated_response):
#     # if "link" in response_dict.keys():
#     possible_response_list = ["\nFor more information, we recommend you to refer these links:- \n {link}", "\nPlease check these links for details regarding this course\n:-{link}", "\nPlease refer this link to get your query resolved \n {link}","\ncheck out this link: {link} to know more", "\nThis information may vary. Validate it from the link provided below below.\n{link}"]
#     if response_dict["programme_not_available_flag"] == True:
#         special_message = (random.choice(possible_response_list)).format(link = response_dict["link"])
#         generated_response += special_message
#     return generated_response

#1
def format_response_number_of_colleges_in_university(response_dict):
    possible_responses = [
        "There are {no_of_colleges} colleges offering Undergraduate courses at the university", 
        "There are {no_of_colleges} colleges affiliated by the University." 
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_colleges = response_dict["no_of_college"])  
    return generated_response

#2
def format_response_number_of_faculties_in_university(response_dict):
    possible_responses = [
        "There are {no_of_faculties} faculties at the university", 
        "There are {no_of_faculties} faculties the University.", 
        "{no_of_faculties} faculties are there at DU." 
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_faculties = response_dict["no_of_faculties"])  
    return generated_response

#3
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

#4
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

#5
def format_response_number_faculties_in_college(response_dict):
    return "No faculty exists in a college"

#6
def format_response_total_number_of_seats_for_degree_degreetype_course_at_college(response_dict):
    generated_response = str()
    if response_dict["programme_not_available_flag"] == True:
        generated_response = "{dg} {dt} {crs} is not available in {clg}".format(dg = response_dict["degree"].title(), dt = response_dict["degreetype"], crs = response_dict["course"].title(), clg = response_dict["college"].title())    # "This Programme is not available in this college."

    elif response_dict["ba_program_flag"] == True : # len(response_dict["link"]) != 0:   # we are getting response_dict["link"] from the rule_handler when degree  == "B.A." and degreetype == "program".
        generated_response = "{clg} offers {dg} {dt}, but the number of seats for may vary according the combination of courses you select for the degree. You can find related details by following this link : {link}".format(link = response_dict["link"], dg = response_dict["degree"].title(), dt = response_dict["degreetype"].title(), clg = response_dict["college"].title())
    
    else:
        possible_responses = [
        "There are {total_no_of_seats} total seats in {dg} {dt} {crs} at {clg}", 
        "There are {total_no_of_seats} seats available in {dg} {dt} {crs} at {clg}", 
        "{total_no_of_seats} seats in total for {dg} {dt} {crs} at {clg}"
        ]
        generated_response = (random.choice(possible_responses)).format(total_no_of_seats = response_dict["total seats"], 
                                                                    clg = response_dict["college"].title(), 
                                                                    dg = response_dict["degree"].title(),
                                                                    dt = response_dict["degreetype"],
                                                                    crs = response_dict["course"].title()                       
                                                                    )  
        # generated_response = check_and_add_available_link_in_response(response_dict,generated_response)
    return generated_response

#7
def format_response_number_of_seats_for_category_for_degree_degreetype_course_at_college(response_dict):
    # print("formatter")
    generated_response = str()
    if response_dict["programme_not_available_flag"] == True:
        generated_response = "{dg} {dt} {crs} is not available in {clg}".format(dg = response_dict["degree"].title(), dt = response_dict["degreetype"], crs = response_dict["course"].title(), clg = response_dict["college"].title())    # "This Programme is not available in this college."
        # print("hh")
    
    elif response_dict["ba_program_flag"] == True : # len(response_dict["link"]) != 0:   # we are getting response_dict["link"] from the rule_handler when degree  == "B.A." and degreetype == "program".
        generated_response = "{clg} offers {dg} {dt}, but the number of seats for may vary according the combination of courses you select for the degree. You can find related details by following this link : {link}".format(link = response_dict["link"], dg = response_dict["degree"].title(), dt = response_dict["degreetype"].title(), clg = response_dict["college"].title())
    
    else:
        possible_responses = [  
        "There are {no_of_seats} seats for {ctgry} category in {dg} {dt} {crs} at {clg}", 
        "There are {no_of_seats} seats available for {ctgry} category in {dg} {dt} {crs} at {clg}", 
        "{no_of_seats} seats for {ctgry} category in {dg} {dt} {crs} at {clg}"
        ]

        generated_response = (random.choice(possible_responses)).format(no_of_seats = response_dict["seats"],
                                                                        clg = response_dict["college"].title(), 
                                                                        dg = response_dict["degree"].title(),
                                                                        dt = response_dict["degreetype"],
                                                                        crs = response_dict["course"].title(),
                                                                        ctgry = response_dict["category"]
                                                                        )
        # generated_response_with_link = check_and_add_available_link_in_response(response_dict,generated_response)   
    return generated_response

#8
def format_response_number_of_programmes_at_college(response_dict):
    possible_responses = [
                        "There are {no_of_prgms} programmes at {clg}", 
                        "{no_of_prgms} programmes are there at {clg}"]
    generated_response = (random.choice(possible_responses)).format(
                                                                    no_of_prgms = response_dict["no_of_programmes_at_college_set"],
                                                                    clg = response_dict["college"]
                                                                    )  
    return generated_response

#9
def format_response_number_of_programmes_in_faculty(response_dict):
    return "data is not available"

#10
def format_response_number_of_programmes_in_department(response_dict):
    return "data is not available"

#11
def format_response_number_of_programmes_in_department_at_college(response_dict):
    return "data is not available"

#12
def format_response_number_of_department_at_college(response_dict):
    return "data is not available"

#13
def format_response_number_of_department_under_faculty_at_college(response_dict):
    return "data is not available"

#14
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

#15
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

#16
def format_response_list_of_faculties_in_college(response_dict):
    pass

#17
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

#18
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

#19
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

#20
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

#21
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
                                                                    no_of_courses = len(response_dict["programme_set"]), 
                                                                    clg = response_dict["college"], 
                                                                    s = final_output_list 
                                                                    )  
    return generated_response 

#22
def format_response_list_of_programmes_in_faculty(response_dict):
    pass

#23
def format_response_list_of_programmes_in_department(response_dict):
    pass

#24
def format_response_list_of_programmes_in_department_at_college(response_dict):
    pass

#25
def format_response_list_of_department_at_college(response_dict):
    pass

#26
def format_response_list_of_department_under_faculty_at_college(response_dict):
    pass

#27
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

#28
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
                                                                    prgm = response_dict["programme"].strip(),
                                                                    s = final_output_list 
                                                                    )  
    return generated_response

#29
def format_response_cutoff_for_category_for_degree_degreetype_course_college(response_dict):
    pass

#30
def format_response_cutoff_for_degree_degreetype_course_for_college(response_dict):
    pass

#31
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

#32
def format_response_details_for_degree_degreetype_course(response_dict):
    possible_responses = [
        "Get details regarding course {details} for {prgm} here:-\n {link}", 
        "Find course {details} and retaled details for {prgm} here at this link:- \n{link}"
        ]
    generated_response = (random.choice(possible_responses)).format(prgm = response_dict["programme"], 
                                                                    link = response_dict["link"],
                                                                    details = response_dict["details"]
                                                                    )  
        
    return generated_response

# #32
# def format_response_details_for_eligibility_of_degree_degreetype_course(response_dict):
#     possible_responses = [
#         "Get details regarding eligibility for {prgm} here:-\n {link}", 
#         "Find eligibility details for {prgm} here at this link:- \n{link}"
#         ]
#     generated_response = (random.choice(possible_responses)).format(prgm = response_dict["programme"], 
#                                                                     link = response_dict["link"] 
#                                                                     )  
        
#     return generated_response

# #33
# def format_response_details_for_duration_of_degree_degreetype_course(response_dict):
#     possible_responses = [
#         "Get details regarding {prgm} duration and other related details here:-\n{link}", 
#         "Find duration and syllabus related details for {prgm} here at this link:- \n{link}",
#         "Get duration and related information for {prgm} here at this link:- \n{link}"
#         ]
#     generated_response = (random.choice(possible_responses)).format(prgm = response_dict["programme"], 
#                                                                     link = response_dict["link"] 
#                                                                     )  
        
#     return generated_response


# def format_response_details_for_syllabus_of_degree_degreetype_course(response_dict):
#     possible_responses = [ 
#         "Get details regarding syllabus of {prgm} here:-\n{link}", 
#         "Find syllabus related details for {prgm} here at this link:- \n{link}"
#         ]
#     generated_response = (random.choice(possible_responses)).format(prgm = response_dict["programme"], 
#                                                                     link = response_dict["link"] 
#                                                                     )  
        
#     return generated_response



#33
def format_response_number_of_programme_under_degree(response_dict):

    possible_responses = [
        "There are {no_of_programmes} programmes under {degree} degree.", 
        "{no_of_programmes} programmes are there under {degree} degree."
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_programmes = len(response_dict["programme_set"]), 
                                                                    degree = response_dict["degree"], 
                                                                    )  

    return generated_response


#34
def format_response_list_of_programme_under_degree(response_dict):
    serial_no = 1
    final_output_list = ''
    for i in response_dict["programme_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = [
        "There are {no_of_programmes} programmes under {degree} degree.\nHere is the list :- \n{s}", 
        "{no_of_programmes} programmes are there under {degree} degree.\nHere is the list :- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_programmes = len(response_dict["programme_set"]), 
                                                                    degree = response_dict["degree"], 
                                                                    s = final_output_list
                                                                    )  

    return generated_response

#35
def format_response_number_of_programme_under_degreetype(response_dict):

    possible_responses = [
        "There are {no_of_programmes} programmes of under {degreetype} degreetype.", 
        "{no_of_programmes} programmes are there under {degreetype} degreetype."
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_programmes = len(response_dict["programme_set"]), 
                                                                    degreetype = response_dict["degreetype"], 
                                                                    )  

    return generated_response


#36
def format_response_list_of_programme_under_degreetype(response_dict):
    serial_no = 1
    final_output_list = ''
    for i in response_dict["programme_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = [
        "There are {no_of_programmes} programmes under {degreetype} degreetype.\nHere is the list :- \n{s}", 
        "{no_of_programmes} programmes are there under {degreetype} degreetype.\nHere is the list :- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_programmes = len(response_dict["programme_set"]), 
                                                                    degreetype = response_dict["degreetype"], 
                                                                    s = final_output_list
                                                                    )  

    return generated_response




#37
def format_response_number_of_programme_under_degree_degreetype(response_dict):

    possible_responses = [
        "There are {no_of_programmes} programmes of under {degree} degree and {degreetype} degreetype.", 
        "{no_of_programmes} programmes are there under {degree} degree and {degreetype} degreetype."
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_programmes = len(response_dict["programme_set"]), 
                                                                    degree = response_dict["degree"],
                                                                    degreetype = response_dict["degreetype"] 
                                                                    )  

    return generated_response


#38
def format_response_list_of_programme_under_degree_degreetype(response_dict):
    serial_no = 1
    final_output_list = ''
    for i in response_dict["programme_set"]:
        a = "\n" + str(serial_no)+ ". " + i 
        final_output_list += a
        serial_no += 1

    possible_responses = [
        "There are {no_of_programmes} programmes under {degree} degree and {degreetype} degreetype.\nHere is the list :- \n{s}", 
        "{no_of_programmes} programmes are there under {degree} degree and {degreetype} degreetype.\nHere is the list :- \n{s}"
        ]
    generated_response = (random.choice(possible_responses)).format(no_of_programmes = len(response_dict["programme_set"]), 
                                                                    degree = response_dict["degree"],
                                                                    degreetype = response_dict["degreetype"], 
                                                                    s = final_output_list
                                                                    )  

    return generated_response

#39
def format_response_for_availability_of_programme_in_college(query_dict):
    pass

#40
def format_response_for_availability_of_degree_in_college(query_dict):
    pass

#41 
def format_response_for_availability_of_degreetype_degree_in_college(query_dict):
    pass

