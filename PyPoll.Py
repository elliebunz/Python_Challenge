import os
import csv 

#create path for csv file from Resources 
csvpath = os.path.join("Resources", "election_data.csv")

#define variables - starting number of votes as 0 for each canidate 
total_votes = 0 

#define variables - store votes and create vote counter 
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

vote_count = []

#open csv 
with open(csvpath) as csvfile: 

csvreader = csv.reader(csvfile, delimiter=',')

#print
print(csvreader)

#find the total number of votes by using list and length of rows 
votes = int(row[0])
vote_counter.append(vote)
total_votes = len(vote_counter)

#define canidate names and count votes for reach 
Candidate_name = row[2]
if Candidate_name == "khan"
    khan_votes.append(Candidate_name)
elif Candidate_name == "Correy":
    correy_votes.append(Candidate_name)

elif Candidate_name == "Li": 
    Li_votes.append(Candidate_name)
else 
    otooley_votes.append(Candidate_name)


khan_total = len(khan_votes)
correy_total = len(correy_votes)
Li_total = len(Li_votes)
otooley_total = len(otooley_votes)

# find percent of total for all canidates - not sure 
    khan_pct = khan_total / total_votes
    correy_pct = correy_total / total_votes
    li_pct = li_total / total_votes
    otooley_pct = otooley_total / total_votes
    

    # find the winner using max 

    winner = max(khan_total, correy_total, li_total, otooley_total)

    #use if statement to find winning_candidate
    if winning_candidate== khan_total:
        winning_candidate_name = "Khan"
    elif winning_candidate == correy_total:
        winning_candidate_name = "Correy"
    elif winning_candidate == li_total:
        winning_candidate_name = "Li"
    else:
        winning_candidate_name = "O'Tooley"
    #print(winning_candidate_name)


#print results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_pct} ({khan_total})")
print(f"Correy: {correy_pct} ({correy_total})")
print(f"Li: {li_pct} ({li_total})")
print(f"O'Tooley: {otooley_pct} ({otooley_total})")
print("-------------------------")
print(f"Winning_candidate: {winning_candidate_name}")
print("-------------------------")


