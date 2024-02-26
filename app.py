
# Name = input("What's the name")
# Code = int(input("Whta's the code"))
# print("Name:"+Name)
# if Code == 456:
#     print("abs")

# else:
#     print("The code ain't right")
# def generate_blanks(num_blanks):
    # return "_" * num_blanks
Name = input("NAME:____")
print("Name:  "+ Name)


Roll_num = input("What's the roll number")
print("Name: "+Name+ "\n Roll no is "+ Roll_num)

def read_login_id(Name_of_file): #To convert the login_id.txt in list (you may create the text file as list as well.. Okay? see diary)
    with open (Name_of_file, "r") as file: #it'll actually go inside that was created by me i.e. login_id.txt
    #"open"    will open the file. and "r" is for read mode. 
    #"as file"    simply means that after reading it'll assign the value to the variable named "file"
        login_ids = [line.strip() for line in file]
     #Look, Muntaha, I created a file named "file" now Line.strip will remove all sort of spaces in it. it's also a creation of list
    return login_ids

def check_login(login_user, login_ids)     : #it's simply to verify that ids by user matches the ids in the file
    return login_user in login_ids
        
    #login_user is provided by the the user and login_ids is the login ids in file(list)


file_name= "login_id.txt"
login_ids = read_login_id(file_name)
while True:
    login= int(input("login id _____") )
    check_login(login, login_ids)
    if check_login(login, login_ids):
        print("Correct login_id proceed with the Test... Wish you best of Luck")
        break
    else :
        print("Wrong login.. Retry")   







    



