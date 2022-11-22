
keyword_classes = {
 
    # "entities": {"Course"},

    # filled _ slots = keyword classes with values provided by the users e.g college = ARSD
    #  keywords with respect to values are required   = no. of colleges ?
    "entity":{"degree", "faculty", "department", "college", "course", "seats", "category", "eligibility", "duration", "syllabus", "cutoff", "coursefee" },
    
    "quantifier": {"Number"},    
    "show": {"List", "Details"},
    # "details" : {"eligibility", "duration", "syllabus", "cutoff", "coursefee"},

   ## "degree": { "BA", "BSc"},
    # "degreetype": {"Honours", "programme"}, #vocational; diploma
    # all the faculties at DU and all the dept. at facuty of arts are added
    "faculty": { "Faculty of Arts", "Faculty of Applied Social Sciences and Humanities", "Faculty of Commerce and Business Studies", "Faculty of Education", "Faculty of Interdisciplinary and Life Sciences", "Faculty of Law", "Faculty of Management Studies", "Faculty of Mathematical Sciences", "Faculty of Medical Sciences", "Faculty of Music", "Faculty of Open Learning", "Science", "Faculty of Social Sciences", "Faculty of Technology", "Faculty of Affiliated Faculties" },
    "department": { "Department of Arabic","Department of English", "Department of Germanic & Romance Studies", "Department of Hindi", "Department of Library & Information Science", "Department of Linguistics", "Department of Modern Indian Languages and Literary Studies", "Department of Persian", "Department of Philosophy", "Department of Psychology", "Department of Slavonic & Finno-Ugrian Studies", "Department of Sanskrit", "Department of Punjabi", "Department of Urdu", "Department of Buddhist Studies" }, # to be discussed
    "college": {"Acharya Narendra Dev College","Aditi Mahavidyalaya(W)", "Aryabhatta College", "Atma Ram Sanatan Dharma College", "Bhagini Nivedita College", "Bharati College", "Daulat Ram College","Bhaskaracharya College Of Applied Sciences", "College Of Vocational Studies", "Deen Dayal Upadhyaya College"},
   ## "course": {"Economics", "History", "English", "Sanskrit", "Hindi", "Punjabi", "Bengali", "Urdu", "Arabic", "Persian", "French", "German", "Hindi", "Italian", "Spanish" },  # to be discussed ( deprtment / faculty / course name )
    "course": {"B.Sc. (Prog.) Physical Science Electronics", "B.A. (Vs) Management And Marketing Of Insurance", "B.A. (H)Economics", "B.A. (H) Social Work", "B.A. (H) Psychology", "B.Sc. Physical Science With Electronics", "B.Sc. Life Sciences", "B.A. (Vs) Marketing Management And Retail Business", "B.Sc. (H) Mathematics", "B.A. (H) Philosophy", "B.Sc. (Prog.) Physical Science Computer Science", "B.Sc. (Prog.) Applied Physical Science Industrial\r\nChemistry", "B.Sc. (H) Microbiology", "B.Sc. Physical Science With Comp. Science", "B.A. (H) Geography", "B.Sc. Physical Science With Computer", "B.A. (Vs)Material Management", "B.Sc. (H) Polymer Science", "B.A. (H) Hindi Journalism", "B.Sc. (H) Psychology", "B.A. (Vs)Tourismmanagement", "B.A. (H) History", "B.Sc. (H) Instrumentation", "B.A. (Vs) Small And Medium Enterprises", "B.Sc. Physical Science With Chemistry", "B.A. (H) Sanskrit", "B.A. (H) Music", "B.Sc. (H) Food Technology", "B.A. (H) English", "B.Com (Prog.)", "B.Sc. (H) Home Science", "B.Com.", "B.Sc. Physical Science With Computer Science", "B.A. (Vs) Human Resource Management", "B.Sc. (H) Mathematics", "B.A. Prog.", "B.A. (H) Economics", "B.Sc. (H) Chemistry", "B.Com (H)", "B.A. (H) Political Science", "B. Com. (H)", "B.Sc. (H) Biochemistry", "B.Sc. Mathematical Science", "B.Sc.(H) Mathematics", "B.Sc. (H) Computer Science", "B. Com.(H)", "B.A. (H) Pol. Science", "B. A (H) Sociology", "B.Sc. Life Science", "B.Sc. (H) Botany", "B.A. (Prog.) (History + Political Science)", "B.Sc. (H) Physics", "B.A. (Vs) Office Management And Secretarial Practice", "B.Sc.(H) Computer Science", "B.A. (H) Hindi", "B.Sc. (Prog.) Physical Science Chemistry", "B.A. (H) Journalism", "B.Sc. (H) Electronics", "B.A. (Prog.)", "B.Sc. (H) Zoology", "B.Sc. (H) Computer  Science", "B.Com. (P)", "B.Sc. (H) Biomedical Science", "B.Com. (H)", "B. Com."},
    # , ("Applied Psychoogy","Psychology"), "Philosophy", ("Hindi Patrakarita"),
    #{"total", "category wise"},
    "category": {"General", "SC", "ST", "OBC", "Minority", "EWS", "Total Seats"}, 

    
    # "details" : {"eligibility", "duration", "syllabus", "cutoff", "coursefee"},
    # "eligibility":{} ,
    # "duration": {} , 
    # "syllabus": {}, 
    # "cutoff": {}, 
    # "coursefee": {}
 
}
