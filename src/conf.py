from src.model import Action

""" 
Every selenium function can be called by inserting an Action object inside an actions[] array.
The array name must start with "actions_".

Action is a object defined in the class model.py
    
Action(description, action_type, action_target, action_selector_kind, wait_for, wait_for_selector_kind, keys, timeout)

    description:

    action_type:   
        - goback: Clicks on the browser's GoBack action (Navigates to the previous link).
        - gofoward: Clicks on the browser's GoFoward action (Navigates to the next link).
        - navigation: Navigates to the action_target value.
        - download: Enables Webdriver download and navigates to the action_target value.
        - click: Clicks on the WebElement.
        - send_keys: Send keys(types) on the WebElement. 
        - hover: Hover over WebElement. 
        - drag_and_drop: Drag and drops WebElement. 

    action_target: 
        - action_target can be any url, element's id, element's selector, element's xpath, element's link or partial link text, element's class or tag name.
            e.g.:  "button_id", "nth-child(3) > name", "Button Label"

    action_selector_kind: 
        equivalement to driver.find_by_...() selenium's function.
        - id: WebElement's id.
        - name: WebElement's name.
        - xpath: WebElement's xpath.
        - link_text: WebElement's link text.
        - partial_link_text: WebElement's partial link text.
        - tag_name: WebElement's tag name.
        - class_name: WebElement's class name.
        - css_selector: WebElement's css selector.

    wait_for: 
        - wait_for can be any element's id, element's selector, element's xpath, element's link or partial link text, element's class or tag name.
            e.g.:  "button_id", "nth-child(3) > name", "Button Label

    wait_for_selector_kind:
        equivalement to driver.find_by_...() selenium's function.
        - id: WebElement's id.
        - name: WebElement's name.
        - xpath: WebElement's xpath.
        - link_text: WebElement's link text.
        - partial_link_text: WebElement's partial link text.
        - tag_name: WebElement's tag name.
        - class_name: WebElement's class name.
        - css_selector: WebElement's css selector.

    keys:
        - keys is a paremeter which stores input keys for the Action. It can be use with send_keys action_type.

    timeout:
        - timeout is the amount of seconds the Selenium webdriver will use as it's own timeout to throw an error.
"""

# Example Crawler which navigates to Amazon and search for a product
actions_list = [
    # Navigates to your favorite video
    Action('navigation', 'https://www.amazon.com/'),
    # Waits for 5 seconds
    Action('wait', 5),
    # Clicks on the search box
    Action('click', 'twotabsearchtextbox', 'id'),
    # Sends "roly-poly toy" keys to search box
    Action('send_keys', 'twotabsearchtextbox', 'id', keys='roly-poly toy'),
    # Clicks on the Search button
    Action('click', '#nav-search > form > div.nav-right', 'selector'),
    # Waits for 5 seconds
    Action('wait', 5),
    # Clicks on the first item of the products list
    Action('click', '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[2]/div[3]/div/span/div/div/span/a/div', 'xpath')
]
