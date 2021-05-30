from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/aula_05_b.html'

navegador = Firefox()

navegador.get(url)

topico  = navegador.find_element_by_class_name('topico')

linguagens = navegador.find_elements_by_class_name('linguagens')

for linguagen in linguagens:
    print(
        (linguagen.find_element_by_tag_name('h2').text,
         linguagen.find_element_by_tag_name('p').text)
        )


