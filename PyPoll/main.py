#import dependencies
import os
import csv
#save the file locatiuon to be read in
#I could not use a relative path because windows is dumb
#YOU WILL NEED TO CHANGE THIS CODE IN ORDER TO RUN ON A DIFFERENT COMPUTER
csvpath = "PyPoll/resources/election_data.csv"

#set open lists for manipulating data
ballot_ID = []
county = []
candidate = []


# Read in the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    pypoll = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(pypoll)

    for row in pypoll:
        ballot_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#save the number of votes cast into a new variabe
number_of_votes = len(ballot_ID)

#Counting Votes using a loop
Charles_votes = 0
for i in candidate:
    if i == "Charles Casper Stockham":
        Charles_votes += 1


        
#counting votes using the count function
Diana_votes = candidate.count('Diana DeGette')

Raymon_votes = candidate.count('Raymon Anthony Doane')


#create a function for calculating the percentage of the votes
def percentage(candidate_votes):
  x = (candidate_votes/number_of_votes)*100
  return x

#apply function to get percentages
Charles_percent = percentage(Charles_votes)
Diana_percent = percentage(Diana_votes)
Raymon_percent = percentage(Raymon_votes)

#Just for fun, an if statement for returning the winner
if Charles_votes > Diana_votes and Charles_votes > Raymon_votes:
    winner = 'Winner: Charles Casper Stockham'
elif Diana_votes > Charles_votes and Diana_votes > Raymon_votes:
    winner ='Winner: Diana DeGette'
elif Raymon_votes > Charles_votes and Raymon_votes > Diana_votes:
    winner ='Winner: Raymon Anthony Doane'

#Print a pretty outpuit to the terminal
print(f"Election Results\n-----------------------------\nTotal Votes: {number_of_votes} \n-----------------------------\nCharles Casper Stockham: {round(Charles_percent,3)}% ({Charles_votes}) \nDiana DeGette: {round(Diana_percent,3)}% ({Diana_votes}) \nRaymon Anthony Doane: {round(Raymon_percent,3)} ({Raymon_votes}) \n-------------------------\n{winner}\n-------------------------")


#Write the pretty output to a text file
output_path = r'C:\Users\EmGre\OneDrive\Desktop\Class Repositories\python-challenge\PyPoll\analysis\pypoll_analysis.txt'
with open(output_path, "w") as txtfile:
    txtfile.writelines(f"Election Results\n-----------------------------\nTotal Votes: {number_of_votes} \n-----------------------------\nCharles Casper Stockham: {round(Charles_percent,3)}% ({Charles_votes}) \nDiana DeGette: {round(Diana_percent,3)}% ({Diana_votes}) \nRaymon Anthony Doane: {round(Raymon_percent,3)} ({Raymon_votes}) \n-------------------------\n{winner}\n-------------------------")












