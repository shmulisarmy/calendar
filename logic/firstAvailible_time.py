fpm = [
    ("08:00", "09:00"),
    ("09:30", "10:30"),
    ("12:30", "14:00"),
    ("14:30", "16:00"),
    ("16:30", "18:00"),
]

spm = [
    ("08:00", "09:00"),
    ("09:30", "10:30"),
    ("12:30", "14:00"),
    ("14:30", "16:00"),
    ("16:30", "18:00"),
    ("18:30", "20:00"),
]

def minus(a, b):
    return (int(a[0:2]) * 60 + int(a[3:5])) - (int(b[0:2]) * 60 + int(b[3:5]))


combined_schedule = fpm + spm
combined_schedule.sort(key=lambda x: x[0])

looking_for_time = 30

total_slots = len(combined_schedule) - 1
i = 0 
while i < total_slots-1:
    if spm[i][1] > fpm[i + 1][0]:
        spm[i][1] = max(spm[i][1], fpm[i + 1][1])
        spm.pop(i + 1)
        total_slots -= 1
    
    if minus(spm[i + 1][0],  fpm[i][1] ) >= looking_for_time:
        print(fpm[i][1], spm[i + 1][0])

    

    i += 1
