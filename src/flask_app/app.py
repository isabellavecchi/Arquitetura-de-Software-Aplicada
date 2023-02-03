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

# from connectDB import ConectaBD
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

class AppFunctions():
    # Constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
        self.aviaoDAO = AviaoDAO(self.conectaBD)
        self.usuarioDAO = UsuarioDAO(self.conectaBD)
        self.aeroportoDAO = AeroportoDAO(self.conectaBD)
        self.vooDAO = VooDAO(self.conectaBD)
        self.passagemDAO = PassagemDAO(self.conectaBD)
        
    ## Functions

    ''' Com essa função dá pra ordenar qualquer array, só passando a string do nome da chave
        tipo o "valor" da passagem, tem exemplo lá embaixo '''
    def sortJsonArrayByKey(json_array, str_key_name):
        data = json.loads(json_array)
        data.sort(key=operator.itemgetter(str_key_name))
        return json.dumps(data)

    #voos
    # json_voo = {id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00" ,passagens:"25"}
    # retornar somente as que passagens != 0 
    def getVooJson(self, voo):
        aeroportoSaida = self.aeroportoDAO.getAeroportoById(voo.getIdAeroportoSaida())
        ''' Aqui eu n sabia se deixava cidade, estado, nome, me fala depois o que cê acha mió pro front? '''
        partida = aeroportoSaida.getNome() + " - " + aeroportoSaida.getCidade() + ', ' + aeroportoSaida.getEstado() 
        voo.setIdAeroportoSaida(partida)

        aeroportoChegada = self.aeroportoDAO.getAeroportoById(voo.getIdAeroportoChegada())
        destino = aeroportoChegada.getNome() + " - " + aeroportoChegada.getCidade() + ', ' + aeroportoChegada.getEstado() 
        voo.setIdAeroportoChegada(destino)

        return voo.to_json()


    ## Inserts

    def criarUsuario(self, json_usr):
        try:            
            usuario = Usuario.from_json(json_usr)
            usuario = self.usuarioDAO.addUsuario(usuario)
            return usuario
        except Exception as e:
            logging.info(f'XABUUUUU ... {e}')
            return None
    # usuario1 = '{"id":234,"nome":"Usuario app", "email":"usuwarioAwqpp@ufu.br", "senha":"12412312523"}'
    # criarUsuario(usuario1)
    # usuario = '{"nome":"Usuario app", "email":"usuariowAqpp@ufu.br", "senha":"12412312523"}'
    # criarUsuario(usuario)

    def criarAeroporto(self, json_aeroporto):
        aeroporto = Aeroporto.from_json(json_aeroporto)
        self.aeroportoDAO.insertAeroporto(aeroporto)

    # # aeroporto = '{"id":"3","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}'
    # aeroporto2 = '{"nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}'
    # # criarAeroporto(aeroporto)
    # criarAeroporto(aeroporto2)

    def criarNovoVoo(self, json_voo):
        voo = Voo.from_json(json_voo)
        self.vooDAO.insertVoo(voo)

    ''' Aqui precisa vir o aeroporto inteiro... então talvez seja mais fácil padronizar '''
    # json_voo = '{"id":"162", "partida":{"id":"40","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "destino":{"id":"39","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "diaPartida":"22/07/2023", "horarioPartida":"19:00",\
    #             "diaChegada":"25/11/2023", "horarioChegada":"12:00", "valor":"350.00" ,"passagens":"25"}'
    # criarNovoVoo(json_voo)
    # json_voo2 = '{"partida":{"id":"39","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "destino":{"id":"3","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "diaPartida":"22/07/2023", "horarioPartida":"19:00",\
    #             "diaChegada":"25/11/2023", "horarioChegada":"14:00", "valor":"150.00" ,"passagens":"25"}'
    # criarNovoVoo(json_voo2)

    def venderPassagem(self, novaPassagem_json):
        passagem = Passagem.from_json(novaPassagem_json)
        self.passagemDAO.insertPassagem(passagem)

    ''' Aqui onde era o idVoo, se pá a gente pode sempre chamar de "viagem", pq senão quebra o dicionário '''
    # novaPassagem_json1 = '{"id":"2","viagem":"16", "nomePassageiro":"nome", "cpf":"11111111111"}'
    # venderPassagem(novaPassagem_json1)
    # novaPassagem_json = '{"viagem":"16", "nomePassageiro":"nome", "cpf":"11111111111"}'
    # venderPassagem(novaPassagem_json)

    ## Deletes
    ''' NOTA: COLOAR ENTRADA EM JSON '''
    def deletePassagem(self, idPassagem):
        passagem = self.passagemDAO.getPassagemById(idPassagem)
        voo = self.vooDAO.getVooById(passagem.getIdVoo())
        # deixando um lugar disponivel no voo
        voo.setQtLugaresDisponiveis(voo.getQtLugaresDisponiveis() + 1)
        self.vooDAO.updateVooById(voo)
        self.passagemDAO.deletePassagemByIDs([idPassagem])

    # deletePassagem(2)

    ''' NOTA: COLOAR ENTRADA EM JSON '''
    def deleteVoo(self, idVoo):
        # delete passagens
        self.vooDAO.deleteVooByIDs([idVoo])

    # deleteVoo(16)

    ''' NOTA: COLOAR ENTRADA EM JSON '''
    def deleteAeroporto(self, idAeroporto):
        #delete voos e passagens
        self.aeroportoDAO.deleteAeroportoByIDs([idAeroporto])

    # deleteAeroporto(3)

    ''' NOTA: COLOAR ENTRADA EM JSON '''
    def deleteUsuario(self, idUsuario):
        self.usuarioDAO.deleteUsersByIDs([idUsuario])

    # deleteUsuario(70)

    ## Updates

    def updateVoo(self, json_voo):
        voo = Voo.from_json(json_voo)
        
        print("################### aap.py from json ################")
        print("voo",voo)
        voo = self.vooDAO.updateVooById(voo)
        
        print("################### aap.py updateid ################")
        print("voo",voo)

    ''' No aeroporto não faz diferença se tá só a id ou se tá o object inteiro. É só 1 linha que se altera,
        mas daí preciso saber certinho como ele vai vir '''
    # json_voo = '{"id":"45", "partida":{"id":"40","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "destino":{"id":"42","nomeAeroporto":"congonhas","cidade":"uberlandia", "estado":"MG"}, "diaPartida":"01/07/2023", "horarioPartida":"19:00",\
    #             "diaChegada":"05/11/2023", "horarioChegada":"12:00", "valor":"250.00" ,"passagens":"0"}'
    # updateVoo(json_voo)


    ## Gets
    def listarAeroportos(self):
        aeroportos = self.aeroportoDAO.getTbAeroporto()
        aeroportos_json = []
        for aeroporto in aeroportos:
            aeroporto_json = aeroporto.to_json()
            aeroportos_json.append(json.loads(aeroporto_json))
        return json.dumps(aeroportos_json)

    # print(json.dumps(listarAeroportos(), indent=2))

    def listarVoos(self):
        voos = self.vooDAO.getTbVoo()
        voos_json = []
        for voo in voos:
            voos_json.append(json.loads(self.getVooJson(voo)))
        return json.dumps(voos_json)
    ''' exemplo da lista total dos voos ordenado por preço '''
    # # print(sortJsonArrayByKey(listarVoos(),'valor'))
    # print(json.dumps(sortJsonArrayByKey(listarVoos(),'valor'), indent=2))

    def listarVoosDisponiveis(self, nPessoas=0):
        voos = self.vooDAO.getTbVoo()
        voos_json = []
        for voo in voos:
            if(voo.getQtLugaresDisponiveis() > nPessoas):
                voos_json.append(json.loads(self.getVooJson(voo)))
        return json.dumps(voos_json)

    # print(sortJsonArrayByKey(listarVoosDisponiveis(),'valor'))

    # print(listarVoosDisponiveis())

    ''' Objeto das passagens com o nome do passageiro e sem o valor na viagem '''
    #passagens
    # {id:"1",nomePassageiro:"Joao", cpf:"1111111111", viagem:{id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00"}}
    def listarPassagens(self):
        passagens = self.passagemDAO.getTbPassagem()
        passagens_json = []
        for passagem in passagens:
            voo = self.vooDAO.getVooById(passagem.getIdVoo())
            viagem = json.loads(self.getVooJson(voo))
            del viagem['passagens']
            passagem.setIdVoo(viagem)
            passagem_json = json.loads(passagem.to_json())

            passagens_json.append(passagem_json)
        return json.dumps(passagens_json)

    # print(listarPassagens())