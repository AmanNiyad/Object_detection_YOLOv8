import numpy as np
from flask import Flask, request, render_template, Response
import pickle
# from distutils.log import debug
from fileinput import filename
import os
import cv2

save_dir = os.path.join('static', 'uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = save_dir

model = pickle.load(open('models/model.pkl', 'rb'))
cam_port = 0
cam = cv2.VideoCapture(cam_port)
def gen_frames():  
    while True:
        success, frame = cam.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  

@app.route('/')
def main():
    return render_template('index1.html')

# @app.route('/result', methods=['POST','GET'])
# def result():
#     if (request.method == 'POST'):
#         f = request.files['file']
#         full_filename = os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
#         f.save(full_filename)
#         model(full_filename, save=True, project=app.config['UPLOAD_FOLDER'], exist_ok=True)
#         output = os.path.join(app.config['UPLOAD_FOLDER'],'predict',f.filename)
#         return render_template("acknowledgement.html",user_image = output)
#     # return render_template("acknowledgement.html")
#
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
