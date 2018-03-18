import time
def changeFileExtension(obj):
	filename = obj.filename
	ext = ''
	if '.' in filename:
		l = filename.rsplit( chr(46), 1)
		ext = l[1]
		name = l[0]
	if ext == '':
		return False
	ext = ext.lower()
	obj.filename = name+'.'+ext
	return True
	
def changeFileName(filename):	
	l= filename.rsplit('.',1)
	name = l[0].replace('/','').replace('\\','')
	ext= l[1].replace('/','').replace('\\','')
	ctime = time.localtime(time.time())
	s = str(ctime[3]) + str(ctime[4]) + str(ctime[5]) +'_'+ str(ctime[2]) + str(ctime[1])+str(ctime[0])
	filename = name +'_'+ s+'.'+ext
	return filename