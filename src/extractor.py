import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.model import Action
from src.conf import actions_list
import src.vars as vars

def enable_download_headless(browser, download_dir):
    """ 
    method enable_download_headless()
        This method enables that a webdriver download files even if it's a headless webdriver.

    Attributes: 
        - browser: Selenium web driver.
        - download_dir: Folder to store the downloads.
    """
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def build_chrome_options(headless=True):
    """ 
    method build_chrome_options()
        This method builds options for Chrome Driver.

    Attributes: 
        - headless: Indicates if the driver will be headless (hidden).
    """
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
    chrome_options.add_argument('--headless=' + str(headless))

    return chrome_options

def build_firefox_options():
    """ 
    method build_firefox_options()
        This method builds options for Gecko Driver.

    Attributes: 
            - headless: Indicates if the driver will be headless (hidden).
    """
    print('build options for Gecko Driver is not available yet.')

def extract(browser, timeout):
    """ 
    method extract()
        This method builds a selenium webdriver and navigates through websites.

    Attributes: 
        - browser: Which browser will be instantiatated by Selenium (Google Chrome or Mozilla Firefox).
        - timeout: Amount of seconds the Selenium webdriver will use as it's own timeout.
    """
    verify_conf()
    driver = build_driver(browser, timeout)
    navigate(driver)

def verify_conf():
    # TODO Fazer um método de verificação
    try:
        for action in actions_list:
            print('Action ' + str(action) + ' verified.')
    except:
        raise

def build_driver(browser='chrome', timeout=30):
    """ 
    method build_driver()
        This method builds a selenium webdriver.

    Attributes: 
        - browser: Which browser will be instantiatated by Selenium (Google Chrome or Mozilla Firefox).
        - timeout: Amount of seconds the Selenium webdriver will use as it's own timeout.
    """
    print('Building Driver...')
    if 'chrome' in browser.lower() or 'google' in browser.lower():
        # build options
        chrome_options = build_chrome_options(False)
        # initialize webdriver
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=vars.chromedriver_path)
        # maximize window
        driver.maximize_window()

        return driver
    elif 'firefox' in browser.lower() or 'gecko' in browser.lower() or 'mozilla' in browser.lower():
        print('Gecko Driver is not available yet.')
        
def screenshot(driver, download_dir=vars.download_dir, filename=vars.filename, fileformat=None):
    """ 
    method screenshot()
        This method takes a Screenshot from the screen.

    Attributes: 
        - driver: Selenium web driver.
        - download_dir: Folder to store screenshot file.
        - filename: Screenshot's file name.
        - fileformat: Screenshot's file format.
    """
    if os.path.exists(download_dir + filename):
        os.remove(download_dir + filename)
    driver.save_screenshot(download_dir + filename)
    print('Screenshoted screen and saved file at ' + str(download_dir))

def return_by(string_by):
    """ 
    method return_by()

    Attributes: 
        - return_by: Selenium web driver.
    """
    if string_by == 'id':
        return By.ID
    elif string_by == 'name':
        return By.NAME
    elif string_by == 'xpath':
        return By.XPATH
    elif string_by == 'link_text':
        return By.LINK_TEXT
    elif string_by == 'partial_link_text':
        return By.PARTIAL_LINK_TEXT
    elif string_by == 'tag_name':
        return By.TAG_NAME
    elif string_by == 'class_name':
        return By.CLASS_NAME
    elif string_by == 'css_selector':
        return By.CSS_SELECTOR

def waitfor(driver, action):
    """ 
    method waitfor()
        This method navigates through websites executing every Action inside actions_list (from conf.py file).

    Attributes: 
        - driver: Selenium web driver.
        - action: Webdriver action object
    """
    # Wait for element
    if action.wait_for and action.wait_for_selector_kind:
        wait = WebDriverWait(driver, action.timeout)
        element = wait.until(ec.visibility_of_element_located((return_by(action.wait_for_selector_kind), action.wait_for)))
        # ActionChains(driver).move_to_element(element).perform()

def navigate(driver):
    """ 
    method navigate()
        This method navigates through websites executing every Action inside actions_list (from conf.py file).

    Attributes: 
        - driver: Selenium web driver.
    """
    for action in actions_list:
        try:
        # Action(description, action_type, action_target, action_selector_kind, wait_for, wait_for_selector_kind, keys, timeout)
            waitfor(driver, action)
            # Navigation Action
            if 'navigation' in action.action_type.lower() or 'navigate' in action.action_type.lower():
                driver.get(action.action_target)
            # Download Action
            elif 'download' in action.action_type.lower():
                enable_download_headless(driver, vars.download_dir)
                driver.get(action.action_target)
            # Goback Action
            elif 'goback' in action.action_type.lower():
                driver.execute_script("window.history.go(-1)")
            # Goforward Action
            elif 'goforward' in action.action_type.lower():
                driver.execute_script("window.history.go(+1)")
            # Implicit Wait Action
            elif 'wait' in action.action_type.lower() or 'w8' in action.action_type.lower():
                time.sleep(int(action.action_target))
            # Execute script
            elif 'execute' in action.action_type.lower():
                driver.execute_script(action.action_target)
            # New Window Action
            elif 'newwindow' in action.action_type.lower() or 'new_window' in action.action_type.lower():
                window_after = driver.window_handles[1]
                driver.switch_to_window(window_after)
            # Previous Window Action
            elif 'prevwindow' in action.action_type.lower() or 'prev_window' in action.action_type.lower() or 'previouswindows' in action.action_type.lower():
                window_prev = driver.window_handles[0]
                driver.switch_to_window(window_prev)
            # Switch Window Action
            elif 'switchwindow' in action.action_type.lower() or 'switch_window' in action.action_type.lower():
                window_switch = driver.window_handles[int(action.action_target)]
                driver.switch_to_window(window_switch)
            # Scroll Actions
            elif 'scroll' in action.action_type.lower() and action.action_target:
                driver.execute_script(str(action.action_target)f"window.scrollTo(%s,document.body.scrollHeight)")
            # Scroll Actions
            elif 'scrolldown' in action.action_type.lower() or 'scroll_down' in action.action_type.lower() or 'scroll_bottom' in action.action_type.lower():
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
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
            elif 'sendkeys' in action.action_type or 'send_keys' in action.action_type:
                if 'id' in action.action_selector_kind.lower():
                    driver.find_element_by_id(action.action_target).send_keys(action.keys)
                elif 'name' in action.action_selector_kind.lower():
                    driver.find_element_by_name(action.action_target).send_keys(action.keys)
                elif 'xpath' in action.action_selector_kind.lower():
                    driver.find_element_by_xpath(action.action_target).send_keys(action.keys)
                elif 'partial_link_text' in action.action_selector_kind.lower():
                    driver.find_element_by_partial_link_text(action.action_target).send_keys(action.keys)
                elif 'link_text' in action.action_selector_kind.lower():
                    driver.find_element_by_link_text(action.action_target).send_keys(action.keys)
                elif 'tag_name' in action.action_selector_kind.lower():
                    driver.find_element_by_tag_name(action.action_target).send_keys(action.keys)
                elif 'class_name' in action.action_selector_kind.lower():
                    driver.find_element_by_class_name(action.action_target).send_keys(action.keys)
                elif 'selector' in action.action_selector_kind.lower():
                    driver.find_element_by_css_selector(action.action_target).send_keys(action.keys)
            # Hover actions
            elif 'hover' in action.action_type:
                actions_chains = ActionChains(driver)
                if 'id' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_id(action.action_target)
                elif 'name' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_name(action.action_target)
                elif 'xpath' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_xpath(action.action_target)
                elif 'partial_link_text' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_partial_link_text(action.action_target)
                elif 'link_text' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_link_text(action.action_target)
                elif 'tag_name' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_tag_name(action.action_target)
                elif 'class_name' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_class_name(action.action_target)
                elif 'selector' in action.action_selector_kind.lower():
                    parent_level_menu = driver.find_element_by_css_selector(action.action_target)
                actions_chains.move_to_element(parent_level_menu).perform()
        except:
            driver.close()
            raise
        finally:
            driver.close()
    print('Actions successfully executed. Closing browser and exiting crawler...')
    time.sleep(5)