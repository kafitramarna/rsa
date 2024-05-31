from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import rsa
import base64

class HomeController(QDialog):
    def __init__(self, parent=None):
        super(HomeController, self).__init__(parent)
        loadUi('views/home.ui', self)
        self.btnEncrypt.clicked.connect(self.encrypt)
        self.btnDecrypt.clicked.connect(self.decrypt)
        self.btnClear.clicked.connect(self.clear)
        self.btnGenerateKeys.clicked.connect(self.generate_keys)
    
    def encrypt(self):
        try:
            plain = self.txtPlain.text().encode('utf-8')
            public_key = self.get_public_key()
            chiper = rsa.encrypt(plain, public_key)
            chiper = base64.b64encode(chiper).decode('utf-8')
            self.txtChiper.setText(chiper)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        
    def decrypt(self):
        try:
            chiper_b64 = self.txtChiper.text()
            private_key = self.get_private_key()
            chiper = base64.b64decode(chiper_b64)
            plain = rsa.decrypt(chiper, private_key).decode('utf-8')
            self.txtPlain2.setText(plain)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def clear(self):
        self.txtPlain.clear()
        self.txtChiper.clear()
        self.txtPlain2.clear()
        self.txtPublicKey.clear()
        self.txtPrivateKey.clear()

    def generate_keys(self):
        try:
            (public_key, private_key) = rsa.newkeys(512)
            self.txtPublicKey.setText(public_key.save_pkcs1().decode('utf-8'))
            self.txtPrivateKey.setText(private_key.save_pkcs1().decode('utf-8'))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def get_public_key(self):
        try:
            public_key_data = self.txtPublicKey.text().encode('utf-8').replace(b'\\n', b'\n')
            return rsa.PublicKey.load_pkcs1(public_key_data)
        except Exception as e:
            raise ValueError("Invalid public key")

    def get_private_key(self):
        try:
            private_key_data = self.txtPrivateKey.text().encode('utf-8').replace(b'\\n', b'\n')
            return rsa.PrivateKey.load_pkcs1(private_key_data)
        except Exception as e:
            raise ValueError("Invalid private key")
