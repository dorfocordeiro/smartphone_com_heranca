from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
# Cria um arquivo com o módulo pathlib

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
        # NotImplementedError é para avisar que não é pra usar a super classe
        # Mas as subclasses dele
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
    # Isso é válido para todas as classes
    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log): # Avisa os devs para adicionar funções na herança multipla
    def _log(self, msg):
        self.msg = msg # Mudar a assinatura pode quebrar um pricípio da programação
        format_msg =  f'{msg} ({self.__class__.__name__})'
        print()
        print('Salvando no log', format_msg)
        with open(LOG_FILE, 'a') as file:
            file.write(format_msg)
            file.write('\r\n')
# Para arquivo de log, não apagar completamente, e sim no with open, coloque 'a'


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

# Passa os métodos protegidos com _ para avisar que é pra ser usado para lógica dentro da classe

if __name__ == '__main__':  
# Para executar o módulo só quando o __name__ for __main__
# Caso esse módulo esteja sendo importado em outro arquivo
# Assim ainda gera um erro mas é só mudar o nome da classe 

    log_print = LogPrintMixin()
    log_print.log_error(msg='Ainda quero um PC novo')
    log_print.log_success(msg='Ainda quero um PC novo')

    log_file = LogFileMixin()
    log_file.log_success(msg='Ainda quero um PC novo')
    log_file.log_error(msg='Ainda quero um PC novo')

    print(LOG_FILE)
