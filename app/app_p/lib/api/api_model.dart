import 'package:jwt_decoder/jwt_decoder.dart';

class UserLogin {
  String username;
  String password;

  UserLogin({required this.username, required this.password});

  Map<String, dynamic> toDatabaseJson() =>
      {"username": this.username, "password": this.password};
}

class Token {
  String token;
  String refreshToken;

  Token({required this.token, required this.refreshToken});

  factory Token.fromJson(Map<String, dynamic> json) {
    return Token(
        token: json['access'].toString(),
        refreshToken: json['refresh'].toString());
  }
}

class UserRegistration {
  String email;
  String username;
  String password1;
  String password2;

  UserRegistration(
      {required this.email,
      required this.username,
      required this.password1,
      required this.password2});

  Map<String, dynamic> toDatabaseJson() => {
        "email": this.email,
        "username": this.username,
        "password1": this.password1,
        "password2": this.password2,
      };
}
