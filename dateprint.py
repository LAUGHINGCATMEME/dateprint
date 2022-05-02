def date_list(year_d, month_d):
    month_days = {
    1: "31",
    2: "28",
    3: "31",
    4: "30",
    5: "31",
    6: "30",
    7: "31",
    8: "31",
    9: "30",
    10: "31",
    11: "30",
    12: "31"
}
    no_of_days = int(month_days[month_d])
    # if February in leap year
    if month_d == 2 and year_d % 4 == 0:
        no_of_days = 29
    
    final_string = ""
    for i in range(no_of_days):
        i += 1
        if len(str(i)) < 2: i = "0" + str(i)
        if len(str(month_d)) < 2: month_d = "0" + str(month_d)
        if len(str(year_d)) < 2:
            year_d = "0" + str(year_d)
        final_string += f"{str(year_d)}{str(month_d)}{str(i)}:\n"
    return final_string

if __name__ == "__main__":
    while 1:
        yearr = int(input ("(last 2 digit) year> "))
        mont = int(input("month> "))
        print(date_list(yearr, mont))
