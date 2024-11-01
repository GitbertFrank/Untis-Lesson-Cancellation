import webuntis
import datetime

with open("C:/Users/Robert Frank/Desktop/Coding/Python/UntisToCalendar/src/credentials.txt") as creds_file:
    creds = creds_file.readlines()

creds = [line.strip() for line in creds]

s = webuntis.Session(
    server=creds[0],
    username=creds[1],
    password=creds[2],
    school=creds[3],
    useragent=creds[4]
)

s.login()

start_date = datetime.datetime(2024, 11, 1)
end_date = datetime.datetime(2024, 11, 7)

# not usable:
# getTimetable: timetable view for the requested element
# getTeachers: masterdata teachers read for all
# getStudents: masterdata students read for all
# getKlassen: masterdata Klassen read for all
# getClassregEvents: classregevents read for all
# getExams: examinations read for all
# getExamTypes: examtypes read for all
# getTimetableWithAbsences: Student absences
# getClassregCategories: classregister
# getClassregCategoryGroups: classregister
# getClassregEvents: classevent

status_data = s.statusdata()

# Extract the lstypes and codes from the status data
print(status_data)
s.logout()