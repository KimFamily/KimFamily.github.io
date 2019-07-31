#1 /usr/bin/python
import cgi,cgitb
cgitb.enable()
import webbrowser
new = 2

original="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
scrambled="RWgUIa5v2TxsZj7otp3FqKrNEDzhL6B0O4QXHeicMYf1kSdGPubAVC8lnwy9mJ"

def add(user, pw):
    straw=open("users.csv", "a")
    if (available(user)):
        straw.write(encrypt(user) + "," + encrypt(pw) + "\n")
        print("New Account Made.")
        return True
    else:
        print("Username Already Taken.")
        return False
        
        
def available(user):
    straw=open("users.csv", "rU")
    data=straw.read()
    data=data.split('\n')
    data=data[:-1]
    for i in range(len(data)):
        data[i] = data[i].split(",")
    user = encrypt(user)
    for l in data:
        if user == l[0]:
            return False
    return True

def encrypt(text):
    e = ""
    for c in text:
        if (original.find(c) == -1):
            e += c
        else:
            e += scrambled[original.find(c)]
    return e

# def decrypt(text):
#     d = ""
#     for c in text:
#         if (scrambled.find(c) == -1):
#             d += c
#         else:
#             d += original[scrambled.find(c)]
#     return d

def main():
    form=cgi.FieldStorage()
    user = form.getValue("username",'')
    pass1 = form.getValue("password1",'')
    pass2 = form.getValue("password2",'')
    # if pass1 == pass2:
    #     webbrowser.open("https://KimFamily.github.io/signup.html")
    webbrowser.open("https://KimFamily.github.io/signup.html")

main()