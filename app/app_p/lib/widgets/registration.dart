import 'package:app_p/widgets/books/books_page.dart';
import 'package:flutter/material.dart';
import 'package:app_p/controllers/home_controller.dart';
import 'package:app_p/main.dart';
import 'package:app_p/widgets/login.dart';
import 'package:select_form_field/select_form_field.dart';

class RegistrationPage extends StatefulWidget {
  @override
  _RegistrationState createState() => _RegistrationState();

  final HomeController _homeController = HomeController();
}

class _RegistrationState extends State<RegistrationPage> {
  TextEditingController usernameController = TextEditingController();
  TextEditingController emailController = TextEditingController();
  TextEditingController password1Controller = TextEditingController();
  TextEditingController password2Controller = TextEditingController();
  TextEditingController phoneController = TextEditingController();
  int _district = 0;

  String error = '';
  GlobalKey<FormState> formkey = GlobalKey<FormState>();

  List<Map<String, dynamic>> _items = [];

  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text("Регистрация"),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Padding(
              padding: EdgeInsets.all(20),
              child: TextField(
                controller: usernameController,
                decoration: InputDecoration(
                    border: InputBorder.none, hintText: 'Введите ваше имя'),
              ),
            ),
            Padding(
              padding: EdgeInsets.all(20),
              child: TextField(
                controller: emailController,
                decoration: InputDecoration(
                    border: InputBorder.none, hintText: 'Введите ваш email'),
              ),
            ),
            Padding(
              padding: EdgeInsets.all(20),
              child: TextField(
                controller: phoneController,
                decoration: InputDecoration(
                    border: InputBorder.none, hintText: 'Введите ваш номер телефона'),
              ),
            ),
            Padding(
              padding: EdgeInsets.all(20),
              child: TextField(
                controller: password1Controller,
                decoration: InputDecoration(
                  border: InputBorder.none, hintText: "Придумайте пароль"
                ),
              ),
            ),
            Padding(
              padding: EdgeInsets.all(20),
              child: TextField(
                controller: password2Controller,
                decoration: InputDecoration(
                  border: InputBorder.none, hintText: "Повторите ваш пароль"
                ),
              ),
            ),
            Padding(
              padding: EdgeInsets.all(20),
              child: ElevatedButton(
                  onPressed: () {
                    String username = usernameController.text;
                    String email = emailController.text;
                    String password1 = password1Controller.text;
                    String password2 = password2Controller.text;
                    String phone_number = phoneController.text;

                    widget._homeController
                        .registerUser(username, email, phone_number, password1, password2);
                  },
            ),
            )
            Container(
            child: TextButton(
                    onPressed: () {
                      Navigator.push(
                        context, MaterialPageRoute(builder: (context) => BooksPage())),
                    },
                  )),
          ],
        ),
      ),
    );
  }
}
