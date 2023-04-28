import 'package:http/http.dart' as http;
// fetchdata(String url)async{
//   http.Response response = await http.get(Uri.parse(url));
//   return response.body;
// }
Future<String> fetchdata(String url) async {
  try {
    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      return response.body;
    } else {
      throw Exception('Failed to fetch data');
    }
  } catch (e) {
    throw Exception('Failed to connect to the server');
    
  }
}
