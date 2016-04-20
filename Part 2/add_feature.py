import re
import sys

# find tokens with labels "label" in given training file
def find_org_data(label):
	global labeled_data, size
	tokens = [];
	for data,i in zip(labeled_data,range(size)):
		try:
			if(len(data.split())==2 and data.split()[1] == label):
				tokens.append(i)
		except:
			pass
	return tokens

def add_to_feature(label, arr):
	global features
	for i in arr:
		features[i].append(arr)

# find tokens with labels that wrongly predicted
def covering_wrong(label, predicted):
	global tokens, labels
	golden = find_org_data(label)
	print "covering wrong"
	for i in predicted:
		if not(i in golden):
			print tokens[i], labels[i]

# find tokens with labels that not predicted at all
def not_covering(label, predicted):
	global tokens, labels
	golden = find_org_data(label)
	print "not covering"
	for i in golden:
		if not(i in predicted):
			print tokens[i], labels[i]

# print final array with features to a file
def print_file():
	global tokens, features ,labels
	a_featured = [[tokens[i]] for i in range(size)]
	for i in range(size):
		a_featured[i].extend(features[i])
		a_featured[i].append(labels[i])
	with open("train.txt","wb") as f:
		for data in a_featured:
			f.write(' '.join(data))
			f.write('\n')

# reading labeled file
labeled_data = open("a2_train.txt").readlines()
# reading tokens and labels
tokens = []; labels = []
for data in labeled_data:
	if(len(data.split())==0):
		tokens.append("")
		labels.append("")
	else:
		tokens.append(data.split()[0 ])
		labels.append(data.split()[-1])

size	 = len(tokens)
features = [[] for i in range(size)]

# for Telephone number
prefixes = open("Sub_strings/telephone.txt").read().splitlines()
# T_feature= []
for i in range(size):
	org_data = labeled_data[i]
	# should not empty
	if len(org_data.split()) == 0:
		continue
	data = org_data.lower()

	numbers = ''.join(re.findall('([\d\+])',   data))
	letters = ''.join(re.findall('([a-z])', data.split()[0]))
	# having more than 8 numbers
	add = 0
	if 8<len(numbers):
		add = 1
	# have +91 at starting
	if numbers[:3]=='+91':
		add = 1
	# should not have any alphabets
	if len(letters) != 0:
		add -= 1
	# but may have list of substrings with numbers
	if any(prefix in data for prefix in prefixes):
		add += 1
	# should not be a link
	if "http" in data:
		add -= 1
	if add>0:
		features[i].append("Tel")
		# T_feature.append(i)

# for Locations
prefixes = open("Sub_strings/DelhiNcrLocations.txt").read().splitlines()
L_feature = []
for i in range(size):
	

print_file()