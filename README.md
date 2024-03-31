
# Sign Language Recognition System

## About The Project

This Sign Language Recognition System is designed to translate sign language into text in real-time, making communication for the deaf and hard of hearing community more accessible. Using a dataset of 300 images for each gesture and machine learning technology, this system can recognize various signs and translate them into corresponding letters or words.

## Target Audience

The project is aimed at individuals, educators, and institutions within the deaf and hard of hearing community, aiming to facilitate smoother communication through technology. It's also an invaluable resource for developers and researchers working on assistive technologies.

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Pip for Python package installation
- A webcam for real-time gesture recognition

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone <repository-url>
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Program

- To collect data for new gestures, run:
    ```bash
    python data_collection.py
    ```
    Follow the on-screen instructions to capture images of the gestures.

- To test the system with your webcam, run:
    ```bash
    python test.py
    ```
    Make gestures in view of the webcam to see the system's real-time recognition.

## Technologies Used

- **Python**: The primary programming language used.
- **OpenCV**: For image capture and processing.
- **cvzone**: A helper library for hand tracking and classification.
- **Teachable Machine**: For training the machine learning model with the collected gesture images.
- **Keras**: Utilized for the machine learning model's creation and training process.

## Project Structure

- `data_collection.py`: Script for collecting gesture images using a webcam.
- `test.py`: Main application script for gesture recognition.
- `labels.txt`: File containing the labels for each gesture recognized by the system.
- `keras_model.h5`: The trained model file used for gesture recognition.
- `data/`: Folder containing the images for each gesture used in machine learning training.

## Contribution

Contributions to enhance the Sign Language Recognition System are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is open-source and available under the MIT License.

## Contact

Project Creator: Mateusz Gurgul

Email: [mateusz.gurgul.2003@gmail.com](mailto:mateusz.gurgul.2003@gmail.com)
