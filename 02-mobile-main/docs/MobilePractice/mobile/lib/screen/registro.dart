import 'dart:ffi';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:mobile/controller/controller.dart';
import 'package:mobile/screen/time.dart';
import '../TraduccionesAppLocalizations.dart';
import 'home.dart';

class Registro extends StatefulWidget {
  const Registro({Key? key}) : super(key: key);

  @override
  State<Registro> createState() => _RegistroState();
}

class _RegistroState extends State<Registro> {
  bool buttonDisabled = true;
  bool flag = (Controller.type == "IN");
  String qrCode = 'Unknown';
  final List<bool> isSelected = [true, false];
  final TextEditingController _inputController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      appBar: AppBar(
        title:  Text(localizations!.register),
        centerTitle: true,
        backgroundColor: Colors.blueAccent,
      ),
      body: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Row(
              children: <Widget>[
                 Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 25, 0, 0),
                  child: Text(
                    localizations.name + ':',
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(15.0, 25, 0, 0),
                  child: Text(
                    Controller.name,
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      fontSize: 20,
                    ),
                  ),
                ),
              ],
            ),
            Row(
              children: <Widget>[
                 Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 50, 0, 0),
                  child: Text(
                    localizations.surname + ': ',
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(15.0, 50, 0, 0),
                  child: Text(
                    Controller.surname,
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      fontSize: 20,
                    ),
                  ),
                ),
              ],
            ),
            Row(
              children: <Widget>[
                 Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 50, 0, 0),
                  child: Text(
                    localizations.uuid + ': ',
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Flexible(
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(15, 50, 0, 0),
                    child: Text(
                      Controller.uuid,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        fontSize: 20,
                      ),
                    ),
                  ),
                ),
              ],
            ),
            Row(
              children: <Widget>[
                 Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 50, 0, 0),
                  child: Text(
                    localizations.temperature + ': ',
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(15.0, 50, 0, 0),
                  child: SizedBox(
                    height: 40,
                    width: 35,
                    child: TextField(
                      enabled: flag,
                      controller: _inputController,
                    ),
                  ),
                ),
              ],
            ),
            Row(
              children: <Widget>[
                 Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 50, 0, 0),
                  child: Text(
                    localizations.date + ': ',
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(15.0, 50, 0, 0),
                  child: Text(
                    Controller.date,
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      fontSize: 20,
                    ),
                  ),
                ),
                 Padding(
                  padding: EdgeInsets.fromLTRB(15.0, 50, 0, 0),
                  child: Text(
                    localizations.time + ": ",
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(15.0, 50, 0, 0),
                  child: ElevatedButton(
                    child: const Icon(
                      Icons.access_time_outlined,
                    ),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => const Time()),
                      );
                    },
                  ),
                ),
              ],
            ),
            Row(
              children: <Widget>[
                 Padding(
                  padding: EdgeInsets.fromLTRB(15.0, 50, 0, 100),
                  child: Text(
                    localizations.in_out + ':',
                    textAlign: TextAlign.center,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.fromLTRB(15.0, 50, 0, 100),
                  child: ToggleButtons(
                    children: const <Widget>[
                      Text('IN'),
                      Text('OUT'),
                    ],
                    onPressed: (int index) {
                      setState(() {
                        isSelected[index] = !isSelected[index];
                        isSelected[(index + 1) % 2] =
                        !isSelected[(index + 1) % 2];
                        if (isSelected[index] == true && index == 0) {
                          flag = true;
                          Controller.type = "IN";
                        } else {
                          flag = false;
                          Controller.type = "OUT";
                        }
                      });
                    },
                    isSelected: isSelected,
                  ),
                ),
              ],
            ),
            Padding(
              padding: const EdgeInsets.symmetric(),
              child: ElevatedButton(
                onPressed: () {
                  saveInfo();
                },
                child: const Icon(Icons.save_alt),
                style: ElevatedButton.styleFrom(
                  onSurface: Colors.blueAccent,
                  minimumSize: const Size(150, 75),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  saveInfo() async {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);

    if(localizations!.localeName == 'en' && _inputController.text != ""){
      double aux = double.parse(_inputController.text);
      aux = (aux - 32) * 5 / 9;
      Controller.temperature = aux.toStringAsFixed(1).toString();
    }else{
      Controller.temperature = _inputController.text;
    }

    try {
      if (Controller.type == "IN") {
        if (Controller.temperature != "" && Controller.temperature != " ") {
          await Controller.postDataUser();
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => Home()),
          );
        } else {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text(localizations.temperature_empty)),
          );
        }
      } else if (Controller.type == "OUT") {
        await Controller.postDataUser();
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => Home()),
        );
      }
    }on Exception catch (_, e){
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(localizations.errorBD)),
      );
    }
  }
}