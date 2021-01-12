import random
import array

#first fix the length a random number 
length=100
#Give in all the digits and lower and upper case characters from 
#which your password will be made   
digits = ['0','1','2','3','4','5','6','7','8','9']
l_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
u_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
          'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
          'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')']

#Once initializing that now, generate random characters from that
#by using the random Library

rand_digit = random.choice(digits)
rand_l_case = random.choice(l_case)
rand_u_case = random.choice(u_case)
rand_symbols = random.choice(symbols)
#initially add all the randomly generated ones 
temp = rand_digit+rand_l_case+rand_u_case+rand_symbols
#now iterate them in order to get the required length of the password
for a in range(length):
    temp = temp+rand_digit+rand_l_case+rand_u_case+rand_symbols
#in order to avoid printing the same password everytime.
#we have to make use of the shuffle function
#also before utilizing the shuffle you have to convert it into a list
    if len(temp)>12:
        break
    else:
        temp_list=list(temp)
        random.shuffle(temp_list)
#Once the password is formed print it by iterating in the for loop
password=''
for b in temp_list:
    password = password + b

print("Your randomly generated password is {}".format(password))
