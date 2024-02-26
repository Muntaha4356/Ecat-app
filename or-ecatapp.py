# from login_id import login_ids
# import os
# main_fil_path = os.path.abspath("or-ecatapp.py")
# login_id_file_path = os.path.abspath("login_id.py")
# main_directory = os.path.dirname(main_fil_path)
# login_id_directory = os.path.dirname(login_id_file_path)
# if main_directory == login_id_directory:
     
#      print("both in same")
# else:
#      print("diff")
Name= input("Name:")
Roll_no= input("Roll number= ")
login_ids = [123, 456, 789, 345, 678, 147]
def check(login_user):
    return login_user in login_ids
    

while True : # it'll repeat until the id entered is correct.

     login= int(input("Login_in id: "))
     if check(login):
          print("Correct Log_in id... Proceed with the test")
          break
     else: 
          print("Invalid... please reenter")

print(f"Name: {Name}")  
print(f"Roll no. : {Roll_no}") 
# questions_Maths=  [["What is the value of pi (π) to two decimal places?"],
# ["A. 3.12" ,\
# "B. 3.14", \
# "C. 3.16"] ]

print("Get Ready for the test")

marks = []
i = 0
wrong = 0
correct = 0
while i<10:

   print("CHEMISTRY PORTION")



   print("Which of the following is NOT a noble gas?")
   option= ["A. Helium","B. Argon","C. Nitrogen", "D.skip", "E. Submit"]
   print(option)
   choice= input("choice").upper
   i+=1

   if choice == 'C':
     marks.append(4)
     correct += 1
     print("2nd Question" )
   elif choice == "D":
     continue
   elif choice == "E":
     break

   else:
     wrong+=1
     print("2nd Question")
   print  ("Which of the following is a non-metal?")
   option= ["A. Sodium", \
           "B. Iron", \
           "C. Carbon", "D. Skip", "E.submit"]
   i+=1
   print(option) 
   choice = input("choice") .upper()
   if choice == 'C':
     marks.append(4)
     correct += 1
     print("3rd Question" )
   elif choice == "D":
      continue
   elif choice == "E":
     break
   else:
     wrong +=1
     print("3rd Question")  
   print("Which of the following is a halogen?")
   option =["A. Fluorine",\
            "B. Hydrogen", \
             "C. Oxygen", "D. Skip", "E. Submit "]
   print(option) 
   choice = input("choice") 
   i+=1
   if choice == 'A':
     marks.append(4)
     correct += 1
     print("4th Question" )
   elif choice == "D":
      continue
   elif choice == "E":
     break
   else:
     wrong += 1
     print("4th Question") 
   print("Maths Portion:")  
   print("What is the value of pi (π) to two decimal places?")
   option = ["A. 3.12", \
         "B. 3.14", \
        "C. 3.16", "D.Skip", "E.Submit"] 
   print(option) 
   choice = input("choice") .upper()
   i+=1
   if choice == 'B':
     marks.append(4)
     correct += 1
     print("5th Question" )
   elif choice == "D":
      continue
   elif choice == "E":
     break
  
   else:
     wrong +=1
     print("5th Question") 
   print("What is the square root of 49?")
   option= ["A. 6", \
        "B. 7", \
       "C. 8", "D. Skip", "E. Submit"]  
   print(option) 
   choice = input("choice") .upper()
   i+=1
   if choice == 'B':
     marks.append(4)
     correct += 1
     print("6th Question" )
   elif   choice == "D":
     continue
   elif choice == "E":
     break
   else:
     wrong +=1
     print("6th Question") 
   print("What is the value of 5 squared?")
   option = ["A. 10", \
             "B. 20" \
           "C. 25", "D. Skip", "E. Submit"]
   print(option) 
   choice = input("choice") .upper()
   i+=1
   if choice == 'C':
     marks.append(4)
     correct += 1
     print("7th Question" )
   elif choice == "D":
     continue
   elif choice == "E":
     break   
   else:
     wrong +=1
     print("7th Question") 
   print("PHYSICS PORTION")
   print("Which of the following is NOT a vector quantity?")
   option = ["A. Force", \
          "B. Velocity", \
           "C. Temperature"]
   print(option) 
   choice = input("choice") .upper()
   i+=1
   if choice == 'C':
     marks.append(4)
     correct += 1
     print("8th Question" )
   elif  choice == "D":
     continue
   elif choice == "E":
     break  
   else:
     wrong +=1
     print("8th Question") 
   print("Which of the following is a unit of energy?")
   option =["A. Newton", \
              "B. Joule", 
          "C. Watt"]
   print(option) 
   choice = input("choice") .upper()
   i+=1
   if choice == 'B':
     marks.append(4)
     correct += 1
     print("9th Question" )
   elif choice == "D":
     continue
   elif choice == "E":
     break

   else:
     wrong +=1
     print("9th Question") 
   print("Which of the following is a scalar quantity?")
   option = ["A. Acceleration", \
              "B. Displacement", \
           "C. Force", "D. Skip"]
   print(option) 
   choice = input("choice") .upper()
   i+=1
   if choice == 'B':
     marks.append(4)
     correct += 1
     print("10th Question" )
   elif choice == "D":
     continue
   elif choice == "E":
     break

   else:
     wrong += 1
     print("10th Question") 
   print("English Portion")
   print("Which of the following is NOT a verb?")
   option = ["A. Run ",\
               "B. Jump ", \
          "C. Blue"]
   print(option) 
   choice = input("choice") .upper()
   i+=1
   if choice == 'C':
     marks.append(4)
     correct += 1
     print("Questions End ... You Completed your test")
   elif choice == "D":
     continue
   elif choice == "E":
     break
     
   else:
     wrong += 1
     print("Questions End... You completed your test")   

marks = sum(marks)     
print(f"The total marks are {marks- wrong}")   
print(f"Wrong answers are {wrong}") 
print(f"Attempted Question are {correct}")   
     

