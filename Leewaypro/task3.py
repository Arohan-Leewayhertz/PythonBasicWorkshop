string=input("Enter a string :")
def check_string(string):
    for i in range(len(string)):
        flag=0
        if(string[i]=='s'):
            flag=1
    if flag:
        print("The String Contains letter s")
    else:
        print("The String does not contain letter s")

check_string(string)