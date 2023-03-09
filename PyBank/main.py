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

