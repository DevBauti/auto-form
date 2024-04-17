import pandas as pd
from selenium import webdriver

#set
driver = webdriver.Firefox()
driver.get('https://forms.gle/dvCcGFRaiWCzoeLd6')
driver.implicitly_wait(0.5)

#read document 
df = pd.read_csv(r'C:\\Users\\devba\\Desktop\\utilidades\\lista.csv', delimiter=",")
#itertion
for _,d in df.iterrows():
    # searh element and load data
    driver.find_element("xpath","/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(d[0])
    driver.find_element("xpath","/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(d[1])
    driver.find_element("xpath","/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(d[2])
    driver.find_element("xpath","/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(d[3])
    driver.find_element("xpath","/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(d[4])
    driver.find_element("xpath","/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div").click()
    #Reload
    driver.get('https://forms.gle/dvCcGFRaiWCzoeLd6')

#end
print('termino la carga')
driver.implicitly_wait(5)
driver.quit()