import 'package:app_p/models/book/genre.dart';
import 'package:app_p/models/book/author.dart';
import 'package:app_p/models/book/press.dart';
import 'package:app_p/models/book/language.dart';

class Books {
  String name;
  Genre genre;
  Author author;
  Press press;
  int year;
  Language language;
  int page;
  int price;
  int isbn;
  String img;
  Books(
      {required this.name,
      required this.genre,
      required this.author,
      required this.press,
      required this.year,
      required this.language,
      required this.page,
      required this.price,
      required this.isbn,
      required this.img});

  factory Books.fromJson(Map<String, dynamic> json) {
    if (json['name'] == '') {
      json['name'] = 'Товар отсуствует';
    }
    return Books(
        name: json['name'],
        genre: json['genre'],
        author: json['author'],
        press: json['press'],
        year: json['year'],
        language: json['language'],
        page: json['page'],
        price: json['price'],
        isbn: json['isbn'],
        img: json['img']);
  }
}
