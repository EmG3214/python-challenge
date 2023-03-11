#Load in dependencies
import os
import csv
#save the file locatiuon to be read in
#YOU WILL NEED TO CHANGE THIS CODE IN ORDER TO RUN ON A DIFFERENT COMPUTER
csvpath = r"C:\Users\EmGre\OneDrive\Desktop\python-challenge\python-challenge\PyBank\Resources\budget_data.csv"

#Define empty lists for placing in dates and profit/losses
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

# save the total of months to a variable
total_months = len(date_list)
#save the total profits and losses to a variable
total_total = sum(profit_loss_list)

#in order to find the avg change, we have to calculate the changes between each month
changes = [profit_loss_list[i+1]-profit_loss_list[i] for i in range(len(profit_loss_list)-1)]
avg_change = sum(changes)/len(changes)
#round it to 2 decimal places for prettiness
avg_change = round(avg_change, 2)

#-------------------------------

## now we have to find where the biggest change was 
# alongside the correct month where the change happened. 

#first we have to correct the length of the changes list because the first
#change should be a 0 for the first month, as there can be no change because it is the first month
# then the second row should be the change from Jan10 to Feb10, and so on.

changes_aligned = [0] + changes

#zip lists to make new dataset and make it an iterateable list
pybank_zip = zip(date_list, profit_loss_list, changes_aligned)
pybank_list = list(pybank_zip)

#for statement for finding the max and min changes, then saving the data
#along with the associated month to a variable for printing out later
for i in range(len(pybank_list)):
     if pybank_list[i][2] == min(changes):  
        biggest_dec = f"{pybank_list[i][0]} ({pybank_list[i][2]})"

     elif pybank_list[i][2] == max(changes):  
        biggest_inc = f"{pybank_list[i][0]} ({pybank_list[i][2]})"


#---------------------------------------------

#print a pretty output to the terminal
print(f"Financial Analysis\n-----------------------------\nTotal Months {total_months} \nTotal: ${total_total} \nAverage Change: ${avg_change}  \nGreatest Increase in Profits: {biggest_inc} \nGreatest Decrease in Profits: {biggest_dec} ")

#This code writes the pretty output to the text file
output_path = r"C:\Users\EmGre\OneDrive\Desktop\python-challenge\python-challenge\PyBank\analysis\pybank_analysis.txt"
with open(output_path, "w") as txtfile:
    txtfile.writelines(f"Financial Analysis\n-----------------------------\nTotal Months {total_months} \nTotal: ${total_total} \nAverage Change: ${avg_change}  \nGreatest Increase in Profits: {biggest_inc} \nGreatest Decrease in Profits: {biggest_dec} ")

