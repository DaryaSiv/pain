class User {
  late int id;
  late String username;
  late String password1;
  late String password2;
  late String email;
  late String phone_number;
  late String token;

  User();

  Map<String, dynamic> toJson(User user) {
    return {
      'username': user.username,
      'password': user.password1,
    };
  }

  Map<String, dynamic> toRegisterJson(User user) {
    return {
      'username': user.username,
      'password1': user.password1,
      'password2': user.password2,
      'phone_number': user.phone_number,
      'email': user.email,
    };
  }
}
