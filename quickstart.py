from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
exists = False

for file1 in file_list:
	print 'title: %s, id %s' % (file1['title'], file1['id'])

	if file1['title'] == 'Hello.txt':
		exists = True

	elif file1['title'] == 'RapportMall':
		print 'found %s' %file1['title']
		content = file1.GetContentFile('test.html', mimetype='text/html')

if exists == True:
	print 'file already exists'

else:
	file1 = drive.CreateFile({'title': 'Hello.txt'})
	file1.Upload()
	print 'title: %s, id %s' % (file1['title'], file1['id'])

#Iterate over files
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print 'title: %s, id: %s' % (file1['title'], file1['id'])

