from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/aula_05_a.html'

navegador = Firefox()

navegador.get(url)

div_python = navegador.find_element_by_id('python')

div_hk = navegador.find_element_by_id('haskell')

print(div_hk.text)


