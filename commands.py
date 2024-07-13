# NOTE:: Downloading an instance
# !nvidia-smi
# pip install -U pip
# pip install Ninja
# pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu121
# pip install xformers==0.0.22.post7
# pip install https://huggingface.co/r4ziel/xformers_pre_built/resolve/main/triton-2.0.0-cp310-cp310-win_amd64.whl
# ! git clone https://github.com/TencentARC/InstantMesh.git
# cd InstantMesh
# pip install -r requirements.txt
# pip install "jax[cuda12_pip]==0.4.23" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
# import torch
# torch.cuda.empty_cache()
# pip install -U huggingface_hub

# NOTE:: To run an instance
# %run run.py configs/instant-nerf-base.yaml examples/bird.jpg


# NOTE:: To remove the outputs 
# import shutil
# import os

# # Path to the folder you want to download
# folder_path = './outputs'

# # Name for the zip file
# zip_file_name = 'Instant_Mesh'

# if os.path.exists(folder_path):
#     if os.path.exists(zip_file_name):
#         os.remove(zip_file_name)


# # Create a zip file of the folder
# shutil.make_archive(zip_file_name, 'zip', folder_path)

import subprocess
import os

def run_instant_nerf(image_path):

    current_dir = os.getcwd()
    instant_mesh_dir = os.path.join(current_dir, "InstantMesh")

    print(os.path.basename(current_dir))
    if os.path.basename(current_dir) == "InstantMesh":
        print(f"Already in InstantMesh directory: {current_dir}")
        instant_mesh_dir = current_dir
    else:
        # Check if InstantMesh directory exists
        if os.path.exists(instant_mesh_dir):
            os.chdir(instant_mesh_dir)
            print(f"Changed to InstantMesh directory: {os.getcwd()}")
        else:
            print(f"InstantMesh directory not found at {instant_mesh_dir}")

    config_path = 'configs/instant-nerf-base.yaml'
    command = ['python', 'run.py', config_path, image_path]
    print("Attempting to connect")
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")


# image_path = 'examples/pikachu.png'  
# run_instant_nerf(image_path)
