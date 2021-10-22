import requests
import json


URl=requests.get("https://api.merakilearn.org/courses") 
meraki_URl=URl.json() 
# print(meraki_URl)
with open("tex.json","w")as file_deta :
    file=json.dump(meraki_URl,file_deta,indent=3)


serial_number=1
for i in meraki_URl:
    print(serial_number,i["name"],i["id"])
    serial_number+=1

course_no=int(input("enter the courses"))
print(meraki_URl[course_no-1]["name"])
var1=meraki_URl[course_no-1]["id"]


url_1=requests.get("http://api.merakilearn.org/courses/"+str(var1)+"/exercises")
var=url_1.json()
# # print(url_1)
with open("monika.json","w")as t:
    json.dump(var,t,indent=4)


    serial_number2=1
    list1=[]
    list2=[]
for j in var["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(serial_number2,j["name"])
        print("   ",serial_number2,j["slug"])
        serial_number2+=1
        # print(j)
        new_no=1
        list1.append(j)
        list2.append(j)
        # print(list1,list2)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial_number2,j["name"])
        serial_number2+=1
        new_no=1
        list1.append(j)
        # print(list1)
    for l in var["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print(" ",new_no,j["name"])
            new_no+=1
            list2.append(j)
            # print(list2)
            break
a=input("enter what do you want next or previous/n/p:")
if a=="p":
    serial_number=1
    for i in meraki_URl:
       print(serial_number,i["name"],i["id"])
       serial_number+=1

    course_no=int(input("enter the courses"))
    print(meraki_URl[course_no-1]["name"])
    var1=meraki_URl[course_no-1]["id"]
    url_1=requests.get("http://api.merakilearn.org/courses/"+str(var1)+"/exercises")
    var=url_1.json()
# # print(url_1)
    with open("monika.json","w")as t:
       json.dump(var,t,indent=4)
       serial_number2=1
       list1=[]
       list2=[]
    for j in var["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_number2,j["name"])
            print("   ",serial_number2,j["slug"])
            serial_number2+=1
            # print(j)
            new_no=1
            list1.append(j)
            list2.append(j)
            # print(list1,list2)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(serial_number2,j["name"])
            serial_number2+=1
            new_no=1
            list1.append(j)
            # print(list1)
        for l in var["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print(" ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                # print(list2)
                break        
    with open("monika_prjapt.json","w")as f:
        json.dump(list1,f,indent=4)
    point=int(input("enter the number point:"))

    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[point-1]["name"])
            num=(list1[point-1]["id"])
            var=[]
            vae3=[]
            new_no1=1
            for n in list2:
                if n["parent_exercise_id"]==num:
                    print(" ",new_no1,n["name"])
                    var.append(n["name"])
                    vae3.append(n["content"])
                    new_no1+=1
            child=int(input("enter the parent exercise do u want"))
            new_no2=1
            for s in range(0,len(var)):
                if child==new_no2:
                    print(var [s])
                    print(vae3[s])
                new_no2+=1
# m=input("enter the we wont to next point")
# if m=="n":
#     sirial_no=1
#     for i in m:
#       if n["parent_exercise_id"]==num:
#             print(" ",new_no1,n["name"])
#             var.append(n["name"])
#             vae3.append(n["content"]    


\





