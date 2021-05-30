from selenium.webdriver import Firefox
from time import sleep




def find_by_text(navegador, tag, text):
    """Encontra o elemento com o texto 'text',

    Argumentos:
        - navegador = Instancia do browser [Firefox, Chrome, ...]
        - texto = conteúdo que deve estar na tag
        - tag = tag onde o texto será procurado
    """
    elementos = navegador.find_elements_by_tag_name(tag) #retorna lista
    for elemento in elementos:
        if elemento.text == text:
            return elemento

def find_by_href(navegador, link):  
    """Encontra o elemento 'a' com o link 'link',

      Argumentos:
         - navegador = Instancia do browser [Firefox, Chrome, ...]
         - link = link que será procurado em todas as tags 'a'
    """
    elementos = navegador.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento




url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

#elemento_ddg = find_by_text(navegador, 'li', 'DuckDuckGo')

elemento_ddg = find_by_href(navegador, 'ddg')
elemento_ddg.get_attribute('href')

