from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import os

if __name__ == "__main__":
    csv_file = []
    
    
    path_driver = os.path.join('file','chromedriver.exe')
    driver = webdriver.Chrome(executable_path = path_driver) 
    driver.get("https://covid19.gov.vn/")

    
    driver.switch_to.frame(1)


    target = driver.find_elements(By.XPATH,"/html/body/div[2]/div[1]/div")
    for data in target:
        cities = data.find_elements(By.CLASS_NAME,"city")
        totals = data.find_elements(By.CLASS_NAME,"total")
        todays = data.find_elements(By.CLASS_NAME,"daynow")
        dies = data.find_elements(By.CLASS_NAME,"die")


    list_cities = [city.text for city in cities]
    list_totals = [total.text for total in totals]
    list_today = [today.text for today in todays]
    list_dead = [dead.text for dead in dies]
    
    for i in range(len(list_cities)):
        row = "{},{},{},{}\n".format(list_cities[i],list_totals[i],list_today[i],list_dead[i])
        csv_file.append(row)


    today_ = (datetime.datetime.now()).strftime("%d%m%Y")
    thongkecovid19 = f"{today_}.csv"
    with open(os.path.join("csv",thongkecovid19),'w+',encoding='utf-8') as f:
        f.writelines(csv_file)
      
        
    driver.close()