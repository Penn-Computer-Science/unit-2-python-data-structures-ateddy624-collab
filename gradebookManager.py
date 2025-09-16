a_grade=(90)
b_grade=(80)
c_grade=(70)
d_grade=(60)
class_dict={"Andrew":[91, 97, 88, 75, 98, 95] ,"Alice":[89, 99, 96, 100, 97, 98] ,"Anthony":[98, 87, 68, 75, 87, 86]}

def print_grades(person):
    try:
        print(person+"'s grades are: "+str(class_dict[person]))
    except KeyError:
        print("Please try again")
def calc_avg_grade(person):
    try:
        person_avg=0
        number=0
        for i in class_dict[person]:
            person_avg+=i
            number+=1
        person_avg=person_avg/number
        person_avg=round(person_avg, 2)
        #print(person+"'s average grade is "+str(person_avg)+"%")
        return person_avg
    except KeyError:
        print("Invalid student. Please try again")
def add_student(person):
    class_dict[person]=[]
def grade_summary():
    print(class_dict)
def high_grade():
    student_avg={"No Students":"No highest grade"}
    high_percent=0
    for i in class_dict:
        #try:
        avg_grade=float(calc_avg_grade(i))
        #except:
        #    avg_grade=0
        if avg_grade>round(float(high_percent),2):
            high_percent=round(float(calc_avg_grade(i)),2)
            
            try:
                student_avg=student_avg.pop()
            except TypeError:
                student_avg[i]=round(float(calc_avg_grade(i)),2)
        #except TypeError:
            #pass
    print(student_avg)

    #high_grade=0
    #who_high_grade=[]
    #for i in class_dict:
    #    high_percent=calc_avg_grade(i)
    #    try:
    #        if high_percent>high_grade:
    #            while True:
    #                try:
    #                    who_high_grade.pop()
    #                except IndexError:
    #                    break
    #            high_grade=high_percent
    #            who_high_grade[0]=i
    #        elif high_percent==high_grade:
    #            num=1
    #            for i in who_high_grade:
    #                num+=1
    #            who_high_grade[num]=i
    #    except TypeError:
    #        high_grade=high_grade[i]
    #    #except TypeError:
    #    #    while True:
    #    #            try:
    #    #                who_high_grade.pop()
    #    #            except IndexError:
    #    #                break
    #    #    high_grade=high_percent
    #    #    who_high_grade.append(i)
    #highest_grade="The student with the highest average score is "+str(who_high_grade)+" with a score of "+str(high_grade)
    #print(highest_grade)

high_grade=high_grade()
#add_student(input("Enter student name: "))
#print_grades(input("Select a student to view their grades "))
#calc_avg_grade(input("Select a student to view their average grade "))


#while True:
