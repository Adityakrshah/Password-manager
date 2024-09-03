from cryptography.fernet import Fernet


def write_key():
    key= Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
    


def load_key():
    file= open("key.key","rb")
    key=file.read()
    file.close()
    return key

#write_key()
key= load_key()
fer=Fernet(key)

master =input("PLEASE TYPE MASTER PASSWORD:")
if master.lower() != "adi":
    print("Incorrect Password!!")
    quit()
    
def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("||")
            print("user:",user,"passw:",passw)
            fer.decrypt(passw.encode()).decode()
            
def add():
    acc_name=input("Enter Account name:")
    pwd=input("Enter Password:")
    with open('password.txt','a') as f:
        f.write(acc_name + "||" + fer.encrypt(pwd.encode()).decode() + "\n")
    

while True:
    mode=input("Press:\n1) A if you want to Add password.\n2) V if you want to View stored password.\n3) Q if you want to quit:\n").lower()
    if mode=="a":
        add()
    elif mode=="v":
        view()
    elif mode == "q":
        quit()
    else:
        print("Invalid Mode!!")
        continue

