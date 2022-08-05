import os
import csv
import collections
from collections import Counter

# Variables
candidates = []
votes = []


# Collect data
election_data_csv_path = os.path.join("Resources1", "election_data.csv")

# Open csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read header
    csv_header = next(csvfile)

    # Print
    for row in csv_reader:

        candidates.append(row[2])

    # Sort
    sorted_list = sorted(candidates)
    arrange_list = sorted_list

    # Count
    count_candidate = Counter (arrange_list)
    votes.append(count_candidate.most_common())

    # Calculate
    for item in votes:
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
          

# Print Analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes[0][0][0]}: {first}% ({votes[0][0][1]})")
print(f"{votes[0][1][0]}: {second}% ({votes[0][1][1]})")
print(f"{votes[0][2][0]}: {third}% ({votes[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes[0][0][0]}")
print("-------------------------")


# Export Analysis
with open('Pypoll_Elect.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    text.write("-------------------------\n")
    text.write(f"{votes[0][0][0]}: {first}% ({votes[0][0][1]})\n")
    text.write(f"{votes[0][1][0]}: {second}% ({votes[0][1][1]})\n")
    text.write(f"{votes[0][2][0]}: {third}% ({votes[0][2][1]})\n")
    text.write("-------------------------\n")
    text.write(f"Winner:  {votes[0][0][0]}\n")
    text.write("-------------------------\n")
