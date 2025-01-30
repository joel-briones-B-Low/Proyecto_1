document.addEventListener('DOMContentLoaded',()=>{
    fetch('http://localhost:8080/usuario/get', {
    method: 'GET', 
    headers: {
        'Content-Type': 'application/json',
    }
})
.then(response => {
    if (!response.ok) {
        throw new Error('Error en la respuesta del servidor');
    }
    return response.json(); 
})
.then(data => {
    console.log('Datos recibidos:', data); 
})
.catch(error => {
    console.error('Error al hacer la petición:', error);
});
})