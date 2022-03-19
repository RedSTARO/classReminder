import csv
from debug import *

path = pathGeter("csv")
timeZone = pytz.timezone("Asia/Shanghai")
dutyList = []
people = []
dutyDict = {}

# Read csv data
with open(path + "duty.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    log("Matched duty.csv")
    for allLine in reader:
        # log(allLine)
        # if allLine[0] == "#":
        #     continue
        #     log(f"Find a explanation. Line{allLine[0]}")

        # Match weelday to do
        if allLine[0] == "weekdayToDo":
            log("Macthed weekdayToDo line")
            for everyEments in allLine[1:]:
                dutyList.append(everyEments)

        # Match weekday
        if allLine[0] == datetime.datetime.now().strftime("%w"):
            log(f"Matched toady, week {datetime.datetime.now().strftime('%w')}")
            for everyEments in allLine[1:]:
                people.append(everyEments)

# log(people)
# log(dutyList)

# Match people and dutyList
def duty():
    for weekdayToDo in dutyList:
        # index the position of elements
        position = dutyList.index(weekdayToDo)
        # match dutyList and people
        peopleName = people[position]
        log(f"Matched people and duty:{peopleName} should do {weekdayToDo}")
        # dutyDict.update(people = peopleName, duty = "weekdayToDo")
        dutyDict[weekdayToDo] = peopleName

    log(f"Total duty dict: {dutyDict}")
    return dutyDict


if __name__ == "__main__":
    duty()
