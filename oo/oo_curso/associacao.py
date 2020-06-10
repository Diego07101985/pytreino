from classes import Caneta
from classes import Escritor
from classes import MaquinaDeEscrever

caneta = Caneta('Bic')
escritor = Escritor('Joãozinho')
maquinha = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta = maquinha

escritor.ferramenta.escrever()
