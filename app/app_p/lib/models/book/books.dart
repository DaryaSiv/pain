import 'package:app_p/models/book/genre.dart';
import 'package:app_p/models/book/author.dart';
import 'package:app_p/models/book/press.dart';
import 'package:app_p/models/book/language.dart';

class Book {
  late String name;
  late Genre genre;
  late Author author;
  late Press press;
  late int year;
  late Language language;
  late int page;
  late int price;
  late int isbn;
  late String img;
  Book();

  factory Book.fromJson(Map<String, dynamic> json) {
    if (json['name'] == '') {
      json['name'] = 'Товар отсуствует';
    }

    Book book = Book();

    book.name = json['name'];
    book.genre = json['genre'];
    book.author = json['author'];
    book.press = json['press'];
    book.year = json['year'];
    book.language = json['language'];
    book.page = json['page'];
    book.price = json['price'];
    book.isbn = json['isbn'];
    book.img = json['img'];

    return book;
  }
}
