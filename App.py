from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import os,cv2
from screenshotAnalyzer import convertImage2json
from slotToTime import convertSlotToTime
import matplotlib.pyplot as plt
app = Flask(__name__)

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
        return filename
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True)
    
    
