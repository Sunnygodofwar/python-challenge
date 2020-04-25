import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

#empty list
#foo bar as first item in the list
votes = []
candidates = []

#read CSV module
with open(election_data_csv, newline='') as csvfile:

    #csv reader
    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)
    csv_header = next(csvreader)


    #append columns in csvreader
    
    for column in csvreader:
        votes.append(column[0])
        candidates.append(column[2])

    #count Total Votes
    Total_Votes = (len(votes))
    
    #assign each candidate to an int value so it counts the total number of candidates in the list
    Khan = int(candidates.count("Khan"))

    Correy = int(candidates.count("Correy"))

    # apostrophe ' because count list will read it as a value if underscored _
    O_Tooley = int(candidates.count("O'Tooley"))

    Li = int(candidates.count("Li"))

    #assign value to each candidate and their percentage to get a vote total times a 100

    Khan_Percent = (Khan/Total_Votes) * 100

    Li_Percent = (Li/Total_Votes) * 100

    O_Tooley_Percent = (O_Tooley/Total_Votes) * 100

    Correy_Percent = (Correy/Total_Votes) * 100

    #use > formula to compare and pick the actual winner with the most votes; if; else if move on to the next winner

    if Khan > Correy > Li > O_Tooley:
        Winner = "Khan"
    
    elif O_Tooley > Khan > Correy > Li:
        Winner = "O_Tooley"
    
    elif Correy > Khan > Li > O_Tooley:
        winner = "Correy"
    
    elif Li > Khan > Correy > O_Tooley:
        Winner = "Li"
    
    

print("Election Results")
print("________________")
print(f"Total Votes: {Total_Votes}")
print(f"Khan: {Khan_Percent}% ({Khan})")
print(f"Correy: {Correy_Percent}% ({Correy})")
print(f"Li: {Li_Percent}% ({Li})")
print(f"O'Tooley: {O_Tooley_Percent}% ({O_Tooley})")
print(f"Winner: {Winner}")

#output to a .txt file

output = open("output.txt", "w")

line1 = "Election Results"

line2 = "----------------"

line3 = str(f"Total Votes: {Total_Votes}")

line4 = "--------------------------------"

line5 = str(f"Khan: {Khan_Percent}% ({Khan})")

line6 = str(f"Correy: {Correy_Percent}% ({Correy})")

line7 = str(f"Li: {Li_Percent}% ({Li})")

line8 = str(f"O'Tooley: {O_Tooley_Percent}% ({O_Tooley})")

line9= str(f"Winner: {Winner}")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}n\{}n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9))











