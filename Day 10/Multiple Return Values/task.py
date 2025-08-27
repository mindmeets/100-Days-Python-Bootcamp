def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("", ""))

print(format_name("SaTyaRANjan", "sABaT"))

def leap_year(year):
    """Determine if a year is a leap year.
    This is a docstring. This tells about the function"""
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            else:
                return True
print(leap_year(2000))
print(leap_year(2100))


def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False

print(canBuyAlcohol(18.0))
print(canBuyAlcohol(21))
print(canBuyAlcohol(15))


