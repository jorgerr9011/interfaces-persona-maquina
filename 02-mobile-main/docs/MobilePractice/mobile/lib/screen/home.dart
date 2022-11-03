import 'package:flutter/material.dart';
import 'package:mobile/TraduccionesAppLocalizations.dart';
import 'data_entry.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/services.dart';
import 'package:mobile/controller/controller.dart';

import 'info.dart';

class Home extends StatefulWidget {
  Home({Key? key}) : super(key: key);

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final TextEditingController _inputController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      appBar: AppBar(
        title:  Text(
          localizations!.appName,
        ),
        centerTitle: true,
        backgroundColor: Colors.blueAccent,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(100, 175, 100, 100),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              SizedBox(
                height: 100,
                width: 200,
                child: TextFormField(
                  controller: _inputController,
                  decoration:  InputDecoration(
                      icon: Icon(Icons.home), labelText: localizations.hintID),
                ),
              ),
              ValueListenableBuilder<TextEditingValue>(
                valueListenable: _inputController,
                builder: (context, value, child) {
                  return ElevatedButton(
                    child:  Text(localizations.register),
                    style: ElevatedButton.styleFrom(
                      onSurface: Colors.blueAccent,
                      minimumSize: const Size(200, 75),
                    ),
                    onPressed: value.text.isNotEmpty
                        ? () => navigatorToDataEntry()
                        : null,
                  );
                },
              ),
              const SizedBox(height: 60.0),
              ValueListenableBuilder<TextEditingValue>(
                valueListenable: _inputController,
                builder: (context, value, child) {
                  return ElevatedButton(
                    onPressed:
                        value.text.isNotEmpty ? () => navigatorToInfo() : null,
                    child:  Text(localizations.info),
                    style: ElevatedButton.styleFrom(
                      onSurface: Colors.blueAccent,
                      minimumSize: const Size(200, 75),
                    ),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  navigatorToDataEntry() async {
    Controller.id_facility = _inputController.text.trim();
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    try{
      if (await Controller.existIdFacility(Controller.id_facility)) {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const DataEntry()),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(localizations!.facilityID_notFound)),
        );
      }
    }on Exception catch (_, e){
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(localizations!.errorBD)),
      );
    }

  }

  navigatorToInfo() async {
    Controller.id_facility = _inputController.text.trim();
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    try{
      if (await Controller.existIdFacility(Controller.id_facility)) {
        await Controller.getNumVisitors();
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const Info()),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(localizations!.facilityID_notFound)),
        );
      }
    }on Exception catch (_, e){
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(localizations!.errorBD)),
        );
    }
  }
}
