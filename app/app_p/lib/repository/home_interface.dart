import 'dart:ffi';

import 'package:app_p/models/user_model.dart';
import 'package:app_p/api/api_model.dart';

abstract class IHomeRepository {
  Future<void> loginUser(String username, String password);
}
