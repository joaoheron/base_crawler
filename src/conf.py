from src.model import Action

# Extractor actions list
# each Action object inside actions_list must contain: 'action_type', 'action_target' and 'action_selector_kind'. Other parameters are optional.

""" 
actions_list is a variable which stores as many Actions as you want.
Action is a object defined in the class model.py
    
Action(action_type, action_target, action_selector_kind, wait_for, wait_for_kind, type_text, timeout)

    action_type:   
                - navigation - Allowed inputs: click, hover, type, drag_and_drop
                - download - Allowed inputs: any selector string
                - click - Allowed inputs: id, name, xpath, link_text, partial_link_text, tag_name, class_name, css_selector
                - type - Allowed inputs: any selector string
                - hover - Allowed inputs: id, name, xpath, link_text, partial_link_text, tag_name, class_name, css_selector
                - drag_and_drop - Allowed inputs: any string

    action_target:
                - 

    action_selector_kind:
                - id
                - name
                - xpath
                - link_text
                - partial_link_text
                - tag_name
                - class_name
                - css_selector

    Action(action_type, action_target, action_selector_kind, wait_for, wait_for_kind, type_text, timeout)
"""
actions_list = [
    Action('navigation', 'https://essentia-app.indicium.tech/dashapp/'),
    Action('type', 'email', 'id', type_text='emailcadastrado'),
    Action('type', 'password', 'id', type_text='senhacadastrada'),
    Action('click', '/html/body/div[1]/div/div/div/div/div/div[2]/div/form/button', 'xpath'),
]
