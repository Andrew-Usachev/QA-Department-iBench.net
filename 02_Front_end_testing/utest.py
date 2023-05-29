import unittest
import HtmlTestRunner

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

    def find_it_company(self):
        self.ibench.find_it_company()

    def find_employee(self):
        self.find_employee()

    def sell_lead(self):
        self.sell_lead()

    def pt_find_contractors(self):
        self.pt_find_contractors()

    def nt_registration_not_exist_email(self):
        self.ibench.nt_registration_not_exist_email()

    def nt_registration_200_symbol_pswd(self):
        self.ibench.nt_registration_200_symbol_pswd()

    def nt_registration_with_not_matched_pswds(self):
        self.ibench.nt_registration_with_not_matched_pswds()

    def nt_registration_with_not_accepted_terms(self):
        self.ibench.nt_registration_with_not_accepted_terms()

    def adhoc_system_not_accepts_certain_value_digits(self):
        self.adhoc_system_not_accepts_certain_value_digits()

    def adhoc_system_not_accepts_certain_value_symbols(self):
        self.adhoc_system_not_accepts_certain_value_symbols()

    def adhoc_system_has_restrictions_on_field_symbol_amount(self):
        self.adhoc_system_has_restrictions_on_field_symbol_amount()

    def adhoc_system_has_restrictions_on_field_fixed_price(self):
        self.adhoc_system_has_restrictions_on_field_fixed_price()

    def bt_1_find_contractors(self):
        self.bt_1_find_contractors()

    def bt_2_find_contractors(self):
        self.bt_2_find_contractors()

    def bt_3_find_contractors(self):
        self.bt_3_find_contractors()

    def bt_4_find_contractors(self):
        self.bt_4_find_contractors()

    def bt_5_find_contractors(self):
        self.bt_5_find_contractors()

    def tearDown(self) -> None:
        self.ibench.WD.close()
        self.ibench = None


class FirefoxPositiveTest(ChromePositiveTest):
    browser_name = "Firefox"


class EdgePositiveTest(ChromePositiveTest):
    browser_name = "Edge"


class OperaPositive(ChromePositiveTest):
    browser_name = "Opera"


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReport'))
