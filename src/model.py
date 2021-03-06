import src.vars as vars

# Base Extractor
class BaseExtractor():
    """
    class BaseExtractor

    This class defines a Selenium Extractor.

    Attributes: - download_dir - Allowed inputs: any string path
                - browser - Allowed inputs: chrome, firefox
    """
    download_dir = None
    browser = None

    def __init__(self, download_dir=vars.download_dir, browser='chrome'):
        self.download_dir = download_dir
        self.browser = browser

# Base Requester
class BaseRequester():
    """
    class BaseRequester

    This class defines a Http Requester.

    Attributes: - download_dir - Allowed inputs: any string path
    """
    download_dir = None

    def __init__(self, download_dir=vars.download_dir):
        self.download_dir = download_dir

# Action
class Action():
    """
    class Action

    This class defines a webdriver action.

    Attributes: - action_type - Allowed inputs: click, hover, type, drag_and_drop
                - action_target - Allowed inputs: any selector string
                - action_selector_kind - Allowed inputs: id, name, xpath, link_text, partial_link_text, tag_name, class_name, css_selector
                - wait_for - Allowed inputs: any selector string
                - wait_for_selector_kind - Allowed inputs: id, name, xpath, link_text, partial_link_text, tag_name, class_name, css_selector
                - keys - Allowed inputs: any string
                - timeout - Allowed inputs: any float
    """
    action_type = None
    action_target = None
    action_selector_kind = None
    wait_for = None
    wait_for_selector_kind = None
    keys = None
    timeout = None

    def __init__(self, action_type=None, action_target=None, action_selector_kind=None, wait_for=None, wait_for_selector_kind=None, keys=None, timeout=30):
        self.action_type = action_type
        self.action_target = action_target
        self.action_selector_kind = action_selector_kind
        self.wait_for = wait_for
        self.wait_for_selector_kind = wait_for_selector_kind
        self.keys = keys
        self.timeout = timeout
