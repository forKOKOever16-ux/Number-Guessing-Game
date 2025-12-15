
user_input = input("Enter the roman numerals you want to convert:")

def roman_to_int(numeral):
    final_answer = 0

    if "CM" in numeral:
        final_answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_answer += 4
        numeral = numeral.replace("IV", "")

    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1

    print("The roman numerals you entered translates to: " + str(final_answer) + "!")


def int_to_roman(num):
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    roman = ""

    for value, symbol in values:
        while num >= value:
            roman += symbol
            num -= value

    print("The integer you entered translates to:", roman, "!")
    return roman
# --- هنا عشان يشوف : هل المستخدم كتب رقم ولا روماني؟ ---

if user_input.isdigit():  # إذا كانت المدخلات كلها أرقام → روح للدالة int_to_roman
    int_to_roman(int(user_input))
else:
    roman_to_int(user_input.upper())
