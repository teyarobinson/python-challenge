#dependicies 
import os
import csv

#define list 
months = []
netprofit = []
avgchange = []
increase = []
decrease = []

#function to find average 
def average(x):
    return sum(x) / len(x)

#link to csv file so you cah do analysis 
csvpath = os.path.join('Resources','budget_data.csv')

#enable reading of csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print("CSV Header:" + {csv_header})
    
    #test the connection
    #for row in csvreader:
        #print(row)
    
    # * The total number of months included in the dataset

    for row in csvreader:
    #adding items to my list
        months.append(row[0])
        netprofit.append(int(row[1]))
    
  
        #greatest increase in profits 
    for i in range(len(netprofit)):
        avgchange.append(netprofit[i +1]-netprofit[i])    
   
    avg = average(netprofit)
  
    #total amount of months, profits, averate of profits, greatest increase in profits, greatest decrease in loss 
    print("Total Amount of Months" + " " + str(len(months))) 
    print ("The sum of the profits is" + " "+ str((sum(netprofit))))
    print("The sum of the profits is" + " "+ str(round(avg,2)))