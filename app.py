import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple PyQt App")  # Set window title
        self.setGeometry(100, 100, 300, 200)  # Set window position and size

        # Create a label
        self.label = QLabel("Hello, PyQt!")
        # Create a button
        self.button = QPushButton("Click Me")

        # Set up the layout (vertical box layout)
        layout = QVBoxLayout()
        layout.addWidget(self.label)  # Add label to the layout
        layout.addWidget(self.button)  # Add button to the layout

        self.setLayout(layout)  # Set the layout for the window

        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText("Button clicked!")  # Change label text when button is clicked


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application object
    window = MainWindow()  # Create the main window
    window.show()  # Show the window
    sys.exit(app.exec())  # Start the event loop