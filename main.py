import random

#lists
lowerchars = "qwertyuiopasdfghjklzxcvbnm"
upperchars = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
specialchars = "!@#$%^?.,&*"
unclassed = "()_+|}[;'/:][{"


#inputs
length = int(input("Length of selection?: "))

print("For each answer with y/n")

lower = str(input("Lower case characters included?: ")).lower
upper = str(input("Upper case characters included?: ")).lower
num = str(input("Numbers included?: ")).lower
special = str(input("Special characters included? (!@#$%^?.,&*): ")).lower
ambigious = str(input("Ambigious characters included? (()_+|}[;'/:][{:): ")).lower

selection = ''

if lower == 'y': 
    selection = lowerchars
if upper == 'y':
    selection = ''.join([selection, upperchars])
if num == 'y':
    selection = ''.join([selection, numbers])
if special == 'y':
    selection = ''.join([selection, specialchars])
if ambigious == 'y':
    selection = ''.join([selection, unclassed])

print(selection)






