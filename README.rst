# Base Crawler
![Base Crawler](/res/assets/logo.png "Base Crawler is your anytime crawler buddy.")

Base crawler is an Python based tool which facilitates [Selenium Framework](https://github.com/SeleniumHQ/selenium "Selenium HQ Github project.") usage.
It enables the development of selenium based crawlers way faster.

### Understanding Base Crawler

Base Crawler uses selenium to make navigation through websites easier as it gets.

Many selenium functions and interactions are implemented by this application, and you can call them in a very easy way.

Every selenium function can be called by inserting an Action object inside an actions[] array. 
Everything can be configured in the conf.py file. You can also find out examples of usage in the configuration file or in the section **Examples**

### Getting started

Be aware you must have a basic knowledge of Python and Selenium to understand how to use this application. 
To configure your selenium navigation, follow the steps below:

1. Open src/conf.py file.
2. Configure actions_list variable as you like, by adding as many Actions() as you want. 

    - Action() object can have the following parameters:
     
    `Action(action_type, action_target, action_selector_kind, wait_for, wait_for_selector_kind, keys, timeout)`
 
    1. **action_type**:   
        1. goback: Clicks on the browser's GoBack action (Navigates to the previous link).
        2. gofoward: Clicks on the browser's GoFoward action (Navigates to the next link).
        3. navigation: Navigates to the action_target value.
        4. download: Enables Webdriver download and navigates to the action_target value.
        5. click: Clicks on the WebElement. 
        6. send_keys: Send keys(types) on the WebElement. 
        7. hover: Hover over WebElement. 
        8. drag_and_drop: Drag and drops WebElement. 

    2. **action_target**(optional): 
        - action_target can be any url, element's id, element's selector, element's xpath, element's link or partial link text, element's class or tag name.
        - e.g.:  `"button_id"`, `"nth-child(3) > name"`, `"Button Label"`

    3. **action_selector_kind**(optional): 
        - equivalement to driver.find_by_...() selenium's function.
        1. id: WebElement's id.
        2. name: WebElement's name.
        3. xpath: WebElement's xpath.
        4. link_text: WebElement's link text.
        5. partial_link_text: WebElement's partial link text.
        6. tag_name: WebElement's tag name.
        7. class_name: WebElement's class name.
        8. css_selector: WebElement's css selector.

    4. **wait_for**(optional): 
        - wait_for can be any element's id, element's selector, element's xpath, element's link or partial link text, element's class or tag name.
        - e.g.:  `"button_id"`, `"nth-child(3) > name"`, `"Button Label"`

    5. **wait_for_selector_kind**(optional):
        - equivalement to driver.find_by_...() selenium's function.
        1. id: WebElement's id.
        2. name: WebElement's name.
        3. xpath: WebElement's xpath.
        4. link_text: WebElement's link text.
        5. partial_link_text: WebElement's partial link text.
        6. tag_name: WebElement's tag name.
        7. class_name: WebElement's class name.
        8. css_selector: WebElement's css selector.

    6. **keys**(optional):
        - keys is a paremeter which stores input keys for the Action. It can be use with send_keys action_type.

    7. **timeout**(optional):
        - timeout is the amount of seconds the Selenium webdriver will use as it's own timeout before throw an error.

### Examples 
The project's default example is already enabled on `conf.py ` file. To set your own configurations, change the Actions() called inside the array named actions_list. 

1. Example Crawler which navigates to Amazon, searches for products named "roly-poly toy" and clicks on the first item displayed:
```bash
actions_list = [
    Action('navigation', 'https://www.amazon.com/'),
    Action('wait', 5),
    Action('click', 'twotabsearchtextbox', 'id'),
    Action('send_keys', 'twotabsearchtextbox', 'id', keys='roly-poly toy'),
    Action('click', '#nav-search > form > div.nav-right', 'selector'),
    Action('wait', 5),
    Action('click', '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[2]/div[3]/div/span/div/div/span/a/div', 'xpath')
]
```

### Running Base Crawler
After configuring `conf.py` the way you like, as suggested on the **Examples** section, you must be aware:

- This application supports 2 arguments: browser and timeout.
1. browser means which navigator will be instantiatated by Selenium. 
    - e.g.: `chrome` for Google Chrome or `firefox` for Mozilla Firefox.
2. timeout is the amount of seconds the Selenium webdriver will use as it's own timeout before throw an Exception due inactivity. 
    - e.g.: `30` for 30 seconds.

You can easily run the application with the following command:

```bash
    python -m src.main chrome 30
```
