#Developed by Anish Katariya
import subprocess
import csv

#Defines the function to take the given url
#Ping for ipv4 it and save the relevant result to a text file
def pingSite(URL):
    ping = subprocess.Popen(["ping", "-c", "10",URL],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    out, error = ping.communicate()
    out = out.strip()
    error = error.strip()
    output = open("PingResults.txt",'a')
    output.write(str(out))
    output.write(str(error))
    output.write("\n\n====================\n\n")
    print(out)
    print(error)
    output.close()
#Defines the function to take the given url
#Ping for ipv6 it and save the relevant result to a text file
def pingSite6(URL):
    ping = subprocess.Popen(["ping6", "-c", "10",URL],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    out, error = ping.communicate()
    out = out.strip()
    error = error.strip()
    output = open("PingResults6.txt",'a')
    output.write(str(out))
    output.write(str(error))
    output.write("\n\n====================\n\n")
    print(out)
    print(error)
    output.close()
#Goes through each line in the given csv file
#Extracs the URL and send it to both files
with open('Top100sites.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter = ',')
    for row in readCsv:
        URL=row[1]
        pingSite(URL)
        pingSite6(URL)
