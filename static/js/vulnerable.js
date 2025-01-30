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
    .then(data => {console.log(data)})
    .catch(error => console.error('Error:', error));
    document.addEventListener('DOMContentLoaded', () => {
        const boton = document.querySelector('#boton');
        const id = 1; // Define el id antes de agregar el listener al botón
        
        boton.addEventListener('click', () => eliminarUsuario(id)); 
        
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
    });
    