function inicio()
{
    var modal = document.getElementById("modal");
    var boton_mensaje = document.getElementById("boton_mensaje");
    var modal_cerrar = document.getElementById("modal_cerrar");

    boton_mensaje.addEventListener("click", function(){
        modal.style.display = "block";
    }, false);

    modal_cerrar.addEventListener("click", function(){
        modal.style.display = "none";
    }, false);

    window.addEventListener("click", function(){
        if(event.target == modal)
        {
            modal.style.display = "none";
        }
    }, false);

    //-----[Mensajes de error en el formulario]-----
    var formulario = document.querySelector("form");
    var boton_formulario = document.getElementById("enviar");

    boton_formulario.addEventListener("click", function(){
        var mensajes_error = document.querySelectorAll("span[class='fallo']");
        if(formulario["nombre"].value == "")
        {
            mensajes_error[0].innerHTML = "Rellenar";
            return false;
        }
        else
        {
            mensajes_error[0].innerHTML = "";
        }

        if(formulario["telefono"].value == "")
        {
            mensajes_error[1].innerHTML = "Rellenar con numeros";
            return false;
        }
        else
        {
            mensajes_error[1].innerHTML = "";
        }

        if(formulario["explicacion"].value == "")
        {
            mensajes_error[2].innerHTML = "Rellenar";
            return false;
        }
        else
        {
            mensajes_error[2].innerHTML = "";
        }

        formulario.submit();
    }, false);
}

window.onload = inicio;
