f main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # ازالة علامة $ وتحويل النص الى رقم عشري
    d_without_dollar = d.replace("$", "")
    return float(d_without_dollar)

def percent_to_float(p):
    #ازالة علامة % وتحويل النص الى رقم وقسمته على 100
    p_without_percent = p.replace("%", "")
    return float(p_without_percent) / 100

main()
