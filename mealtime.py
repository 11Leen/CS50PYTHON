def main():
    # أضفت مسافة هنا بعد علامة الاستفهام لتجنب تداخل الكلام
    answer = input("What time is it? ")
    time = convert(answer)

    # الشروط يجب أن تكون هكذا بدقة (بدون كلمة time == قبلها)
    if 7.0 <= time <= 8.0:
        print("breakfast time")

    elif 12.0 <= time <= 13.0:
        print("lunch time")

    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    # فصل الساعات والدقائق
    hours, minutes = time.split(":")

    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()
