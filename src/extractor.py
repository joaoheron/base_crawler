import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.model import Action
from src.conf import actions_list
import src.vars as vars

def enable_download_headless(browser, download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def build_chrome_options(headless=True):
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
    # chrome_options.add_argument('--headless=' + str(headless))

    return chrome_options

def build_firefox_options():
    print('Loading...')

def extract(browser, timeout):
    driver = build_driver(browser, timeout)
    navigate(driver)

def build_driver(browser='chrome', timeout=30):
    print('Starting Crawler...')
    if 'chrome' in browser:
        # build options
        chrome_options = build_chrome_options()
        # initialize webdriver
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=vars.chromedriver_path)
        # set download folder
        enable_download_headless(driver, vars.download_dir)
        # maximize window
        driver.maximize_window()

        return driver
    elif 'firefox' in browser or 'gecko' in browser:
        print('Gecko Driver is no available yet.')
        
def download_file(url, download_dir=vars.download_dir, filename=vars.filename, fileformat=None, sq=True):
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

def navigate(driver):
    """ 
    function navigate()

    This function navigates through websites.

    Attributes: - driver
    """
    for action in actions_list:
        # Navigation and download actions
        if 'navigation' in action.action_type.lower() or 'download' in action.action_type.lower():
            driver.get(action.action_target)
        # Click actions
        elif 'click' in action.action_type.lower():
            if 'id' in action.action_selector_kind.lower():
                driver.find_element_by_id(action.action_target).click()
            elif 'name' in action.action_selector_kind.lower():
                driver.find_element_by_name(action.action_target).click()
            elif 'xpath' in action.action_selector_kind.lower():
                driver.find_element_by_xpath(action.action_target).click()
            elif 'partial_link_text' in action.action_selector_kind.lower():
                driver.find_element_by_partial_link_text(action.action_target).click()
            elif 'link_text' in action.action_selector_kind.lower():
                driver.find_element_by_link_text(action.action_target).click()
            elif 'tag_name' in action.action_selector_kind.lower():
                driver.find_element_by_tag_name(action.action_target).click()
            elif 'class_name' in action.action_selector_kind.lower():
                driver.find_element_by_class_name(action.action_target).click()
            elif 'selector' in action.action_selector_kind.lower():
                driver.find_element_by_css_selector(action.action_target).click()
        # Type actions
        elif 'type' in action.action_type:
            #  id, name, xpath, link_text, partial_link_text, tag_name, class_name, css_selector
            if 'id' in action.action_selector_kind.lower():
                driver.find_element_by_id(action.action_target).send_keys(action.type_text)
            elif 'name' in action.action_selector_kind.lower():
                driver.find_element_by_name(action.action_target).send_keys(action.type_text)
            elif 'xpath' in action.action_selector_kind.lower():
                driver.find_element_by_xpath(action.action_target).send_keys(action.type_text)
            elif 'partial_link_text' in action.action_selector_kind.lower():
                driver.find_element_by_partial_link_text(action.action_target).send_keys(action.type_text)
            elif 'link_text' in action.action_selector_kind.lower():
                driver.find_element_by_link_text(action.action_target).send_keys(action.type_text)
            elif 'tag_name' in action.action_selector_kind.lower():
                driver.find_element_by_tag_name(action.action_target).send_keys(action.type_text)
            elif 'class_name' in action.action_selector_kind.lower():
                driver.find_element_by_class_name(action.action_target).send_keys(action.type_text)
            elif 'selector' in action.action_selector_kind.lower():
                driver.find_element_by_css_selector(action.action_target).send_keys(action.type_text)
        # Hover actions
        elif 'hover' in action.action_type:
            print('hovered')
        # Drag and drop actions
        elif 'drag_and_drop' in action.action_type:
            print('drag and dropped')
