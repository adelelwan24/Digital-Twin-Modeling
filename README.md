# Digital Twin Modeling

This repository contains code and documentation for the Digital Twin Modeling project, which involves creating digital twins of physical objects using 3D modeling techniques. The project focuses on automating data collection, preprocessing 3D models, and generating 3D objects and floor plans from 2D images. 

https://github.com/user-attachments/assets/2416c077-745a-48c6-bb93-a7498d81b95a

## Table of Contents
- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Preprocessing Steps](#preprocessing-steps)
- [Data Output](#data-output)
- [Research](#research)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Digital Twin Modeling project aims to enhance smart city simulations by providing accurate digital representations of physical objects and environments. By integrating cutting-edge 3D modeling techniques, this project enables detailed and realistic simulations, which can be instrumental in urban planning, infrastructure management, and emergency response strategies. 

The project is divided into two main components:

1. **3D Object Generation**: This involves creating precise 3D models of individual objects using advanced techniques such as neural radiance fields (NeRF). These models are essential for generating realistic simulations and visualizations.

2. **3D Floorplan Generation**: This component focuses on converting 2D floorplans into 3D models, allowing for comprehensive simulations of indoor spaces. By utilizing classical Computer Vistion(Rule-Based approch), we can generate accurate floorplans that are crucial for various applications within smart cities.

## Data Collection

### Overview

The data collection process involves automating the generation of different 2D images from a single 3D mesh at various positions and orientations. The primary data sources for 3D models include websites like Thingiverse, GrabCAD, TurboSquid, CGTrader, and Sketchfab.

### Data Sources

- **3D Model**: Imported from websites like Thingiverse, GrabCAD, TurboSquid, CGTrader, and Sketchfab.
- **Formats**: Compatible 3D mesh formats (e.g., .obj, .glb).

## Preprocessing Steps

1. **Object Initialization**: Script identifies and sets the 3D mesh location to the origin (0, 0, 0).
2. **Camera Configurations**: Predefined views based on optimal angles from research papers.
3. **Lighting Configurations**: Multiple light sources with varying configurations for detailed visualization.

## Data Output

- **Rendered Images**:
  - **Predefined Views**: Six images per folder, each from different angles.
  - **Random Query Images**: Ten additional images from random camera positions.
- **File Structure**: Folders contain the predefined views and one query image per folder.

## Research

- **Plan2Scene**: Focuses on texturing floor, wall, and window surfaces. [Plan2Scene](https://3dlg-hcvc.github.io/plan2scene/)
- **InstantMesh**: 3D Mesh Generation from a Single Image. [InstantMesh](https://github.com/TencentARC/InstantMesh)
- **FloorNet**: Converts RGBD videos of indoor spaces into vector-graphics floorplans. [FloorNet](https://art-programmer.github.io/floornet.html)
- **Raster-to-Vector**: Converts raster floorplan images to vector graphics. [Floorplan Transformation](https://art-programmer.github.io/floorplan-transformation.html)

## Dependencies

- **Blender**: free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling. [Blender](https://www.blender.org)
- **InstantMesh**: Efficient 3D Mesh Generation from a Single Image. [InstantMesh](https://github.com/TencentARC/InstantMesh)
- **FloorplanToBlender3d**: A tool to convert floor plans to 3D models in Blender. [FloorplanToBlender3d](https://github.com/grebtsew/FloorplanToBlender3d)
- **Three.js**: A JavaScript library for 3D graphics. [Three.js](https://threejs.org/)
- **Gradio**: A Python library for building interactive UIs for machine learning models. [Gradio](https://www.gradio.app/)


## Usage

1. Clone the repository:
    ```sh
    https://github.com/adelelwan24/Digital-Twin-Modeling.git
    cd Digital-Twin-Modeling
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    pip install -r InstantMesh/requirements.txt
    ```
3. Run the server:
    ```sh
    python server.py
    ```
4. Run the gradio froolplan app:
    ```sh
    python gradio_floorplan.py
    ```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
