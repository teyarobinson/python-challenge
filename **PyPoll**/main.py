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
    #for row in csvreader:
        #print(row)
    
    for row in csvreader:
        #The total number of votes cast
        totalvoters.append(row[0])

        #A complete list of candidates who received votes
        
        candidates.append(row[2])
        #The percentage of votes each candidate won

        #The total number of votes each candidate won

        #The winner of the election based on popular vote.
    print (totalvoters)
   