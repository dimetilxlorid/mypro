## -*- coding: utf-8 -*
import time
from appTest import app,get_db
from forms import FileUploadForm
from flask import g, redirect, url_for, flash, request, render_template, send_from_directory
from flask_uploads import UploadSet, IMAGES, configure_uploads, UploadConfiguration
from myModule import changeFileExtension, changeFileName
from werkzeug.utils import secure_filename


images = UploadSet('images', IMAGES)
configure_uploads(app, (images,))

@app.route('/')
@app.route('/index')
def index():
	return redirect( url_for('pictures'))
	
@app.route('/upload')
def upload():
	form = FileUploadForm();
	header = 'Cтраница загрузки'.decode('utf-8')
	return render_template('upload.html', title = app.config['TITLE'], header= header, form= form)

@app.route('/uploading', methods= ['GET','POST']) 
def uploading():
	form = FileUploadForm()
	if request.method == 'POST':
		if form.validate_on_submit() and 'picFile' in request.files:
			file = request.files['picFile']
			#flash(file.filename)
			if changeFileExtension(file):
				filename = file.filename
				if images.file_allowed(file,filename):
					#filename = secure_filename(filename)
					filename = changeFileName(filename)
					path= 'pict'
					name_for_save = images.resolve_conflict( path, filename)
					images.save(file, path ,name_for_save)
					# db
					db = get_db();
					db.execute( 'INSERT INTO PICTURES ( path, filename, comment, data ) VALUES (?,?,?,?)', [ path , name_for_save, request.form['comment'], time.time() ] )
					db.commit()
					return redirect(url_for('pictures'))
			form.errors['picFile'] = ('file extension is not supported',)	
	header = 'Страница загрузки'.decode('utf-8')
	return render_template('upload.html', title = app.config['TITLE'], header= header, form= form)

@app.route('/pictures')
def pictures():
	db = get_db();
	curs = db.execute('SELECT * FROM pictures')
	fetch = curs.fetchall()
	#if fetch:
	#	return redirect(url_for('upload'))
	l=[]
	for r in fetch:
		shortcomm = r['comment']
		if len(shortcomm) > 42:
			shortcomm= shortcomm[0:42]+'...'
		d={'path':r['path'],'filename':r['filename'], 'comment':r['comment'],'shortcomm': shortcomm, 'data':r['data']}
		l.append(d)
	header = 'Галерея'.decode('utf-8')
	return render_template('pictures.html', title= app.config['TITLE'], header = header , rows = l)

@app.route('/files/<path>/<filename>')
def files(path, filename):
	return send_from_directory(app.config['UPLOADED_IMAGES_DEST'].split('/',1)[1]+'/'+path, filename)

@app.route('/file/<path>/<filename>')
def file(path,filename):
	return render_template('pic.html', title= app.config['TITLE'], path= path, filename= filename)
	
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite3_db'):
        g.sqlite3_db.close()
