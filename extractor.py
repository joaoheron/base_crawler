import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import vars

def enable_download_headless(browser, download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def build_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_experimental_option("prefs", {
            "download.default_directory": 'vars.download',
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
    })
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--headless=True')

    return chrome_options

def build_firefox_options():
    print('Loading...')

def download_file(url, download_dir=vars.download_dir, timeout=10, browser='chrome', filename=vars.filename, fileformat=None, sq=True):
    print('Starting Crawler...')
    if 'chrome' in browser:
        # build options
        chrome_options = build_chrome_options()
        # initialize webdriver
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=vars.chromedriver_path)
        # set download folder
        enable_download_headless(driver, download_dir)
        # navigate to url and downloads spreadsheet
        driver.get(url)
        print('Download of the file has began.')
        if sq:
            if os.path.exists(download_dir + filename):
                os.remove(download_dir + filename)
            driver.save_screenshot(download_dir + filename)
        time.sleep(int(timeout))
        print('Download of the file has been finished.')
        driver.close
        driver.quit
