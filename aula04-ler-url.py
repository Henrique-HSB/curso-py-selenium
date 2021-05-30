from selenium.webdriver import Firefox
from urllib.parse import urlparse # biblioteca para ler o endereco da pagina

url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'

navegador = Firefox()

navegador.get(url)

url_parseada = urlparse(browser.current_url) #  obtem url parcionada a pagina atual
