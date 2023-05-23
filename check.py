import re

password = "qwerty1234"

if (len(password)<8):
    print("short password, must more 8 xters")

elif not re.search("[a-z]", password):
    print("INVALID PASSWORD, no small letter")

elif not re.search("[A-Z]", password):
    print("INVALID PASSWORD, no capital letter")

elif not re.search("[0-9]", password):
    print("INVALID PASSWORD, no numbers")

elif not re.search("[_@$]", password):
    print("INVALID PASSWORD, no symbol")

else:
    print("VALID PASSWORD")