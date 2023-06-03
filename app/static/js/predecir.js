//Obtenemos los datos de cada predicción
const leon = document.getElementById('leon').textContent;
const gato = document.getElementById('gato').textContent;
const tigre = document.getElementById('tigre').textContent;
const pantera = document.getElementById('pantera').textContent;

//LLenamos el div de porcentaje según el porcentaje de prediccion
document.getElementById('nivel_leon').style.width = leon;
document.getElementById('nivel_gato').style.width = gato;
document.getElementById('nivel_tigre').style.width = tigre;
document.getElementById('nivel_pantera').style.width = pantera;

//Obtener referencia al botón de realizar predicción
const botonRealizarPrediccion = document.getElementById('btnPredecir');

//Agregar evento click al botón
botonRealizarPrediccion.addEventListener('click', function(event) {
    // Obtener referencia al campo de archivo
    const inputImagen = document.getElementById('imagen-input');

    //Verificar si no se ha seleccionado ninguna imagen
    if (!inputImagen.files || inputImagen.files.length === 0) {
    //Mostrar alerta con SweetAlert2
    Swal.fire({
        icon: 'error',
        title: 'Error',
        text: "Por favor seleccione una imagen.",
        showConfirmButton: false,
        timer: 2000,
        customClass: {
            popup: 'custom-popup-class',
            title: 'custom-title-class',
            content: 'custom-content-class'
        },
        width: '300px'
    });    

    //Detener el envío del formulario
    event.preventDefault();
    }
});