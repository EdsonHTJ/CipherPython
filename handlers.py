import cifras
from PyQt5 import QtGui, QtWidgets


class handlers():

    def setupHandlers(obj):
        obj.pushButtonCript.clicked.connect(lambda: handlers.Cript(obj))
        obj.pushButtonDecript.clicked.connect(lambda: handlers.Decript(obj))
        obj.errorCloseButton.clicked.connect(lambda: obj.frame_popuperror.hide())
        obj.pushButtonCriptArquivo.clicked.connect(lambda: handlers.CriptArquivo(obj))
        obj.pushButtonDecriptArquivo.clicked.connect(lambda: handlers.DecriptArquivo(obj))
        obj.frame_popuperror.hide()

    def Cript(obj):
        selecionado = str(obj.comboBoxAlgoritmo.currentText())
        txtPadrao = obj.caixaTextoPadrao.toPlainText()
        txtKey = obj.caixaTextoChave.toPlainText()
        if selecionado == "Cesar":
            try:
                Ct = cifras.en_cesar(txtPadrao,txtKey)
                obj.caixaTextoCript.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "XOR":
            try:
                Ct = cifras.en_xor(txtPadrao,txtKey)
                obj.caixaTextoCript.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "S-DES":
            try:
                Ct = cifras.en_sDES(txtPadrao,txtKey)
                obj.caixaTextoCript.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "DES":
            try:
                Ct = cifras.en_DES(txtPadrao,txtKey)
                obj.caixaTextoCript.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "AES":
            try:
                Ct = cifras.en_AES(txtPadrao,txtKey)
                obj.caixaTextoCript.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)

    def Decript(obj):
        selecionado = str(obj.comboBoxAlgoritmo.currentText())
        txtCript = obj.caixaTextoCript.toPlainText()
        txtKey = obj.caixaTextoChave.toPlainText()
        if selecionado == 'Cesar':
            try:
                Ct = cifras.dec_cesar(txtCript,txtKey)
                obj.caixaTextoPadrao.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == 'XOR':
            try:
                Ct = cifras.dec_xor(txtCript,txtKey)
                obj.caixaTextoPadrao.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "S-DES":
            try:
                Ct = cifras.dec_sDES(txtCript,txtKey)
                obj.caixaTextoPadrao.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "DES":
            try:
                Ct = cifras.dec_DES(txtCript,txtKey)
                obj.caixaTextoPadrao.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "AES":
            try:
                Ct = cifras.dec_AES(txtCript,txtKey)
                obj.caixaTextoPadrao.setPlainText(Ct)
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)

    def CriptArquivo(obj):

        selecionado = str(obj.comboBoxAlgoritmo.currentText())
        txtKey = obj.caixaTextoChave.toPlainText()

        if selecionado == 'Cesar':
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.en_cesar(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_cript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == 'XOR':
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.en_xor(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_cript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "S-DES":
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.en_sDES(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_cript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "DES":
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.en_DES(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_cript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)

        elif selecionado == "AES":
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.en_AES(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_cript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)

    def DecriptArquivo(obj):

        selecionado = str(obj.comboBoxAlgoritmo.currentText())
        txtKey = obj.caixaTextoChave.toPlainText()

        if selecionado == 'Cesar':
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.dec_cesar(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_decript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == 'XOR':
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.dec_xor(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_decript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "S-DES":
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.dec_sDES(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_decript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "DES":
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.dec_DES(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_decript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)
        elif selecionado == "AES":
            Ct = handlers.SelecionarArquivo(obj)
            try:
                f = open(Ct,'rb').read()
                fcp = cifras.dec_AES(f,txtKey,1)
                nome_arquivo = Ct[len(Ct)-Ct[::-1].index("/"):]
                x = nome_arquivo.index(".")
                ext = nome_arquivo[x:]
                nome_arquivo = nome_arquivo[:x]
                open("deploy/"+nome_arquivo+"_decript"+ext,'wb').write(bytes(fcp))
                handlers.sucesso(obj)
            except:
                handlers.erro(obj)


    def SelecionarArquivo(obj):
        dialog = QtWidgets.QFileDialog(None,"","","")
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        if dialog.exec_():
            file_name = dialog.selectedFiles()
            file_bytes = open(str(file_name)[2:(len(str(file_name))-2)],'rb').read()
            nome_tratado = str(file_name)[2:(len(str(file_name))-2)]
            return nome_tratado

    def sucesso(obj):
        obj.frame_popuperror.setStyleSheet("background-color: rgb(0, 255, 127);")
        obj.errorCloseButton.setStyleSheet("QPushButton{\n"
"font: 75 8pt \"Verdana\";\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 205, 147);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        obj.label_error.setText("         SUCESSO")
        obj.frame_popuperror.show()
    def erro(obj):
        obj.frame_popuperror.setStyleSheet("background-color: rgb(217, 103, 105);")
        obj.errorCloseButton.setStyleSheet("QPushButton{\n"
"font: 75 8pt \"Verdana\";\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(122, 69, 70);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        obj.label_error.setText("ERRO INESPERADO")
        obj.frame_popuperror.show()
#LEMBRAR DE ADICIONAR NA UI -> handlers.handlers.setupHandlers(self)
