import 'dart:async';
import 'package:app_p/models/book/books.dart';
import 'package:app_p/repository/books_interface.dart';
import 'package:app_p/models/user_model.dart';
import 'package:app_p/api/api_connection.dart';

class BooksRepository implements IBooksRepository {
  BooksRepository();

  @override
  Future<List<dynamic>> getAllBooks() {
    return booksApi();
  }
}
