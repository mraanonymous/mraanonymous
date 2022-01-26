#python code for calculator
#Firstly we will define functions for operations
def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

#now we will show user the operation options

print("please select operations -- \n"\
      "1.Addition\n"\
      "2.Subtract\n"\
      "3.Multiply\n"\
      "4.Divide\n")       

#Now we will take input from user 

Select = int(input("Select operations from 1,2,3,4 : "))

number_1 = int(input("Enter first number : "))
number_2 = int(input("Enter second number : "))

#declaring conditions and mathematical operations using functions defined in starting of the code

if Select==1:
   print(number_1,"+",number_2,"=",add(number_1,number_2))

elif Select==2:
    print(number_1,"-",number_2,"=",subtract(number_1, number_2))  

elif Select==3:
    print(number_1,"*",number_2,"=",multiply(number_1, number_2))    

elif Select==4:
    print(number_1,"/",number_2,divide(number_1, number_2))

else:
    print("invalid input")    

#lets run the code!!!
#hence we have successfully made the calculator using python>>>>>