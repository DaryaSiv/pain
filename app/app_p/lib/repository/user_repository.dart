import 'dart:async';
import 'dart:convert';
// import 'package:flutter_session/flutter_session.dart';
import 'package:jwt_decoder/jwt_decoder.dart';
import 'package:meta/meta.dart';
import 'package:http/http.dart' as http;

import 'package:app_p/models/user_model.dart';
import 'package:app_p/api/api_model.dart';
import 'package:app_p/api/api_connection.dart';
import 'package:app_p/repository/user_interface.dart';

class UserRepository implements IUserRepository {
  UserRepository();

  @override
  Future<List<User>> getAll() {
    // TODO: implement getAll
    throw UnimplementedError();
  }

  @override
  Future<void> delete(int id) {
    // TODO: implement delete
    throw UnimplementedError();
  }

  @override
  Future<User?> getOne(int id) {
    // TODO: implement getOne
    throw UnimplementedError();
  }

  @override
  Future<String> login(String username, String password) {
    // TODO: implement login
    throw UnimplementedError();
  }

  @override
  Future<bool> register(String email, String username, String password) {
    // TODO: implement register
    throw UnimplementedError();
  }

  @override
  Future<void> update(User user) {
    // TODO: implement update
    throw UnimplementedError();
  }

}
