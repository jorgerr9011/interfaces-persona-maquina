import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:mobile/controller/controller.dart';
import 'dart:async';

import '../controller/controller.dart';

class Model {
  static String IP = "192.168.1.43";

  static Future<bool> existIdFacility(String id_facility) async {
    var url =
        Uri.parse("http://" + IP + ":8080/api/rest/facilities/" + id_facility);
    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },
    );

    var decodedJson = json.decode(response.body);

    List<dynamic> facilities = decodedJson["facilities"];

    if (facilities.isEmpty) {
      return false;
    } else {
      return true;
    }
  }

  static Future<bool> findDataUser(String name, String surname) async {
    var url = Uri.parse(
        "http://" + IP + ":8080/api/rest/user?name="+name+ "&surname=" + surname);
    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },
    );

    var decodedJson = json.decode(response.body);
    var users = decodedJson["users"];
    if(users.toString() == "[]"){

      return false;
    }

    Controller.uuid = users[0]["uuid"];
    Controller.name = users[0]["name"];
    Controller.surname = users[0]["surname"];
    return true;
  }

  static Future<void> postDataUser() async {
    if (Controller.type == "IN") {
      await Model.postDataUsertoFacility();
    } else {
      var url = Uri.parse(
          "http://" + IP + ":8080/api/rest/user_access_log/" + Controller.uuid);
      var response = await http.get(
        url,
        headers: {
          "x-hasura-admin-secret": "myadminsecretkey",
        },
      );

      var decodedJson = json.decode(response.body);
      var access_log = decodedJson["access_log"];

      for (var element in access_log) {
        //Los registros se guardan por orden por eso funciona esto
        Controller.temperature = element["temperature"];
      }

      await Model.postDataUsertoFacility();
    }
  }

  static Future<void> postDataUsertoFacility() async {
    var data = {
      "user_id": Controller.uuid,
      "facility_id": Controller.id_facility,
      "timestamp": Controller.date +
          "T" +
          Controller.time +
          "+00:00", // "timestamp": "2021-10-14T18:58:00+00:00",
      "type": Controller.type,
      "temperature": Controller.temperature
    };

    var url = Uri.parse("http://" + IP + ":8080/api/rest/access_log");
    var response = await http.post(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },
      body: json.encode(data),
    );
  }

  static Future<void> getNumVisitors() async {
    Map<String, int> map = {};
    int numVisitantes = 0;
    int totalVisitors = 0;

    var url = Uri.parse("http://" +
        IP +
        ":8080/api/rest/facility_access_log/" +
        Controller.id_facility);
    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },
    );

    var decodedJson = json.decode(response.body);
    var acces_log = decodedJson["access_log"];

    for (int i = 0; i < acces_log.length; i++) {
      if (!map.containsKey(decodedJson["access_log"][i]["user"]["uuid"])) {
        totalVisitors += 1;
        map[decodedJson["access_log"][i]["user"]["uuid"]] = 1;
      } else {
        map.update(
            decodedJson["access_log"][i]["user"]["uuid"], (value) => value + 1);
      }
    }

    for (var values in map.values) {
      if (values % 2 != 0) {
        numVisitantes += 1;
      }
    }

    Controller.actualVisitors = numVisitantes.toString();
    Controller.totalVisitors = totalVisitors.toString();
  }



  static Future<void> getListUsersFacility() async {

    List<String> listaUsers = [];
    List<String> startDate = Controller.infoStartDate.split(" ");
    List<String> endDate = Controller.infoEndDate.split(" ");

    var url = Uri.parse(
        "http://"+IP+":8080/api/rest/facility_access_log/"+Controller.id_facility+"/daterange?offset=0");
    var dates = {
      'startdate': startDate[0]+"T"+startDate[1]+":00+00:000",
      'enddate': endDate[0]+"T"+endDate[1]+":00+00:000"
    };
    var request = http.Request("GET", url);
    request.body = json.encode(dates);
    request.headers.addAll({"x-hasura-admin-secret": "myadminsecretkey"});
    var client = http.Client();
    var streamedResponse = await client.send(request);
    var dataAsString = await streamedResponse.stream.bytesToString();
    client.close();
    var data = json.decode(dataAsString) ;
    List<dynamic> lista = data["access_log"];

    for(var element in lista){
      listaUsers.add(element["user"]["name"].toString()+" "+element["user"]["surname"].toString()+" "+element["user"]["uuid"].toString());
    }
    var distinct = listaUsers.toSet().toList();
    Controller.listaUsers = distinct;
  }
}
