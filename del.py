# importing required modules
import os
import time

# folder is the name of the folder in which we
# have to perform the delete operation
folder = "demo"

# N is the number of days for which
# we have to check whether the file
# is older than the specified days or not
N = 3

# changing the current working directory
# to the folder specified
os.chdir(os.path.join(os.getcwd(), folder))

# get a list of files present in the given folder
list_of_files = os.listdir()

# get the current time
current_time = time.time()

# "day" is the number of seconds in a day
day = 86400

# loop over all the files
for i in list_of_files:
	# get the location of the file
	file_location = os.path.join(os.getcwd(), i)
	# file_time is the time when the file is modified
	file_time = os.stat(file_location).st_mtime

	# if a file is modified before N days then delete it
	if(file_time < current_time - day*N):
		print(f" Delete : {i}")
		os.remove(file_location)
