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

    def test_find_it_company(self):
        self.ibench.find_it_company()

    def test_find_employee(self):
        self.ibench.find_employee()

    def test_sell_lead(self):
        self.ibench.sell_lead()

    def test_pt_find_contractors(self):
        self.ibench.pt_find_contractors()

    def test_nt_registration_not_exist_email(self):
        self.ibench.nt_registration_not_exist_email()

    def test_nt_registration_200_symbol_pswd(self):
        self.ibench.nt_registration_200_symbol_pswd()

    def test_nt_registration_with_not_matched_pswds(self):
        self.ibench.nt_registration_with_not_matched_pswds()

    def test_nt_registration_with_not_accepted_terms(self):
        self.ibench.nt_registration_with_not_accepted_terms()

    def test_adhoc_system_not_accepts_certain_value_digits(self):
        self.ibench.adhoc_system_not_accepts_certain_value_digits()

    def test_adhoc_system_not_accepts_certain_value_symbols(self):
        self.ibench.adhoc_system_not_accepts_certain_value_symbols()

    def test_adhoc_system_has_restrictions_on_field_symbol_amount(self):
        self.ibench.adhoc_system_has_restrictions_on_field_symbol_amount()

    def test_adhoc_system_has_restrictions_on_field_fixed_price(self):
        self.ibench.adhoc_system_has_restrictions_on_field_fixed_price()

    def test_bt_1_find_contractors(self):
        self.ibench.bt_1_find_contractors()

    def test_bt_2_find_contractors(self):
        self.ibench.bt_2_find_contractors()

    def test_bt_3_find_contractors(self):
        self.ibench.bt_3_find_contractors()

    def test_bt_4_find_contractors(self):
        self.ibench.bt_4_find_contractors()

    def test_bt_5_find_contractors(self):
        self.ibench.bt_5_find_contractors()

    def test_tearDown(self) -> None:
        self.ibench.WD.close()
        self.ibench = None


class FirefoxPositiveTest(ChromePositiveTest):
    browser_name = "Firefox"


class EdgePositiveTest(ChromePositiveTest):
    browser_name = "Edge"


class OperaPositive(ChromePositiveTest):
    browser_name = "Opera"


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='./HtmlReport'))
