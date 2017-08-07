import datetime

start = 20
end = 6

for n in range(0,24):
    now = datetime.datetime.now().replace(hour=n)
    startTime = now.replace(hour=start, minute=0, second=0)
    endTime = now.replace(hour=end, minute=59, second=59)
    
    if startTime.time() > endTime.time():
        endTime += datetime.timedelta(days=1)
    
    print("start = " + str(startTime.day) + "-" + str(startTime.time()))
    print("now = " + str(now.day) + "-" + str(now.time()))
    print("end = " + str(endTime.day) + "-" + str(endTime.time()))
    print("should execute = " + str(now >= startTime and now <= endTime))
    print("---------------")
    now += datetime.timedelta(days=1)
    print("start = " + str(startTime.day) + "-" + str(startTime.time()))
    print("now = " + str(now.day) + "-" + str(now.time()))
    print("end = " + str(endTime.day) + "-" + str(endTime.time()))
    print("should execute = " + str(now >= startTime and now <= endTime))
    print(" ")
    print("===============")