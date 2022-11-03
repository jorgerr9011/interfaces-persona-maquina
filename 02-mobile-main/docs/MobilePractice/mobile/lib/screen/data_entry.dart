import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:mobile/controller/controller.dart';
import 'package:flutter_barcode_scanner/flutter_barcode_scanner.dart';
import 'package:mobile/screen/registro.dart';

import '../TraduccionesAppLocalizations.dart';

class DataEntry extends StatefulWidget {
  const DataEntry({Key? key}) : super(key: key);

  @override
  State<DataEntry> createState() => _DataEntryState();
}

class _DataEntryState extends State<DataEntry> {
  final TextEditingController _inputController = TextEditingController();

  bool buttonDisabled = true;
  String qrCode = 'Unknown';

  @override
  Widget build(BuildContext context) {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(context, TraduccionesAppLocalizations);
    return Scaffold(
      appBar: AppBar(
        title:  Text(localizations!.qr),
        centerTitle: true,
        backgroundColor: Colors.blueAccent,
      ),
      body: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            const SizedBox(height: 100),
            ElevatedButton(
              onPressed: () => scanQRCode(),
              child:  Text(localizations.scan),
              style: ElevatedButton.styleFrom(
                onSurface: Colors.blueAccent,
                minimumSize: const Size(300, 112.5),
              ),
            ),
            const SizedBox(height: 150.0),
            Row(
              children: [
                const SizedBox(width: 25.0),
                SizedBox(
                  height: 100,
                  width: 250,
                  child: TextFormField(
                    controller: _inputController,
                    decoration:  InputDecoration(
                        icon: Icon(Icons.person),
                        labelText: localizations.name_surname_hint),
                  ),
                ),
                const SizedBox(width: 30.0),
                ValueListenableBuilder<TextEditingValue>(
                  valueListenable: _inputController,
                  builder: (context, value, child) {
                    return ElevatedButton(
                      child: const Icon(
                        Icons.search,
                      ),
                      onPressed:
                          value.text.isNotEmpty ? () => metodoAux() : null,
                    );
                  },
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  metodoAux() async {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(
        context, TraduccionesAppLocalizations);
    List<String> listaNS;
    List<String> listaDate;

    var now = DateTime.now();
    String aux = now.toString();
    listaDate = aux.split(" ");
    Controller.date = listaDate[0];

    listaNS = _inputController.text.split(" ");

    try {
      if(await Controller.findDataUser(listaNS[0], listaNS[1]) == true){
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => Registro()),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(localizations!.userNotFound)),
        );
      }
    } on Exception catch (_, e) {
        ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(localizations!.errorBD)),
      );
    }
  }

  Future<void> scanQRCode() async {
    TraduccionesAppLocalizations? localizations =
    Localizations.of<TraduccionesAppLocalizations>(
        context, TraduccionesAppLocalizations);

    List<String> listaNS;
    List<String> listaDate;

    try {
      final qrCode = await FlutterBarcodeScanner.scanBarcode(
          '#ff6666', 'Cancel', false, ScanMode.QR);
      if (!mounted) return;

      setState(() {
        this.qrCode = qrCode;
      });
    } on PlatformException {
      qrCode = 'Failed';
    }

    final newValue =
        qrCode.replaceAll("{", "").replaceAll("}", "").replaceAll(",", "");
    listaNS = newValue.split(" ");

    var now = DateTime.now();
    String aux = now.toString();
    listaDate = aux.split(" ");
    Controller.date = listaDate[0];

    try{
      if(await Controller.findDataUser(listaNS[0], listaNS[1]) == true){
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => Registro()),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(localizations!.userNotFound)),
        );
      }
    }on Exception catch (_, e){
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(localizations!.errorBD)),
      );
    }
  }
}
