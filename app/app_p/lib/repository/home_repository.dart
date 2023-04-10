import 'dart:async';
import 'dart:convert';
import 'dart:ffi';
// import 'package:flutter_session/flutter_session.dart';
import 'package:app_p/repository/home_interface.dart';
import 'package:jwt_decoder/jwt_decoder.dart';
import 'package:meta/meta.dart';
import 'package:http/http.dart' as http;

import 'package:app_p/models/user_model.dart';
import 'package:app_p/api/api_model.dart';
import 'package:app_p/api/api_connection.dart';
import 'package:app_p/repository/user_interface.dart';

class HomeRepository implements IHomeRepository {
  HomeRepository();

  @override
  Future<void> loginUser(String username, String password) async {
    User user = User();
    user.username = username;
    user.password = password;

    await loginApi(user);
  }
}
