import sys
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("socialnetwork.ui", self)  # Load UI directly into self

        # Set up image
        pixmap = QPixmap("/Users/mncedisimotsepe/Downloads/images-3.jpeg")
        self.label_10.setPixmap(pixmap)
        self.label_10.setScaledContents(True)

        # Set up table headers/columns
        self.ApplicationWidget.setColumnCount(5)
        self.ApplicationWidget.setHorizontalHeaderLabels(["User", "Age", "Email", "GAME", "GPA"])

        # Connect buttons
        self.pushButton.clicked.connect(self.add_data_to_table)
        self.pushButton_2.clicked.connect(self.application_page)
        self.pushButton_3.clicked.connect(self.exit_page)
        self.pushButton_4.clicked.connect(self.clear_inputs)

    # ---------- Button functions ----------
    def exit_page(self):
        self.close()

    def clear_inputs(self):
        self.nameedit.clear()
        self.ageedit.clear()
        self.emailedit.clear()
        self.gpaedit.clear()

    # ---------- Add row to table ----------
    def add_data_to_table(self):
        name = self.nameedit.text().strip()
        age_text = self.ageedit.text().strip()
        email = self.emailedit.text().strip()
        gpa_text = self.gpaedit.text().strip()
        game = self.comboBox.currentText()

        # Convert numbers safely
        try:
            age = int(age_text)
        except ValueError:
            age = 0

        try:
            gpa = float(gpa_text)
        except ValueError:
            gpa = 0

        # Validate age
        if age < 18:
            self.show_message("ERROR", "User must be 18 or older to apply!", QMessageBox.Icon.Warning)
            self.clear_inputs()
            return

        # Clear table first (only one row at a time)
        self.ApplicationWidget.setRowCount(0)

        # Add data to table
        self.ApplicationWidget.insertRow(0)
        self.ApplicationWidget.setItem(0, 0, QTableWidgetItem(name))
        self.ApplicationWidget.setItem(0, 1, QTableWidgetItem(str(age)))
        self.ApplicationWidget.setItem(0, 2, QTableWidgetItem(email))
        self.ApplicationWidget.setItem(0, 3, QTableWidgetItem(game))
        self.ApplicationWidget.setItem(0, 4, QTableWidgetItem(str(gpa)))

        # Clear inputs after adding
        self.clear_inputs()

    # ---------- Application page ----------
    def application_page(self):
        # Get GPA from the table (first row, column 4)
        if self.ApplicationWidget.rowCount() == 0:
            self.show_message("ERROR", "No application found!", QMessageBox.Icon.Warning)
            return

        gpa_item = self.ApplicationWidget.item(0, 4)  # 0 = first row, 4 = GPA column
        gpa = float(gpa_item.text())

        if gpa >= 65:
            self.show_message("WELCOME", "Welcome to The Social Network!", QMessageBox.Icon.Information)
        else:
            self.show_message("ERROR", "Your GPA is too low to be in The Social Network.", QMessageBox.Icon.Warning)
            # Clear table and inputs if GPA too low
            self.ApplicationWidget.setRowCount(0)
            self.clear_inputs()

    # ---------- Helper: show popup ----------
    def show_message(self, title, text, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
