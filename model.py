import vars

# Base Extractor
class BaseExtractor():
    download_dir = None
    browser = None

    def __init__(self, download_dir=vars.download_dir, browser='chrome'):
        self.download_dir = download_dir
        self.base_timeout = base_timeout
        self.browser = browser

# Base Requester
class BaseRequester():
    download_dir = None
    
    def __init__(self, download_dir=vars.download_dir):
        self.download_dir = download_dir

# Action
class Action():
    action_type = None
    action_target = None
    action_selector_kind = None
    wait_for = None
    wait_for_kind = None
    type_text = None
    timeout = None

    def __init__(self, action_type='click', action_target='id_do_elemento', action_selector_kind='id', wait_for='elemento_a_esperar', wait_for_kind='id', type_text='abcdef', timeout=30):
        self.action_type = action_type
        self.action_target = action_target
        self.action_selector_kind = action_selector_kind
        self.wait_for = wait_for
        self.wait_for_kind = wait_for_kind
        self.type_text = type_text
        self.timeout = timeout
