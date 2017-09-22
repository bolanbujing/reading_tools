import os
import re

pattern_select = re.compile(r'\) \{')

current_path = os.getcwd()
file_list = os.listdir(current_path)
for dir_ in file_list:
	path_name = current_path+'/'+dir_
	if os.path.isdir(path_name):
		print path_name
	else:
		a,b = os.path.splitext(path_name)
		if b=='.h' or b=='.hpp' or b=='.cpp' or b=='.cc':
			rf = open(path_name)
			temp_file = path_name+".temp"
			wf = open(temp_file)
			wf.write("#include <iostream>")
			for line in rf:
				wf.write(line)
				selectObj = pattern_select.search(line)
				if selectObj:
					wf.write("\tstd::cout<<__file__<<\" , \"<<__line__<<std::endl;")
					print line
			rf.close()
			wf.close()
