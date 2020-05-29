# Class Televisão - criação de método simples de controle de canais e volume em uma televisão
# Métodos - Ligar e Desligar Televisão
# Metodos - Aumentar e Dominuir canal
# Método - Mutar Televisão

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.volume = 10

    def power(self): # método ligar e desligar Televisão
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentar_canal(self): # método mudando de Canal
        if self.ligada: # muda de canal SE a televisão estiver ligada = True
            self.canal += 1

    def diminuir_canal(self): # método para diminuir o canal
        if self.ligada: # muda de canal SE a televisão estiver ligada = True
            self.canal -= 1

    def aumentar_volume(self): # método aumentar volume
        if self.ligada:
            self.volume += 1
    
    def diminuir_volume(self): # Método diminuir volume
        if self.ligada:
            self.volume -= 1
    
    def mute(self): # método mutar televisão
        if self.ligada:
            self.volume = 'mute'

televisao = Televisao()
print(f'Televisão ligada: ',televisao.ligada)
televisao.power()
print(f'Televisão ligada: ',televisao.ligada)
televisao.power()
print(f'Televisão ligada: ',televisao.ligada)
televisao.power()
print(f'Televisão ligada: ',televisao.ligada)
print(f'Canal: ',televisao.canal)
televisao.aumentar_canal()
print(f'Canal: ',televisao.canal)
televisao.aumentar_canal()
print(f'Canal: ',televisao.canal)
televisao.diminuir_canal()
print(f'Diminuindo a faixa de canal: ',televisao.canal)
print(f'Volume: ',televisao.volume)
televisao.aumentar_volume()
print(f'Volume: ',televisao.volume)
televisao.diminuir_volume()
print(f'Volume: ',televisao.volume)
televisao.mute()
print(f'Volume: ',televisao.volume)
