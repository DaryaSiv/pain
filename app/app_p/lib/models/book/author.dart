import 'package:flutter/material.dart';

class Author {
  String name;
  Author({required this.name});
  factory Author.fromJson(Map<String, dynamic> json) {
    return Author(
      name: json['name']);
  }
}
