class handlers():

    def setupHandlers(obj):
        obj.pushButtonCript.clicked.connect(lambda: handlers.Cript(obj))
        obj.pushButtonDecript.clicked.connect(lambda: handlers.Decript(obj))

    def Cript(obj):
        selecionado = str(obj.comboBoxAlgoritmo.currentText())
        txtPadrao = obj.caixaTextoPadrao.toPlainText()
        txtKey = obj.caixaTextoChave.toPlainText()
        if selecionado == "Cesar":
            obj.caixaTextoCript.setPlainText(cifras.en_cesar(txtPadrao,txtKey))
        elif selecionado == "XOR":
            obj.caixaTextoCript.setPlainText(cifras.en_xor(txtPadrao,txtKey))
        elif selecionado == "AES":
            obj.caixaTextoCript.setPlainText(cifras.en_AES(txtPadrao,txtKey))

    def Decript(obj):
        selecionado = str(obj.comboBoxAlgoritmo.currentText())
        txtCript = obj.caixaTextoCript.toPlainText()
        txtKey = obj.caixaTextoChave.toPlainText()
        if selecionado == "Cesar":
            obj.caixaTextoPadrao.setPlainText(cifras.dec_cesar(txtCript,txtKey))
        elif selecionado == "XOR":
            obj.caixaTextoPadrao.setPlainText(cifras.dec_xor(txtCript,txtKey))
        elif selecionado == 'AES':
            obj.caixaTextoPadrao.setPlainText(cifras.dec_AES(txtCript,txtKey))

#handlers.setupHandlers(self)
