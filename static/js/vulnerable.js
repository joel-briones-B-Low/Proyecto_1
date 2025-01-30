fetch('http://127.0.0.1:8080/consulta', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        url: 'http://localhost:8080/usuarios'
    })
})
    .then(response => response.json())
    .then(data => { console.log(data) })
    .catch(error => console.error('Error:', error));
document.addEventListener('DOMContentLoaded', () => {
    const boton = document.querySelector('#boton');
    const url = document.querySelector('#url');
    const id = 2; // Define el id antes de agregar el listener al botón

    boton.addEventListener('click', () => eliminarUsuario(id));
    url.addEventListener('click', () => leerurl());

    function eliminarUsuario(id) {
        fetch(`http://127.0.0.1:8080/usuario/eliminar/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                if (response.ok) {
                    console.log(`Usuario con ID ${id} eliminado correctamente`);
                } else {
                    console.error('Error al eliminar el usuario');
                }
            })
            .catch(error => console.error('Error:', error));
    }

    function leerurl() {
        fetch('http://127.0.0.1:8080/consulta/archivo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                url: '/usuarios'
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status_code === 200) {
                console.log('Contenido del archivo usuarios.js:', data.data);
            } else {
                console.error('Error:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));
        
    }
});
