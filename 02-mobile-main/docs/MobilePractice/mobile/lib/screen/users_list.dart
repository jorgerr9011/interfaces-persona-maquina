import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:mobile/controller/controller.dart';

import '../TraduccionesAppLocalizations.dart';

class UsersList extends StatefulWidget {
  UsersList({Key? key}) : super(key: key);

  @override
  State<UsersList> createState() => _UsersListState();
}

class _UsersListState extends State<UsersList> {

  @override
  Widget build(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      appBar: AppBar(
        title:  Text(localizations!.usersList),
        centerTitle: true,
        backgroundColor: Colors.blueAccent,
      ),
      body: SingleChildScrollView(
        child: Text(
          Controller.listaUsers.toString().replaceAll("[", "").replaceAll("]", "").replaceAll(",", "\n\n"),
        ),
      ),
    );
  }
}