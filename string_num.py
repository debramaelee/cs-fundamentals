# Given this string, find the highest_value variable and print highest highest

string_input = '1, 23,4,55,,1,,,33,  ,3,,5,103,  74,3'
string_split = string_input.split(",")

for i in range(len(string_split)):
	string_split[i] = string_split[i].strip()

highest = 0
for j in string_split:
	if len(j) != 0:
		n = int(j)
		if n > highest:
			highest = n

print(highest)

#HW do it in one loop

