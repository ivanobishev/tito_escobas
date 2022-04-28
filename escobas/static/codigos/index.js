function inicio()
{
    var boton_prev = document.querySelector(".prev");
    var boton_next = document.querySelector(".next");
    var posicion = 0;
    var foto_actual = document.querySelector("#diapositiva img");
    var url_fotos = [
        "https://i.imgur.com/myQhkxV.jpeg", 
        "https://i.imgur.com/IK9aAXo.jpg"
    ];

    boton_prev.addEventListener("click", function(){
        if(posicion == 0) { return 0 ;}
        posicion--;
        foto_actual.setAttribute("src", url_fotos[posicion]);
        boton_next.style.color = "black";
        if(posicion == 0)
        { 
            boton_prev.style.color = "#bfbfbf";
        }
    }, false);

    boton_next.addEventListener("click", function(){
        if(posicion == url_fotos.length - 1) { return 0 ; }
        posicion++;
        foto_actual.setAttribute("src", url_fotos[posicion]);
        boton_prev.style.color = "black";
        if(posicion == url_fotos.length - 1)
        { 
            boton_next.style.color = "#bfbfbf";
        }
    }, false);
}
window.onload = inicio;
