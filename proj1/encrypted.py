my_dict = {"A":"E", "B":"F", "C":"G", "D":"H", "E":"I",
           "F":"J", "G":"K", "H":"L", "I":"M", "J":"N",
           "K":"O", "L":"P", "M":"Q", "N":"R", "O":"S",
           "P":"T", "Q":"U", "R":"V", "S":"W", "T":"X",
           "U":"Y", "V":"Z", "W":"A", "X":"B", "Y":"C",
           "Z":"D", " ":" "}

message = input("Enter message to be encrypted : ").upper()
code = ""
for i in message:
    if i in my_dict:
        code = code + my_dict[i]
    else:
        code = code + i

print(code)