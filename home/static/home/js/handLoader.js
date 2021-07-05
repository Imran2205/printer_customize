if ( ! Detector.webgl ) Detector.addGetWebGLMessage();

var camera, scene, renderer;
var WIDTH = window.HEIGHT/2.2;
var HEIGHT = window.WIDTH/2.2;

init();

function init() {

    scene = new THREE.Scene();
    scene.add( new THREE.AmbientLight( 0xFFFFFF ) );
    scene.background = new THREE.Color( 0x72645b );

    camera = new THREE.PerspectiveCamera( 35, WIDTH / HEIGHT, 1, 500 );

    // Z is up for objects intended to be 3D printed.

    camera.up.set( 0, 0, 1 );
    camera.position.set( 0, -9, 6 );

    camera.add( new THREE.PointLight( 0xffffff, 0.8 ) );

    scene.add( camera );

    let grid = new THREE.GridHelper( 25, 50, 0xffffff, 0x555555 );
    grid.rotateOnAxis( new THREE.Vector3( 1, 0, 0 ), 90 * ( Math.PI/180 ) );
    scene.add( grid );

    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setClearColor( 0x999999 );
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( WIDTH, HEIGHT );
    document.getElementById("3d_viewer").appendChild( renderer.domElement );

    let loader = new THREE.STLLoader();


    // Binary files

    let material = new THREE.MeshPhongMaterial( { color: 0xAABB55, specular: 0x111111, shininess: 200 } );
    loader.load( '{% static "home/models/model.stl" %}', function ( geometry ) {
        let mesh = new THREE.Mesh( geometry, material );

        mesh.position.set( 0, 0, 0 );
        mesh.rotation.set( 0, 0, 0 );
        mesh.scale.set( .02, .02, .02 );
        mesh.rotateX(-90 * ( Math.PI/180 ) );
        mesh.rotateY(0);
        mesh.rotateZ(0);

        mesh.castShadow = true;
        mesh.receiveShadow = true;


        scene.add( mesh );
        render();
    });

    var controls = new THREE.OrbitControls( camera, renderer.domElement );
    controls.addEventListener( 'change', render );
    controls.target.set( 0, 1.2, 2 );
    controls.update();
    window.addEventListener( 'resize', onWindowResize, false );

}

function onWindowResize() {

    camera.aspect = WIDTH / HEIGHT;
    camera.updateProjectionMatrix();

    renderer.setSize( WIDTH, HEIGHT );

    render();

}

function render() {
    renderer.render( scene, camera );
}