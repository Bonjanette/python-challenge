import os
import csv

# set paths for reading source data and writing output data files
PyPoll_csv = os.path.join("Resources", "election_data.csv")
PyPoll_results = os.path.join("analysis", "election_results.txt")

# initialize Total Votes cast counter and dictionary for storing candidates and vote counts
total_votes = 0
candidates = {}

# Read data file
with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Count total votes
    for row in csvreader:
        total_votes +=1

        # retrieve candidates and store them and their vote counts in dictionary
        if row[2] in candidates.keys():
            candidates[row[2]] +=1
        else:
            candidates[row[2]] = 1

# Begin Election Results printing/writing
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------------")
with open(PyPoll_results, 'w') as results:
    results.write("Election Results\n")
    results.write("------------------------------\n")
    results.write("Total Votes: " + str(total_votes) +"\n")
    results.write("------------------------------\n")
    

# Calculate percentage for each candidate, print/write results
for candidate, vote in candidates.items():
    percentage = round(float((vote/ total_votes)*100), 3)
    print(candidate + ": " + str(percentage) +"% (" + str(vote) + ")")
    with open(PyPoll_results, 'a') as results:
        results.write(candidate + ": " + str(percentage) +"% (" + str(vote) + ")\n")
print("------------------------------")
with open(PyPoll_results, 'a') as results:
    results.write("------------------------------\n")
    

# Sort the candidates dictionary to get the winner which will be the candidate with the highest index in the key list
sorted_candidates = {}
sorted_key = sorted(candidates, key=candidates.get)
for candidate in sorted_key:
    sorted_candidates[candidate] = candidates[candidate]
sorted_candidates_list = list(sorted_candidates)
winner_index = len(sorted_candidates_list)-1
print("Winner: " + sorted_candidates_list[winner_index])
print("------------------------------")
with open(PyPoll_results, 'a') as results:
    results.write("Winner: " + sorted_candidates_list[winner_index] + "\n")
    results.write("------------------------------\n")