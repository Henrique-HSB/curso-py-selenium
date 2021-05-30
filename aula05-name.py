from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_05_c.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

def melhor_filme( filme, email, telefone):
    # Encontra os elementos e preenche o formulario automatico
    navegador.find_element_by_name('filme').send_keys(filme)
    navegador.find_element_by_name('email').send_keys(email)
    navegador.find_element_by_name('telefone').send_keys(telefone)
    navegador.find_element_by_name('enviar').click()


melhor_filme('parasita','asd@asd.das','(011)987654321')


"""
#substituido pela funcao (def) melhor_filme

filme = navegador.find_element_by_name('filme').send_keys('parasita')

email = navegador.find_element_by_name('email')

email.send_keys('asd@asd.das')

telefone = navegador.find_element_by_name('telefone')

telefone.send_keys('(011)987654321')

navegador.find_element_by_name('enviar').click()
"""