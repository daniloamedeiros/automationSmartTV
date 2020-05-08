from selenium import webdriver

driver = webdriver.Chrome("venv/chromedriver.exe")
driver.maximize_window()
driver.get("http://tv.globoplay.com.br/v2/release")
driver.implicitly_wait(10)

menu_categoria = driver.find_element_by_xpath("//a[text()='Categorias']")
menu_categoria.click()

driver.implicitly_wait(10)
categoria_novelas = driver.find_element_by_xpath("//body/div[@id='root']/div[contains(@class,'page-categories')]/div[contains(@class,'content-container')]/div[contains(@class,'with-animation')]/div[1]")
categoria_novelas.click()

driver.implicitly_wait(10)
primeira_novela = driver.find_element_by_xpath("//div[contains(@class,'category_poster with-border-radius category_poster__selected-item')]")
primeira_novela.click()