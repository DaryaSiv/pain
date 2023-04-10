import 'package:flutter/material.dart';

class Language {
  String name;
  Language({required this.name});
  factory Language.fromJson(Map<String, dynamic> json) {
    return Language(name: json['name']);
  }
}
