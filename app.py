from flask import Flask, render_template, request, redirect, send_from_directory
import os
from werkzeug.utils import secure_filename
from main import FloorplanToBlenderRunner 

app = Flask(__name__, static_url_path='')

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)
            
            name = filename.split('.')[0]
            if os.path.exists(f"static/models/floorplan/{name}.glb"):
                model_name = f"{name}.glb"
                return render_template('viewer.html', model_name=model_name)
                
            floor_path = FloorplanToBlenderRunner(image_path, name)
            model_name = os.path.split(floor_path)[-1]
            print(f'Floor Path: {floor_path} | File Name: {model_name}')
            return render_template('viewer.html', model_name=model_name)

        else:
            return redirect(request.url)
    return render_template('upload.html')

@app.route('/editor')
def display():
    # return render_template('3d.html', model='final_object.glb')
    # return render_template('drag_cubes.html')
    # return render_template('drag.html')
    return render_template('editor.html')

@app.route('/viewer')
def viewer():
    return render_template('viewer.html', model='final_object.glb')
    # return render_template('drag.html')

@app.route('/floor')
def send_report():
    return send_from_directory('static', 'models/floorplan.glb')

if __name__ == '__main__':
    app.run(debug=True)
