from settings import weekDayThatMonthStartsOn

daysTool = {(str(i) if i > 9 else f"0{str(i)}"): [] for i in range(31)}
sortedCalendarDates = [[(str(week+day) if week+day > 9 else f"0{str(week+day)}") for day in range(1, 8)] for week in range(weekDayThatMonthStartsOn, 28+weekDayThatMonthStartsOn, 7)]

print(f"{sortedCalendarDates = }")
print(f"{daysTool = }")