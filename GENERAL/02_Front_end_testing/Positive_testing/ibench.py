# Import class Selen and simple Locator names and variables
from selen import *

from time import sleep
# file
from security import EMAIL, PASSW


# Class of project
class iBench(Selen):

    def __init__(se, wd="Chrome"):
        super().__init__(wd)
        # Web-site and tests environment settings
        se.url = "https://ibench.net/"
        se.ok_assert = False
        se.ok_print = True

    # locators
    l_login_btn = (CLASS, "Navigation_login__JL_4K")
    l_login_fields = ((CLASS, "Login_form__2mvFD"), (TAG, "input"))

    l_fp_registration = (CLASS, "FrontPage_registrationLinks__2DkiO")
    l_btn_wrap = (CLASS, "FrontPage_btnWrapper__2Q75S")
    l_check_button = (CLASS, 'FrontPage_btnWrapper__2Q75S')
    l_btn = (TAG, "a")

    def home(se):
        se.WD.get(se.url)  # Get page from WD
        # Wait element and check inner text
        se.Wait(l_h1).text('Looking for a developers, UX/UI designer, QA or DevOps...or development agency?')
        se.title('iBench - real-time developers Hiring')  # Check title
        se.curr_url("https://ibench.net/")  # Check url
        se.Img(check=True).stat.out()  # Check all Images

    def login(se):
        lc_submit_button = ((CLASS, "Login_submit_wrapper__2-PYe"), (TAG, "button"))  # Submit button locator

        se.home()  # Start main page
        se.Contains("Log in").click().Wait(l_h2).text("Log in")  # Click to login and wait for new page header with tex
        se.curr_url("https://ibench.net/login").title("Log in | iBench - real-time developers Hiring")
        # se.Img(check=True).check_links()

        # Enter email and password with checking for update 'value' attribute and green checkmarks
        se.Find(NAME, "email").type(EMAIL).sleep(0.2).attr('value', EMAIL).out()
        se.parent(2).tag("span").attr('class', 'validation_status_ok')
        # se.Find(NAME, "email").xpath_query().out("XPath")
        se.Find(NAME, "password").type(PASSW).sleep(0.2).attr('value', PASSW)
        se.parent(2).tag("span").attr('class', 'validation_status_ok')

        # se.Find(*lc_submit_button).click().sleep(2)  #click submit button
        se.Tag('button').click().sleep(2, 4)

        se.Wait(l_h1).text("Daily updates")
        se.curr_url("https://ibench.net/stats").title("Daily updates | iBench - real-time developers Hiring")
        # se.Img(check=True).check_links()

        # sleep(5)

    def about(se):
        se.Wait(l_h1).text(
            """iBench is an easy hiring way to find new highly-skilled Remote developers in 2-3 business days after your request.""")
        se.curr_url('https://ibench.net/about').title('About | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def blog(se):
        se.Wait(CLASS, "breadcrumbs").Tag("span", 1).text("Blog")
        se.curr_url('https://ibench.net/blog/').title('iBench - iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def hire_remote_team(se):
        se.Wait(l_h1).text('Hire remote developers team')
        se.title().out("Title :")
        se.title("iBench - real-time developers Hiring")
        se.curr_url('https://ibench.net/team-search')  # .title('About | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def support_slack(se):
        se.Wait(CLASS, 'c-link').img().attr("alt", "Slack")

    def privacy(se):
        se.Wait(l_h1).text('Privacy Notice')
        se.curr_url('https://ibench.net/privacy-policy').title('Privacy Notice | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def cookie(se):
        se.Wait(l_h1).text('Cookie Policy')
        se.curr_url('https://ibench.net/cookie-policy').title('Cookie Policy | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def terms(se):
        se.Wait(l_h1).text('Terms Of Use')
        se.curr_url('https://ibench.net/terms-of-use').title('Terms Of Use | iBench - real-time developers Hiring')
        se.Img(check=True).check_links()

    def nav_menu(se, locator):
        texts = [elem.text for elem in se.Wait(locator).elems]
        for text in texts:
            se.Find(locator).contains(text)
            func = text.lower().replace(" ", "_")
            print("Checking menu element... ", func)
            old_url = se.curr_url()
            se.click()
            eval(f"se.{func}()")
            if old_url != se.curr_url():
                se.WD.back()
            sleep(1)

    def head_nav_menu(se):
        se.WD.get(se.url)  # Get page from WD
        se.Wait(CLASS, 'Navigation_menu__Xg4DA').tag('a')
        se.nav_menu(((CLASS, 'Navigation_menu__Xg4DA'), (TAG, 'a')))

    def foot_nav_menu(se):
        se.WD.get(se.url)  # Get page from WD
        se.Wait(CLASS, "cookieinfo-close").click()
        se.nav_menu(((CLASS, 'Footer_menu__3wGBS'), (TAG, 'a')))

    def login_cookies(se):
        se.add_cookies()
        se.WD.get(se.url + 'stats')
        sleep(20)
        # self.main_page()

    def registration(se):
        se.WD.get(se.url)
        se.WD.maximize_window()
        se.Wait(CLASS, "Navigation_btn__3RPM8").text("Register").out("Message: ")
        se.title("iBench - real-time developers Hiring").curr_url("https://ibench.net/")
        # se.Cls("Navigation_auth_buttons__29gW3").contains("Register").click()
        se.Contains("Register").click()
        se.Wait(TAG, "h2").text("Create your iBench account")
        se.title("Registration | iBench - real-time developers Hiring").curr_url("https://ibench.net/registration")
        # se.Img(check=True)
        se.Xpath("/html/body[1]/div[2]/span[1]/img[1] ").display()
        # se.Img(check=True)
        # se.check_links()
        se.Contains("Client").click()
        se.Find(NAME, "email").type("qa@smarttech.com").sleep(2).attr("value", "qa@smarttech.com").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "company_name").type("Smart Technologies").attr("value", "Smart Technologies").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password").type("Serena2232").attr("value", "Serena2232").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "password_copy").type("Serena2232").attr("value", "Serena2232").parent(2)
        se.tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "country").dropdown_select("United States").click()
        se.Find(NAME, "terms_accepted").click(action=True)
        se.Contains("Try iBench").click(action=True)
        se.sleep(5)
        # se.Cls("validation_status_ok").attr("class", "validation_status_ok")



    def recovery_password(se):
        se.WD.get(se.url + "login")
        se.Wait(l_h2).text('Log in')
        se.Cls("Login_recovery_link__1asIj").sleep(1, 3).click()
        se.Wait(l_h1).text("Recovery password")
        se.title().out()
        se.curr_url("https://ibench.net/krecovery").title("Recovery password | iBench - real-time developers Hiring")
        se.Img(check=True)
        se.check_links()
        se.Contains({"name": "email", "type": "email"}).out()


    def find_it_company(se):
        se.WD.get(se.url)
        # se.WD.maximize_window()
        se.login()
        # se.Find(XPATH, "//li/a[contains(text(),'Find IT companies')]").click()
        # se.Contains("Find IT companies").click()
        se.Cls("DashboardMenu_menuLink__JkSw7", 3).click()
        se.curr_url('https://ibench.net/outsource').title("Outsource | iBench - real-time developers Hiring").sleep(3)
        se.Wait(l_h1).text("Find IT companies")
        se.Cls("Outsource_freeSlot__7mxFS").click()
        se.Find(NAME, "vetted").dropdown_select("1").click()
        se.parent(2).tag("span").attr('class', 'validation_status_ok')
        # se.Find(CLASS, "rw-input-reset").type("United States" + Keys.ENTER + "Canada" + Keys.ENTER)
        se.Find(NAME, "location").dropdown_multiselect(random_max=3)
        se.Find(NAME, "name").type("Project for QA analysis")
        se.Find(CLASS, "ql-editor").type("Our project is a software ")
        se.Find(NAME, "markets").dropdown_multiselect(random_max=4)
        # old not updated version of the script works in key-chains
        # se.Contains({"aria-owns":"rw_4_listbox rw_4_notify_area rw_4_taglist"}).type("Information Technology" + Keys.ENTER + "Technology" + Keys.ENTER)
        se.Tag("html").elem.send_keys(Keys.PAGE_DOWN)
        se.Tag("input").contains({"name": "budget"}).click(random=True)
        se.Tag("input").contains({"name": "project_start"}).click(random=True)
        # - #version with higher level of hierarchy for random click
        # se.Find((CLASS, "OutsourceAdding_radioGrouptWrapper__23Y0R", 1),(CLASS, "RadioButton_wrapper__3Q5Rq")).click(random=True)
        se.Find(NAME, "links").type('https://www.linkedin.com/')
        se.Cls("OutsourceAdding_submit__1o3MH").click(action=True)
        se.sleep(5)

    def find_employee(se):
        # se.WD.get(se.url + "login")
        se.login()
        se.Cls("DashboardMenu_menuLink__JkSw7", 2).click()
        se.curr_url('https://ibench.net/search-employee-slots').title("iBench - real-time developers Hiring").sleep(2)
        # se.Cls("DashboardMenu_menuLink__JkSw7").contains("Find Employee").click()
        se.Cls("FreelancerSlots_free_slot__6EdsB").click()
        se.Find(NAME, "vetted").dropdown_select(2)
        # se.Find(CLASS, "rw-input-reset").type("United States" + Keys.ENTER)
        # se.Cls("rw-select").tag("span").click(random=True)
        # se.Cls("FormControls_label__1UFBV").tag("span").click(random=True)

        se.sleep(5)


    def main(se):
        pass


if __name__ == "__main__":
    # iBench('Edge').foot_nav_menu()
    # iBench().head_nav_menu()
    # iBench('Seleniumwire').login()

    iBench().find_it_company()
    # iBench().login_cookies()
    print('FINISHED')
