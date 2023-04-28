// ignore_for_file: implementation_imports, unused_local_variable, void_checks
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_application_2/data.dart';
// ignore: unused_import
import 'package:http/http.dart' as http;
class Result extends StatefulWidget {

  // const Result({super.key});
    final String scannedText;
  // ignore: use_key_in_widget_constructors
  const Result(this.scannedText);

  @override
  State<Result> createState() => ResultState();
}

class ResultState extends State<Result> {
   dynamic output = 'Upload any Image';
   Future<void> getresult()async {
    String url = 'http://10.0.2.2:5000/api?query=${widget.scannedText}';
    String data = await fetchdata(url);
    dynamic decode = jsonDecode(data);
    if (decode is List) {
    setState(() {
      output = decode.map((e) => e.toString()).join('\n');
    });
  } else if (decode is Map) {
    setState(() {
      output = decode['output'].toString();
    });
  } else {
    setState(() {
      output = decode['output'].toString();
    });
  }
  }
  void updateResult() {
    getresult();
  }
  @override
  Widget build(BuildContext context) {
    
    return Scaffold(
      appBar: AppBar(  
        title: const Text('Result'),  
      ), 
           body: Center(  
            child:Column
            (
              children:[
                 // ignore: prefer_const_constructors
                 Text(
              'Given Probelm',
              style: const TextStyle(
                fontSize: 20.0,
                fontWeight: FontWeight.bold,
              ),),
                const SizedBox(height: 20.0),
                // ignore: prefer_const_constructors
                Text(
                    widget.scannedText,
                    style: const TextStyle(
                    fontSize: 20.0,
                    ),
                    ),
                    // ignore: prefer_const_constructors
                     Text(
                   'The Solution Is',
              style: const TextStyle(
                fontSize: 20.0,
                fontWeight: FontWeight.bold,
              ),
              ),
              // ignore: prefer_const_constructors, avoid_unnecessary_containers
               Container(
                  child: Text(
                    output,
                    style: const TextStyle(fontSize: 20),
                  ),
                  ), 
              ]
      ),
            ),
         
    ); 
    
   
  }
  @override
  void initState() {
    super.initState();
    getresult();
  }
   @override
  void didUpdateWidget(Result oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.scannedText != oldWidget.scannedText) {
      updateResult();
    }
  }
  
}

 