def constrct_equaations(House):
    return House
Text1="House construction"
Text2="In a square circle"
print(Text1,"",Text2)
num_len=int(input("Enter the size of length list:"))
Len_List=[]
for i in range(num_len):
    value = int(input(f"Enter value {i + 1}:"))
    Len_List.append(value)

Num=int(input("Enter the size of width list:"))
Width_list=[]
for i in range(Num):
    value=int(input(f"Enter value {i+1}:"))
    Width_list.append(value)
if len(Len_List)!=len(Width_list):
    print("Error the size of both list don't match")
else:
    area_list=[l*w for l,w in zip(Len_List,Width_list)]
    print("The length list size:",Len_List)
    print("The width list size:",Width_list)
    print("Calculated area of each pair for squarecircle:")
    print(area_list)
