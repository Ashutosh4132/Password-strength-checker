import string

password=input("Enter Your password: ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
whitespace = any([1 if c in string.whitespace else 0 for c in password])

characters = [upper_case, lower_case, special, digits, whitespace]

length=len(password)

score = 0

with open('commonpasswords.txt','r') as f:
    common = f.read().splitlines()

    if password in common:
        print("Very common password. Score = 0/7")
        exit

if length >8:
    score+=1
if length >12:
    score+=1
if length>17:
    score=+1
if length>20:
    score+=1

print(f"password length is : {str(length)}, adding {str(score)} points!")

if sum(characters)>1:
    score+=1
if sum(characters)>2:
    score+=1
if sum(characters)>3:
    score+=1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters)-1)} ponts! ")

if score <4:
    print(f"The password is quite weak! Score {str(score)} / 8")
elif score ==4:
    print(f"The password is moderate! Score {str(score)} / 8")
elif 4<score<6:
    print(f"The password is quite strong! Score {str(score)} / 8")
elif score >=6:
    print(f"The password is Strong! Score {str(score)} / 8")