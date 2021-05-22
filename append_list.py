import time
def append_list(check_name):
    print(f"***** Student Information Update - {check_name} *****")
    a=a=time.asctime(time.localtime(time.time())) 
    with open(f"{check_name}.txt",'a') as write:
        write.write(f"\nDatabase Updated at {a}\n")
    while True:
        title=input("Name the field you want to update: ")
        info = input("Add info: ")
        with open(f"{check_name}.txt",'a') as write:
            write.write(f"{title} ---> {info}\n")
        check = input("""Do you want to continue
    Press Y to continue updating.
    Press any other key to exit """)
        if check.lower() =='y':
            continue
        else:
            break
