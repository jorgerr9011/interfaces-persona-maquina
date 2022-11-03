import 'package:flutter_time_picker_spinner/flutter_time_picker_spinner.dart';
import 'package:flutter/material.dart';
import 'package:mobile/controller/controller.dart';

import '../TraduccionesAppLocalizations.dart';

class Time extends StatefulWidget {
  const Time({Key? key}) : super(key: key);

  @override
  State<Time> createState() => _TimeState();
}

class _TimeState extends State<Time> {
  List<String> lista = [];

  Widget clock() {
    return TimePickerSpinner(
      is24HourMode: false,
      normalTextStyle: const TextStyle(
        fontSize: 24,
      ),
      highlightedTextStyle: const TextStyle(
        fontSize: 24,
      ),
      spacing: 50,
      itemHeight: 80,
      isForce2Digits: true,
      onTimeChange: (time) {
        setState(() {
          lista = time.toString().split(" ");
          Controller.time = lista[1].replaceAll(".000", "");
        });
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      appBar: AppBar(
        title:  Text(localizations!.setTime),
        centerTitle: true,
        backgroundColor: Colors.blueAccent,
      ),
      body: Center(
        child: clock(),
      ),
    );
  }
}
