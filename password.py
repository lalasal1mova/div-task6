
def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("en azi 8 simvol olmalidir")

    upper = False
    lower = False
    digit = False

    for i in password:
        if i.isupper():
            upper = True

        if i.islower():
            lower = True

        if i.isdigit():
            digit = True

    if upper == False:
        errors.append("en azi 1 boyuk herf olmalidir")

    if lower == False:
        errors.append("en azi 1 kicik herf olmalidir")

    if digit == False:
        errors.append("en azi 1 reqem olmalidir")

    if " " in password:
        errors.append("bosluq olmamalidir")

    return errors


attempt = 3

while attempt != 0:
    password = input("Sifre daxil edin: ")

    errors = check_password(password)

    if len(errors) == 0:
        print("Sifre qebul olundu :)")
        break

    else:
        for i in errors:
            print(i)

        attempt -= 1

if attempt == 0:
    print("Cehdler bitdi :(")
