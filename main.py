from add import add
from append_list import append_list
import os
import sys
not_in_list=0
name_in_list = 0
check_name=''
def want_to_add(check_name):
    if not_in_list ==1:
        print("""The name you entered doesn't belong to student in the data base do you want to add student
Do you want to add student information to our database
Press 1 to add
Press 2 to end program""")
        choice = int(input())
        if choice==1:
            with open("main_database.txt", "r+") as m:
                check_in_life = m.readlines()
                check_name_copy=check_name+'\n'
                if check_name_copy not in check_in_life:
                    m.write(check_name+'\n')
                    add(check_name)
        elif choice ==2:
            sys.exit()
        else:
            print("Please enter correct option:")
            want_to_add(check_name)

def list_append(check_name):
    if name_in_list ==1:
        print("""The name you entered belong to student in the data base do you want to add student
Do you want to update student information to our database
Press 1 to update
Press 2 to end program""")
        choice = int(input())
        if choice==1:
            append_list(check_name)
        elif choice ==2:
            sys.exit()
        else:
            print("Please enter correct option:")
            list_append(check_name)


def main():
    global not_in_list
    global name_in_list
    global check_name
    not_in_list=0
    check_name = input("Enter students name:")
    with open("main_database.txt", "r+") as m:
        check_in_life = m.readlines()
        check_name_copy=check_name+'\n'
        if check_name_copy not in check_in_life:
            not_in_list=1
            want_to_add(check_name)
        else:
            name_in_list=1
            list_append(check_name)
main()


while True:
    print("""Do you want to add/update more records: 
Press 1 to go to main menu
Press any other key to end program""")
    choice = input()
    if choice=="1":
        main()
    else:
        sys.exit()