import bcrypt
from collections import defaultdict

from settings import weekDayThatMonthStartsOn

daysTool = {(str(i) if i > 9 else f"0{str(i)}"): [] for i in range(31)}
sortedCalendarDates = [[(str(week+day) if week+day > 9 else f"0{str(week+day)}") for day in range(1, 8)] for week in range(weekDayThatMonthStartsOn, 28+weekDayThatMonthStartsOn, 7)]


generateSalt = lambda: bcrypt.gensalt().decode('utf-8')

def hash(password: str, salt: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def inifiniteDict() -> defaultdict:
    return defaultdict(inifiniteDict)


tree = inifiniteDict()
def treeInsert(word):
    node = tree
    for letter in word:
        node = node[letter]

def commonPassword(word) -> str|False:
    execused = False
    node = tree
    for letter in word:
        if letter not in node:
            if execused:
                return False
            execused = True
        node = node[letter]
    if execused:
        return "this password is very similar to a common password"
    return "this password is common"