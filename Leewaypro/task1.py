guest={};
n=int(input("Enter the number of guests coming to the party :"));
for i in range(n):
    guest_info=[]
    name=input("Enter name:")
    food=input("Enter favorite food:")
    guest_info.append(name)
    guest_info.append(food)
    guest[name]=guest_info

for item,value in guest.items():
    print(item,":",value[1])

