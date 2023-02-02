from connectDB import ConectaBD
from classes.Usuario import Usuario
from classes.Aviao import Aviao
from classes.Aeroporto import Aeroporto
from classes.Voo import Voo
from classes.Passagem import Passagem

from classesDAO.UsuarioDAO import UsuarioDAO
from classesDAO.AviaoDAO import AviaoDAO
from classesDAO.AeroportoDAO import AeroportoDAO
from classesDAO.VooDAO import VooDAO
from classesDAO.PassagemDAO import PassagemDAO
import logging

conectaBD = ConectaBD()
aviaoDAO = AviaoDAO(conectaBD)
usuarioDAO = UsuarioDAO(conectaBD)
aeroportoDAO = AeroportoDAO(conectaBD)
vooDAO = VooDAO(conectaBD)
passagemDAO = PassagemDAO(conectaBD)

## TESTES AVIAO
aviao = Aviao(idAviao="7", qtTotalAssentos=30)
print(aviao.__repr__())
aviaoDAO.insertAviao(aviao)

aviao = Aviao(qtTotalAssentos=30)
print(aviao.__repr__())
aviaoDAO.insertAviao(aviao)
''' 

print(aviao.to_json())

avioes = aviaoDAO.getTbAviao();
for aviao in avioes:
    print(aviao)

print("\nUPDATE\n")
aviao = Aviao(idAviao=7, qtTotalAssentos=12)
aviaoDAO.updateAviaoById(aviao)

avioes = aviaoDAO.getTbAviao();
for aviao in avioes:
    print(aviao)
print("\nGET\n")

aviao = aviaoDAO.getAviaoById(7)
aviao.printa()

aviaoDAO.deleteAviaoByIDs([7])

print("\nDELETE\n")
avioes = aviaoDAO.getTbAviao();
for aviao in avioes:
    print(aviao)
''' 

## TESTES USUARIO
user = Usuario(nome="Usuario cinco", email="usuario5@ufu.br", senha="12412312523" )
print(user.__repr__())

usuarioDAO.addUsuario(user)
# print("criou")

arrUsuario = []
# print("antes do 1")
usuario1 = Usuario(nome="Usuario tres", email="usuario3@ufu.br", senha="Rua_3")
usuario1.printa() 
arrUsuario.append(usuario1)
# print("antes do 2")
usuario2 = Usuario(nome="Usuario quatro", email="Usuario4@ufu.br", senha="Rua_4")
print(usuario2.__repr__())
# print("depois do 2 e antes de add na lista")
arrUsuario.append(usuario2)
usuarioDAO.addListUsuarios(arrUsuario)
# print("depois de add a lista tb")
''' 


arrUsuario = usuarioDAO.getAllUsers()
# arrUsuario = usuarioDAO.getAllUsersOrderedName()
# arrUsuario = usuarioDAO.getUsersByNameOrderedName("sua")
# arrUsuario = usuarioDAO.getAllUsersByNames(["Usuario Dois","Usuario um"])


for aluno in arrUsuario:
    print(aluno.__repr__())

qtd = usuarioDAO.getQtdUser()
print(qtd) '''
 
## TESTES AEROPORTO
aeroporto = Aeroporto(idAeroporto="203", nome = "garulhos", estado="Brasil", cidade="Sao Paulo")
print(aeroporto.__repr__()) 

aeroportoDAO.insertAeroporto(aeroporto)

aeroporto = Aeroporto(nome = "garulhos", estado="Brasil", cidade="Sao Paulo")
print(aeroporto.__repr__())
aeroportoDAO.insertAeroporto(aeroporto)
''' 

print(aeroporto.to_json())

avioes = aeroportoDAO.getTbAeroporto();
for aeroporto in avioes:
    print(aeroporto)

print("\nUPDATE\n")
aeroporto = Aeroporto(idAeroporto="2", nome = "modificado", estado="Brasil-sil", cidade="SP")
aeroportoDAO.updateAeroportoById(aeroporto)

avioes = aeroportoDAO.getTbAeroporto();
for aeroporto in avioes:
    print(aeroporto)
print("\nGET\n")

aeroporto = aeroportoDAO.getAeroportoById(2)
aeroporto.printa()

aeroportoDAO.deleteAeroportoByIDs([1])

print("\nDELETE\n")
avioes = aeroportoDAO.getTbAeroporto();
for aeroporto in avioes:
    print(aeroporto)
''' 

## TESTES VOO

voo = Voo(idVoo=14, lugaresDisponiveis=20, dataDeSaida="02-02-2023", idAeroportoSaida=203, dataDeChegada="04-05-2023", idAeroportoChegada=2, preco=218.00)
print(voo.__repr__()) 

vooDAO.insertVoo(voo)

voo = Voo(lugaresDisponiveis=20, dataDeSaida="02-02-2023", idAeroportoSaida=203, dataDeChegada="04-05-2023", idAeroportoChegada=2, preco=218.00)
print(voo.__repr__())
vooDAO.insertVoo(voo)
print(voo.to_json())
'''

voos = vooDAO.getTbVoo();
for voo in voos:
    print(voo)

print("\nUPDATE\n")
voo = Voo(idVoo=1, idAviao=1, lugaresDisponiveis=19, dataDeSaida="02-02-2023", idAeroportoSaida=3, dataDeChegada="04-05-2023", idAeroportoChegada=2, preco=218.00)
vooDAO.updateVooById(voo)

voos = vooDAO.getTbVoo();
for voo in voos:
    print(voo)

print("\nGET\n")
voo = vooDAO.getVooById(1)
voo.printa()

vooDAO.deleteVooByIDs([14])

print("\nDELETE\n")
voos = vooDAO.getTbVoo();
for voo in voos:
    print(voo)
'''

## TESTES PASSAGEM
# passagem = Passagem(idPassagem=5, idVoo=3, nomeComprador="Augusto", cpfComprador="12312345678")
# print(passagem.__repr__())
# passagemDAO.insertPassagem(passagem)

passagem = Passagem(idVoo=14, nomeComprador="Isabella", cpfComprador="05155425123")
print(passagem.__repr__()) 
passagemDAO.insertPassagem(passagem)

'''

print(passagem.to_json())

passagems = passagemDAO.getTbPassagem();
for passagem in passagems:
    print(passagem)

print("\nUPDATE\n")
passagem = Passagem(idPassagem=5, idVoo=1, nomeComprador="Augusto Salgado", cpfComprador="12312345678")
passagemDAO.updatePassagemById(passagem)

passagems = passagemDAO.getTbPassagem();
for passagem in passagems:
    print(passagem)

print("\nGET\n")
passagem = passagemDAO.getPassagemById(1)
passagem.printa()

passagemDAO.deletePassagemByIDs([1])

print("\nDELETE\n")
passagems = passagemDAO.getTbPassagem();
for passagem in passagems:
    print(passagem)
'''
