from string import *
import csv

dict1={}
dict2={}

with open('vocab.txt', newline='') as raw:
	csvread = csv.reader(raw, delimiter='	');
	print(1)
	print(csvread)
	for row in csvread:
		print(row[0])
		row[0] = row[0].capitalize();
		dict1[row[0]] = row[1];
	print(dict1);
		
with open('vocab2.txt', 'r') as raw2:
	csvread = csv.reader(raw2, delimiter='	');
	for row in csvread:
		row[0] = row[0].capitalize();
		dict2[row[0]] = row[1];

for i,j in dict1.items():
	if i not in dict2.items():
		dict2[i] = j;
		
master = dict(list(dict1.items()) + list(dict2.items()));

with open('truevocab2.txt', 'w', newline="") as csvfile:
	writa = csv.writer(csvfile, delimiter = '	')
	for w,d in master.items():
		writa.writerow([w,d,0,0,False]);

