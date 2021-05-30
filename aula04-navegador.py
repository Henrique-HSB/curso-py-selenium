from selenium.webdriver import Firefox
from time import sleep



def find_by_text(navegador, tag, text):
    """Encontra o elemento com o texto 'text',

    Argumentos:
        - navegador = Instancia do browser [Firefox, Chrome, ...]
        - texto = conteendo que deve estar na tag
        - tag = tag onde o texto sera procurado
    """
    elementos = navegador.find_elements_by_tag_name(tag) #retorna lista
    for elemento in elementos:
        if elemento.text == text:
            return elemento

def find_by_href(navegador, link):  
    """Encontra o elemento 'a' com o link 'link',

      Argumentos:
         - navegador = Instancia do browser [Firefox, Chrome, ...]
         - link = link que sera procurado em todas as tags 'a'
    """
    elementos = navegador.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento




url = 'https://curso-python-selenium.netlify.app/aula_04_b.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

nomes_das_caixas = ['um', 'dois','tres', 'quatro']

for nome in nomes_das_caixas:
    find_by_text(navegador, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(0.2)
    navegador.back()

for nome in nomes_das_caixas:
    sleep(0.2)
    navegador.forward()

   
#for texto in['um', 'dois', 'tres', 'quatro']:
    #find_by_text(navegador, 'div', texto).click()

