from connectDB import ConectaBD
# from flask_app.classes.Usuario import Usuario
from classes.Aviao import Aviao
# from flask_app.classes.Aeroporto import Aeroporto
# from flask_app.classes.Voo import Voo
# from flask_app.classes.Passagem import Passagem

# from flask_app.classesDAO.UsuarioDAO import UsuarioDAO
from classesDAO.AviaoDAO import AviaoDAO
# from flask_app.classesDAO.AeroportoDAO import AeroportoDAO
# from flask_app.classesDAO.VooDAO import VooDAO
# from flask_app.classesDAO.PassagemDAO import PassagemDAO
import logging

conectaBD = ConectaBD()
aviaoDAO = AviaoDAO(conectaBD)

# aviao = Aviao(idAviao="3", qtAssentosEconomicos=3, qtAssentosExecutivos=5)
aviao = Aviao(qtAssentosEconomicos=3, qtAssentosExecutivos=5)
# print(aviao.__repr__())
# aviaoDAO.insertAviao(aviao)

aviao = Aviao(idAviao="5", qtAssentosEconomicos=12, qtAssentosExecutivos=24)
# print(aviao.to_json())
aviaoDAO.updateAviaoById(aviao)
# rAviao = aviaoDAO.getAviaoById(2)
# aviaoDAO.deleteAviaoByIDs([4,6,7])

avioes = aviaoDAO.getTbAviao();
for aviao in avioes:
    print(aviao)
