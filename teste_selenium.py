#Analisar a versao do Driver do google em: chrome://settings/help
#Baixar o Driver do Chrome usado em: https://chromedriver.chromium.org/downloads (salvar na mesma pasta do projeto)

#instalar o pacote  >> pip install selenium    (conexao com a web)
#instalar o pacote  >> pip install PySimpleGUI (interface grafica)
#instalar o pacote  >> pip install PyInstaller (criar executavel)

#rodar na pasta do arquivo: pyinstaller yourscript.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PySimpleGUI import PySimpleGUI as sg

class telaPython:
	"""Classe para o encapsulamento da lógica da tela"""
	def __init__(self):   #defini as informações inicial que precisa dentro da classe
		#Laytout
		sg.change_look_and_feel('Topanga')
		layout = [
		   [sg.Text('Usuario',size=(5,1)), sg.Input(key='usuario', size=(15,1))],
		   [sg.Text('Senha',size=(5,1)), sg.Input(key='senha',password_char='*', size=(15,1))],
		   [sg.Text('Lote',size=(5,1)), sg.Input(key='lote', size=(15,1))],
		   #[sg.Checkbox('Salvar o login?')],
		   [sg.Button('Entrar')],
		   [sg.Output(size=(30,20))]
		]
		#Janela
		self.janela = sg.Window('Tela de Login').layout(layout)

	def Iniciar(self):
	#Ler os eventos
		while True:
			eventos, valores = self.janela.read()
			if eventos == sg.WINDOW_CLOSED:
				break
			if eventos == 'Entrar':
				if valores['usuario'] == 'amanda' and valores['senha'] == '12':
					lote = valores['lote'] 
					#lote = self.values['lote']
					print(f'Lote(s) listado(s): {lote}')
					

tela = telaPython()
tela.Iniciar()


#-- driver = webdriver.Chrome(executable_path=r'C:\Users\Amanda\Desktop\MESTRADO USP\PYTHON\chromedriver_win32\chromedriver.exe')
#-- driver.get('https://www.google.com.br')

#driver.find_element_by_name("q").send_keys("Bolo Chocolate").send_keys(Keys.RETURN)
#-- driver.find_element_by_name("q").send_keys("Como fazer miojo" + Keys.RETURN)

#driver.find_element_by_name("email").send_keys("email.da.amanda1092@gmail.com");
#driver.find_element_by_name("pass").send_keys("senha_segura")



#driver.find_element_by_name("login").Click();

#driver.find_element_by_name("q").send_keys(Keys.RETURN)
