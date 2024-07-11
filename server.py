from flask import Flask, render_template, request, redirect, jsonify, url_for
import os
from werkzeug.utils import secure_filename
from floorplan import FloorplanToBlenderRunner 

app = Flask(__name__, static_url_path='')

UPLOAD_FOLDER = 'static/uploads/'
FLOORPLANS_FOLDER = 'floorplans'
OBJECTS_FOLDER = 'objects'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_IMG_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ALLOWED_OBJ_EXTENSIONS = {'glb', 'gltf'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename:str, extensions:list)  -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/floorplan', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')

        #### Validate File Constrains
        if file and file.filename and allowed_file(file.filename, ALLOWED_IMG_EXTENSIONS):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)
            
            name = filename.split('.')[0]
            if os.path.exists(f"static/models/{FLOORPLANS_FOLDER}/{name}.glb"):
                model_name = f"{name}.glb"
                return redirect(url_for('viewer', obj_type=FLOORPLANS_FOLDER, model_name=model_name))
                
            floor_path = FloorplanToBlenderRunner(image_path, name)
            model_name = os.path.split(floor_path)[-1]
            print(f'Floor Path: {floor_path} | File Name: {model_name}')

            return redirect(url_for('viewer', obj_type=FLOORPLANS_FOLDER, model_name=model_name))

        else:
            return redirect(request.url)
    return render_template('upload.html')


@app.route('/editor', methods=['GET', 'POST'])
def editor():
    # return render_template('editor.html')
    if request.method == 'POST':
        floorplan = request.files.get('floorplan')
        obj = request.files.get('object')

        floor_filename = ''
        obj_filename = ''
        #### Validate File Constrains
        if floorplan and floorplan.filename and allowed_file(floorplan.filename, ALLOWED_OBJ_EXTENSIONS):
            floor_filename = secure_filename(floorplan.filename)
            floor_path = os.path.join(app.static_folder, 'models', FLOORPLANS_FOLDER, floor_filename)
            floorplan.save(floor_path)

        if obj and obj.filename and allowed_file(obj.filename, ALLOWED_OBJ_EXTENSIONS):
            obj_filename = secure_filename(obj.filename)
            obj_path = os.path.join(app.static_folder, 'models', OBJECTS_FOLDER, obj_filename)
            obj.save(obj_path)
        
        if not (obj or floorplan):
            return render_template('editor_uploader.html')
            return redirect(url_for('editor'))
        
        return redirect(url_for('editor', floorplan=floor_filename, obj=obj_filename)) 
    else:
        floorplan = request.args.get('floorplan')
        obj = request.args.get('obj')

        if not (obj or floorplan):
            return render_template('editor_uploader.html')

        return render_template('editor.html', floorplan=floorplan, obj=obj)

@app.route('/viewer/<obj_type>/<model_name>')
def viewer(obj_type, model_name):
    return render_template('viewer.html', obj_type=obj_type, model_name=model_name)

@app.route('/models')
def list_models():
    floorplan_path = os.path.join(app.static_folder, 'models', FLOORPLANS_FOLDER)
    objects_path = os.path.join(app.static_folder, 'models', OBJECTS_FOLDER)
    
    floorplans = [f for f in os.listdir(floorplan_path) 
                  if f.endswith(('.glb', '.gltf'))] if os.path.exists(floorplan_path) else []
    objects = [f for f in os.listdir(objects_path) 
               if f.endswith(('.glb', '.gltf'))] if os.path.exists(objects_path) else []

    return render_template('models.html', floorplans= floorplans, objects= objects)

if __name__ == '__main__':
    app.run(debug=True)
