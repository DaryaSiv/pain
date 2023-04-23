import 'dart:convert';
import 'dart:io';
import 'package:app_p/repository/books_repository.dart';
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

class BooksController {
  BooksRepository booksRepository = BooksRepository();

  Future<List<Book>> getAllBooks() async {
    List<Book> listBooks = [];

    List<dynamic> allBooks = await booksRepository.getAllBooks();

    allBooks.forEach((element) {
      Book book = Book();

      Genre genre = Genre();
      genre.name = element['genre']['name'];

      Press press = Press();
      press.name = element['press']['name'];

      Author author = Author();
      author.name = element['author']['name'];

      book.author = author;
      book.name = element['name'];
      book.genre = genre;
      book.price = element['price'];
      book.press = press;

      listBooks.add(book);
    });
    print('SAASSSS $listBooks');

    return listBooks;
  }
}
