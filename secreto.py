import os
def rename_files():
#step 1 -> get file names
	print ("Insert File Path:")
	file_path = raw_input("> ")

	file_list = os.listdir(file_path)
	print (file_list)

	saved_path = os.getcwd()
	print ("Current Working Directory is "+saved_path)
	os.chdir(file_path)

#step 2 -> rename each file
	for file_name in file_list:

		print ("Old Name -> "+file_name)
		print ("New_Name -> "+file_name.translate(None, "0123456789"))

		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()