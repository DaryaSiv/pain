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
      body: SizedBox(
          width: 500,
          height: 200,
          child: Card(
            margin: EdgeInsets.all(10),
            color: Colors.green[100],
            shadowColor: Colors.blueGrey,
            elevation: 10,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                const ListTile(
                  leading: Icon(Icons.album, color: Colors.cyan, size: 45),
                  title: Text(
                    "Let's Talk About Love",
                    style: TextStyle(fontSize: 20),
                  ),
                  subtitle: Text('Modern Talking Album'),
                ),
              ],
            ),
          )),
    );
  }
}
