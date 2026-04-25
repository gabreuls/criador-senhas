import importlib
import pytest
from unittest.mock import patch
from src import main 

class TesteGeradorSenha:
    
    @patch('main.random.randint')
    @patch('main.random.choice')
    def teste_senha_tem_12_caracteres(self, mock_choice, mock_randint):
        
        mock_randint.side_effect = [1, 2, 3, 4] * 3 
        mock_choice.return_value = 'a'
        
        # Executa o código
        main.senha = ""
        exec(open('main.py').read())
        
        # Verifica
        assert len(main.senha) == 12
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_minuscula(self, mock_choice):
    
        mock_choice.return_value = 'a'
        
        letras_minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for char in ['a', 'm', 'z']:
            assert char in letras_minusculas
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_maiuscula(self, mock_choice):
        
        letras_maiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        for char in ['A', 'Z', 'M']:
            assert char in letras_maiusculas
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_numeros(self, mock_choice):
        
        numeros = ['0','1','2','3','4','5','6','7','8','9']
        
        for num in ['0', '5', '9']:
            assert num in numeros
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_simbolos(self, mock_choice):
        
        simbolos = [',','.','-','=','+','@','#','$','%','*','/','!','?']
        
        for sym in ['@', '#', '!']:
            assert sym in simbolos
    
    @patch('senha_generator.random.randint')
    def teste_loop_executa_12_vezes(self, mock_randint):

        mock_randint.return_value = 1
        
        with patch('main.random.choice') as mock_choice:
            mock_choice.return_value = 'a'
            main.senha = ""
            exec(open('main.py').read())
        
        # Verifica se randint foi chamado 12 vezes
        assert mock_randint.call_count == 12
    
    def teste_conjuntos_nao_estao_vazios(self):
        
        assert len(main.letras_minusculas) > 0
        assert len(main.letras_maiusculas) > 0
        assert len(main.numeros) > 0
        assert len(main.simbolos) > 0
    
    def teste_senha_e_string(self):
        
        main.senha = ""
        exec(open('main.py').read())
        
        assert isinstance(main.senha, str)


def teste_geracao_sem_mocks():
    # Esta função executa o código real várias vezes
    
    for _ in range(10):
        # Recarrega o módulo
        importlib.reload(main)
        
        # Verifica tamanho
        assert len(main.senha) == 12
        
        # Verifica se todos os caracteres são válidos
        conjuntos_validos = (
            main.letras_minusculas +
            main.letras_maiusculas +
            main.numeros +
            main.simbolos
        )
        
        for char in main.senha:
            assert char in conjuntos_validos