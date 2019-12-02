import random

char_set=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
        'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
        'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',
        '!','@','#','$','%','^','&','*','(',')','{','}','[',']','=','+','-',
        '_','/','.',';',':','?','<','>','\'','|','\\']
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
        'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
        'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','{','}','[',']','=','+','-',
         '_','/','.',';',':','?','<','>','\'','|','\\']
pswrd_len=int(input("Enter length of password(atleast 6 and atmost 20): "))
no_of_letters=int(input("No of letters needed in password: "))
no_of_number=int(input("How many numbers needed in password: "))
no_of_symbols=pswrd_len-no_of_number-no_of_letters
password=""
while pswrd_len!=len(password):
    while no_of_letters!=0:
        password=password+random.choice(alphabet)
        no_of_letters-=1
    while no_of_symbols!=0:
        password=password+random.choice(symbols)
        no_of_symbols-=1
    while no_of_number!=0:
        password=password+random.choice(numbers)
        no_of_number-=1
p_list=list(password)
random.shuffle(p_list)
password="".join(p_list)
print("Generated password is: "+password)
