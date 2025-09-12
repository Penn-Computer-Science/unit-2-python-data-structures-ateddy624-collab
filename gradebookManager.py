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
        print(person+"'s average grade is "+str(person_avg)+"%")
    except KeyError:
        print("Invalid student. Please try again")
def
#print_grades(input("Select a student to view their grades "))
#calc_avg_grade(input("Select a student to view their average grade "))