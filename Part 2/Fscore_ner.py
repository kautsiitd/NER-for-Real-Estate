import sys
import os
import pdb,re
if not(os.path.isfile(sys.argv[1]) and  os.path.isfile(sys.argv[2])):
	print "Error:n Atleast one of file does not exist"
	sys.exit(1)

in_file_user = open(sys.argv[1],"r")
in_file_gold = open(sys.argv[2],"r")

lines_user = in_file_user.readlines()
lines_gold = in_file_gold.readlines()

num_lines_user=len(lines_user)
num_lines_gold=len(lines_gold)
in_file_user.close()
in_file_gold.close()

# for ner
classes_list = ['L', 'P', 'LA','C', 'N','T','A','O']
classes = {}
index = 0
for c in classes_list:
	classes[c] = index
	index += 1
table = [[0 for i in range(len(classes))] for j in range(len(classes))]
for i in range(num_lines_user):
	s_user=lines_user[i].strip().split()
	s_gold=lines_gold[i].strip().split()
	if(len(s_user)<1):
		continue
	else:
		user_label = s_user[1]
		gold_label = s_gold[1]
	actual_index = classes[gold_label]
	predicted_index = classes[user_label]
	table[actual_index][predicted_index] += 1

all_precisions = []
all_recalls = []
for i in range(len(classes)):
	column_sum = sum(row[i] for row in table)	
	if column_sum == 0:
		precision = 1.0
	else:
		precision = table[i][i]/float(column_sum)
	all_precisions.append(precision)
	row_sum = sum(table[i])
	if row_sum == 0:
		recall = 1.0
	else:
		recall = table[i][i]/float(row_sum)
	all_recalls.append(recall)

for i in range(len(classes)):
	print "For Class ",classes_list[i]
	print "precision ", all_precisions[i]
	print "recall ",all_recalls[i]
	print "Fscore", 2*all_precisions[i]*all_recalls[i]/(all_recalls[i]+all_precisions[i])
	print "------------" 

num_classes = len(classes)-1 # for ner, don't count 'O' class
macroPrecision=sum(all_precisions[:num_classes])/num_classes
macroRecall=sum(all_recalls[:num_classes])/num_classes

if((macroPrecision==0)and(macroRecall==0)):
	macroF_Score=0
else:
	macroF_Score=2*macroPrecision*macroRecall/(macroPrecision+macroRecall)

print "macroF_Score is %f, " %(macroF_Score) 
print "macroPrecision is %f" %(macroPrecision) 
print "macroRecall is %f" %(macroRecall)


