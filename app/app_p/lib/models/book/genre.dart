import 'package:flutter/material.dart';

class Genre {
  late String name;
  Genre();
  factory Genre.fromJson(Map<String, dynamic> json) {
    Genre genre = Genre();
    genre.name = json['name'];

    return genre;
  }
}
