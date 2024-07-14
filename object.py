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
    """
    Run the InstanceMesh model.

    parameters
    ----------
    image_path : str 
        The path to the image relative to the path: ../InstantMesh
    """

    print(image_path)

    if os.path.basename(os.getcwd())  == "InstantMesh":
        config_path = 'configs/instant-nerf-base.yaml'
        ouput_folder = "../static/models/objects"
        run = 'run.py'
    else:
        config_path = 'InstantMesh/configs/instant-nerf-base.yaml'
        ouput_folder = "static/models/objects"
        run = 'InstantMesh/run.py'
    command = ['python', run, config_path, image_path, '--output_path',  ouput_folder]

    print("Starting the process...")
    try:
        subprocess.run(command, check=True)
        print("Process completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")



