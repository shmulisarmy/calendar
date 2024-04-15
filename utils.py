import bcrypt
from collections import defaultdict

from settings import weekDayThatMonthStartsOn, minDifferenceFromCommonPasswords

daysTool = {(str(i) if i > 9 else f"0{str(i)}"): [] for i in range(31)}
sortedCalendarDates = [[(str(week+day) if week+day > 9 else f"0{str(week+day)}") for day in range(1, 8)] for week in range(weekDayThatMonthStartsOn, 28+weekDayThatMonthStartsOn, 7)]


generateSalt = lambda: bcrypt.gensalt().decode('utf-8')

def hash(password: str, salt: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def inifiniteDict() -> defaultdict:
    return defaultdict(inifiniteDict)

passwordTree = inifiniteDict()
def passwordTreeInsert(word):
    node = passwordTree
    for letter in word:
        node = node[letter]

def commonPassword(word) -> str|bool:
    execused = 0
    node = passwordTree
    for letter in word:
        if letter not in node:
            if execused >= minDifferenceFromCommonPasswords:
                return False
            execused += 1
        else:
            node = node[letter]
    if execused:
        return "this password is very similar to a common password"
    return "this is common password"



with open("commonPasswords.txt") as f:
    for line in f:
        passwordTreeInsert(line.strip())

print(f"{commonPassword('password') = }")
print(f"{commonPassword('passwrd') = }")
print(f"{commonPassword('92365gh2') = }")