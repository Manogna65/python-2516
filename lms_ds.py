# LMS sub features - student mangement system
# system information ----> Tuple
system_info=("LMS student portal","v1.0","2025","Edify University")
admin_info=("admin@edify.ai","9100585677","201")
# diaplay information

print("="*50)
print(f"Welcome to {system_info[0]}")
print(f"Welcome to {system_info[3]}")
print("="*50)

# store all students

students={}

# start with option selection
while True:
    print("choose an option from (1-5): ")
    print("1-Add student")
    print("2-Update student")
    print("3-Delete student")
    print("4-List All student")
    print("5-Exit system")

    choice=input("enter your choice: ")

    if choice == "1":
        print("performing operation 1")
        student_id=input("Enter student id: ")
        # student exits
        if student_id in students:
            print("student id is already exist")
        else:
            name=input("enter student name: ").capitalize()
            # store multiple scores
            scores=[]
            while True:
                score_input=input("Enter your score or type Done: ")
                if score_input =="done":
                    break
                if score_input.isdigit():
                    score= int(score_input)
                    if 0<= score <=100:
                        scores.append(score)
                    else:
                        print("score should between 0-100")
                else:
                    print("score should be number only")

            # store multiple skills
            skills= set()
            while True:
                skill_input=input("enter your skill or type done: ")
                if skill_input=="done":
                    break
                skills.add(skill_input.strip().title())
            
            # save students details received 
            students[student_id]={
                "name":name,
                "scores":scores,
                "skills":skills
            }
            print("student added sucessfully!")

            # for verification
            print(students)


    elif choice== "2":
        print("performing operation 2")
        student_id=input("enter student id to modify: ")
        if student_id in students:
            new_name=input("Enter new name to update: ").title()
            students[student_id]["name"]=new_name
            print("student updated succesfully")
        else:
            print("student id does not exit......!")
        print(students)


    elif choice == "3":
        print("performing operation 3")
        student_id=input("enter student id to delete: ")
        removed=students.pop(student_id,None)
        if removed:
            print("student successfully removed")
        else:
            print("student id doesn't exist!")
        print(students)


    elif choice== "4":
        print("performing operation 4")
        # id - student id
        # skills 
        # scores
        # students
        if not students:
            print("no students avalabale")
        else:
            print("="*50)
            print("student details")
            print("="*50)

            for sid, data in students.items():
                name= data["name"]
                scores= data["scores"]

                if scores:
                    avg = sum(scores)/len(scores)
                else:
                    avg=0

                if scores:
                    top_score = max(scores)
                else:
                    top_score=0
               
                skills =data["skills"]
                print(f"ID: {sid}")
                print(f"name: {name}")
                print(f"scores: {scores}")
                print(f"average score: {avg}")
                print(f"top score: {top_score}")
                print(f"skills: {skills}")
                print(f"skills count: {len(skills)}")

                


    elif choice == "5":
        print("performing operation 5")
        print("="*50)
        print("contact admin for further queries")
        print(f"admin contact: {admin_info[1]}")
        print(f"admin email: {admin_info[0]}")
        print("="*50)
        break
    else:
        print("invalid option,option avalabale from (1-5)")       

