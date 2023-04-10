class User {
  late int id;
  late String username;
  late String password;
  late String token;

  User();

  Map<String, dynamic> toJson(User user) {
    return {'username': user.username, 'password': user.password};
  }
}
