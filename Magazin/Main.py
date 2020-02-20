'''
Created on 31 ian. 2020

@author: Alex
'''

#teste
from teste.testeValid import TestValid
from teste.testeRepo import TestRepo
from teste.testeService import TestService

#validari
from validari.validation import ValidProdus
validProdus = ValidProdus()

#repository
from infrastructure.repository import RepositoryFile
from domain.entitati import Produs
repoProdus = RepositoryFile('./stoc.txt',Produs)

#service
from business.service import ServiceProdus
srvProdus = ServiceProdus(repoProdus,validProdus)

#UI
from prezentare.console import Console
ui = Console(srvProdus)
ui.run()