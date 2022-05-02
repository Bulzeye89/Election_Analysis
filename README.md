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

When the script is ran on the election data, the above data will be displayed in the terminal output (as seen in below screenshot) as well as saved in an easily accessible txt file.  

![terminal output](https://github.com/Bulzeye89/Election_Analysis/blob/main/Resources/Election-Analysis-terminal-output.png)



## Election Audit Summary

As shown above, this election audit for these three counties can be done in a fractions of a second once all the data has been aggregated together.  If the Colorado Board of elections wishes to use this for other counties in the state, for future elections, or if they have any contacts in neighboring states that would benefit from this audit process, I will be at your disposal.  An additional insight that could be explored from the data provided is the total votes each candidate received in each county.  It's possible that Diana Deggete won the election but only one Denver county and lost the other two counties.  This could be easily added into the code to highlight.  In addition, if additional data sources were combined with what had been provided, more than things could have been explored in the audit.  For instance, if census info or candidate's campaign budgets were were combined with this data, there are many different relationships we could explore with the total vote outcomes that would many future candidates would be interested in learning.  

