from model import Action

# Extractor actions list
# each Action object inside actions_list must contain: 'action_type', 'action_target' and 'action_selector_kind'. Other parameters are optional.

actions_list = [
    Action('click'),
    Action('hover'),
    Action('type'),
    Action('drag_and_drop')
]
