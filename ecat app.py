login_ids= [1223,4453, 1234, 9876, 4785]
Name= input("Name:")
Roll_no= input("Roll number= ")
import time
login_ids = [123, 456, 789, 345, 678, 147]
def check(login_user):
    return login_user in login_ids

set = True
start = 0
marks= []
wrong= []
attempt= []
skipped= []
    

while set== True : # it'll repeat until the id entered is correct.

     login= int(input("Login_in id: "))
     if check(login):
          print("Correct Log_in id... Proceed with the test")
          set = False
          start= 1
          
          break
     else: 
          print("Invalid... please reenter")
time.sleep(1)          
if start ==1:
   print(f"Name: {Name}")  
   time.sleep(1)
   print(f"Roll no. : {Roll_no}")
   time.sleep(1)
#    for i in questions:
   questions = ((("Which of the following is NOT a noble gas? \n A. Helium","B. Argon","C. Nitrogen"), ("D.skip"), ("E. Submit"), ("C")),(("Which of the following is a non-metal? \n A. Sodium  B. Iron C. Carbon"),("D. Skip"), ("E. Submit"), ("C")), (("Which of the following is a weak acid \n A. HYDROCHORIC ACID, B. Nitric Acid, C.Acetic Acid"),("D. Skip"), ("E.Submit"), ("C")), (("Who is the author of novel TO KILL A MOCKINGBIRD \n  A. Harper lee B. J.K. Rowling C. Ernest Hemingway"), ("D. Submit"),("E. skip"), ("A")), (("solve equation : 3x-7=2? \n A. x= 3, B. x= 1, C. x= 5"), ("D. Skip"), ("E. submit"), ("A")), (("If f(x)= 2x^2-3x+1=0, what are the soltuionfor x? \n A. (x= -1,4) B.(x= -4,-1) C. (x= 1, -4)"), ("D. Skip"), ("E. Submit"), ("C")), (("if f(x)= 2x^2-3x+1...find f(3) \n A. f(3)= 7, B. f(3)= 13, C. f(3)= 11"),("D. Skip"), ("E. skip"),("C") ),(("What is the SI unit of electric charge. A. Volt B. Coloumb. C. Ohm"),("D. Skip"), ("E. Submit"), ("B")), (("What's SI unit of energy. A. Joules. B. Couloumbs C. Watts "), ("D. Submit"), ("E. Submit" ), ("A")))            
   for i in questions:
       for j in i:
         index= questions.index(i)
       print(questions[index][0])
       print(questions[index] [1])
       print(questions [index][2])
       correct = questions[index][3]
       choice = input("Choose the correct option").upper()
       if choice == "D":
           skipped.append(1)
           time.sleep(1)
           continue
       elif choice == "E":
          
        break  
       elif choice == correct:
           marks.append (4)
           attempt.append(1)
           time.sleep(1)
       else:
            wrong.append(1)  
            time.sleep(1)

total_marks = sum(marks)   
attempted= sum(attempt)
deduct= sum(wrong)
skip= sum(skipped)

print(f"total marks are {total_marks - deduct}")   
print(f"attempted question: {attempted}")   
print(f"skipped question : {skip}")    
print(f"wrong questions:{deduct}") 



           
         
       

