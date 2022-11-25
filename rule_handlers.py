# frofaculty_department_collegem utils import invalid_query_prompt #,bot_print_with_name, bot_print
import random
import csv

path_1 = "C:\du_chatbot_terminal\data\college_course_category_seats.csv"
file_1 = open(path_1, newline = '')
reader1 = csv.reader(file_1)
header1 = next(reader1)

path_2 = "C:\du_chatbot_terminal\data\\faculty_department.csv"
file_2 = open(path_2, newline = '')
reader2 = csv.reader(file_2)
header2 = next(reader2)


path_3 = "C:\du_chatbot_terminal\data\college_course.csv"
file_3 = open(path_3, newline = '')
reader3 = csv.reader(file_3)
header3 = next(reader3)

path_4 = "C:\du_chatbot_terminal\data\college_course_category_coursefee.csv"
file_4 = open(path_4, newline = '')
reader4 = csv.reader(file_4)
header4 = next(reader4)


# def get_csv_iterator(path):
#     file = open(path, newline = "")

# path_1 = "D:\\new_chat\\new_bot\data\college_course_category_seats.csv"
# file_1 = open(path_1, newline = '')
# reader1 = csv.reader(file_1)
# header1 = next(reader1)


# path_2 = "D:\\new_chat\\new_bot\data\\faculty_department.csv"
# file_2 = open(path_2, newline = '')
# reader2 = csv.reader(file_2)
# header2 = next(reader2)

# path_3 = "D:\\new_chat\\new_bot\data\college_course.csv"
# file_3 = open(path_3, newline = '')
# reader3 = csv.reader(file_3)
# header3 = next(reader3)

# path_4 = "D:\new_chat\new_bot\data\college_course_category_coursefee.csv"
# file_4 = open(path_4, newline = '')



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

    colleges_set = set()

    for row in reader4:
        colleges_set.add(row[0].strip().title())
        # print(row[0])

    response_dict = dict()
    response_dict["colleges_set"] = colleges_set
    response_dict["no_of_college"] = len(colleges_set)

    file_4.seek(0)
    next(reader4)


    return response_dict
    

#file reader iterator needs to go to the first line after everycall


def get_number_of_faculties_in_university (query_dict): 
    faculties_set = set()
    for row in reader2:
        faculties_set.add(row[0].strip().title())

    response_dict = dict()
    response_dict["faculties_set"] = faculties_set
    response_dict["no_of_faculties"] = len(faculties_set)

    file_2.seek(0)
    next(reader2)

    return response_dict


def get_number_of_departments_in_university(query_dict): 

    departments_set = set()
    for row in reader2:
        departments_set.add(row[1].strip().title())
    
    response_dict = dict()
    response_dict["departments_set"] = departments_set
    response_dict["no_of_departments"] = len(departments_set)
   
    file_2.seek(0)
    reader2.next()

    return response_dict


def get_number_of_courses_in_university(query_dict):

    courses_set = set()
    for row in reader3:
        courses_set.add(row[1].strip().title())

    response_dict = dict()
    response_dict["courses_set"] = courses_set
    response_dict["no_of_courses"] = len(courses_set)
      
    file_3.seek(0)
    next(reader3)

    return response_dict

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
    return "No faculty exists in college"

def get_total_number_of_seats_for_course_at_college(query_dict):
    college = query_dict['college']
    course = query_dict['course']

    for row in reader1:
        if row[0].lower() == college.lower() and row[1].lower() == course.lower():
            query_results = int(row[2])

    response_dict = dict()
    response_dict["college"] = college
    response_dict["course"] = course
    response_dict["total seats"] = query_results

    file_1.seek(0)
    next(reader1)

    return response_dict
    

def get_number_of_seats_for_category_for_course_at_college(query_dict):
    college = query_dict['college']
    course = query_dict['course']
    category = query_dict['category']

    category_index_form_csv = header1.index(category)

    for row in reader1:
        if row[0].lower() == college.lower() and row[1].lower() == course.lower() :
            query_results = int(row[category_index_form_csv])

    # query_results = 7 #logic to count total no. of seats for a course at a college  ; form the csv, --> available doc has seat matrix for category for course at all the colleges ; category,course,college
    response_dict = dict()
    response_dict["college"] = college
    response_dict["course"] = course
    response_dict["category"] = category
    response_dict["seats"] = query_results
    
    return response_dict

    

def get_number_of_courses_at_college(query_dict):
    if query_dict['entity'] == 'course' :
        college = query_dict['college']

        courses_at_college_set = set()

        for row in reader1:
            if row[0].lower() == college.lower():
                courses_at_college_set.add(row[1].strip().title())

        query_results = len(courses_at_college_set)

        response_dict = dict()
        response_dict["college"] = college
        response_dict["college_set"] = courses_at_college_set
        response_dict["no_of_courses_at_college_set"] = query_results

        return response_dict
    else :
        get_number_of_colleges_offering_course(query_dict)



def get_number_of_courses_in_faculty(query_dict):
    # faculty = query_dict['faculty']    

    # path = "D:\\new_chat\\new_n\\faculty_course.csv"
    # file = open(path, newline = '')
    # reader = csv.reader(file)
    # header = next(reader)

    # courses_at_faculty_set = set()
    # for row in reader:
    #     if row[0].lower() == faculty.lower():
    #         courses_at_faculty_set.add(row[2])

    
    # query_results = len(courses_at_faculty_set) 
    #pass facultyname #logic to count total no. course faculty; form the csv, --> available doc ?

    # possible_responses = ["There are {no_of_courses} courses at {ffaculty}", "There are {no_of_courses} courses at {ffaculty}", "{no_of_courses} courses at {ffaculty}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_courses = query_results, ffaculty = faculty )  

    # return generated_response
    return "data is not available"


def get_number_of_courses_in_department(query_dict):
    # department = query_dict['department']    

    # reader = csv.reader(file_) # DEPARTMENT _ COURSE
    # header = next(reader)

    # courses_in_department_set = set()
    # for row in reader:
    #     if row[1].lower() == department.lower():
    #         courses_in_department_set.add(row[2])

    # query_results = len(courses_in_department_set) #pass college name #logic to count total no. course at a college  ; form the csv, --> available doc no of courses per college with vcategoruy wise fee

    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment}", "There are {no_of_courses} courses at {ddepartment}", "{no_of_courses} courses at {ddepartment}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department )  

    # return generated_response
    return "data is not available"


def get_number_of_courses_in_department_at_college(query_dict):
    # college level department
    # to be discussed college level detail 
    # college = query_dict['college']
    # department = query_dict['department']    

    # query_results = 11 #pass collegename and dept name #logic to count total no. course at a college  ; form the csv, --> available doc no of courses per college with vcategoruy wise fee
   
    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment} at {ccollege}.", "There are {no_of_courses} courses at {ddepartment} at {ccollege}.", "{no_of_courses} courses at {ddepartment} at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department, ccollege = college )  

    # return generated_response
    return "college level detail ... will be updated soon"


def get_number_of_department_at_college(query_dict):
    # college level department
    #college level detail
    # create college dept document;
    # college = query_dict['college']

    # query_results = 12 #pass college name #logic to count total no. departments at a college  ; form the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will be updated soon"


def get_number_of_department_under_faculty_at_college(query_dict):    
 #clear
    # list of department at college level needs to be categorized faculty wise
    # faculty = query_dict['faculty']
    # college = query_dict['college']

    # query_results = 13 #pass faculty, department name #logic to count total no. departments at a college  ; form the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will get updated soon"



def get_number_of_department_under_faculty(query_dict):
    faculty = query_dict['faculty']

    department_under_faculty_set = set()
    for row in reader2:
        if row[0].lower() == faculty.lower():
            department_under_faculty_set.add(row[1].strip().title())    

    response_dict = dict()

    response_dict["faculty"] = faculty
    response_dict["department_under_faculty_set"] = department_under_faculty_set

    return response_dict


def get_number_of_colleges_offering_course(query_dict):
    if query_dict['entity'] == 'college':
        course = query_dict['course']

        colleges_offering_course_set = set()

        for row in reader3:
            if row[1].lower() == course.lower() :
                colleges_offering_course_set.add(row[1].strip().title())
        
        response_dict = dict()
        response_dict["course"] = course
        response_dict["colleges_offering_course_set"] = colleges_offering_course_set

        return response_dict
    else:
        get_number_of_courses_at_college(query_dict)



def get_list_of_faculties_in_college(query_dict):
    # faculties at college
    pass
    # return generated_response


def get_list_of_colleges_in_university(query_dict):

    colleges_set = set()
    for row in reader1:
        colleges_set.add(row[0].strip().title())
        # print(row[0])
    
    response_dict = dict()
    response_dict["college_set"] = colleges_set

    return response_dict





def get_list_of_faculties_in_university(query_dict):

    faculties_set = set()
    for row in reader2:
        faculties_set.add(row[0].strip().title())

    response_dict = dict() 
    response_dict["faculties_set"] = faculties_set

    return response_dict


def get_list_of_departments_in_university(query_dict):

    departments_set = set()
    for row in reader2:
        departments_set.add(row[1].strip().title())

    response_dict = dict() 
    response_dict["departments_set"] = departments_set

    return response_dict


def get_list_of_courses_in_university(query_dict):

    courses_set = set()
    for row in reader3:
        courses_set.add(row[1].strip().title())

    response_dict = dict() 
    response_dict["courses_set"] = courses_set
    
    return response_dict


def get_list_of_courses_at_college(query_dict):
    if query_dict['entity'] == 'course':
        college = query_dict['college']

        courses_at_college_set = set()

        for row in reader1:
            if row[0].lower() == college.lower():
                courses_at_college_set.add(row[1].strip().title())
        
        response_dict = dict() 
        response_dict["college"] = college
        response_dict["courses_at_college_set"] = courses_at_college_set

        return response_dict
    else : 
        get_list_of_colleges_offering_course(query_dict)

# def get_list_of_courses_at_college():
#     pass 


def get_list_of_courses_in_faculty(query_dict):
    # faculty = query_dict['faculty']    

    # path = "D:\\new_chat\\new_n\\faculty_course.csv"
    # file = open(path, newline = '')
    # reader = csv.reader(file)
    # header = next(reader)

    # courses_at_faculty_set = set()
    # for row in reader:
    #     if row[0].lower() == faculty.lower():
    #         courses_at_faculty_set.add(row[2])

    
    # query_results = len(courses_at_faculty_set) 
    #pass facultyname #logic to count total no. course faculty; form the csv, --> available doc ?

    # possible_responses = ["There are {no_of_courses} courses at {ffaculty}", "There are {no_of_courses} courses at {ffaculty}", "{no_of_courses} courses at {ffaculty}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_courses = query_results, ffaculty = faculty )  

    # return generated_response
    return (random.choice("data is not available", "data will be availavble soon ..."))


def get_list_of_courses_in_department(query_dict):
    # department = query_dict['department']    


    # reader = csv.reader(file_2)  DEPARTMETN - COURSE
    # header = next(reader)

    # courses_in_department_set = set()
    # for row in reader:
    #     if row[1].lower() == department.lower():
    #         courses_in_department_set.add(row[2])

    # query_results = len(courses_in_department_set) #pass college name #logic to count total no. course at a college  ; form the csv, --> available doc no of courses per college with vcategoruy wise fee

    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment}", "There are {no_of_courses} courses at {ddepartment}", "{no_of_courses} courses at {ddepartment}"]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department )  

    # return generated_response
    return "data is not available"


def get_list_of_courses_in_department_at_college(query_dict):
    # college level department
    # to be discussed college level detail 
    # college = query_dict['college']
    # department = query_dict['department']    

    # query_results = 11 #pass collegename and dept name #logic to count total no. course at a college  ; form the csv, --> available doc no of courses per college with vcategoruy wise fee
   
    # possible_responses = ["There are {no_of_courses} courses offered by {ddepartment} at {ccollege}.", "There are {no_of_courses} courses at {ddepartment} at {ccollege}.", "{no_of_courses} courses at {ddepartment} at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_seats = query_results, ddepartment = department, ccollege = college )  

    # return generated_response
    return "college level detail ... will be updated soon"


def get_list_of_department_at_college(query_dict):
    # college level department
    #college level detail
    # create college dept document;
    # college = query_dict['college']

    # query_results = 12 #pass college name #logic to count total no. departments at a college  ; form the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will be updated soon"


def get_list_of_department_under_faculty_at_college(query_dict):
    #clear
    # list of department at college level needs to be categorized faculty wise
    # faculty = query_dict['faculty']
    # college = query_dict['college']

    # query_results = 13 #pass faculty, department name #logic to count total no. departments at a college  ; form the csv, --> available doc no of courses per college with category wise fee
   
    # possible_responses = ["There are {no_of_departments} departments at {ccollege}.", "There are {no_of_departments} departments at {ccollege}.", "{no_of_departments} departments are there at {ccollege}."]
    # generated_response = (random.choice(possible_responses)).format(no_of_departments = query_results, ccollege = college)  

    # return generated_response
    return "college level detail ... will be updated soon"


def get_list_of_department_under_faculty(query_dict):
    faculty = query_dict['faculty']

    department_under_faculty_set = set()
    for row in reader2:
        if row[0].lower() == faculty.lower():
            department_under_faculty_set.add(row[1].strip().title())    

    response_dict = dict()
    response_dict["faculty"] = faculty
    response_dict["department_under_faculty_set"] = department_under_faculty_set   


def get_list_of_colleges_offering_course(query_dict):
    if query_dict['entity'] == 'college':
        course = query_dict['course']
        
        colleges_offering_course_set = set()

        for row in reader3:
            if row[1].lower() == course.lower() :
                colleges_offering_course_set.add(row[0].strip().title())
    
        response_dict = dict()
        response_dict["course"] = course
        response_dict["colleges_offering_course_set"] = colleges_offering_course_set
        
        return response_dict

    else:
        get_list_of_courses_at_college(query_dict)
    


def get_cutoff_for_category_for_course_college(category, course, college):
    pass 


def get_cutoff_for_course_for_college( course, college):
    pass


def get_coursefee_for_category_for_course_college(query_dict):
    college = query_dict['college']
    course = query_dict['course']
    category = query_dict['category']

    category_index_form_csv = header4.index(category)

    for row in reader4:
        if row[0].lower() == college.lower() and row[1].lower() == course.lower() :
            query_results = int(row[category_index_form_csv])

    response_dict = dict()
    response_dict["college"] = college
    response_dict["course"] = course
    response_dict["category"] = category
    response_dict["coursefee"] = query_results

    return response_dict
    


def get_details_for_eligibility_of_course(query_dict):
    #csv course_eligibility_syllabus_duration_about_...
    return "details will get updated soon" 


def get_details_for_duration_of_course(query_dict):
    #csv course_eligibility_syllabus_duration_about_...
    return "details will get updated soon"
     

def get_details_for_syllabus_of_course(query_dict):
    #csv course_eligibility_syllabus_duration_about_...
    return "details will get updated soon"