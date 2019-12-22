import time
import threading
import os
import sys
import itertools
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

done = False
def wait():
    for c in itertools.cycle(['+', '-', '*', '/']):
        if done:
           break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.2)

t = threading.Thread(target=wait)
t.start()

chrome_options = Options()  
chrome_options.add_argument("--headless")  

browser = webdriver.Chrome('./chromedriver',options=chrome_options)
browser.get('http://www.google.com/search?q=premier+league')

elem = browser.find_element_by_xpath('//*[@id="sports-app"]/div/div[2]/div/div/div/ol/li[3]')
total_height = elem.size["height"]+1000
browser.set_window_size(800, total_height)
elem.click()
time.sleep(1)
browser.save_screenshot('standing.png')
os.system("open standing.png ; /usr/bin/osascript -e 'tell application \"Preview\"' -e \"activate\" -e 'tell application \"System Events\"' -e 'keystroke \"f\" using {control down, command down}' -e \"end tell\" -e \"end tell\"")
browser.quit()
done = True
