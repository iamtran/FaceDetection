from flask import Flask, redirect, url_for, render_template,request , send_from_directory
from werkzeug import secure_filename
import os
##########
import sys
import facedetection
from facedetection import *

#from app import app


#UPLOAD_FOLDER = '/home/me/Desktop/projects/flask/uploads'
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

directory = UPLOAD_FOLDER
if not os.path.exists(directory):
    os.makedirs(directory)

@app.route('/basic')
def basic_image():
   return render_template('basic_image.html')


#@app.route('/upload')
@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']

      filename = secure_filename(f.filename)
      #print(">>>> DEBUG", os.getcwd())
      #print (os.path.join(app.config['UPLOAD_FOLDER'], filename))
      #print(os.path.exists((os.path.join(app.config['UPLOAD_FOLDER'], filename))))
      #print(sys.version)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      ####
      outfile = "out-" + filename
      #print (filename, outfile)
      full_ifile = os.path.join(app.config['UPLOAD_FOLDER'] ,filename)
      full_ofile = os.path.join(app.config['UPLOAD_FOLDER'] ,outfile)
      #print (full_ifile)
      #print (full_ofile)
      out_img = read_image_file_2_detect (full_ifile)
      test_outfile = write_image_2_file (out_img, full_ofile)

      ####
      return redirect(url_for('uploaded_file', filename=outfile))

@app.route('/show/<filename>')
def uploaded_file(filename):
   host_str = get_Host_name_IP() #Function call
   return render_template('template007.html', filename=filename, myhost=host_str)

@app.route('/uploads/<filename>')
def send_file(filename):
   print (UPLOAD_FOLDER, filename)
   return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)
