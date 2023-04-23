import 'package:flutter/material.dart';

class Author {
  late String name;
  Author();
  factory Author.fromJson(Map<String, dynamic> json) {
    Author author = Author();
    author.name = json['name'];

    return Author();
  }
}
