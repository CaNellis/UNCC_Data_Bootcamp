#PyPoll Activity

# import os and csv module
import os
import csv

# set path for file
csvPath = os.path.join("election_data.csv") 
# open and read csv file - - from activity 3:2:5 BasicRead and 3:2:8 Netflix
with open(csvPath) as file:
    csvReader = csv.reader(file)
    #print(csvReader)
    #csvHeader = next(csvReader)
    #print(csvHeader)
    #for row in csvReader:
        #print(row)
   
    # skip the header row in file - - from activity 3:3:1 Cereal Cleaner
    next(csvReader)
    
    # create lists - - - from activity: 3:3:11 UdemyZip
    votersID = []
    votersCounty = []
    votersCandidate = []
    uniqueCandidates = []

    # loop through each row
    for row in csvReader:
        # Calculate total number of votes cast
        # add all column 1 values to votersID list 
        votersID.append(float(row[0]))
        # add all column 2 values to votersCounty list 
        votersCounty.append(row[1])
        # add all column 3 values to votersCandidate list
        votersCandidate.append(row[2])
        # add only unique candidates to uniqueCandidates list
        if row[2] not in uniqueCandidates:
           uniqueCandidates.append(row[2])

    # create variable to calculate number of total votes to reference in later output
    # be sure you are outside of the loop..
    totalVotes = len(votersID)

    # check length of unique candidates to know how many to reference in output
    # be sure to keep print function outside of loop.. 
    #print(len((uniqueCandidates)))
    # Now, use that number to define candidate variables to reference in later output
    candidateOne = uniqueCandidates[0]
    candidateTwo = uniqueCandidates[1]
    candidateThree = uniqueCandidates[2]
    candidateFour = uniqueCandidates[3]

    # find total and percentage of votes each candidate won
    # create variables for each candidate and set their initial total as zero
    totalCandidateOne = 0
    totalCandidateTwo = 0
    totalCandidateThree = 0
    totalCandidateFour = 0    
    # create a for loop to go through the list to identify occurrances of each candidate
    for vote in votersCandidate:
        # if a list item is the same as our unique Candidate One, then
        if vote == candidateOne:
            # add to variable for candidate one's total votes to later reference in output
            totalCandidateOne = totalCandidateOne + 1
        # if a list item is the same as our unique Candidate Two, then
        if vote == candidateTwo:
            # add to variable for candidate two's total votes to later reference in output
            totalCandidateTwo = totalCandidateTwo + 1
        # if a list item is the same as our unique Candidate Three, then
        if vote == candidateThree:
            # add to variable for candidate three's total votes to later reference in output
            totalCandidateThree = totalCandidateThree + 1
        # if a list item is the same as our unique Candidate Four, then
        if vote == candidateFour:
            # add to variable for candidate four's total votes to later reference in output
            totalCandidateFour = totalCandidateFour + 1
    # now we can use these totals and the total of all votes to calculate candidates' percentage of votes
    # pay attention to indentation and make sure it is outside of any loops
    # use round function from activity 3:3:11 UdemyZip 
    percentCandidateOne = round((totalCandidateOne / totalVotes) * 100)
    percentCandidateTwo = round((totalCandidateTwo / totalVotes) * 100)
    percentCandidateThree = round((totalCandidateThree / totalVotes) * 100)
    percentCandidateFour = round((totalCandidateFour / totalVotes) * 100)

# to find the candidate with the highest total number of votes,
## This would be more efficient if I could figure out how to use a dictionary 

# create a list with all of the candidates' totals:
allCandidateTotals = [totalCandidateOne, totalCandidateTwo, totalCandidateThree, totalCandidateFour]
# create variable to hold the maximum value
winner = max(allCandidateTotals)
# create variable to hold index of winner
winnerIndex = allCandidateTotals.index(winner)
# create conditional to match the index to the candidate
if winnerIndex == 0:
    winningCandidate = candidateOne
elif winnerIndex == 1:
    winningCandidate = candidateTwo
elif winnerIndex == 2:
    winningCandidate = candidateThree
else:
    winningCandidate = candidateFour

# print poll results in terminal as displayed in example
# use those f-strings - - - defined in activity 3:1:3
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
print(f"{candidateOne}: {percentCandidateOne}%, ({totalCandidateOne})")
print(f"{candidateTwo}: {percentCandidateTwo}% ({totalCandidateTwo})")
print(f"{candidateThree}: {percentCandidateThree}% ({totalCandidateThree})")
print(f"{candidateFour}: {percentCandidateFour}% ({totalCandidateFour})")
print("-------------------------")
print(f"Winner: {winningCandidate}")
print("-------------------------")

# need to export a text file with election results - - look at activity 3:2:11 UdemyZip
# create variable for output
solvedPyPollFile = os.path.join("electionResults.txt")
# create text for results
# help for writing multiple lines in text file: https://www.tutorialspoint.com/How-to-write-multiple-lines-in-text-file-using-Python
line1 = "Election Results"
line2 = "-------------------------"
line3 = f"Total Votes: {totalVotes}"
line4 = "-------------------------"
line5 = f"Total Votes: {totalVotes}"
line6 = "-------------------------"
line7 = f"{candidateOne}: {percentCandidateOne}%, ({totalCandidateOne})"
line8 = f"{candidateTwo}: {percentCandidateTwo}% ({totalCandidateTwo})"
line9 = f"{candidateThree}: {percentCandidateThree}% ({totalCandidateThree})"
line10 = f"{candidateFour}: {percentCandidateFour}% ({totalCandidateFour})"
line11 = "-------------------------"
line12 = f"Winner: {winningCandidate}"
line13 = "-------------------------"
# open output file
with open(solvedPyPollFile, "w") as dataFile:
    dataFile.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13))