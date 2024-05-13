# Model 1: OpenLRM: Open-Source Large Reconstruction Models

Large Reconstruction Model (LRM) that predicts the 3D model of an object from a single input image within just **5 seconds**. In contrast to many previous methods that are trained on small-scale datasets such as ShapeNet in a category-specific fashion, LRM adopts a highly scalable transformer-based architecture with 500 million learnable parameters to directly predict a neural radiance field (NeRF) from the input image.  trained  model in an end-to-end manner on massive multi-view data containing around 1 million objects, including both synthetic renderings from Objaverse and real captures from MVImgNet. This combination of a high-capacity model and large-scale training data empowers model to be highly generalizable and produce high-quality 3D reconstructions from various testing inputs

## Architecture

- **Image encoder** : encodes the input image to patch-wise feature tokens
- I**mage-to triplane decode**r : projects image features onto triplane tokens via cross-attention

![Untitled](Model%201%20OpenLRM%20Open-Source%20Large%20Reconstruction%20M%20638bb01404df49f18c1f5bc049696f1d/Untitled.png)

## Datasets

LRM is trained on:

- **Objaverse**: Synthetic 3D assets, normalized and rendered from various views.
- **MVImgNet**: Real-world object videos, frames extracted and pre-processed.

For evaluation:

- Various datasets used, including Objaverse, MvImgNet, ImageNet, etc.
- 50 unseen 3D shapes and 50 unseen videos from Objaverse and MvImgNet, respectively, were randomly selected for analysis.

## Requirements

- Prepare RGBA images or RGB images with white background (with some background removal tools, e.g., [Rembg](https://github.com/danielgatis/rembg), [Clipdrop](https://clipdrop.co/)).
- The recommended PyTorch version is `>=2.1`. Code is developed and tested under PyTorch `2.1.2`.
- If you encounter CUDA OOM issues, please try to reduce the `frame_size` in the inference configs.
- You should be able to see `UserWarning: xFormers is available` if `xFormers` is actually working.

## Limitations

- Blurry textures for occluded regions due to deterministic nature of the model.
- Misalignment of fixed camera parameters during inference, causing distorted shape reconstruction.
- Limited to objects without background; unable to handle complex scenes.
- Assumes Lambertian objects, neglecting view-dependent appearance of materials like shiny metals, glossy ceramics, etc.

## **Model Input and Output**:

- Input:

![Untitled](Model%201%20OpenLRM%20Open-Source%20Large%20Reconstruction%20M%20638bb01404df49f18c1f5bc049696f1d/3060cb4a-8376-4a68-b01c-9fb8ab1e64d6.png)

- output :

[view?usp=sharing](https://drive.google.com/file/d/14SPugaXUnej0z3NriLr5J0zDsVLgYaZV/view?usp=sharing)

- Notebook:

[https://www.kaggle.com/code/olaadelhussien/openlrm](https://www.kaggle.com/code/olaadelhussien/openlrm)

## Conclusion

output  at the end not satisfied

## **Model Source**

[https://github.com/3DTopia/OpenLRM](https://github.com/3DTopia/OpenLRM)

# **Model 1 : TripoSR: Fast 3D Object Reconstruction from a Single Image**

TripoSR, a 3D reconstruction model leveraging transformer architecture for fast feed-forward 3D generation, producing 3D mesh from a single image in under **0.5 seconds.** Building upon the LRM network architecture, TripoSR integrates substantial improvements in data processing, model design, and training techniques. Evaluations on public datasets show that TripoSR exhibits superior performance, both quantitatively and qualitatively, compared to other open-source alternatives. Released under the MIT license, TripoSR is intended to empower researchers, developers, and creatives with the latest advancements in 3D generative AI.

## Dataset

[Objaverse](https://paperswithcode.com/dataset/objaverse)

## Evaluation

![Untitled](Model%201%20OpenLRM%20Open-Source%20Large%20Reconstruction%20M%20638bb01404df49f18c1f5bc049696f1d/Untitled%201.png)

There is big different between OpenLRM and TripoSR

## **Model Input and Output**:

output

[mesh (1).obj](https://drive.google.com/file/d/1XOhlbRN6UsngezEG_ynRZU_Ulx_ilFlf/view?usp=sharing)

Notebook:

[https://www.kaggle.com/code/olaadelhussien/triposr-model-2d](https://www.kaggle.com/code/olaadelhussien/triposr-model-2d)

## **Model Source**

 **[https://github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR)**

## Conclusion:

More efficient than LRM in results 

# **Model 3 : InstantMesh: Efficient 3D Mesh Generation from a Single Image with Sparse-view Large Reconstruction Models**

InstantMesh, a feed-forward framework for instant 3D mesh generation from a single image, featuring state-of-the-art generation quality and significant training scalability. By synergizing the strengths of an off-the-shelf multiview diffusion model and a sparse-view reconstruction model based on the LRM architecture, InstantMesh is able to create diverse 3D assets within 10 seconds. To enhance the training efficiency and exploit more geometric supervisions, e.g, depths and normals, we integrate a differentiable iso-surface extraction module into our framework and directly optimize on the mesh representation. Experimental results on public datasets demonstrate that InstantMesh significantly outperforms other latest image-to-3D baselines, both qualitatively and quantitatively.

## Architecture

![Untitled](Model%201%20OpenLRM%20Open-Source%20Large%20Reconstruction%20M%20638bb01404df49f18c1f5bc049696f1d/Untitled%202.png)

## **Model Input and Output**:

output

![Untitled](Model%201%20OpenLRM%20Open-Source%20Large%20Reconstruction%20M%20638bb01404df49f18c1f5bc049696f1d/Untitled%203.png)

ObJ:

[tmpfk__n428.obj](https://drive.google.com/file/d/1MOyA5rGjFl5spbM8lr4sjQesjk7r7AVL/view?usp=sharing)

Notebook:

[https://colab.research.google.com/drive/1zMQhc_aOw_pAhvfvOp6VRfureog_wfYp?usp=sharing](https://colab.research.google.com/drive/1zMQhc_aOw_pAhvfvOp6VRfureog_wfYp?usp=sharing)

## **Model Source**

[https://github.com/TencentARC/InstantMesh](https://github.com/TencentARC/InstantMesh)

Limitations:

1. **Resolution Bottleneck**:
    - The 64x64 resolution of the triplane decoder may limit high-definition 3D modeling.
2. **Multi-view Inconsistency**:
    - Diffusion model's multi-view inconsistency affects the quality of 3D generation.
3. **FlexiCubes Effectiveness**:
    - FlexiCubes, while improving mesh smoothness, are less effective for modeling tiny and thin structures compared to NeRF.

## Conclusion:

More efficient than LRM and TRipoSR in final results