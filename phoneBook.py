import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.number = None

class PhoneBook:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, name, number):
        current = self.root
        for char in name:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True
        current.number = number

    def search(self, name):
        current = self.root
        for char in name:
            if char not in current.children:
                return None
            current = current.children[char]
        if current.is_word:
            return current.number
        else:
            return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Book")
        self.setGeometry(100, 100, 500, 500)

        self.phonebook = PhoneBook()

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        name_layout = QHBoxLayout()
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        number_layout = QHBoxLayout()
        number_label = QLabel("Number:")
        self.number_input = QLineEdit()
        number_layout.addWidget(number_label)
        number_layout.addWidget(self.number_input)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_contact)
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_contact)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(search_button)

        self.contact_list = QListWidget()

        layout.addLayout(name_layout)
        layout.addLayout(number_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.contact_list)

        self.setCentralWidget(widget)

    def add_contact(self):
        name = self.name_input.text().strip()
        number = self.number_input.text().strip()
        if name and number:
            self.phonebook.insert(name, number)
            self.name_input.clear()
            self.number_input.clear()

    def search_contact(self):
        name = self.name_input.text().strip()
        if name:
            number = self.phonebook.search(name)
            if number:
                item = QListWidgetItem(name + ": " + number)
                self.contact_list.addItem(item)
            else:
                self.contact_list.addItem("No matching contact found for \"" + name + "\"")
            self.name_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
