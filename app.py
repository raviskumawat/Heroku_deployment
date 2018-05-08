from flask import Flask, render_template,request
#from werkzeug import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER']="/static"

@app.route("/")
def hello():
    return render_template('layout.html')

# @app.route('/test_audio')
# def test_audio():
#     return render_template('audio_play.html')


@app.route('/play_audio',methods=['GET','POST'])
def play_audio():
    if request.method=='POST':
        x=request.files['audio_file']
        x.save(os.path.join(app.root_path,'static',x.filename))
    return render_template('audio_play.html',**locals())


if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port='5000')
