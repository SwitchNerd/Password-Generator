import random
flag = False

#lists
lowerchars = "qwertyuiopasdfghjklzxcvbnm"
upperchars = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
specialchars = "!@#$%^?.,&*"
unclassed = "()_+|}[;'/:][{"

def main():

    dec = input("Would you like to looad prefer preferences? (y/n): ")
    if dec == 'y':
        from prefer import lower, upper, num, special, ambigious
        flag = True
        length = int(input("Length of selection?: "))
    else:

        #inputs
        length = int(input("Length of selection?: "))
        
        lower = str(input("Lower case characters included?: "))
        upper = str(input("Upper case characters included?: "))
        num = str(input("Numbers included?: "))
        special = str(input("Special characters included? (!@#$%^?.,&*): "))
        ambigious = str(input("Ambigious characters included? (()_+|}[;'/:][{:): "))

        if lower == 'y': 
            lower = lowerchars
        else:
            lower = ''
        if upper == 'y':
            upper = upperchars
        else:
            upper = ''
        if num == 'y':
            num = numbers
        else: 
            num = ''
        if special == 'y':
            special = specialchars
        else:
            special = ''
        if ambigious == 'y':
            ambigious = unclassed
        else:
            ambigious = ''

        
    s = ''
    password = ''
    s = lower + upper + num + special + ambigious
    for i in range (length):
        password += random.choice(s)

    print('--------------------------------------------')
    print(password)
    print('--------------------------------------------')\
    
    if flag == False:
        option = input('Would you like to save these preferences?: (y/n): ')
        if option == 'y':
            creatnew(lower, upper, num, special, ambigious)
    

def creatnew(l,u,n,s,a):
    with open("prefer.py", "w") as p:
        p.write(f'lower = "{l}" \n')
        p.write(f'upper = "{u}" \n')
        p.write(f'num = "{n}" \n')
        p.write(f'special = "{s}" \n')
        p.write(f'ambigious = "{a}" \n')

main()