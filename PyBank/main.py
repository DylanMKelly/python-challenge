import os
import csv

# Opening csv file for reading and interpertation 
with open ('C:\\Users\\16474\\Python_Challenge\\python-challenge\\PyBank\\Resources\\budget_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # Removing headers from data being evaluated
    csv_header = next(csv_reader)

    # Empty variable lists 
    total_months = []
    total_profit = []
    profit_change = []

    for row in csv_reader:
        # Storing values for months and profits to correlate with respective areas in CSV 
        total_profit.append(int(row[1]))
        total_months.append(row[0])
    
    # Repeat through profit value to compare 
    for i in range(1,len(total_profit)):

        # Appending the difference between two months for change in monthly profit
        profit_change.append(int(total_profit[i])-int(total_profit[i-1]))

# Calculate total amount of months in csv
Number_Months = len(total_months)

# Calculate total amount of profit within all rows
Total = sum(total_profit)

# Calculate the average change in profits between months, rounding to two decimals 
average_change = round(sum(profit_change)/len(profit_change),2)

# Calculate the maximum value and minimum value 
max_increase_profit = max(profit_change)
max_decrease_profit = min(profit_change)

# Correlate Maximum and minimum with respective month
max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1 

# Print in console the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(Number_Months)}")
print(f"Total: ${str(Total)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_profit))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_profit))})")

# Print results into txt file in Anlaysis folder
with open('C:\\Users\\16474\\Python_Challenge\\python-challenge\\PyBank\\Analysis\\Analysis.txt','w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {str(Number_Months)}\n")
    file.write(f"Total: ${str(Total)}\n")
    file.write(f"Average Change: ${str(average_change)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_profit))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_profit))})\n")