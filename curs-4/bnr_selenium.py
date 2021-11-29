from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')
table_text = table.text

lista = table_text.split('\n')
#print(lista)


header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split('\n')
dictionar = {i: [] for i in header}
#print(header.text.split('\n'))

for j in range(len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
    print()
print(dictionar)

df = pd.DataFrame(dictionar)
df.to_csv(".\\curs-4\\BNR_all_data.csv")

time.sleep(5)
browser.close()

