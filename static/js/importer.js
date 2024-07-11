import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

/**
 * Loads a GLTF object from the given path.
 * @param {string} path - The path to the GLTF file.
 * @returns {Promise<Object3D>} - A promise that resolves with the loaded GLTF object.
 */
export function loadGLTFObject(path) {
    return new Promise((resolve, reject) => {
        const loader = new GLTFLoader();

        loader.load(
            path,
            (gltf) => {
                resolve(gltf.scene);
            },
            // called while loading is progressing
            function ( xhr ) {
                console.log( Math.round( xhr.loaded / xhr.total * 100 ) + '% loaded' );
            },
            (error) => {
                reject(error);
            }
        );
    });
}

// // Usage example
// loadGLTFObject('/path/to/your/model.glb')
//     .then((gltfObject) => {
//         console.log('GLTF Object loaded:', gltfObject);
//         // Add the object to your scene here
//     })
//     .catch((error) => {
//         console.error('Error loading GLTF Object:', error);
//     });
