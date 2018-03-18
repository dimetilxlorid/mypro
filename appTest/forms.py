#from appTest import app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES, configure_uploads
from werkzeug.utils import secure_filename
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired
 




class FileUploadForm(FlaskForm):
	picFile  = FileField(validators=[FileRequired()])#, FileAllowed(images,'Images only!')])
	comment  = TextField(validators=[]) #validators=[DataRequired()]
	checkbox = BooleanField()