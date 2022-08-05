import os
import csv

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    #Variables
    monthly_count = []
    profit = []
    profit_change = []
    
                      
    #Count , total , sort list
    for row in csvreader:
        monthly_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
                      
#Greatest increase/decrease in profits
increase = max(profit_change)
decrease = min(profit_change)

#Index
monthly_increase = profit_change.index(max(profit_change))+1
monthly_decrease = profit_change.index(min(profit_change))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(monthly_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {monthly_count[monthly_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {monthly_count[monthly_decrease]} (${(str(decrease))})")

with open('Pybank_budget.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------------\n")
    text.write(f"Total Months:{len(monthly_count)}\n")
    text.write(f"Total: ${sum(profit)}\n")
    text.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}\n")
    text.write(f"Greatest Increase in Profits: {monthly_count[monthly_increase]} (${(str(increase))})\n")
    text.write(f"Greatest Decrease in Profits: {monthly_count[monthly_decrease]} (${(str(decrease))})\n")

