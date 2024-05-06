from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import string

class HomeController(QDialog):
    def __init__(self, parent=None):
        super(HomeController, self).__init__(parent)
        loadUi('views/home.ui', self)
        self.btnEncrypt.clicked.connect(self.encrypt)
        self.btnDecrypt.clicked.connect(self.decrypt)
        self.btnClear.clicked.connect(self.clear)
        self.btnKunciEncrypt.clicked.connect(self.encrypt_key)
        self.btnKunciDecrypt.clicked.connect(self.decrypt_key)
    
    def encrypt(self):
        try:
            plain = self.txtPlain.text().replace(' ', '')
            if not plain.isalpha():
                raise ValueError("Input harus berupa huruf dan key tidak boleh memiliki spasi")
            m = int(self.txtM.text())
            if (not(self.is_prime(m))):
                raise ValueError("nilai m harus relatif prima terhadap 26")
            b = int(self.txtB.text())
            
            alfabet = string.ascii_lowercase
            chiper = ''
            for i in range(len(plain)):
                chiper += alfabet[((alfabet.index(plain[i].lower()) * m) + b) % 26]
            self.txtChiper.setText(chiper)
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
        
    def decrypt(self):
        try:
            chiper = self.txtChiper.text().replace(' ', '')
            if not chiper.isalpha():
                raise ValueError("Input harus berupa huruf dan key tidak boleh memiliki spasi")
            
            m = int(self.txtM.text())
            if not self.is_prime(m):
                raise ValueError("Nilai m harus relatif prima terhadap 26")
            b = int(self.txtB.text())
            m_inv = 0
            for i in range(26):
                if (m * i) % 26 == 1:
                    m_inv = i
                    break
            alfabet = string.ascii_lowercase
            plain = ''
            for i in range(len(chiper)):
                plain += alfabet[m_inv * (alfabet.index(chiper[i].lower()) - b) % 26]
            self.txtPlain2.setText(plain)
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def clear(self):
        self.txtPlain.clear()
        self.txtM.clear()
        self.txtB.clear()
        self.txtChiper.clear()
        self.txtPlain2.clear()
    
    def is_prime(self, num, i=2):
        if num <= 2:
            return num == 2
        if num % i == 0:
            return False
        if i * i > num:
            return True
        return self.is_prime(num, i + 1)

    def encrypt_key(self):
        try:
            m = int(self.txtM.text())
            if (not(self.is_prime(m))):
                raise ValueError("nilai m harus relatif prima terhadap 26")
            b = int(self.txtB.text())
            QMessageBox.information(self, "Key", f"m: {m}\nb: {b}")
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def decrypt_key(self):
        try:
            m = int(self.txtM.text())
            if not self.is_prime(m):
                raise ValueError("Nilai m harus relatif prima terhadap 26")
            b = int(self.txtB.text())
            m_inv = 0
            for i in range(26):
                if (m * i) % 26 == 1:
                    m_inv = i
                    break
            QMessageBox.information(self, "Key", f"m: {m_inv}\nb: {b}")
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))