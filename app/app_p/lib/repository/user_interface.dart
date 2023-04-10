import 'package:app_p/models/user_model.dart';
import 'package:app_p/api/api_model.dart';

abstract class IUserRepository {
  Future<List<User>> getAll();

  Future<User?> getOne(int id);

  Future<bool> register(String email, String username, String password);

  Future<String> login(String username, String password);

  Future<void> update(User user);

  Future<void> delete(int id);
}
