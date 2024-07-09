import { GLTFExporter } from 'three/addons/exporters/GLTFExporter.js';

// ------------------------------------------------------------------
// Export Functions
// ------------------------------------------------------------------
export function exportGLTF( input, params) {

    const gltfExporter = new GLTFExporter();

    const options = {
        trs: params.trs,
        onlyVisible: params.onlyVisible,
        binary: params.binary,
        maxTextureSize: params.maxTextureSize
    };
    gltfExporter.parse(
        input,
        function ( result ) {

            if ( result instanceof ArrayBuffer ) {

                saveArrayBuffer( result, params.title + '.glb' );

            } else {

                const output = JSON.stringify( result, null, 2 );
                console.log( output );
                saveString( output, params.title + '.gltf' );
            }
        },
        function ( error ) {
            console.log( 'An error happened during parsing', error );
        },
        options
    );
    }

    const link = document.createElement( 'a' );
    link.style.display = 'none';
    document.body.appendChild( link ); // Firefox workaround, see #6594

    function save( blob, filename ) {

        link.href = URL.createObjectURL( blob );
        link.download = filename;
        link.click();
        // URL.revokeObjectURL( url ); breaks Firefox...
    }

    function saveString( text, filename ) {
        save( new Blob( [ text ], { type: 'text/plain' } ), filename );
    }


    function saveArrayBuffer( buffer, filename ) {
        save( new Blob( [ buffer ], { type: 'application/octet-stream' } ), filename );
    }