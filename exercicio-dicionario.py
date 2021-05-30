from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

ps = navegador.find_elements_by_tag_name('p')
h1 = navegador.find_element_by_tag_name('h1').text

dicionario_de_atributos = {}

for p in ps:
    dicionario_de_atributos.update(
        {p.get_attribute('atributo'): p.text}
    )

print({h1: dicionario_de_atributos})

"""
outra solucao possiveel:

for p in ps:
    diciionario_de_atributos[p.get_attribute('atributo')]= p.text

"""

"""
mais uma solução com o zip (junta os elementos)

attrs = []
texts = []

for p in ps:
    attrs.append(p.get_atribute('atributo'))

for p in ps:
    texts.append(p.text)

print({h1:dict(zip(attrs, text))})
"""



 