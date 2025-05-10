msg = input("Enter message: ")

len_msg = len(msg)

if len(msg) < 3 :
    print("Msg must be atleast 3 char long")
elif len_msg > 50:
    print("Msg can be only a maximum of 50 char long")
else:
    print("Msg looks good!")