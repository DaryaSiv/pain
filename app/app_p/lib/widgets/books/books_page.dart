// ignore_for_file: unused_local_variable

import 'package:app_p/controllers/books_controller.dart';
import 'package:app_p/controllers/home_controller.dart';
import 'package:app_p/widgets/home_page.dart';
import 'package:flutter/material.dart';

import '../../models/book/books.dart';

class BooksPage extends StatefulWidget {
  final HomeController _homeController = HomeController();
  final BooksController _booksController = BooksController();

  @override
  _BooksPageState createState() => _BooksPageState();
}

class _BooksPageState extends State<BooksPage> {
  List<Book> _listBooks = [];

  @override
  void initState() {
    super.initState();
  }

  Future<void> getAllBooks() async {
    var listBooks = await widget._booksController.getAllBooks();

    setState(() {
      _listBooks = listBooks;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Books'),
      ),
      body: ListView.builder(
        itemCount: _listBooks.length,
        itemBuilder: (BuildContext context, int index) {
          Book book = _listBooks[index];
          return ListTile(
            title: Text(book.name),
            subtitle: Text(book.author as String),
            trailing: Text('\$${book.price}'),
          );
        },
      ),
    );
  }
}
