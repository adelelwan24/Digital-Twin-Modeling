import bpy
import math
import random
import os
import shutil

# Function to convert degrees to radians
def to_radians(degrees):
    return tuple(math.radians(angle) for angle in degrees)

# Adjusted list of camera positions and rotations based on the image
camera_views = [
    {'location': (7.0, 7.0, 5.0), 'rotation': to_radians((30, 0, 30))},   
    {'location': (0, 10, 0), 'rotation': to_radians((-20, 0, 90))},          
    {'location': (-7.0, 7.0, 5.0), 'rotation': to_radians((30, 0, 150))}, 
    {'location': (-10, 0, 0), 'rotation': to_radians((-20, 0, 210))},        
    {'location': (-7.0, -7.0, -5.0), 'rotation': to_radians((30, 0, 270))}, 
    {'location': (0, -10, 0), 'rotation': to_radians((-20, 0, 330))},        
]

# Light configurations
light_configs = [
    {'location': (10, 10, 10), 'type': 'POINT', 'energy': 1000}, # First light
    {'location': (-10, -10, 10), 'type': 'POINT', 'energy': 500},
    {'location': (-20, 0, 10), 'type': 'POINT', 'energy': 1000, 'rotation': (0, math.radians(-90), 0)}, # Light to the left
    {'location': (0, 0, 20), 'type': 'POINT', 'energy': 1000, 'rotation': (math.radians(-90), 0, 0)}, # Light at the top
    {'location': (20, 0, 10), 'type': 'POINT', 'energy': 1000, 'rotation': (0, math.radians(90), 0)},  # Light to the right
    {'location': (0, 0, -10), 'type': 'POINT', 'energy': 1000, 'rotation': (math.radians(90), 0, 0)},  # Light at the bottom
]

# Set render settings
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.resolution_percentage = 100

# Find the imported object
imported_obj = None
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        imported_obj = obj
        break

# Ensure the imported object is found
if imported_obj is not None:
    imported_obj.location = (0, 0, 0)
else:
    raise Exception("No imported object found in the scene.")

# Add light sources to the scene
lights = []
for light_data in light_configs:
    bpy.ops.object.light_add(type=light_data['type'], location=light_data['location'])
    light = bpy.context.object
    light.data.energy = light_data['energy']
    lights.append(light)

# Function to generate a random location and rotation for the query image
def random_angles():
    location = (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10))
    rotation = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
    return location, to_radians(rotation)

# Loop through each camera view
for i, view in enumerate(camera_views):
    # Add a new camera
    bpy.ops.object.camera_add(location=view['location'])
    camera = bpy.context.object

    # Set the camera rotation
    camera.rotation_euler = view['rotation']

    # Ensure the camera is pointing at the object
    constraint = camera.constraints.new(type='TRACK_TO')
    constraint.target = imported_obj
    constraint.track_axis = 'TRACK_NEGATIVE_Z'
    constraint.up_axis = 'UP_Y'

    # Set the camera as active
    bpy.context.scene.camera = camera
    
    # Render the scene
    bpy.context.scene.render.filepath = f"E:/render_{i}.png"
    bpy.ops.render.render(write_still=True)

    # Remove the camera
    bpy.data.objects.remove(camera, do_unlink=True)

# Generate and save 10 query images with random angles
for j in range(10):
    query_location, query_rotation = random_angles()
    
    # Add a new camera for the query image
    bpy.ops.object.camera_add(location=query_location)
    query_camera = bpy.context.object
    query_camera.rotation_euler = query_rotation
    
    # Ensure the camera is pointing at the object
    constraint = query_camera.constraints.new(type='TRACK_TO')
    constraint.target = imported_obj
    constraint.track_axis = 'TRACK_NEGATIVE_Z'
    constraint.up_axis = 'UP_Y'
    
    # Set the camera as active
    bpy.context.scene.camera = query_camera
    
    # Create a folder for the output
    output_folder = f"E:/output_{j+1}"
    os.makedirs(output_folder, exist_ok=True)
    
    # Copy the existing images to the new folder
    for i in range(6):
        source = f"E:/render_{i}.png"
        destination = f"{output_folder}/render_{i}.png"
        shutil.copy(source, destination)
    
    # Render the query image
    bpy.context.scene.render.filepath = f"{output_folder}/query_image.png"
    bpy.ops.render.render(write_still=True)
    
    # Remove the query camera
    bpy.data.objects.remove(query_camera, do_unlink=True)

# Optional: If you want to remove the lights after rendering
for light in lights:
    bpy.data.objects.remove(light, do_unlink=True)
