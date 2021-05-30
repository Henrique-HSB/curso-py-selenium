from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

a = navegador.find_element_by_tag_name('a')


#print(f'texto de a: {a.text}')
#print(f'texto de p: {p.text}')




for click in range(10): 
    p = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'texto de p: {p[-1].text} valor do click:{click}')
    print(f'Os valores sao iguais {p[-1].text == str(click)}')


#navegador.quit()