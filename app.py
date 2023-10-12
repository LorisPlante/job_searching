from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import sys

import sqlite3



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(20,50,800,700)

        # Récupérer les données depuis la base de données
        data = get_data_from_database()

        # Création du tableau avec les données
        table = MyTable(data)

        self.new_window = None


        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)


        button_layout = QHBoxLayout()  
        main_layout.addLayout(button_layout)    

        btn_all = QPushButton("Tout", self)
        btn_stage = QPushButton("Stage", self)
        btn_alternance = QPushButton("Alternance", self)
        btn_emploi = QPushButton("Emploi", self)
        btn_ajout = QPushButton("Ajouter", self)

        button_layout.addWidget(btn_all)
        button_layout.addWidget(btn_stage)
        button_layout.addWidget(btn_alternance)
        # btn_alternance.clicked.connect(self.get_alternance_from_database)
        button_layout.addWidget(btn_emploi)

        button_layout.addWidget(btn_ajout)
        btn_ajout.clicked.connect(self.open_new_window)


        main_layout.addWidget(table)

    def open_new_window(self):
        # Fonction pour ouvrir une nouvelle fenêtre
        self.new_window = AddWindow()
        self.new_window.show()

class AddWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Configuration de la nouvelle fenêtre
        self.setWindowTitle('Ajouter un job')
        self.setGeometry(100, 100, 400, 400)
        
        self.job_type_text = QLineEdit(self)
        self.job_type_text.setPlaceholderText("Type de job (Alternance / Stage / Emploi)")

        self.job_status_text = QLineEdit(self)
        self.job_status_text.setPlaceholderText("Statut de job (Oui / Non / En attente)")

        self.job_date_text = QLineEdit(self)
        self.job_date_text.setPlaceholderText("Date de job (jj/mm/aaaa)")

        self.job_compagny_text = QLineEdit(self)
        self.job_compagny_text.setPlaceholderText("Nom de l'entreprise du job")

        self.job_name_text = QLineEdit(self)
        self.job_name_text.setPlaceholderText("Titre du job")

        self.job_location_text = QLineEdit(self)
        self.job_location_text.setPlaceholderText("Lieu du job")

        self.job_description_text = QTextEdit(self)
        self.job_description_text.setPlaceholderText("Description du job")

        btn_ajouter = QPushButton("AJOUTER UN JOB", self)

        # Layout pour organiser les éléments dans la fenêtre
        ajout_layout = QVBoxLayout()

        ajout_layout.addWidget(self.job_type_text)
        ajout_layout.addWidget(self.job_status_text)
        ajout_layout.addWidget(self.job_date_text)
        ajout_layout.addWidget(self.job_compagny_text)
        ajout_layout.addWidget(self.job_name_text)
        ajout_layout.addWidget(self.job_location_text)
        ajout_layout.addWidget(self.job_description_text)
        ajout_layout.addWidget(btn_ajouter)

        self.setLayout(ajout_layout)

        btn_ajouter.clicked.connect(self.ajout_a_db)


    def ajout_a_db(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = "INSERT INTO jobs (job_type, job_status, job_date, job_compagny_name, job_name, job_location, job_description) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (self.job_type_text.text(), self.job_status_text.text(), self.job_date_text.text(), self.job_compagny_text.text(), self.job_name_text.text(), self.job_location_text.text(), self.job_description_text.toPlainText()))
        print("good")
        conn.commit()

class MyTable(QTableWidget):
    def __init__(self, data):
        super().__init__()

        # Configuration du tableau
        self.setRowCount(len(data))
        self.setColumnCount(len(data[0]))

        # Remplissage du tableau avec les données
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.setItem(row_index, col_index, item)

def get_data_from_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT job_type, job_status, job_date, job_compagny_name, job_name, job_location, job_description FROM jobs")
    data = cursor.fetchall()
    conn.close()
    return data

# def get_alternance_from_database():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT job_type, job_status, job_date, job_compagny_name, job_name, job_location, job_description FROM jobs WHERE job_type = "Alternance"')
#     data = cursor.fetchall()
#     conn.close()
#     return data

def get_alternance_from_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT job_type, job_status, job_date, job_compagny_name, job_name, job_location, job_description FROM jobs WHERE job_type = 'Alternance'")
    data = cursor.fetchall()
    conn.close()
    return data


    









        

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("Job searching")
window.show()

app.exec()

