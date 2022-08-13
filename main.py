import json
import sys
import time
from time import sleep

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By


class Dv:
    def __init__(self, driver_income=None):
        self.driver = driver_income

    def window_fix(self):
        self.driver.maximize_window()

    def launch(self, path: str = ''):
        self.driver.get(path)

    def css_send(self, path: str = '', txt: str = ''):
        self.driver.find_element(By.CSS_SELECTOR, path).send_keys(txt)

    def css_click(self, path: str = '') -> int:
        self.driver.find_element(By.CSS_SELECTOR, path).click()
        return 1

    def xpath_click(self, path: str = ''):
        self.driver.find_element(By.XPATH, path).click()
        return 1


if __name__ == '__main__':
    driver = webdriver.Chrome()

    dr = Dv(driver)

    dr.launch('https://www.instagram.com/accounts/login/')
    dr.window_fix()
    sleep(15)
    # dr.css_click('.bIiDR')
    sleep(10)
    dr.css_send('#loginForm > div > div:nth-child(1) > div > label > input', 'username')
    sleep(1)
    dr.css_send('#loginForm > div > div:nth-child(2) > div > label > input', 'pass')
    sleep(1)
    dr.css_click('#loginForm > div > div:nth-child(3)')
    sleep(10)
    dr.css_click('.cmbtv > button')
    sleep(10)
    dr.css_click('._a9-v > div:nth-child(3) > button:nth-child(2)')

    start_at = 188
    total = 5000
    time_p = time.time()
    sv_is = (total - start_at)
    sv_i = abs((total - start_at) - total)
    with open('story.json', 'r') as read:
        story = json.load(read)
    for i in range(sv_i):
        link = f'www.boredhamster.com/collection/{sv_i}/'
        desc = f'{link}\n {story[f"{sv_i}"]} \n#bored_hamster \n#boredhamster \n#bored_hamster_NFT \n#bored_NFT \n#hamster_NFT \n#NFT_hamster \n#NFT_bored \n#NFT_bored_hamster \n#NFT \n#NFTs \n#NFT_collection \n#NFT_collection_bored_hamster \n#hamster_collection \n#NFT_hamster_collection \n#hamster \n#nft_project \n#bored_hamster_project \n#NFTart \n#crypto \n#NFT_giveaway \n#NFTcommunity \n#NFTcollectors \n#openseaNFT \n#NFTtmarketplace \n#NFTdrop \n#NFTshill \n#NFTsale \n#NFTgallery \n#{sv_i}'
        sleep(5)
        dr.css_click('._acus > div:nth-child(3) > div >button')
        sleep(5)
        dr.css_click('._ac2r > div:nth-child(1) > div > div > div:nth-child(3) > div > button')
        sleep(6)
        print(f'E:\\Python\\NFT-Generator\\old_shits\\images\\{sv_i}.png')
        pyautogui.write(f'E:\\Python\\NFT-Generator\\old_shits\\images\\{sv_i}.png', interval=0.1)
        pyautogui.press('enter')
        sleep(2)
        dr.css_click('._ac76 > div:nth-child(3) > div > button')
        sleep(2)
        dr.css_click('._ac76 > div:nth-child(3) > div > button')
        sleep(2)
        dr.css_send('._ac2w > div > div:nth-child(2) > div:nth-child(1) > textarea', f'{desc}')
        sleep(2)
        dr.css_click('._ac76 > div:nth-child(3) > div > button')
        sleep(20)
        dr.css_click('.hwddc3l5 > div > div:nth-child(1) > div:nth-child(2) > div > div')
        time_d = time.time()
        sv_i += 1
        while time.time() - time_d < 40:
            sys.stdout.write(f'\r {sv_i}/{total} time : {time.time() - time_p:.4f} wait for next : {time.time() - time_d:.4f}')

