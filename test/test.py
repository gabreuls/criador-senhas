import sys
sys.path.insert(0,'./src')

import importlib
from unittest.mock import patch
import main 

class TesteGeradorSenha:
    
    @patch('main.random.randint')
    @patch('main.random.choice')
    def teste_senha_tem_12_caracteres(self, mock_choice, mock_randint):
        
        mock_randint.side_effect = [1, 2, 3, 4] * 3 
        mock_choice.return_value = 'a'
        
        importlib.reload(main)
        
        assert len(main.senha) == 12
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_minuscula(self, mock_choice):
        
        letras_minusculas = main.letras_minusculas
        
        for char in ['a', 'm', 'z']:
            assert char in letras_minusculas
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_maiuscula(self, mock_choice):
        
        letras_maiusculas = main.letras_maiusculas
        
        for char in ['A', 'Z', 'M']:
            assert char in letras_maiusculas
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_numeros(self, mock_choice):
        
        numeros = main.numeros
        
        for num in ['0', '5', '9']:
            assert num in numeros
    
    @patch('main.random.choice')
    def teste_caracteres_permitidos_simbolos(self, mock_choice):
        
        simbolos = main.simbolos
        
        for sym in ['@', '#', '!']:
            assert sym in simbolos
    
    @patch('main.random.randint')
    def teste_loop_executa_12_vezes(self, mock_randint):
        
        mock_randint.return_value = 1
        
        with patch('main.random.choice') as mock_choice:
            mock_choice.return_value = 'a'
            importlib.reload(main)
        
        assert mock_randint.call_count == 12
    
    def teste_conjuntos_nao_estao_vazios(self):
        
        assert len(main.letras_minusculas) > 0
        assert len(main.letras_maiusculas) > 0
        assert len(main.numeros) > 0
        assert len(main.simbolos) > 0
    
    def teste_senha_e_string(self):
        
        importlib.reload(main)
        
        assert isinstance(main.senha, str)

def teste_geracao_sem_mocks():
    
    for _ in range(10):
        importlib.reload(main)
        
        assert len(main.senha) == 12
        
        conjuntos_validos = (
            main.letras_minusculas +
            main.letras_maiusculas +
            main.numeros +
            main.simbolos
        )
        
        for char in main.senha:
            assert char in conjuntos_validos