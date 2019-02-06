#PyBank Activity

# import os and csv module
import os
import csv

# set path for file
csvPath = os.path.join("budget_data.csv") 
# open and read csv file - - from activity 3:2:5 BasicRead and 3:2:8 Netflix
with open(csvPath) as file:
    csvReader = csv.reader(file)
    #print(csvReader)
    #csvHeader = next(csvReader)
    #print(csvHeader)
    #for row in csvReader:
    #    print(row)
   
    # skip the header row in file - - from activity 3:3:1 Cereal Cleaner
    next(csvReader)
    
    # list of data - so you can manipulate values with for loops, length of lists, sum of lists, appending lists
    # look at activity: 3:3:11 UdemyZip
    revenue = []
    date = []
    revenueChange = []

    # calculate total nu months(rows) and net profit/loss for entire period
    # loop through each row
    for row in csvReader:
        # add all column 2 values to revenue list -later print sum of all values in list
        revenue.append(float(row[1]))
        # add all column 1 values to date list - later print nu of (length of) dates (list)
        date.append(row[0])
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {len(date)}")
    print(f"Total: ${round(sum(revenue))}")

    # calculate avg change rows, greatest increase in revenue, and greatest decrease in revenue
    # loop through values within range of number of values in revenue list
    for i in range(1,len(revenue)):
        # calculate the difference between curent revenue value and previous revenue value ,then add to revenueChange list. Will result in list of all changes between rows that we can later search for largest and smallest.
        revenueChange.append(revenue[i] - revenue[i-1])
        #calculate the average of all values in revenueChange: avg = sum of values / nu of values - - later will print as rounded number so won't be too long
        avgRevenueChange = sum(revenueChange) / len(revenueChange)
        # define and calculate max and min values 
        maxRevenueChange = max(revenueChange)
        minRevenueChange = min(revenueChange)
        # find the corresponding dates and cast as string
        maxRevenueChangeDate = str(date[revenueChange.index(max(revenueChange)) + 1])
        minRevenueChangeDate = str(date[revenueChange.index(min(revenueChange)) + 1])
    print(f"Average Change: ${round(avgRevenueChange)}")
    print(f"Greatest Increase in Profits: {maxRevenueChangeDate}, (${round(maxRevenueChange)})")
    print(f"Greatest Decrease in Profits: {minRevenueChangeDate}, (${round(minRevenueChange)})")


# need to export a text file with analysis results - - look at activity 3:2:11 UdemyZip
# create variable for output
solvedPyBankFile = os.path.join("analysisResults.txt")
# create text for results
# help for writing multiple lines in text file: https://www.tutorialspoint.com/How-to-write-multiple-lines-in-text-file-using-Python
line1 = "Financial Analysis"
line2 = "-------------------------------"
line3 = f"Total Months: {len(date)}"
line4 = f"Total: ${round(sum(revenue))}"
line5 = f"Average Change: ${round(avgRevenueChange)}"
line6 = f"Greatest Increase in Profits: {maxRevenueChangeDate}, (${round(maxRevenueChange)})"
line7 = f"Greatest Decrease in Profits: {minRevenueChangeDate}, (${round(minRevenueChange)})"
# open output file
with open(solvedPyBankFile, "w") as dataFile:
 # how to write mupltiple lines in a file in python https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python# 
    dataFile.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))