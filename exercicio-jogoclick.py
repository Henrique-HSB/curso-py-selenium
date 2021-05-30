from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

a = navegador.find_element_by_tag_name('a')
ps = navegador.find_elements_by_tag_name('p')
pss = (ps[-1].text)
print(pss[-1])
p=' '


while p[-1] != pss[-1]:
   a.click()
   b = navegador.find_elements_by_tag_name('p')
   p=(b[-1].text)
  
print("robo ganhou")

navegador.quit()

"""
outra opção

a = navegador.find_element_by_tag_name('a')

resultado = 'Você ganhou'
msg=''

while resultado not in msg:
    a.click()
    msg=navegador.find_elements_by_tag_name('p')[-1].textA

"""