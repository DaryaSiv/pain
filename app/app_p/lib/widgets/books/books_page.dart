import 'package:app_p/controllers/home_controller.dart';
import 'package:app_p/widgets/home_page.dart';
import 'package:flutter/material.dart';

import '../../models/book/books.dart';

class BooksPage extends StatefulWidget {
  final HomeController _homeController = HomeController();

  @override
  _BooksPageState createState() => _BooksPageState();
}

class _BooksPageState extends State<BooksPage> {
  List<Books> _listBooks = [];

  @override
  void initState() {
    super.initState();
    // widget._homeController.getBooks().then((listBooks)) {
    //   setState(() {
    //     _listBooks = listBooks;
    //   })
    // }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Главная страница"),
        ),
        body: Card(
          margin: const EdgeInsets.all(20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              ListTile(
                leading: Image.asset(''),
                title: const Text('Demo Title'),
                subtitle: const Text('This is a simple card in Flutter.'),
              ),
            ],
          ),
        ),
        Card(
          margin: const EdgeInsets.all(20),
          child: Column(
            mainAxisSize: MainAxisSize.max,
            children: <Widget>[
              ListTile(
                leading: Image.asset(''),
                title: const Text('Книга'),
                subtitle: const Text('TUT BOOK'),
              ),
            ],
          ),
        ));
  }
}
