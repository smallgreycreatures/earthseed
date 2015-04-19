import os
import shutil
from pydrive.auth	import GoogleAuth
from pydrive.drive	import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
local_path = '/Users/Frans/Documents/Earthseed/Logbooks'

#Script will work for 985 years, search for logbooks anno 2xxx-xx-xx
file_name = 'Logbook 2'
file_list = drive.ListFile({'q': "title contains '" + file_name + "' and trashed = False"}).GetList()


#listing files in /local_path/
dirs = os.listdir(local_path)

for file1 in file_list:
	file_found = False

	#print 'title: %s, id %s' %(file1['title'], file1['id'])

	for file in dirs:
		if file1['title'] == file:
			file_found = True

	if file_found == False:
		print '%s not found. Downloading' %file1['title']
		file1.GetContentFile(file1['title'], mimetype='text/html')
		#copy to local_path
		print 'Copy file to local directory'
		if not os.path.exists(local_path + '/' + file1['title']):
			os.makedirs(local_path + '/' + file1['title'])
		shutil.copy(file1['title'], local_path + '/' + file1['title'])
		print 'Done! File is saved in %s' %local_path + '/' + file1['title']


print 'All files are up to date!'