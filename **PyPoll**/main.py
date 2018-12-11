#dependecies
import os
import csv 

#creating the lists I will need hold the tallies 
totalvoters = []
candidates =[]
percentage = []
winner = []

#connect to the csv file 
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header when reading data
    csv_header = next(csvreader)

    #test to make sure I am connected 
    for row in csvreader:
        print(row)
