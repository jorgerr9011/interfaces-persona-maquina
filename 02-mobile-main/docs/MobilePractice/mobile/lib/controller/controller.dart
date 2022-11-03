import 'package:mobile/model/model.dart';
import 'package:intl/intl.dart';

class Controller {
  static String uuid = "";
  static String name = "";
  static String surname = "";
  static String temperature = " ";
  static String type = "IN";
  static String date = "";
  static String time = DateFormat.Hms().format(DateTime.now());
  static String id_facility = "";
  static String actualVisitors = " ";
  static String totalVisitors = " ";
  static String infoStartDate = " ";
  static String infoEndDate = " ";
  static List<String> listaUsers = [];

  static Future<bool> findDataUser(String name, String surname) async {
    return await Model.findDataUser(name.trim(), surname.trim());
  }

  static Future<void> postDataUser() async {
    await Model.postDataUser();
  }

  static Future<bool> existIdFacility(String id_facility) async {
    if (await Model.existIdFacility(id_facility)) {
      return true;
    } else {
      return false;
    }
  }

  static Future<void> getNumVisitors() async {
    await Model.getNumVisitors();
  }

  static Future<void> getListUsersFacility() async {
    await Model.getListUsersFacility();
  }

}
