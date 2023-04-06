'''
This program is based on various bank services that are provided online
It asks user to enter their details and what they want to do in their account(withdraw or deposite money).
It also prints the modified balace after completing the process which user asked for. 
Additionally, it provides an option to calculate compound interest on user's investment.   
'''
def data():#definig the first function which will be called at last 
#printing a welcome message for the user     
    print("===================================================")
    print("          # WELCOME TO MYBANK # ")
    print("===================================================")
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #declaring a string which contains all alphabets
    ch = input(" Press Any alphabet And Enter To Continue....")#asking user for to input any alphabet to check it's a human
    if(ch in alphabet):#comparing ch to stings to check if it is a alphabet
        getdata()#if condition is true then function getdata() will be called
    else:#else showing an error 
        print("Error you pressed the wrong key please refresh the page and start again")           
def getdata():#defining new function getdata() 
    user = input(" Enter 'A' to log in as an Administrator or 'S' to log in as a Staff :")#asking user to select how they want to log in
    if(user=='A'):#if user enters 'A' then calling new function get_admin()
        get_admin()
    if(user=='S'):#if user enters 'S' then calling new function get_staff()
        get_staff()
def get_admin():
    print("===================================================")
    print("          # WELCOME AS AN ADMINISTRATOR # ")
    print("===================================================")
    a_ac_num = 98765409 #account number for the user
    a_name = input("Enter The Name Of Administrator               :") #asking user for name
    a_email = input("Enter The Email Address Of Administrator     :") #asking user for email
#printing every information 
    print("======================================================================================================================")
    print("Name                   :",a_name)
    print("Account Number         :",a_ac_num)
    print("Email Address          :",a_email)
    print("======================================================================================================================")
    set()#calling set
def get_staff():
    print("=====================================")
    print("     # WELCOME AS A STAFF # ")
    print("=====================================")
    s_ac_num = 43567890#account number for the user
    s_name = input("Enter The Name Of Staff               :") #asking user for name
    s_email = input("Enter The Email Address Of Staff     :") #asking user for email
#printing every information    
    print("======================================================================================================================")
    print("Name                   :",s_name)
    print("Account Number         :",s_ac_num)
    print("Email Address          :",s_email)
    print("======================================================================================================================")
    set()#calling set()    
def set(): #defining set() function      
    print("======================================================================================================================")
    print("Enter 1 to Deposite the money in your account    :")#telling user to input 1 to deposite money
    print("Enter 2 to Withdraw the money from your account  :")#telling user to input 2 to withdraw money
    print("Enter 3 to Count compound interest on your investment  :")#telling user to input 3 to go to the compound intreset calculator
    number = input("")#asking user to enter a number according to thier chioce of service 
    print("======================================================================================================================")
    if(number=='1'):#if user enters 1 then calling deposite() function
        deposite()
    elif(number=='2'):#if user enters 2 then calling withdraw() function
        withdraw()
    elif(number=='3'):#if user enters 3 then calling investment() function
        investment()
    else: #else showing a error message and redirecting to set()
        print("Sorry!!! Wrong number!!Please try again")
        set()        
def deposite():#defining deposite()
    bb = 200000 #declaring bank balance variable
    d_amount = int(input("Enter the amount that you want to Deposite    :")) #asking user for the amount which they want to deposite
    print("======================================================================================================================")
    print("Your current balance is   :",bb,'dollars') #showing user thier current balance
    print("======================================================================================================================")
    add = bb + d_amount #adding the deposite amount to current balance
    print("      Congrats your amount has been deposited successfully....") #printng a completion message
    print("      Your current balance is       :",add,'dollars') #printing the current balance atfer deposite is done
    print("======================================================================================================================")
    print("Thank you!!") 
def withdraw():#defining withdraw()
    w_amount = int(input("Enter the amount that you want to Withdraw    :")) #asking user for the amount which they want to withdraw
    bb = 200000
    print("======================================================================================================================")
    print("Your current balance is   :",bb,'dollars')#showing user thier current balance
    print("======================================================================================================================")
    sub = bb - w_amount #removing the amount which is to be withdrawn 
    if(sub < bb): #checking if there is sufficient balance to withdraw the given amount
        cando = True
    else:
        cando = False
    if(cando): #if there is sufficient balance to withdraw the given amount then moving forward
        print("      Congrats your amount has been withdrawn successfully....") #printng a completion message
        print("      Your current balance is       :",sub,'dollars') #printing the current balance atfer withdrawal is done
        print("======================================================================================================================")    
        print("Thank you!!") 
    else: #else showing insufficient balance
        print("Insufficient balace!!!!")     
def investment():#defining investment()
    print("======================================================================================================================")
    i_amount= int(input("Enter the investment amount                        :"))#asking user how much money they are planning to invest and coverting the input into integer
    time = int(input("for how many years you are going to keep it invested     :")) #asking user how long they want to keep the amount and coverting the input into integer
    rate = float(input("Enter an interest rate                            :")) #asking user about the interest rate on their investment and coverting the input into float 
    print("======================================================================================================================")
    t_amount = i_amount #total amount at start will be same as the invested amount
    for i in range(0,time):#using for loop to find the total amount after given time with interest
        t_amount = t_amount*(1+rate/100)#formula to count total amount with compound interest 
    print("After",time,"years your total compound interest will be",(t_amount-i_amount))#printing total compound interest after the given time
    print("Total amount after",time,"years :",t_amount)#printing the total amount which the user will get at the end 

data()#calling data() function