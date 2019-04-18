import csv
from tkinter import *
from tkinter import filedialog

set_date = ''

def dateChanger(date):
    global set_date
    dateList = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    new = date.split("-")
    final = new[0] + "/" + dateList[new[1]] + "/" + new[2]
    set_date = new[0] + '-' + dateList[new[1]] + '-' + new [2]
    return final

def convertCSV(file):
    csvData = [['Paddock', 'Cover', 'Date Measured']]
    read = 0
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if read == 0:
                read += 1
                pass
            else:
                tempList = []
                tempList.append(row[1][1:])
                tempList.append(row[2][1:])
                tempList.append(dateChanger(row[7][1:]))
                csvData.append(tempList)

    new_file_name = "Minda Uploads " + set_date + '.csv'

    with open(new_file_name, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in csvData:
            filewriter.writerow(i)


root = Tk()
root.fileName = filedialog.askopenfilename()
convertCSV(root.fileName)
