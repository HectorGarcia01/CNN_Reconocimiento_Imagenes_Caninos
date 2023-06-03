//Obtener la lista de elementos de la barra de navegación
const navItems = document.querySelectorAll('nav ul li');

//Agregar evento de clic a cada elemento de la lista
navItems.forEach(item => {
    item.addEventListener('click', () => {
        //Remover la clase "nav-active" de todos los elementos
        navItems.forEach(item => item.classList.remove('nav-active'));
        //Agregar la clase "nav-active" al elemento clicado
        item.classList.add('nav-active');
    });
});
