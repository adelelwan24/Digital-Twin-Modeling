import bpy
from mathutils import Vector


def read_object(name):
    """
    Function to read an object by its name.
    """
    obj = bpy.data.objects.get(name)
    if obj is None:
        raise ValueError(f"Object '{name}' not found.")
    return obj

def get_floorplan_height(floorplan):
    """
    Function to get the height of the floorplan object.
    """
    # Assuming the height is the Z dimension of the bounding box
    return floorplan.dimensions.z

def scale_object(obj, scale_factor):
    """
    Function to scale an object.
    """
    obj.scale = (scale_factor, scale_factor, scale_factor)

def set_object_position(obj, position):
    """
    Function to set the position of an object.
    """
    obj.location = position

def check_position_in_floorplan(floorplan, position):
    """
    Function to check if the position is inside the floorplan.
    """
    bbox_corners = [floorplan.matrix_world @ Vector(corner) for corner in floorplan.bound_box]
    min_corner = Vector((min([v.x for v in bbox_corners]), min([v.y for v in bbox_corners]), min([v.z for v in bbox_corners])))
    max_corner = Vector((max([v.x for v in bbox_corners]), max([v.y for v in bbox_corners]), max([v.z for v in bbox_corners])))
    return (min_corner.x <= position.x <= max_corner.x and
            min_corner.y <= position.y <= max_corner.y and
            min_corner.z <= position.z <= max_corner.z)

def join_objects(obj1, obj2):
    """
    Function to join two objects into one.
    """
#    bpy.ops.object.select_all(action='DESELECT')
##    bpy.context.view_layer.objects.active = obj1
#    obj1.select_set(True)
#    obj2.select_set(True)
#    bpy.ops.object.join()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()

def save_object(obj, filepath):
    """
    Function to save the final object.
    """
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.ops.export_scene.gltf(filepath=filepath, use_selection=True)


#################### Program ########################
# Delete all objects in the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)


# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

bpy.ops.import_scene.gltf(
    # filepath="F:\\ITI AI intake 44\\Graduation Project\\Digital-Twin-Modeling\\Target\\floorplan.glb", 
    filepath=r"F:\ITI AI intake 44\Graduation Project\Digital-Twin-Modeling\gradio_cached_examples\14\3D Model\ac1af78842fd751f2247\floorplan.glb")
floorplan = bpy.context.active_object
print(f'Floorplan Name: {floorplan.name}')

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

bpy.ops.import_scene.gltf(
    filepath="F:\\ITI AI intake 44\\Graduation Project\\dolphin.glb")
    
other_object = bpy.context.active_object
print(f'Object Name: {other_object.name}')

# Define object names and file path
floorplan_name = floorplan.name  # Replace with the name of your floorplan object
object_name = other_object.name   # Replace with the name of your other object
output_path = "F:/final_object.glb"  # Replace with your desired output path


# Get floorplan height
floorplan_height = get_floorplan_height(floorplan)
print(f"Floorplan Height: {floorplan_height}")

# Scale the object based on the height of the floorplan
scale_factor = floorplan_height / other_object.dimensions.z
#scale_object(other_object, scale_factor)
scale_object(other_object, 5)
# Enter a position to set the object in the floorplan
position = (7.0, 5.0, 0.5)  # Replace with the desired position

# Check if the position is in the floorplan
#if check_position_in_floorplan(floorplan, position):
#    set_object_position(other_object, position)
#else:
#    raise ValueError("Position is outside the floorplan.")

# Join the objects into one
join_objects(floorplan, other_object)

# Save the final object
final_object = bpy.context.view_layer.objects.active
print(f'final object {final_object}')
save_object(final_object, output_path)

print(f"Final object saved at {output_path}")
#max(max(C.active_object.matrix_world))


#############

#import bpy

#def select_object_and_children(obj):
#    """
#    Select an object and all its children recursively.
#    :param obj: The root object to start the selection from.
#    """
#    # Deselect all objects
#    bpy.ops.object.select_all(action='DESELECT')

#    # Define a recursive function to select the object and its children
#    def recursive_select(obj1):
#        obj1.select_set(True)
#        for child in obj1.children:
#            recursive_select(child)

#    # Select the root object and all its children
#    recursive_select(obj)

#    # Set the active object
#    bpy.context.view_layer.objects.active = obj

## Example usage
#object_name = "Floorplan7"  # Replace with the name of your root object
#root_object = bpy.data.objects.get(object_name)

#if root_object:
#    select_object_and_children(root_object)
#    print(f"Object '{object_name}' and its components have been selected.")
#else:
#    print(f"Object '{object_name}' not found.")