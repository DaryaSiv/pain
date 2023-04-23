import 'package:flutter/material.dart';

class Press {
  late String name;
  Press();
  factory Press.fromJson(Map<String, dynamic> json) {
    Press press = Press();
    press.name = json['name'];
    return press;
  }
}
