import yaml
dict_file = "a: [1,2,3,4]" + "\n"
dict_file = dict_file + "b: [1,3,5,7]" + "\n"
dict_file = dict_file + "c: " + "\n"
dict_file = dict_file + "  c1: [1,2,3]" + "\n"
dict_file = dict_file + "  c2:" + "\n"
dict_file = dict_file + "    c11: " + "\n"
dict_file = dict_file + "    - [1,2,3] " + "\n"
dict_file = dict_file + "    - [2,3,4] " + "\n"

for i in range(5):
	dict_file = dict_file + "    - " + "[{},{},{}]".format(i,i,i,) + "\n"

with open('fruits.yaml', 'w') as file:
    file.write(str(dict_file))
    file.close()

