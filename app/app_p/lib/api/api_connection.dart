import 'dart:async';
import 'dart:convert';

import 'package:app_p/models/user_model.dart';
import 'package:http/http.dart' as http;
import 'package:app_p/widgets/login.dart';
import 'package:app_p/models/book/books.dart';
import 'package:app_p/models/book/author.dart';
import 'package:app_p/models/book/genre.dart';
import 'package:app_p/models/book/press.dart';
import 'package:app_p/models/book/language.dart';
import '../services/storage_service.dart';
import 'package:app_p/api/api_model.dart';

final _base = "http://192.168.198.233:8000";
final _signInURL = "/myapp/api/token/";
final _sessionEndpoint = "/api/token/refresh/";
final _registrationEndpoint = "/api/registration/";

final _login = _base + _signInURL;
final _registration = _base + _registrationEndpoint;

Future<void> loginApi(User user) async {
  print("fgf[gdfgrefdswscv ggggggggg: ${user.toJson(user)}");
  final http.Response response = await http.post(
    Uri.parse(_login),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(user.toJson(user)),
  );

  if (response.statusCode == 200) {
    Token token = Token.fromJson(json.decode(response.body));
    SecureStorage storage = SecureStorage();
    storage.addTokenToDb(token.token, token.refreshToken);
  } else {
    throw Exception(json.decode(response.body));
  }
}

Future<List> registrationApi(UserRegistration userRegistration) async {
  final http.Response response = await http.post(
    Uri.parse(_registration),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(userRegistration.toDatabaseJson()),
  );
  List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
  return result;
}

Future<List<dynamic>> booksApi() async {
  var asd = await SecureStorage().getUsername();
  String url = 'http://192.168.254.88:8000/api/books/';
  if (asd != null) {
    url = url + '?username=' + asd;
    print('wvgwrew');
  }
  http.Response response = await http.get(
    Uri.parse(url),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
  );

  List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
  return result;
}
