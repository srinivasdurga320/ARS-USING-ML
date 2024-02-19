# Major Project: Flutter Mobile App & Flask Backend Integration

This project combines a Flutter mobile app for text recognition and a Flask backend for performing mathematical and statistical operations based on user input.

## Demo

You can find a demo of our project below:

[Link to Video](https://github.com/srinivasdurga320/ARS-USING-ML/raw/main/Project.webm)

## Tech Stack

- **Frontend**: Flutter
- **Backend**: Flask

## Flutter Mobile App: ARS Lens

ARS Lens is a Flutter application designed to assist users in extracting text from images using Google ML Kit. The app provides a user-friendly interface for selecting images from the device's gallery or directly capturing photos using the device's camera. Once an image is selected, the app utilizes Google ML Kit's text recognition capabilities to extract text from the image in real-time. The recognized text is then displayed to the user within the app.

### Features

- **Image Selection**: Users can choose an image from the gallery or capture a new photo using the device's camera.
- **Text Recognition**: The app employs Google ML Kit's text recognition API to detect and extract text from images.
- **Real-time Feedback**: Users receive instant feedback as the app performs text recognition, allowing for a seamless user experience.
- **Clean UI**: ARS Lens features a clean and intuitive user interface, making it easy for users to interact with the app and view the extracted text.

### Getting Started

To use ARS Lens:

1. Clone the repository to your local machine.
2. Open the project in a Flutter-compatible IDE such as Android Studio or Visual Studio Code.
3. Ensure that your device is connected to the IDE or has USB debugging enabled.
4. Build and run the project on your device.
5. Launch the ARS Lens app and follow the on-screen instructions to select an image and perform text recognition.

### Contributing

Contributions to ARS Lens are welcome! Whether you'd like to fix bugs, add new features, or improve the user interface, feel free to submit pull requests or open issues on GitHub to contribute to the project's development.

## Flask Backend: Mathematical and Statistical Operations Tool

The Flask backend serves as the computational engine for performing mathematical and statistical operations based on user input. It exposes API endpoints that accept user queries, evaluate mathematical expressions, and compute statistical measures. The backend leverages the NLTK library for natural language processing to analyze and interpret textual input effectively.

### Features

- **Mathematical Expression Evaluation**: The backend can evaluate a wide range of mathematical expressions, including basic arithmetic operations and complex mathematical functions.
- **Statistical Calculations**: Users can request statistical measures such as mean, median, mode, greatest common divisor (gcd), and least common multiple (lcm) of a list of numbers.
- **Textual Input Processing**: The backend analyzes textual input provided by users, identifying keywords and performing corresponding mathematical or statistical operations.
- **Error Handling**: Robust error handling ensures smooth operation even in scenarios with invalid inputs or unexpected errors.

### Usage

To use the Flask backend:

1. Clone the repository to your local machine.
2. Set up a virtual environment and install dependencies using `pip install -r requirements.txt`.
3. Run the Flask app using `python app.py` to start the backend server.
4. Access the API endpoints for mathematical and statistical operations by sending HTTP requests to the appropriate routes.

### Contributing

Contributions to the Flask backend are appreciated! Whether you'd like to enhance existing functionalities, optimize performance, or add new features, you're encouraged to submit pull requests or open issues on GitHub to contribute to the project's development.

## License

This project is licensed under the MIT License, allowing for free use, modification, and distribution of the codebase. Refer to the [LICENSE](LICENSE) file for more details.
