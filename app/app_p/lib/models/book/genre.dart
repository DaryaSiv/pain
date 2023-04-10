import 'package:flutter/material.dart';

class Genre {
  String name;
  Genre({required this.name});
  factory Genre.fromJson(Map<String, dynamic> json) {
    return Genre(name: json['name']);
  }
}
