#voos
# json_voo = {id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00" ,passagens:"25"}
# retornar somente as que passagens != 0 

#passagens
# {id:"1",nomePassageiro:"Joao", cpf:"1111111111", viagem:{id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00"}}
# novaPassagem_json = '{"viagem":"1", "nomePassageiro":"nome", "cpf":"11111111111"}'

#aeroportos
# {"id":"1","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}

#ajeitar doc .env com as variaveis de banco

#definir se vou receber json ou string

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
import json, operator

conectaBD = ConectaBD()
aviaoDAO = AviaoDAO(conectaBD)
usuarioDAO = UsuarioDAO(conectaBD)
aeroportoDAO = AeroportoDAO(conectaBD)
vooDAO = VooDAO(conectaBD)
passagemDAO = PassagemDAO(conectaBD)

## Deletes

def deletePassagem(idPassagem):
    passagem = passagemDAO.getPassagemById(idPassagem)
    voo = vooDAO.getVooById(passagem.getIdVoo())
    # deixando um lugar disponivel no voo
    voo.setQtLugaresDisponiveis(voo.getQtLugaresDisponiveis() + 1)
    vooDAO.updateVooById(voo)
    passagemDAO.deletePassagemByIDs([idPassagem])

# deletePassagem(2)

def deleteVoo(idVoo):
    # delete passagens
    vooDAO.deleteVooByIDs([idVoo])

# deleteVoo(16)

def deleteAeroporto(idAeroporto):
    #delete voos e passagens
    aeroportoDAO.deleteAeroportoByIDs([idAeroporto])

# deleteAeroporto(3)

def deleteUsuario(idUsuario):
    usuarioDAO.deleteUsersByIDs([idUsuario])

# deleteUsuario(70)

## Updates

def updateVoo(json_voo):
    voo = Voo.from_json(json.loads(json_voo))
    vooDAO.updateVooById(voo)

''' No aeroporto não faz diferença se tá só a id ou se tá o object inteiro. É só 1 linha que se altera,
    mas daí preciso saber certinho como ele vai vir '''
# json_voo = '{"id":"45", "partida":{"id":"41","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "destino":{"id":"42","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "diaPartida":"01/07/2023", "horarioPartida":"19:00",\
#             "diaChegada":"05/11/2023", "horarioChegada":"12:00", "valor":"250.00" ,"passagens":"0"}'
# updateVoo(json_voo)


## Inserts

def cadastrar(json_usr):
    usuario = Usuario.from_json(json.loads(json_usr))
    usuarioDAO.addUsuario(usuario)

# usuario1 = '{"id":234,"nome":"Usuario app", "email":"usuwarioAwqpp@ufu.br", "senha":"12412312523"}'
# cadastrar(usuario1)
# usuario = '{"nome":"Usuario app", "email":"usuariowAqpp@ufu.br", "senha":"12412312523"}'
# cadastrar(usuario)

def criarAeroporto(json_aeroporto):
    aeroporto = Aeroporto.from_json(json.loads(json_aeroporto))
    aeroportoDAO.insertAeroporto(aeroporto)

# # aeroporto = '{"id":"3","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}'
# aeroporto2 = '{"nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}'
# # criarAeroporto(aeroporto)
# criarAeroporto(aeroporto2)

def criarNovoVoo(json_voo):
    voo = Voo.from_json(json.loads(json_voo))
    vooDAO.insertVoo(voo)

''' Aqui precisa vir o aeroporto inteiro... então talvez seja mais fácil padronizar '''
# json_voo = '{"id":"162", "partida":{"id":"40","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "destino":{"id":"39","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "diaPartida":"22/07/2023", "horarioPartida":"19:00",\
#             "diaChegada":"25/11/2023", "horarioChegada":"12:00", "valor":"350.00" ,"passagens":"25"}'
# criarNovoVoo(json_voo)
# json_voo2 = '{"partida":{"id":"39","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "destino":{"id":"3","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "diaPartida":"22/07/2023", "horarioPartida":"19:00",\
#             "diaChegada":"25/11/2023", "horarioChegada":"14:00", "valor":"150.00" ,"passagens":"25"}'
# criarNovoVoo(json_voo2)

def venderPassagem(novaPassagem_json):
    passagem = Passagem.from_json(json.loads(novaPassagem_json))
    passagemDAO.insertPassagem(passagem)

''' Aqui onde era o idVoo, se pá a gente pode sempre chamar de "viagem", pq senão quebra o dicionário '''
# novaPassagem_json1 = '{"id":"2","viagem":"16", "nomePassageiro":"nome", "cpf":"11111111111"}'
# venderPassagem(novaPassagem_json1)
# novaPassagem_json = '{"viagem":"16", "nomePassageiro":"nome", "cpf":"11111111111"}'
# venderPassagem(novaPassagem_json)

## Gets
''' Com essa função dá pra ordenar qualquer array, só passando a string do nome da chave
    tipo o "valor" da passagem, tem exemplo lá embaixo '''
def sortJsonArrayByKey(json_array, str_key_name):
    data = json_array
    data.sort(key=operator.itemgetter(str_key_name))
    return json.dumps(data)

def listarAeroportos():
    aeroportos = aeroportoDAO.getTbAeroporto()
    aeroportos_json = []
    for aeroporto in aeroportos:
        aeroporto_json = aeroporto.to_json()
        aeroportos_json.append(json.loads(aeroporto_json))
    return aeroportos_json

# print(json.dumps(listarAeroportos(), indent=2))

#voos
# json_voo = {id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00" ,passagens:"25"}
# retornar somente as que passagens != 0 
def getVooJson(voo):
    aeroportoSaida = aeroportoDAO.getAeroportoById(voo.getIdAeroportoSaida())
    ''' Aqui eu n sabia se deixava cidade, estado, nome, me fala depois o que cê acha mió pro front? '''
    partida = aeroportoSaida.getNome() + " - " + aeroportoSaida.getCidade() + ', ' + aeroportoSaida.getEstado() 
    voo.setIdAeroportoSaida(partida)

    aeroportoChegada = aeroportoDAO.getAeroportoById(voo.getIdAeroportoChegada())
    destino = aeroportoChegada.getNome() + " - " + aeroportoChegada.getCidade() + ', ' + aeroportoChegada.getEstado() 
    voo.setIdAeroportoChegada(destino)

    return voo.to_json()

def listarVoos():
    voos = vooDAO.getTbVoo()
    voos_json = []
    for voo in voos:
        voos_json.append(json.loads(getVooJson(voo)))
    return voos_json
''' exemplo da lista total dos voos ordenado por preço '''
# # print(sortJsonArrayByKey(listarVoos(),'valor'))
# print(json.dumps(sortJsonArrayByKey(listarVoos(),'valor'), indent=2))

def listarVoosDisponiveis(nPessoas=0):
    voos = vooDAO.getTbVoo()
    voos_json = []
    for voo in voos:
        if(voo.getQtLugaresDisponiveis() > nPessoas):
            voos_json.append(json.loads(getVooJson(voo)))
    return voos_json

# print(sortJsonArrayByKey(listarVoosDisponiveis(),'valor'))

# print(listarVoosDisponiveis())

''' Objeto das passagens com o nome do passageiro e sem o valor na viagem '''
#passagens
# {id:"1",nomePassageiro:"Joao", cpf:"1111111111", viagem:{id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00"}}
def listarPassagens():
    passagens = passagemDAO.getTbPassagem()
    passagens_json = []
    for passagem in passagens:
        voo = vooDAO.getVooById(passagem.getIdVoo())
        viagem = json.loads(getVooJson(voo))
        del viagem['passagens']
        passagem.setIdVoo(viagem)
        passagem_json = json.loads(passagem.to_json())

        passagens_json.append(passagem_json)
    return passagens_json

# print(listarPassagens())

## Auth

def login():
    pass