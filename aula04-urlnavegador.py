"""
1- pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2- Navegar ate o exercicio 3
    achar a url do exercicio 3 e ir ate la
"""

from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse # biblioteca para ler o endereço da pagina
from pprint import pprint

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04.html')

def get_links(browser, elemento): # dicionario
    """
    Pega todos os links dentro de um elemento
        - browser = a instancia do navegador
        - element = webelemnt [aide, main, body, ul, ol]
    """
    resultado = {} # dicionario vazio
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href') # dicionario recebe os valores
    return resultado



sleep(1)

#Parte 1

aulas = get_links(browser, 'aside')#substitui tudo das proximas linhas
print(aulas)

#pprint(get_links(browser, 'aside')) 

    
"""
    #   SUBSTITUIDO PELA FUNÇÃO DEF GET_LINK
    aside = browser.find_element_by_tag_name('aside') # aside é a lateral da pagina

    aside_ancoras = aside.find_elements_by_tag_name('a')

    resultado_1 = {} # dicionario vazio

    for ancora in aside_ancoras:
        resultado_1[ancora.text] = ancora.get_attribute('href') # dicionario recebe os calores

    pprint(resultado_1)

    sleep(1)

        #browser.get(resultado_1['Aula 3']) # acessa o link da aula 3
"""
    


    # Parte 2

    # main = browser.find_element_by_tag_name('main')

exercicios = get_links(browser, 'main')

pprint(exercicios)

browser.get(exercicios['Exercício 3']) #acessa no dicionario 'exercicios', o elemento 'Exercicio 3'

url_parseada = urlparse(browser.current_url) #  obtem a pagina atual
print(url_parseada)









# exercicio joogo unicornio

# Primeira Tarefa clicar em 'Começar por aqui'
sleep(1)

links_pag = get_links(browser, 'main')#substitui tudo das proximas linhas
pprint(links_pag)
browser.get(links_pag['Começar por aqui'])





# Segunda tarefa 'Responda ao contrário'

sleep(1)


links_pag = get_links(browser, 'main')#substitui tudo das proximas linhas
pprint(links_pag)
browser.get(links_pag['page_2.html'])