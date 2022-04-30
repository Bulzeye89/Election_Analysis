# Election_Analysis

## Overview of Election Audit
### Background 
A Colorado Board of Elections employee had initially given me the follwing tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

After completing this, the election commission made a secondary request to complete the audit.  The additional data they have requested is:
1. The voter turnout for each county
2. The percentages of votes from each county out of the total count
3. The county with the highest turnout

### Resources
-Data Source: [election_results.csv](https://github.com/Bulzeye89/Election_Analysis/blob/main/Resources/election_results.csv)<br />
-Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana Degette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Antyhony Doane received 3.1% of the vote and 11,606 of the votes.<br />
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

In working the code further to complete the commission's secondary request, the data shows that:
- The voter turnout for each county was:
  - 38,855 votes in Jefferson
  - 306,055 for Denver
  - 24,801 for Arapahoe
- The percentage of votes out of the total count from each county was:
  - 10.5% for Jefferson
  - 82.8% for Denver
  - 6.7% for Arapahoe
- Denver had the highest turnout.  

When the script is ran on the election data, all of this info is saved in an easily accessible txt file for the election.  A screenshot of the output can be seen below.  

<img src="https://github.com/Bulzeye89/Election_Analysis/blob/main/analysis/election_analysis.txt" width=50% height=50%>

## Election Audit Summary




