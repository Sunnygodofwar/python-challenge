#import os
import os
import csv

#directory where the data will be pulled from
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#define list
total_months = 0
total_revenue = 0
value = 0
change = 0
dates = []
profits = []

#open and read CSV file
with open(budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")


    #Reading the header row
    csv_header = next(csvreader)

    #designate what row to read first
    first_row = next(csvreader)
    total_revenue += int(first_row[1])
    value = int(first_row[1])
    total_months += 1
    
    #going through rows of data
    for row in csvreader:
        # append row of dates 
        dates.append(row[0])
        
        # Calculate and add changes
        change = int(row[1])-value

        value = int(row[1])

        profits.append(change)
        
        #Total number of months
        total_months += 1

        #Total revenue with profit and loss where total revenue fetches data over entire period
        total_revenue = total_revenue + int(row[1])


    #calculate greatest decrease or biggest loss in profits
    greatest_decrease = min(profits)
    decrease_index = profits.index(greatest_decrease)
    decrease_date = dates[decrease_index]


    #calculate greatest increase in profits or biggest gain in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]



    #average change over a month
    avg_change = sum(profits)/len(profits)
    



#output to a .txt file

output = open("output.txt", "w")

line1 = "Financial Analysis"

line2 = "---------------------"

line3 = str(f"Total Months: {str(total_months)}")

line4 = str(f"Total: ${str(total_revenue)}")

line5 = str(f"Average Change: ${str(round(avg_change,2))}")

line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")

line7 = str(f"Greatest Decrease in Profits: {decrease_date} (${str(greatest_decrease)})")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))



#print to terminal

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {decrease_date} (${str(greatest_decrease)})")










