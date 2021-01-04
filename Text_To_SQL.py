
import datetime

current_professors = []
new_professors = []

def main():
    in1 = input("Enter the batch file name: ")
    in2 = input("Enter the registrar's file name: ")
    try:
        # try to open the files, throw error if needed
        c_list = open(in1, 'r')
        n_list = open(in2, 'r')

    except Exception as e:
        # catch and print error
        print(e)

    else:
        # read the files into arrays
        for row in c_list:
            current_professors.append(row.split())
        for row in n_list:
            new_professors.append(row.split())

    finally:
        # close open files
        if c_list:
            c_list.close()
        if n_list:
            n_list.close()


    # remove the unneeded column if it exists
    for row in range(len(new_professors)):
        if "Jan" not in new_professors[row][2] and "Feb" not in new_professors[row][2] and \
           "Mar" not in new_professors[row][2] and "Apr" not in new_professors[row][2] and \
           "May" not in new_professors[row][2] and "Jun" not in new_professors[row][2] and \
           "Jul" not in new_professors[row][2] and "Aug" not in new_professors[row][2] and \
           "Sep" not in new_professors[row][2] and "Oct" not in new_professors[row][2] and \
           "Nov" not in new_professors[row][2] and "Dec" not in new_professors[row][2]:

            del new_professors[row][3]
            del new_professors[row][2]


    # Alter ID and date fields in current_professors array
    for row in range(len(new_professors)):
        new_professors[row][0] = ID_Alter(new_professors[row][0])
        new_professors[row][2] = date_convert(new_professors[row][2])
        new_professors[row][3] = date_convert(new_professors[row][3])


    # compare professors on new list to the old list
    try:

        r_out = open("returning.txt", 'w')
        n_out = open("new.txt", 'w')

    except Exception as e:
        print(e)

    else:
        for i in range(len(new_professors)):
            found = False
            while found == False:
                for k in range(len(current_professors)):
                    if new_professors[i][0] == current_professors[k][0]: # and \
                       #new_professors[i][3] == current_professors[k][2] and \
                       #new_professors[i][5] == current_professors[k][3]:

                        sql_query = query_create(new_professors[i][0], new_professors[i][1], new_professors[i][2], new_professors[i][2], current_professors[k][16])
                        r_out.write(sql_query)
                        found = True
                        break
                if found == False:
                    n_out.write('{} {} {} {}\n'.format(new_professors[i][0],new_professors[i][1],new_professors[i][2],new_professors[i][3]))
                    break

    finally:
        if r_out:
            r_out.close()
        if n_out:
            n_out.close()


def query_create(id, issue, date1, date2, batch):
    query_statement = ("DELETE FROM BADGELINK WHERE BADGEKEY={} AND ACCLVLID=75\n".format(id))
    query_statement += ("INSERT INTO BADGELINK {}\n".format(date1))

    return query_statement


def date_convert(date):
    # Converts the date from the new list to the format in the database list
    newDate = date.split("-")

    if newDate[1] == "Jan":
        dateIN = datetime.date(int("20" + newDate[2]), int("01"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Feb":
        dateIN = datetime.date(int("20" + newDate[2]), int("02"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Mar":
        dateIN = datetime.date(int("20" + newDate[2]), int("03"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Apr":
        dateIN = datetime.date(int("20" + newDate[2]), int("04"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "May":
        dateIN = datetime.date(int("20" + newDate[2]), int("05"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Jun":
        dateIN = datetime.date(int("20" + newDate[2]), int("06"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Jul":
        dateIN = datetime.date(int("20" + newDate[2]), int("07"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Aug":
        dateIN = datetime.date(int("20" + newDate[2]), int("08"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Sep":
        dateIN = datetime.date(int("20" + newDate[2]), int("09"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Oct":
        dateIN = datetime.date(int("20" + newDate[2]), int("10"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Nov":
        dateIN = datetime.date(int("20" + newDate[2]), int("11"), int(newDate[0]))
        return str(dateIN)
    if newDate[1] == "Dec":
        dateIN = datetime.date(int("20" + newDate[2]), int("12"), int(newDate[0]))
        return str(dateIN)

def ID_Alter(ID):
    newID = ID
    for c in newID:
        if c == "0" or c == "S":
            newID = newID[1:]
        else:
            return newID

main()
