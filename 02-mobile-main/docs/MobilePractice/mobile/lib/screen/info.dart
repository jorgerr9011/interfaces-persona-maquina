import 'package:date_time_picker/date_time_picker.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:mobile/controller/controller.dart';
import 'package:mobile/screen/users_list.dart';

import '../TraduccionesAppLocalizations.dart';

class Info extends StatefulWidget {
  const Info({Key? key}) : super(key: key);

  @override
  State<Info> createState() => _InfoState();
}

class RIKeys {
  static const riKey1 = Key('__RIKEY1__');
  static const riKey2 = Key('__RIKEY2__');
}

class _InfoState extends State<Info> {
  TextEditingController _controller = TextEditingController(text: " ");
  TextEditingController _controller1 = TextEditingController(text: " ");

  @override
  Widget initDate(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      body: SingleChildScrollView(
        padding: const EdgeInsets.only(left: 20, right: 20, top: 10),
        child: Form(
          key: RIKeys.riKey1,
          child: Column(
            children: [
              DateTimePicker(
                type: DateTimePickerType.dateTime,
                controller: _controller,
                firstDate: DateTime(2000),
                lastDate: DateTime(2100),
                locale: Locale(localizations!.localeName),
                dateLabelText: localizations.startDateTime,
                use24HourFormat: false,
                onChanged: (val) => setState(() {
                  Controller.infoStartDate = val;
                }),
                validator: (val) {
                  setState(() {});
                  return null;
                },
                onSaved: (val) => setState(() {}),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget endDate(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      body: SingleChildScrollView(
        padding: const EdgeInsets.only(left: 20, right: 20, top: 10),
        child: Form(
          key: RIKeys.riKey2,
          child: Column(
            children: [
              DateTimePicker(
                type: DateTimePickerType.dateTime,
                controller: _controller1,
                firstDate: DateTime(2000),
                lastDate: DateTime(2100),
                locale: Locale(localizations!.localeName),
                dateLabelText: localizations.endDateTime,
                use24HourFormat: false,
                onChanged: (val) => setState(() {
                  Controller.infoEndDate = val;
                }),
                validator: (val) {
                  setState(() {});
                  return null;
                },
                onSaved: (val) => setState(() {}),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      appBar: AppBar(
        title:  Text(localizations!.infoBar),
        centerTitle: true,
        backgroundColor: Colors.blueAccent,
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.only(left: 20, right: 20, top: 10),
        child: Column(
          children: <Widget>[
            const SizedBox(
              height: 50,
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(0.0, 0, 0, 0),
              child: Text(
                localizations.currentVisitors + ": " + Controller.actualVisitors,
                textAlign: TextAlign.center,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(0, 5, 0, 0),
              child: Text(
                localizations.totalVisitors + ": " + Controller.totalVisitors,
                textAlign: TextAlign.center,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            const SizedBox(
              height: 100,
            ),
            SizedBox(
              height: 75, // constrain height
              child: initDate(context),
            ),
            const SizedBox(
              height: 50,
            ),
            SizedBox(
              height: 75, // constrain height
              child: endDate(context),
            ),
            const SizedBox(
              height: 100,
            ),
            ElevatedButton(
              onPressed: () {navigatorToInfo();},
              child: Icon(Icons.search),
              style: ElevatedButton.styleFrom(
                onSurface: Colors.blueAccent,
                minimumSize: const Size(75, 75),
              ),
            ),
          ],
        ),
      ),
    );
  }

  navigatorToInfo() async {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    try{
      if (Controller.infoStartDate != " " && Controller.infoEndDate != " ") {
        await Controller.getListUsersFacility();
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => UsersList()),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(localizations!.datesNotEntered)),
        );
      }
    }on Exception catch (_, e){
        ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(localizations!.errorBD)),
      );
    }

  }
}
