import 'dart:convert';
import 'dart:io';
import 'package:app_p/repository/home_repository.dart';
import 'package:app_p/services/storage_service.dart';
import 'package:app_p/api/api_model.dart';
import 'package:app_p/api/api_connection.dart';
import 'package:app_p/models/user_model.dart';
import 'package:app_p/models/book/books.dart';
import 'package:app_p/models/book/author.dart';
import 'package:app_p/models/book/genre.dart';
import 'package:app_p/models/book/press.dart';
import 'package:app_p/models/book/language.dart';
import 'package:app_p/repository/user_repository.dart';
import 'package:flutter/material.dart';

class HomeController {
  HomeRepository homeRepository = HomeRepository();
  Future<void> loginUser(String username, String password) async {
    await homeRepository.loginUser(username, password);

    SecureStorage storage = SecureStorage();
    storage.addUsernameToDb(username);
  }

  Future<String> registerUser(
      String username, String email, String password) async {
    UserRegistration userRegistration =
        UserRegistration(username: username, email: email, password: password);
    dynamic result = await registrationApi(userRegistration);
    String reply = '';
    if (result[0] == 'YES') {
      loginUser(username, password);
    }
    result.forEach((element) {
      reply = reply + '${element}\n';
    });
    return reply;
  }

  Future<List<Books>> getBooks() async {
    List<Books> allBooks = [];
    print(allBooks);
    // List<dynamic> result = await booksApi();
    List<dynamic> result = [];
    print('evabwbw ${result}');
    result.forEach((element) {
      allBooks.add(Books(
          name: element['name'],
          genre: element['genre'],
          author: element['author'],
          press: element['press'],
          year: element['year'],
          language: element['language'],
          page: element['page'],
          price: element['price'],
          isbn: element['isbn'],
          img: element['img']));
    });
    return allBooks;
  }
}
