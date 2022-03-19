import csv
from debug import *

path = pathGeter("csv")
timeZone = pytz.timezone("Asia/Shanghai")
timeStartList = []
timeEndList = []
lessonList = []


def timeChecker(start, end):
    """
    This function is used to check whether time in the time period.
    Period limit: from 0:01 to 23:00.
    You should use it like this:
        "start" is the start time of period, form is "hh:mm"
        "end" is the end time of period, form is same as start.
        ***IMPORTANT*** Every time should in 24h form.
    """
    timezone = pytz.timezone('Asia/Shanghai')

    start_time = datetime.datetime.strptime(
        str(datetime.datetime.now().date()) + start, '%Y-%m-%d%H:%M')

    end_time = datetime.datetime.strptime(
        str(datetime.datetime.now().date()) + end, '%Y-%m-%d%H:%M')

    now_time = datetime.datetime.now(timezone).replace(tzinfo=None)
    if start_time < now_time < end_time:
        return True


# Read csv data
with open(path + "lessons.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    log("Matched lessons.csv")
    for allLine in reader:
        # Match time start
        if allLine[0] == "timeStart":
            log("Macthed timeStart line")
            for everyTime in allLine[1:]:
                # log(everyTime)
                timeStartList.append(everyTime)

        # Match time end
        if allLine[0] == "timeEnd":
            log("Macthed timeEnd line")
            for everyTime in allLine[1:]:
                # log(everyTime)
                timeEndList.append(everyTime)

        # Match weekday
        if allLine[0] == datetime.datetime.now().strftime("%w"):
            log(f"Matched toady, week {datetime.datetime.now().strftime('%w')}")
            for everyEments in allLine[1:]:
                # log(everyEments)
                lessonList.append(everyEments)

# Match now lesson
def lessons():
    for startTime in timeStartList:
        # index the position of elements
        position = timeStartList.index(startTime)
        # match end time with start time
        endTime = timeEndList[position]
        # match lesson
        lessonAtTime = lessonList[position]
        if timeChecker(startTime,endTime) == True:
            log(f"Time in {startTime} to {endTime}")
            log(f"Matched nowLesson: {lessonAtTime}")
            return lessonAtTime
            break
        else:
            log(f"Time donnot in {startTime} to {endTime}, skip")

if __name__ == "__main__":
    lessons()