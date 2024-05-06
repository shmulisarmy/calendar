import sqlite3



to_normal_time = lambda time: f"{time // 60:02d}:{time % 60:02d}"


def get_availabilies(user_id, date):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c = conn.cursor()
    c.execute("select startTime, duration from events where user_id = ? and date = ? and startTime >= 0 and duration >= 0 order by startTime", (user_id, date))
    eventTimes = c.fetchall()

    begin_bound = 480
    end_bound = 1200

    avilibilities = []
    curTime = begin_bound
    for event in eventTimes:
        if curTime < event[0]:
            avilibilities.append((to_normal_time(curTime), to_normal_time( event[0])))
        curTime = event[0] + event[1]

    if curTime < end_bound:
        avilibilities.append((to_normal_time(curTime), to_normal_time(end_bound)))

    return avilibilities



def get_availabilies_together(this_user_id, other_user_id, date):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c = conn.cursor()
    c.execute("select startTime, duration from events where user_id in (?, ?) and date = ? and startTime >= 0 and duration >= 0 order by startTime", (this_user_id, other_user_id, date))
    eventTimes = c.fetchall()

    begin_bound = 480
    end_bound = 1200

    avilibilities = []
    curTime = begin_bound
    for event in eventTimes:
        if curTime < event[0]:
            avilibilities.append((to_normal_time(curTime), to_normal_time( event[0])))
        curTime = event[0] + event[1]

    if curTime < end_bound:
        avilibilities.append((to_normal_time(curTime), to_normal_time(end_bound)))

    return avilibilities