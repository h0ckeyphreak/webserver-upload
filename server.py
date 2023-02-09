import os, argparse, base64, socket, datetime, random, sys, io

from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port",  help="Assign a port for the web_uploader", required=True)
ap.add_argument("-o", "--outfile", help="Destination for uploaded file(s)")
args = ap.parse_args()

if args.port:
    port = args.port

if args.outfile:
    outfile = args.outfile
else:
    outfile = os.getcwd()

hostname = socket.gethostname()
t = datetime.datetime.now()
now = t.strftime('%f')
rand = str(random.randint(100000000000,999999999999))
message = hostname+now+rand
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
print("This is the Authorizaton key needed to upload: " +base64_message)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = outfile
app.secret_key = b'test'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    error = None
    auth = request.form.get('auth')
    file = request.files['file']
    if auth != base64_message:
        flash("Incorrect Authorization Key")
        return redirect(url_for("index"))
    filename = secure_filename(file.filename)
    if filename == '':
        flash("No file selected")
        return redirect(url_for("index"))
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash("File Uploaded Successfully")
    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(port=port)
