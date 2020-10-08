# coding: utf-8
from personalLib import isEmpty


class Coordenador:

	def __init__(self,nome,cpf,idade):
		self.nome = nome
		self.cpf = cpf
		self.idade = idade

	def dados_coodernador(self):
		self.validar_dados()			
		
		return "%s (%d anos), CPF: %s" %(self.nome,self.idade,self.cpf)
	

	def validar_dados(self):
		if isEmpty(self.nome):
			raise Exception("O campo nome do coordenador é obrigatório")
		
		if isEmpty(self.cpf):
			raise Exception("O campo CPF do coordenador é obrigatório")
		
		if (self.idade <= 0):
			raise Exception("O campo idade do coordenador é obrigatório")
	


class Departamento:

	def __init__(self, nome,sigla,localizacao,coordenador):
		self.nome = nome
		self.sigla = sigla
		self.localizacao = localizacao
		self.coordenador = coordenador

	def dados_departamento(self):
		self.validar_dados();

		_sigla =  " (%s)"%(self.sigla) if not isEmpty(self.sigla) else "" 

		dados = "%s%s\n" % (self.nome,_sigla)
		dados += "Localizado em %s\n" % (self.localizacao)
		dados += "Coordernado por %s\n" % (self.coordenador.dados_coodernador())
		return dados;	

	def validar_dados(self):
		if isEmpty(self.nome):
			raise Exception("O campo nome do departamento é obrigatório")
				
		if isEmpty(self.localizacao):
			raise Exception("O campo localizacao do departamento é obrigatório")