import os
import csv

# Create list containing the full names of each candidates
candidates_list = {"full_name": ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]}

# Vote counter that correlates with candidate list
vote_counts = [0, 0, 0]

# Open cvs file for interpertation 
with open('C:\\Users\\16474\\Python_Challenge\\python-challenge\\PyPoll\\Resource\\election_data.csv','r') as csvfile:

    # Specify the delimiter for the csv file, skip headers to iterate through the data 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    data = list(csvreader)

    # Calculate the total amount of votes received 
    total_votes = len(data)

# Loop through data to fill out candidate list and respective votes counted for each
for i in range(0,(total_votes)):
    for j in range(3):
        if data[i][2] == candidates_list["full_name"][j]:
            vote_counts[j] += 1

# Calculate the winner using maximum, correlate the candidates name with the winning vote
winner = (max(vote_counts))
winner_name = vote_counts.index(winner)

# Print results in console
# Calculate vote percentage rounded to 3 decimals - through dividing individual votes by total votes, multiplyed by 100
print ("Election Results")
print ("-------------------------")
print (f"Number of Votes: {total_votes}")
print ("-------------------------")
print (f"{candidates_list['full_name'][0]}: {round((vote_counts[0]/total_votes)*100, 3)}% ({vote_counts[0]})")                                     
print (f"{candidates_list['full_name'][1]}: {round((vote_counts[1]/total_votes)*100, 3)}% ({vote_counts[1]})")
print (f"{candidates_list['full_name'][2]}: {round((vote_counts[2]/total_votes)*100, 3)}% ({vote_counts[2]})")   
print ("-------------------------")
print(f"Winner: {candidates_list['full_name'][winner_name]}")
print ("-------------------------")

# Print results into txt file in Analysis folder            
with open('C:\\Users\\16474\\Python_Challenge\\python-challenge\\PyPoll\\Analysis\\Analysis.txt','w') as file:
    file.write("Election Results\n")
    file.write ("-------------------------\n")
    file.write(f"Number of Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write(f"{candidates_list['full_name'][0]}: {round((vote_counts[0]/total_votes)*100, 3)}% ({vote_counts[0]})\n")                                     
    file.write(f"{candidates_list['full_name'][1]}: {round((vote_counts[1]/total_votes)*100, 3)}% ({vote_counts[1]})\n")
    file.write(f"{candidates_list['full_name'][2]}: {round((vote_counts[2]/total_votes)*100, 3)}% ({vote_counts[2]})\n")   
    file.write ("-------------------------\n")
    file.write(f"Winner: {candidates_list['full_name'][winner_name]}\n")
    file.write("-------------------------\n")