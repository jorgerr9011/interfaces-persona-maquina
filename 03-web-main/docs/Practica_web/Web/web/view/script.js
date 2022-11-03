var listaFacilities = {};


  var login = function(){
    var formData = new FormData();

    var aux = 0;

    if( document.getElementById("user").value != ""){
      formData.append('username', document.getElementById("user").value);
    }else{
      aux++;
    }

    if(document.getElementById("password").value != ""){
      formData.append('password',document.getElementById("password").value);
    }else{
      aux++;
    }

    if(aux!=0){
      alert("Todos los campos son obligatorios");
    }else{
      fetch('http://localhost:5000/login', {
        method: 'POST',
        body: formData
        }).then(response =>{
          if(response.status == 401){
            alert("No se ha introducido correctamente el usuario o la contraseña");
          }else if(response.status == 500){
            alert("Error de conexion con el servidor.");
          }
          return response.json();
        }).then(
          response => {
            response["access_log"].forEach(element => obtenerFacilityNames(element));
  
            // Create items array
            var items = Object.keys(listaFacilities).map(function(key) {
              return [key, listaFacilities[key]];
            });
  
            // Sort the array based on the second element
            items.sort(function(first, second) {
              return second[1] - first[1];
            });
  
            // Create a new array with only the first 5 items
            var arrayFacilities = items.slice(0, 5)
  
            localStorage.setItem("name", response["datos"]["name"]);
            localStorage.setItem("surname", response["datos"]["surname"]);
            localStorage.setItem("email", response["datos"]["email"]);
            localStorage.setItem("phone", response["datos"]["phone"]);
            localStorage.setItem("is_vaccinated", response["datos"]["is_vaccinated"]);
            localStorage.setItem("uuid", response["datos"]["uuid"]);
  
            if(arrayFacilities[0]!=null){
              localStorage.setItem("instalacion0", arrayFacilities[0]);
            }else{
              localStorage.setItem("instalacion0", "");
            }
  
            if(arrayFacilities[1]!=null){
              localStorage.setItem("instalacion1", arrayFacilities[1]);
            }else{
              localStorage.setItem("instalacion1", "");
            }
  
            if(arrayFacilities[2]!=null){
              localStorage.setItem("instalacion2", arrayFacilities[2]);
            }else{
              localStorage.setItem("instalacion2", "");
            }
  
            if(arrayFacilities[3]!=null){
              localStorage.setItem("instalacion3", arrayFacilities[3]);
            }else{
              localStorage.setItem("instalacion3", "");
            }
  
            if(arrayFacilities[4]!=null){
              localStorage.setItem("instalacion4", arrayFacilities[4]);
            }else{
              localStorage.setItem("instalacion4", "");
            }
            
            window.location.href = "http://localhost:5000/datos.html";
          }
        )
    }
  }

  var obtenerFacilityNames = function(element){
    lista = element.split(":");
    facilityName = lista[1];
    facilityName = facilityName.slice(2, -2);

    if(facilityName in listaFacilities){
        listaFacilities[facilityName] += 1;
    }else{
        listaFacilities[facilityName] = 1;
    }
  }

  var mostrarDatos = function(){
    document.getElementById('data_name').innerHTML = localStorage.getItem("name");
    document.getElementById('data_surname').innerHTML = localStorage.getItem("surname");
    document.getElementById('data_email').innerHTML = localStorage.getItem("email");
    document.getElementById('data_phone').innerHTML = localStorage.getItem("phone");

    if(localStorage.getItem("is_vaccinated") == "true"){
      document.getElementById('data_vaccinated').innerHTML = " Si";
    }else{
      document.getElementById('data_vaccinated').innerHTML = " No";
    }
    document.getElementById('data_UUID').innerHTML = localStorage.getItem("uuid");

    document.getElementById('data_instalacion0').innerHTML = localStorage.getItem("instalacion0");
    document.getElementById('data_instalacion1').innerHTML = localStorage.getItem("instalacion1");
    document.getElementById('data_instalacion2').innerHTML = localStorage.getItem("instalacion2");
    document.getElementById('data_instalacion3').innerHTML = localStorage.getItem("instalacion3");
    document.getElementById('data_instalacion4').innerHTML = localStorage.getItem("instalacion4");

    llamarqr();

  }

  var llamarqr = function(){
  
    new QRious({
      element: document.querySelector("#codigo"),
      value: localStorage.getItem("name") + ", " + localStorage.getItem("surname") + ", " + localStorage.getItem("uuid") , // La URL o el texto
     });
              
  }

  var register = function(){
    
    var formData = new FormData();
    var aux = 0;

    if(document.getElementById("name").value != ""){
      formData.append('name', document.getElementById("name").value);
    }else{
      aux++;
    }

    if(document.getElementById("apellido").value != ""){
      formData.append('surname', document.getElementById("apellido").value);
    }else{
      aux++;
    }

    if(document.getElementById("usuario").value != ""){
      formData.append('user', document.getElementById("usuario").value);
    }else{
      aux++;
    }

    if(document.getElementById("password").value != ""){
      formData.append('password', document.getElementById("password").value);
    }else{
      aux++;
    }

    if(document.getElementById("telefono").value != ""){
      formData.append('phone', document.getElementById("telefono").value);
    }else{
      aux++;
    }

    if(document.getElementById("email").value != ""){
      formData.append('email', document.getElementById("email").value);
    }else{
      aux++;
    }

    if (document.getElementById("vacunado").value=='Sí')
      formData.append('vacunado', 'true');
    else
      formData.append('vacunado', 'false');

      if(aux!=0){
        alert("Todos los campos son obligatorios");
      }else{
        fetch('http://localhost:5000/register', {
          method: 'POST',
          body: formData
          }).then(response =>{
            if(response.status == 401){
              alert("El usuario ya existe");
            }else if(response.status == 500){
              alert("Error de conexion con el servidor.");
            }
            return response.json();
          }).then(
            response => {
              console.log(response);
              window.location.href = "http://localhost:5000/index.html";
            }
          )
      }
  }



  