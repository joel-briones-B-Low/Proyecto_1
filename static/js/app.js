document.addEventListener('DOMContentLoaded', () =>{

    // dom
    const inputUsuario = document.querySelector('#userName')
    const inputContra = document.querySelector('#userPass')
    const formulario = document.querySelector('#formLogin')

    const botonLogin = document.querySelector('#botonLogin')

    formulario.addEventListener('submit', peticion)

    function peticion(e){
        e.preventDefault()
        const usuario = inputUsuario.value
        const contrasenia = inputContra.value

        fetch('http://127.0.0.1:8080/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  // Especificamos que estamos enviando JSON
            },
            body: JSON.stringify({
                usuario: usuario,
                contrasenia: contrasenia
            })
        })
        .then(response => response.json())
        .then(data => {
                if(data.USUARIO){
                    window.location.href= '/vulnerable'
                }
        })
        .catch(error => {
            console.error('Error al realizar la petición:', error);
        });
    }

})