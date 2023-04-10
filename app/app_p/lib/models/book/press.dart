import 'package:flutter/material.dart';

class Press {
  String name;
  Press({required this.name});
  factory Press.fromJson(Map<String, dynamic> json) {
    return Press(name: json['name']);
  }
}
