from src.model import Action

""" 
actions_list is a list which stores as many Actions as you want.
Action is a object defined in the class model.py
    
Action(action_type, action_target, action_selector_kind, wait_for, wait_for_kind, keys, timeout)

    action_type:   
        - goback:
        - gofront:
        - navigation:
                - Allowed action_target: Any url.
        - download: 
                - Allowed action_target:  Any url.
        - click:
                - Allowed action_target: : Any id, name, xpath, link_text, partial_link_text, tag_name, class_name or css_selector.
                - Allowed action_selector_kind: "id", "name", "xpath", "link_text", "partial_link_text", "tag_name", "class_name" or "css_selector"
        - send_keys:
                - Allowed action_target: : Any id, name, xpath, link_text, partial_link_text, tag_name, class_name or css_selector.
                - Allowed action_selector_kind: "id", "name", "xpath", "link_text", "partial_link_text", "tag_name", "class_name" or "css_selector"
        - hover:
                - Allowed action_target: : Any id, name, xpath, link_text, partial_link_text, tag_name, class_name or css_selector.
                - Allowed action_selector_kind: "id", "name", "xpath", "link_text", "partial_link_text", "tag_name", "class_name" or "css_selector"
        - drag_and_drop:
                - Allowed action_target: : Any id, name, xpath, link_text, partial_link_text, tag_name, class_name or css_selector.
                - Allowed action_selector_kind: "id", "name", "xpath", "link_text", "partial_link_text", "tag_name", "class_name" or "css_selector"

    action_target: 
        Action targets can be any url, element's id, element's selector, element's xpath, element's link or partial link text, element's class or tag name.

    action_selector_kind:
        - id: Element's id.
        - name: Element's name.
        - xpath: Element's xpath.
        - link_text: Element's link text.
        - partial_link_text: Element's partial link text.
        - tag_name: Element's tag name.
        - class_name: Element's class name.
        - css_selector: Element's css selector.

    wait_for: 
        "Wait for" can be any element's id, element's selector, element's xpath, element's link or partial link text, element's class or tag name.

    wait_for_kind:
        - id: Element's id.
        - name: Element's name.
        - xpath: Element's xpath.
        - link_text: Element's link text.
        - partial_link_text: Element's partial link text.
        - tag_name: Element's tag name.
        - class_name: Element's class name.
        - css_selector: Element's css selector.

    keys:
        Keys is a paremeter which stores input keys for the Action. It can be with send_keys action type.

    timeout:
        Timeout is the amount of seconds the Selenium webdriver will use as it's own timeout.
"""
# Action(action_type, action_target, action_selector_kind, wait_for, wait_for_kind, keys, timeout)

actions_list = [
    Action('navigation', 'https://essentia-app.indicium.tech/dashapp/'),
    Action('sendkeys', 'email', 'id', keys='emailcadastrado'),
    Action('sendkeys', 'password', 'id', keys='senhacadastrada'),
    Action('click', '/html/body/div[1]/div/div/div/div/div/div[2]/div/form/button', 'xpath'),
]
