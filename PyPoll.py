#Module 3.3.3
#The data we need to retrive
#1. The total number of votes cast
#2. A complete list of vandidate who received votees
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#Moduel 3.4.2
#Assign a variable for the file to load and path
#file_to_load = 'Resources/election_results.csv'

    #Using open and close to import data file
    #Open the election results and read the file.
    #election_data = open(file_to_load, 'r')
    #To do: perform analysis.
    #Close the file.
    #election_data.close()

#editing above code to use with statement
#Open the election results and read the file
    #with open(file_to_load) as election_data:

    #To do: perform analysis
        #print(election_data)

#importing with indirect path

#import csv

#import os

#Assign a variable for the file to load and path
#file_to_load = os.path.join("Resources","election_results.csv")
#Open the election results and read the file.
#with open(file_to_load) as election_data:
    #Print the file object
    #print(election_data)

#Module 3.4.3
#Create a filename variable to a direct or indirect path to the file.
#file_to_save =os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file.
    #open(file_to_save, "w")

#changing above as module continues to below code
#Use the open statement to open the file as a text file.
    #outfile = open(file_to_save, "w")
#Write some data to the file.
    #outfile.write("Hello World")

#Close the file
    #outfile.close()

#updating above code to below to use 'with' statement instead of open and close
#Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
    #Write some data to the file.
    #using \n to write each county on own line \n acts as return or enter
    #txt_file.write("Counties in the election\n------------------------")
    #txt_file.write("\nArapahoe\nDenver\nJefferson")

 #Module 3.4.4

 #Add our dependencies

import csv

import os

#Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path.

file_to_save =os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file

with open(file_to_load) as election_data:

    #To do:read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file.
    #for row in file_reader
    #print(row)

#How would you retrive the first item from each row?
    #for row in file_reader:
    #print(row[0])

#Print the header row

    headers = next(file_reader)
    print(headers)

