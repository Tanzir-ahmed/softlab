# 'Hello' ... from [S.O.F.T]lab
# Python 3.6.1

# Verify a Mobile Number_ Input From User _ Draft_01
# Check , if it's a mobile number.
# Check, the mobile company in Bangladesh
# If it's a mobile number & company, then get the number of checking Account Balance. 


ask_mobile_number = input('Enter your Mobile number : ')
mob = int(ask_mobile_number)
print()

print('So your Mobile number is : ', mob)

# print(type(ask_mobile_number))
check_number = ask_mobile_number [ : 4]
mob_digit = 11


# Checking Mobile if it is a mobile number or not

if len(ask_mobile_number) == 11:
    print('It is a Mobile Number in Bangladesh.')
else:
    print('It is not a Mobile number in Bangladesh.')


# Checking Mobile Company

if ask_mobile_number[2] == str(1):
    print('You are using Citycell number.')
    print('To check Account Balance , Please Dial : *877 or *811')

elif ask_mobile_number[2] == str(5):
    print('You are using TeleTalk number.')
    print('To check Account Balance , Please Dial : *152#')

elif ask_mobile_number[2] == str(6):
    print('You are using Airtel number.')
    print('To check Account Balance , Please Dial : *121*112#')

elif ask_mobile_number[2] == str(7):
    print('You are using GrameenPhone number.')
    print('To check Account Balance , Please Dial :  *566#')

elif ask_mobile_number[2] == str(8):
    print('You are using Rabi number.')
    print('To check Account Balance and Validity: Type *222# ')

elif ask_mobile_number[2] == str(9):
