import gradio as gr
import os

from main import FloorplanToBlenderRunner

demo = gr.Interface(
    fn=FloorplanToBlenderRunner,
    inputs=gr.Image(label="Upload an Image", type="filepath"),
    outputs=gr.Model3D(
            clear_color=[0.0, 0.0, 0.0, 0.0],  
            camera_position=[45, 45, 20],
            label="3D Model"),
    title="Image to 3D Model Converter",
    description="Upload an image and it will convert it to a 3D model.",
    examples=[
        [os.path.join(os.path.dirname(__file__), "Images\Examples\example3.png")],
        [os.path.join(os.path.dirname(__file__), "Images\Examples\example5.png")],
        [os.path.join(os.path.dirname(__file__), "Images\Examples\example6.png")],
    ],
    cache_examples=True,
)

if __name__ == "__main__":
    demo.launch()