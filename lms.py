#-------- Enhanced LMS Grade Tracker with String Operations----------

print("="*50)
print("Enhanced LMS Grade Tracker with String Operations")
print("="*50)

#valid id
student_id_valid=False
while not student_id_valid:
    student_id=input("Enter your ID: ")
    #check if valid id based on sign -
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Enter positive values only ")
    elif student_id.isdigit():
        student_id=int(student_id)
        if student_id>0:
            student_id_valid=True
        else:
            print("Enter non-zero values")
    else:
        print("Enter only numbers")
print(student_id)

#format id
formatted_id= "STU" + str(student_id).zfill(5)
print(formatted_id)

#valid name
student_name_valid=False
while not student_name_valid:
    student_name=input("Enter Your Name: ")
    #student_name=student_name.strip().capitalize()
    student_name=student_name.strip().title()
    print(student_name)
     #check the name is alphabetic
    name_check=student_name.replace(" ","")
    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid=True
        print("Name: "+ student_name)
    else:
        if not name_check.isalpha():
            print("Name should contain letters only")
        elif len(student_name) <=3:
            print("Name should contain at least 3 charecters")

#EMAIL GENERATION
name_part=student_name.split()
#print(name_part)
first_name=name_part[0].lower()
student_email= first_name +"."+str(student_id) + "@university.edu"
print(student_email)

#discount calculation
base_course_fee_valid=False
while not base_course_fee_valid:
    base_course_fee=input("Enter your course fee: ")
    #check if valid id based on sign -
    if base_course_fee.startswith("-") and base_course_fee[1:].isdigit():
        print("Enter positive values only ")
    elif base_course_fee.isdigit():
        base_course_fee=int(base_course_fee)
        if base_course_fee>0:
            base_course_fee_valid=True
        else:
            print("Enter non-zero values")
    else:
        print("Enter only numbers")
print(base_course_fee)

#calculation of fee
discount=0
print("Enter Discription")
discription=input()

if discription.lower().find("reference") != -1:
    discount+=5000

if "scholarship" in discription:
    discount+=7000

if "promo" in discription:
    discount+=3000

final_fee=base_course_fee-discount
print(f"base course fee{base_course_fee}")
print(f"you got discount{discount}")
print(f"After discount you pay: {final_fee}")
