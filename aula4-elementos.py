from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

lista_n_ordenada = navegador.find_elements_by_tag_name('ul') #1

lis = lista_n_ordenada.find_elements_by_tag_name('li') #2

lis[0].find_element_by_tag_name('a').text #3

print(lis[0].txt)

"""
1- buscamos 'ul' da pagina html
2- buscamos todos 'li'
3- no primeiro 'li', buscamos 'a' e pegamos seu texto


ul
	li
		a
			texto
		a
	li
ul

"""

