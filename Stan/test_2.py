import unittest
from ibench import iBench as Cls


class ChromeLoginTest(unittest.TestCase):
    browser_name = "Chrome"

    def setUp(self) -> None:
        self.cls = Cls(self.browser_name)

    def test_login(self):
        self.cls.login()

    def test_home_page(self):
        self.cls.home()

    def test_header_menu(self):
        self.cls.head_nav_menu()

    def test_footer_menu(self):
        self.cls.foot_nav_menu()

    def tearDown(self) -> None:
        self.cls.WD.close()
        self.cls = None


class FirefoxLoginTest(ChromeLoginTest):
    browser_name = "Firefox"


class EdgeLoginTest(ChromeLoginTest):
    browser_name = "Edge"


class OperaLoginTest(ChromeLoginTest):
    browser_name = "Opera"


