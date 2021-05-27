from encodings import utf_8
import selenium.webdriver
import time
import os
from colorama import Fore, Back, Style

#initializing
os.system('mode con: cols=80 lines=20')
os.system('title [void] by vanta')
spacer = "       "
url = "https://duckduckgo.com/?q="

#printing ui
def ui():
    os.system("cls")
    print(Fore.LIGHTWHITE_EX+ """

                                   ┬  ┬┌─┐┬┌┬┐""" + Fore.LIGHTBLACK_EX + """
                                   └┐┌┘│ ││ ││""" + Fore.WHITE + """
                                    └┘ └─┘┴─┴┘
                                        by vanta
                  """)
    print(Style.RESET_ALL)
ui()

#setting variables
dork = input(spacer + "$ dork: ")
strpages = input(spacer + "$ pages: ")
pages = int(strpages)

#setting driver and url
driver = selenium.webdriver.Firefox()
driver.get(url + dork + "&kp=-2")
for x in range(pages):
    try:
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_class_name("result--more__btn").click()
    except:
        break
print(spacer + "$ dork opened")
time.sleep(2)

#getting links/ips
ui()
print(spacer + f"$ scanning {dork}...")
total = 0
for element in driver.find_elements_by_xpath("//div[contains(@class,'result__extras__url')]/a[contains(@class,'result__url js-result-extras-url')]"):
    link = element.get_attribute('href')
    date = time.strftime("%Y.%m.%d-%H_%M_%S", time.localtime())
    if "https://duckduckgo.com" not in link:
        total += 1
        output = open(f"VOID {date}.txt","a")
        #print(spacer + f"$ found: {link}")
        output.write(f"{link}\n")
print(spacer + f"$ scan finished [{total} found]")
print(spacer + f"$ exported in {output.name}")
open = input(spacer + "$ open all? (y/n): ")   
if open == "y":
    for element in driver.find_elements_by_xpath("//div[contains(@class,'result__extras__url')]/a[contains(@class,'result__url js-result-extras-url')]"):
        link = element.get_attribute('href')
        if "https://duckduckgo.com" not in link:
            driver.execute_script(f'''window.open("{link}","_blank");''')
            print(spacer + f"$ link opened in new tab")
if open == "n":
    print(spacer + f"$ thanks for using void.")
