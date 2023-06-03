# It is a python program, a part form the library administration system
# In this program, it focus on update the data on the json file.

import json

#value
Chose = 1
Name = "jsfile.json"
Data = dict()
t = 0

#json data structure:
# {Name:[],Author:[],circumstance:[],}
with open(Name,'r') as op:
        Text = op.read()
        Data = json.loads(Text)
#start the program, use the while to decide keep going or leave
while Chose:
    print("0. leave the loop/program")
    print("1. print the json file")
    print("2. upload the data")
    print("3. create a new data(Detel the original json data file)")
    Chose = int(input("Please input the number of chose, such as '0', '1', '2', '3'"))
#find the json file
    if Chose == 1:
        t = 0
        print(Data)
    
    if Chose == 2:
        pass
    
    if Chose == 3:
        Data['Name'] = input("Please input the book name in a list type such as:'Apple,Boy,Cate'").split(",")
        Data['Author'] = input("Please input the author of the book in a list type such as:'Tom,Ben,lily'").split(",")
        Data['Circumstance'] = input("Please input the circumstance of the book in a list type if it is existence in the library,'1',else '0'.such as:'1,0,1,1'").split(",")
        Data['Comment'] = input("Please input the comment in a list type such as:'good,bad,X'").split(",")
        
        print(Data)
        text = json.dumps(Data)
        with open(Name,'w+') as writed:
            writed.write(text)
        
             
