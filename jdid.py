import requests,random,json,os, time,string
cwd = os.getcwd()
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
# brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver_path= f"{cwd}\\chromedriver.exe"
firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')

firefox_options.headless = False
firefox_options.add_argument('--disable-setuid-sandbox')
firefox_options.add_argument('disable-infobars')
firefox_options.add_argument('--ignore-certifcate-errors')
firefox_options.add_argument('--ignore-certifcate-errors-spki-list')
firefox_options.add_argument("--mute-audio")
firefox_options.add_argument("--incognito")
firefox_options.add_argument('--no-first-run')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--disable-infobars")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-popup-blocking")
firefox_options.add_argument('--log-level=3') 
 
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_experimental_option("useAutomationExtension", False)
firefox_options.add_experimental_option("excludeSwitches",["enable-automation"])
firefox_options.add_experimental_option('excludeSwitches', ['enable-logging'])
firefox_options.add_argument('--disable-notifications')
firefox_options.add_argument('--disable-gpu')
from selenium.webdriver.common.action_chains import ActionChains
# firefox_options.binary_location = brave_path
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)
failed = []
success = []

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 650, "pixelRatio": 3.4 },
    }
def xpath_el(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))

    return browser.execute_script("arguments[0].click();", element_all)

def xpath_ex(el):
    element_all = wait(browser,0.3).until(EC.presence_of_element_located((By.XPATH, el)))
    browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_type(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)
def xpath_fast(el):
    element_all = wait(browser,1).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_exs(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    element_all.send_keys(Keys.ENTER)

def xpath_id(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'//input[@{el}]'))).send_keys(word)

def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 

def automation_store(store,path):
    try:
        browser.get(store)
        name_product = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="skuName"]'))).text
        print(f"[*] Produk: {name_product}")
        xpath_el('//*[@class="sea-button type-jdid size-xxl level-main   clickable"]')
        xpath_el('//*[@class="pay-title normal" and contains(text(),"COD")]')
        price = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//*[@class="p-total c-red f-fs18"]'))).text
        print(f"[*] Harga: {price}")
        
        xpath_el('//*[@clstag="pageclick|keycount|epi_confirm_submitOrder|0"]')
        xpath_el('//*[@clstag="pageclick|keycount|epi_cart_confirm_submit_order_ok_2016120713|0"]')
        no_order = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="tip-box-info"]/p[1]/a[1]'))).text
        print(f"[*] Berhasil membeli! No Order: {no_order}")
        with open('success.txt','a+') as f:
            f.write(f'{no_order}|{path}\n')
    except:
        print(f'[*] Gagal Membeli Product!')
    
def login(store):
    global browser
    firefox_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.1.12 Safari/537.3")
    browser = webdriver.Chrome(options=firefox_options,executable_path=driver_path)
    browser.execute_script("document.body.style.zoom='zoom 90%'")
    path = os.listdir(f"{cwd}")
    for acc in path:
        
        if "json" in acc:
            browser.get("https://www.jd.id/")
            with open(acc, 'r') as cookiesfile:
                cookies = json.load(cookiesfile)
            for cookie in cookies:
                browser.add_cookie(cookie)
            browser.get("https://www.jd.id/")
            automation_store(store,path)
            
   
if __name__ == '__main__':
    
    print("[*] Auto Buy JD ID!")
    store = input('[*] Input URL Product: ')
    os.listdir(f"{cwd}")
    login(store)