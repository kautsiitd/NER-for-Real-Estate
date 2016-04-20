token = "ready to move"
o_label = "O O O"
r_label = "A A A"
replace_it = zip(token.split(),o_label)
with_it = zip(token.split(),r_label)

with open("a2_train.txt") as f:
	