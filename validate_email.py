import re

def validate_email(email):
    regex = "^[a-zA-Z]+([1-9]+)?@[a-zA-Z]+\\.[a-zA-Z]+$"
    if re.search(regex, email):
        print(email)

number_of_inputs = int(input())

email_list = []
for i in range(0, number_of_inputs):
    email_list.append(input())


for i in email_list:
    validate_email(i)
    

