import os
import re

pattern_select = re.compile(r'\) *\{|\) *const *\{')
pattern_exclude = re.compile(r' +if \(| +for \(| +while \(|\) *\{.*?\}|\) *const *\{.*?\}')

def reading (current_path):
	file_list = os.listdir(current_path)
	for dir_ in file_list:
		path_name = current_path+'/'+dir_
		if os.path.isdir(path_name):
			reading(path_name)
		else:
			a,b = os.path.splitext(path_name)
			if b=='.h' or b=='.hpp' or b=='.cpp' or b=='.cc':
				rf = open(path_name)
				temp_file = path_name+".temp"
				wf = open(temp_file, 'w+')
				wf.write("#include <iostream>\n")
				for line in rf:
					wf.write(line)
					selectObj = pattern_select.search(line)
					excludeObj = pattern_exclude.search(line)
					if selectObj and not excludeObj:
						wf.write("  std::cout<<__FILE__<<\" , \"<<__LINE__<<std::endl;\n")
						print line
				rf.close()
				wf.close()
				os.remove(path_name)
				os.rename(temp_file, path_name)


if __name__ == '__main__':
	reading(os.getcwd())
