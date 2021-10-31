import json


def password(x):
    if ('a' in x  or 'b' in x  or 'c' in x or 'd' in x or 'e' in x or 'f' in x or 'g' in x or 'h' in x or 'i' in x or 'j' in x or 'k' in x or 'l' in x or 'm' in x or 'n' in x or 'o' in x or 'p' in x or 'q' in x or 'r' in x or 's' in x or 't' in x or 'u' in x or 'v' in x or 'w' in x or 'x' in x or 'y' in x or 'z' in x ) and ('A' in x or 'B' in x or 'C' in x or 'D' in x or 'E' in x or 'F' in x or 'G' in x or 'H' in x or 'I' in x or 'J' in x or 'K' in x or 'L' in x or 'M' in x or 'N' in x or 'O ' in x or 'P' in x or 'Q' in x or 'R' in x or 'S' in x or 'T' in x  or 'U' in x or 'V' in x or 'W' in x or 'X' in x or 'Y' in x or 'Z'in x) and ('0'  in x or '1' in x or '2' in x or '3'in x or '4' in x or '5' in x or  '6' in x or '7' in x or '8' in x or '9' in x) and ('@'in x or '#'in x or '$'in x):
        return True
    else:
        return False
    
def read_json(filename,u_n):
    f=open(filename,"r")
    data=json.load(f)
    val=data["users"]
    for v in val:
        if u_n==v["name"]:
            return False
    return data
def write_json(filename,data):
    f=open(filename,"w")
    json.dumps(data)
    json.dump(data,f)

    
def user_exit(filename,u_n,p_w):
    f=open(filename,"r")
    data=json.load(f)
    val=data["users"]
    for v in val:
        if v["name"]==u_n and v["password"]==p_w:
            return True
def print_fun(d1):
    for i,j in d1.items():
        if i=="name":
            print(i,":",j)
        if i=="profile":
            v1=d1[i]
            for p,q in v1.items():
                print(p,":",q)

def l_s():
    user=input("do u want to do login/signup?:")
    if user=="signup":
        user_name=input("enter the user name:")
        x=input("enter your pass1:")
        p_w=password(x) 
        if p_w==True:
            re_type=input("enter your pass2:")
            if x==re_type:
                d1={"name":user_name,"password":re_type}
                d_r=read_json("usersdata.json",user_name)
                if d_r!=False:
                    d_r["users"].append(d1)
                    print("successfully signup")
                    d_w=write_json("usersdata.json",d_r)
                    des=input("enter ur description")
                    dob=input("enter ur dob:")
                    hob=input("enter ur hobbies:")
                    gender=input("enter ur gender:")
                    d={"description":des,"dob":dob,"hobbies":hob,"gender":gender}
                    d1.update({"profile":d})
                    d_w=write_json("usersdata.json",d_r)
                    print_fun(d1)
                else:
                    print("this user_name is alredy exists")

        else:
            print("plz enter strong password")
    elif user=="login":
        user_name=input("enter the user name:")
        paswrd=input("enter your pass:") 
        l_g=user_exit("usersdata.json",user_name,paswrd)
        if l_g==True:
            print(user_name,"loggedin sucessfully")
        else:
             print("Invalid username and password \n please signup first")

l_s()