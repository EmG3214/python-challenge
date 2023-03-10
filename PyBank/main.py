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

#in order to find the avg change, we have to calculate the changes between each month
changes = [profit_loss_list[i+1]-profit_loss_list[i] for i in range(len(profit_loss_list)-1)]
avg_change = sum(changes)/len(changes)
avg_change = round(avg_change, 2)

#now we have to find where the biggest change was alongside the date. 
#maybe zip together all the lists we have made to make a new matrices?
#This isa wrong because the dates don't match up correctly
# pybank_3 = zip(date_list, profit_loss_list, changes)
# for data in pybank_3:
#     print(data)

#zip lists to make new dataset and make it a list
pybank_zip = zip(date_list, profit_loss_list)
pybank_list = list(pybank_zip)

for i in range(len(pybank_list)-1):
    if (pybank_list[i+1][1]-pybank_list[i][1]) == min(changes):
        print(pybank_list[i])

print(f"Financial Analysis\n-----------------------------\nTotal Months {len(date_list)} \nTotal: ${sum(profit_loss_list)} \nAverage Change: ${avg_change}  \nGreatest Increase in Profits: \nGreatest Decrease in Profits: ")

#This code writes to the text file
output_path = r"C:\Users\EmGre\OneDrive\Desktop\python-challenge\python-challenge\PyBank\analysis\pybank_analysis.txt"
with open(output_path, "w") as txtfile:
    txtfile.writelines(f"Financial Analysis\n-----------------------------\nTotal Months {len(date_list)} \nTotal: ${sum(profit_loss_list)} \nAverage Change: ${avg_change}  \nGreatest Increase in Profits: \nGreatest Decrease in Profits: ")



