import unittest
from ibench import iBench


class ChromePositiveTest(unittest.TestCase):
    browser_name = "Chrome"

    def setUp(self) -> None:
        self.ibench = iBench(self.browser_name)

    def test_login(self):
        self.ibench.login()

    def test_home_page(self):
        self.ibench.home()

    def test_header_menu(self):
        self.ibench.head_nav_menu()

    def test_footer_menu(self):
        self.ibench.foot_nav_menu()

    def test_recovery_password(self):
        self.ibench.recovery_password()

    def tearDown(self) -> None:
        self.ibench.WD.close()
        self.ibench = None


class FirefoxPositiveTest(ChromePositiveTest):
    browser_name = "Firefox"


class EdgePositiveTest(ChromePositiveTest):
    browser_name = "Edge"


class OperaPositive(ChromePositiveTest):
    browser_name = "Opera"


