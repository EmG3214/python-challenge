#Load in dependencies
import os
import csv
#save the file locatiuon to be read in
#YOU WILL NEED TO CHANGE THIS CODE IN ORDER TO RUN ON A DIFFERENT COMPUTER
csvpath = r"C:\Users\EmGre\OneDrive\Desktop\python-challenge\python-challenge\PyBank\Resources\budget_data.csv"

#Define a list for reading in dates and profit/losses

date_list = []
profit_loss_list = []

# Read in the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #need to append data from the csv file into the empty lists
    for row in csvreader:
        date_list.append(row[0])
        profit_loss_list.append(int(row[1]))

#check to make sure that worked
print(f"Total Months {len(date_list)}")
print(f"Total: ${sum(profit_loss_list)}")

#in order to find the avg change, increases, and decreases, 
#we have to calculate the changes between each month
output_path = r"C:\Users\EmGre\OneDrive\Desktop\python-challenge\python-challenge\PyBank\analysis\pybank_analysis.txt"
with open(output_path, "w") as txtfile:
    txtfile.writelines(f"Total Months {len(date_list)} \nTotal: ${sum(profit_loss_list)} \nAverage Change:  \nGreatest Increase in Profits: \nGreatest Decrease in Profits: ")



