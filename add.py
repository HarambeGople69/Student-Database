import time
def add(check_name):
    print(f"***** Student Information - {check_name} *****")
    a=time.asctime(time.localtime(time.time()))
    phone_num = input("Enter Phone number: ")
    location = input("Enter residence location: ")
    dob = input("Enter Date of Birth: ")
    
    with open(f"{check_name}.txt",'w') as write:
        write.write(f"Database created at {a}\n")
        write.write(f"Phone number ---> {phone_num}\n")
        write.write(f"Location ---> {location}\n")
        write.write(f"Date of Birth ---> {dob}\n")
