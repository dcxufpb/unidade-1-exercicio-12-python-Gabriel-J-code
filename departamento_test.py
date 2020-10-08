# coding: utf-8

import departamento
import pytest


def verifica_campo_obrigatorio_objeto(mensagem_esperada, departamento):
    with pytest.raises(Exception) as excinfo:
        departamento.dados_departamento()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

NOME_DEPARTAMENTO = "Depart 1"
SIGLA = "D1"
LOCALIZACAO = "Local1"
NOME_COORDENADOR = "Coorde1"
CPF_COORDENADOR = "123456"
IDADE_COORDENADOR = 30

TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO = """Depart 1 (D1)
Localizado em Local1
Coordernado por Coorde1 (30 anos), CPF: 123456
"""

def test_departamento_completo():
	DEPARTAMENTO_COMPLETO = departamento.Departamento(NOME_DEPARTAMENTO,SIGLA,LOCALIZACAO,departamento.Coordenador(NOME_COORDENADOR,CPF_COORDENADOR,IDADE_COORDENADOR))
	assert(
		DEPARTAMENTO_COMPLETO.dados_departamento() == TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO
	)

TEXTO_ESPERADO_DEPARTAMENTO_SEM_SIGLA = """Depart 1
Localizado em Local1
Coordernado por Coorde1 (30 anos), CPF: 123456
"""

def test_departamento_sem_sigla():
	departamentoSemSigla = departamento.Departamento(NOME_DEPARTAMENTO, "", LOCALIZACAO, departamento.Coordenador(NOME_COORDENADOR,CPF_COORDENADOR, IDADE_COORDENADOR))
	assert( 
		departamentoSemSigla.dados_departamento() == (TEXTO_ESPERADO_DEPARTAMENTO_SEM_SIGLA)
	)



def test_departamento_sem_nome():
	departamentoSemNome = departamento.Departamento("", SIGLA, LOCALIZACAO, departamento.Coordenador(NOME_COORDENADOR,CPF_COORDENADOR, IDADE_COORDENADOR))
	verifica_campo_obrigatorio_objeto("O campo nome do departamento é obrigatório", departamentoSemNome)


def test_departamento_sem_localizacao():
	departamentoSemLocalizacao = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, "", departamento.Coordenador(NOME_COORDENADOR,CPF_COORDENADOR, IDADE_COORDENADOR))
	verifica_campo_obrigatorio_objeto("O campo localizacao do departamento é obrigatório", departamentoSemLocalizacao)


def test_coordenador_sem_nome():
	coordenadorSemNome = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, departamento.Coordenador("",CPF_COORDENADOR, IDADE_COORDENADOR))
	verifica_campo_obrigatorio_objeto("O campo nome do coordenador é obrigatório", coordenadorSemNome)


def test_coordenador_sem_cpf():
	coordenadorSemCPF = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, departamento.Coordenador(NOME_COORDENADOR,"", IDADE_COORDENADOR))
	verifica_campo_obrigatorio_objeto("O campo CPF do coordenador é obrigatório",coordenadorSemCPF)


def test_coordenador_sem_idade():
	coordenadorSemIdade = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, departamento.Coordenador(NOME_COORDENADOR,CPF_COORDENADOR, 0))
	verifica_campo_obrigatorio_objeto("O campo idade do coordenador é obrigatório",coordenadorSemIdade)
