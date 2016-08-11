import csv
import sys

def city_to_state_country(city):
    i=0
    a=[]
    with open('loc161csv/2016-1 UNLOCODE CodeListPart1.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[3] == city:
                #print (i)
                a.append([row[3].replace('"',''), row[5].replace('"',''), row[1].replace('"','')])
            i=i+1
    with open('loc161csv/2016-1 UNLOCODE CodeListPart2.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[3] == city:
                #print (i)
                a.append([row[3].replace('"',''), row[5].replace('"',''), row[1].replace('"','')])
            i=i+1
    with open('loc161csv/2016-1 UNLOCODE CodeListPart3.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[3] == city:
                #print (i)
                a.append([row[3].replace('"',''), row[5].replace('"',''), row[1].replace('"','')])
            i=i+1
    return a

#print city_to_state_country("\""+sys.argv[1]+"\"")
