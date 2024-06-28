from log import LogPrintMixin, LogFileMixin
# Importado para ter uma mensagem bonita

class Eletronic:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False
        # Aqui já foi definido como falso

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            # Então aqui já foi passado para true
            
            
    def desligar(self):
        if self._ligado:
            self._ligado = False
        # E se está ligado desligue
            
class SmartPhone(Eletronic, LogPrintMixin): # Puxando as duas classes
    def ligar(self):
        super().ligar() # Chamando com a super a classe para ligar
        if self._ligado:
            msg = f'{self.nome} Ligado' # Passando o atributo da LogPrintMixin
            self.log_success(msg) # Com um método de lá

    def desligar(self):
        super().desligar() # E como está ligado chama o que desliga
        if not self._ligado: # Faz a lógica que é False
            msg = f'{self.nome} Desligado' # Passa a mensagem
            self.log_error(msg) # Com o log_error para usar tudo

class Xiaomi(Eletronic, LogFileMixin): # Se passar o LogFileMixin, ele salva no log.txt
    def ligar(self):
        super().ligar()
        if self._ligado:
            msg = f'{self.nome} Ligado'
            self.log_success(msg)
    
    # Passando a mesma lógica

    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self.nome} Desligado'
            self.log_error(msg)
