userAction();

function userAction() {
  var params = new URLSearchParams(window.location.search);
  var name_user = params.get("name_user");
  var surname_user = params.get("surname_user");
  var pass_user = params.get("pass_user");
  if (name_user != null && surname_user != null) {
    buscarUsuario(name_user, surname_user);

    return;
  }
}

document
  .querySelector("button#inicio_sesion")
  .addEventListener("click", (event) =>  {
    var name_user = document.querySelector("input#name_user").value;
    var surname_user = document.querySelector("input#surname_user").value;
    var isFirst = true;
    var resultURL = "";
    if (name_user != "") {
      if (isFirst) {
        resultURL = resultURL + "?";
        isFirst = false;
      } else {
        resultURL = resultURL + "&";
      }
      resultURL = resultURL + "name_user=" + name_user;
    }
    if (surname_user != null) {
      if (isFirst) {
        resultURL = resultURL + "?";
        isFirst = false;
      } else {
        resultURL = resultURL + "&";
      }
      resultURL = resultURL + "surname_user=" + surname_user;
    }
    window.location.href = resultURL;
  });

function buscarUsuario(name, surname) {
  fetch(`http://localhost:8080/api/rest/user?name=${name}&surname=${surname}`, {
    method: "get",
    headers: {
      "x-hasura-admin-secret": "myadminsecretkey",
    },
  })
    .then((response) => {
      switch (response.status) {
        case 200:
          response.json().then((user) => showUser(user));
          break;
        case 404:
          console.log("not found error");
          throw Error("not found");
        case 500:
          console.log("server error");
          throw Error("server");
        default:
          console.log("network error");
          throw Error("network");
      }
    })
    .catch((error) => {
      console.log("Error: " + error.message);
      switch (error.message) {
        case "not found":
          document.getElementById("error_busqueda_simple").style.display =
            "block";
          break;
        case "server":
        case "network":
        default:
          document.getElementById("error_red").style.display = "block";
          break;
      }
    });
}


function showUser(user) {
  //userName = user.users[0].name;
  var userName = "";
  userUuid = user.users[0].uuid;
  userSurname = user.users[0].surname;
  userEmail = user.users[0].email;
  userIsVaccinated = user.users[0].is_vaccinated;
  userUsername = user.users[0].username;
  sessionStorage.setItem(userName, user.users[0].name);
  //userSurname, userUuid, userEmail, userIsVaccinated, userUsername);
  console.log(sessionStorage.getItem(userName));
  //var name = document.getElementById('user_data').getElementsByTagName("p")[0];
  //name.textContent = "Nombre: " + userName;
  location.replace("./datos.html", user);
  /*var surname = document.getElementById("user_data").getElementsByTagName("p")[1];
  var login = document.getElementById("user_data").getElementsByTagName("p")[2];
  var email = document.getElementById("user_data").getElementsByTagName("p")[3];
  var vaccinated = document .getElementById("user_data").getElementsByTagName("p")[4];*/
}
