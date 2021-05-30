from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://curso-python-selenium.netlify.app/aula_05.html'

navegador = Firefox()

navegador.get(url)

#nome, email, senha, telefone, btn

sleep(2)

def preenche__form(nome, email, senha, telefone):
    navegador.find_element_by_name('nome').send_keys(nome)
    navegador.find_element_by_name('email').send_keys(email)
    navegador.find_element_by_name('senha').send_keys(senha)
    navegador.find_element_by_name('telefone').send_keys(telefone)
    navegador.find_element_by_name('btn').click()

estrutura = {    
    'nome':'jao',
    'email':'asd@asd.asd',
    'senha':'102030',
    'telefone':'987654321' 
}

preenche__form(**estrutura)

sleep(2)




url_parsead = urlparse(navegador.current_url)

lista_url = url_parsead.query.split('&') #realixa uma lista onde cada item é separado por '&'

texto_resultado = navegador.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"") #troca as '' por ""

dic_result = loads(resultado_arrumado)

assert dic_result == estrutura

print(url_parsead)