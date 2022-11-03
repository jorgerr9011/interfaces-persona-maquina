import 'package:flutter/cupertino.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

import 'package:yaml/yaml.dart';

class TraduccionesAppLocalizations {
  final String localeName;
  YamlMap? translations;

  TraduccionesAppLocalizations(this.localeName);

  static const LocalizationsDelegate<TraduccionesAppLocalizations> delegate =
      _TraduccionesAppLocalizations();

  Future load() async {
    String yamlString = await rootBundle.loadString('lang/${localeName}.yaml');
    translations = loadYaml(yamlString);
  }

  String get errorBD {
    return translations!['home']['errorBD'];
  }

  String get appName {
    return translations!['home']['appName'];
  }

  String get hintID {
    return translations!['home']['hintID'];
  }

  String get register {
    return translations!['home']['register'];
  }

  String get info {
    return translations!['home']['info'];
  }

  String get facilityID_notFound {
    return translations!['home']['facilityID_notFound'];
  }

  String get name {
    return translations!['registro']['name'];
  }

  String get surname {
    return translations!['registro']['surname'];
  }

  String get uuid {
    return translations!['registro']['uuid'];
  }

  String get temperature {
    return translations!['registro']['temperature'];
  }

  String get date {
    return translations!['registro']['date'];
  }

  String get time {
    return translations!['registro']['time'];
  }

  String get in_out {
    return translations!['registro']['in_out'];
  }
  String get temperature_empty {
    return translations!['registro']['temperature_empty'];
  }

  String get qr {
    return translations!['data_entry']['qr'];
  }

  String get scan {
    return translations!['data_entry']['scan'];
  }

  String get name_surname_hint {
    return translations!['data_entry']['name_surname_hint'];
  }

  String get userNotFound {
    return translations!['data_entry']['userNotFound'];
  }

  String get startDateTime {
    return translations!['info']['startDateTime'];
  }

  String get endDateTime {
    return translations!['info']['endDateTime'];
  }
  String get infoBar {
    return translations!['info']['infoBar'];
  }
  String get currentVisitors {
    return translations!['info']['currentVisitors'];
  }
  String get totalVisitors {
    return translations!['info']['totalVisitors'];
  }
  String get datesNotEntered {
    return translations!['info']['datesNotEntered'];
  }

  String get setTime {
    return translations!['time']['setTime'];
  }

  String get usersList {
    return translations!['users_list']['usersList'];
  }

}

class _TraduccionesAppLocalizations
    extends LocalizationsDelegate<TraduccionesAppLocalizations> {
  const _TraduccionesAppLocalizations();

  @override
  bool isSupported(Locale locale) {
    return ['es', 'en'].contains(locale.languageCode);
  }

  @override
  bool shouldReload(LocalizationsDelegate<TraduccionesAppLocalizations> old) {
    return false;
  }

  @override
  Future<TraduccionesAppLocalizations> load(Locale locale) async {
    var t = TraduccionesAppLocalizations(locale.languageCode);
    await t.load();
    return t;
  }
}
