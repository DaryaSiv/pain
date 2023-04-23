import 'dart:ffi';

import 'package:app_p/models/book/books.dart';
import 'package:app_p/models/user_model.dart';
import 'package:app_p/api/api_model.dart';

abstract class IBooksRepository {
  Future<List<dynamic>> getAllBooks();
}
