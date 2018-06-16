from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_pymongo import PyMongo
from screenshotAnalyzer import convertImage2json
from slotToTime import convertSlotToTime


app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'freeslots'
app.config['MONGO_URI'] = 'mongodb://dscfreeslots:freeslots1!@ds147440.mlab.com:47440/freeslots'

mongo = PyMongo(app)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        convertImage2json(filename)
        data = convertSlotToTime()
        print(data)
        user = mongo.db.users
        user.insert(data)
        return filename
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True)
    
    
