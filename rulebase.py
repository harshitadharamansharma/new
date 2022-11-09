# rulebase = {
#     1: {
#         "rule_format": "degree_course_college",
#         "rule_handler": get_courses_for_degree_in_college
    
#     },
#     2: {
#         "rule_format": "_degree_course_college",
#         "rule_handler": "get_seatmatrix_for_degree_in_college"
#         #DIFFERENT METHODS TO GET :- 1.TOTAL SEATS; 2.CATEGORY WISE SEATS; 3.
#     }
# #     3: {
# #         "rule_format": "_",
# #         "rule_handler": "get_seatmatrix_courses_for_degree_in_college",
        
# #     }
# #     4: {
# #         "rule_format": "degree_course_college_SC",
# #         "rule_handler": "get_seatmatrix_courses_for_degree_in_college",
# #     }
# }



rulebase = {
    1: {
        "rule_format": "quantifier_college",
        "rule_handler": "get_number_of_colleges_in_university"
    
    },
    2: {
        "rule_format": "quantifier_faculty",
        "rule_handler": "get_number_of_faculties_in_university"
    },
    3: {
        "rule_format": "quantifier_department",
        "rule_handler": "get_number_of_departments_in_university"
    },
    4:  {  
        "rule_format": "quantifier_course",
        "rule_handler": "get_number_of_courses_in_university"
    },
    5:  {  
        "rule_format": "quantifier_faculty_college",
        "rule_handler": "get_number_of_faculties_in_college"
    },
    6:  {  
        "rule_format": "quantifier_seats_course_college",
        "rule_handler": "get_total_number_of_seats_for_course_at_college"
    },
    7:  {  
        "rule_format": "quantifier_seats_category_course_college",
        "rule_handler": "get_number_of_seats_for_category_for_course_at_college"
    },
    8:  {  
        "rule_format": "quantifier_course_college",
        "rule_handler": "get_number_of_courses_at_college"
    },
    9:  {  
        "rule_format": "quantifier_course_faculty",
        "rule_handler": "get_number_of_courses_in_faculty"
    },
    10:  {  
        "rule_format": "quantifier_course_department",
        "rule_handler": "get_number_of_courses_in_department"
    },
    11:  {  
        "rule_format": "quantifier_course_department_college",
        "rule_handler": "get_number_of_courses_in_department_at_college"
    },
    12:  {  
        "rule_format": "quantifier_department_college",
        "rule_handler": "get_number_of_department_at_college"
    },
    13:  {  
        "rule_format": "quantifier_department_faculty_college",
        "rule_handler": "get_number_of_department_under_faculty_at_college"
    },
    14:  {  
        "rule_format": "quantifier_department_faculty",
        "rule_handler": "get_number_of_department_under_faculty"
    },
    15:  {  
        "rule_format": "quantifier_college_course",
        "rule_handler": "get_number_of_colleges_offering_course"
    },
    16:  {  
        "rule_format": "show_list_faculty_college",
        "rule_handler": "get_list_of_faculties_in_college"
    },

    17: {
        "rule_format": "show_list_college",
        "rule_handler": "get_list_of_colleges_in_university"
    
    },
    18: {
        "rule_format": "show_list_faculty",
        "rule_handler": "get_list_of_faculties_in_university"
    },
    19: {
        "rule_format": "show_list_department",
        "rule_handler": "get_list_of_departments_in_university"
    },
    20:  {  
        "rule_format": "show_list_course",
        "rule_handler": "get_list_of_courses_in_university"
    },
    21:  {  
        "rule_format": "show_list_course_college",
        "rule_handler": "get_list_of_courses_at_college"
    },
    22:  {  
        "rule_format": "show_list_course_faculty",
        "rule_handler": "get_list_of_courses_in_faculty"
    },
    23:  {  
        "rule_format": "show_list_course_department",
        "rule_handler": "get_list_of_courses_in_department"
    },
    24:  {  
        "rule_format": "show_list_course_department_college",
        "rule_handler": "get_list_of_courses_in_department_at_college"
    },
    25:  {  
        "rule_format": "show_list_department_college",
        "rule_handler": "get_list_of_department_at_college"
    },
    26:  {  
        "rule_format": "show_list_department_faculty_college",
        "rule_handler": "get_list_of_department_under_faculty_at_college"
    },
    27:  {  
        "rule_format": "show_list_department_faculty",
        "rule_handler": "get_list_of_department_under_faculty"
    },
    28:  {  
        "rule_format": "show_list_college_course",
        "rule_handler": "get_list_of_colleges_offering_course"
    },
    29:  {  
        "rule_format": "show_deatails_cutoff_category_course_college",
        "rule_handler": "get_cutoff_for_category_for_course_college"
    },
    30:  {  
        "rule_format": "show_deatails_cutoff_course_college",
        "rule_handler": "get_cutoff_for_course_for_college"
    },
    31:  {  
        "rule_format": "show_deatails_cuorsefee_category_course_college",
        "rule_handler": "get_coursefee_for_category_for_course_college"
    },
    32:  {  
        "rule_format": "show_deatails_eligibility_course",
        "rule_handler": "get_details_for_eligibility_of_course"
    },
    33:  {  
        "rule_format": "show_deatails_duration_course",
        "rule_handler": "get_details_for_duration_of_course"
    },
    34:  {  
        "rule_format": "show_deatails_syllabus_course",
        "rule_handler": "get_details_for_syllabus_of_course"
    },



}