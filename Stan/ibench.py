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
        se.ok_assert = True
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
        se.check_links(asynchron=True).sleep(0, 3)  # Check all Links

        # se.Tag("head").out("head:")
        # se.Cls('FrontPage_clientImage__3KW8O').text().out("Image Page")
        # se.Tag('h1').text().out("Text of element:")
        # se.Tag('h1').xpath_query().out()
        # se.title().out("Page title:")  # Output of page title
        # se.Cls('FrontPage_btnWrapper__2Q75S').out("Wrapper element:")
        # se.curr_url().out("URL:")  # Output URL
        # se.check_links(asynchron=False).stat.out("Link Statistic")
        # Checking images on the page
        # se.Img(check=True).sleep(10)  # Check all Images

    def login(se):
        lc_submit_button = ((CLASS, "Login_submit_wrapper__2-PYe"), (TAG, "button"))  # Submit button locator

        se.home()  # Start main page
        se.Contains("Log in").click().Wait(l_h2).text("Log in")  # Click to login and wait for new page header with tex
        se.curr_url("https://ibench.net/login").title("Log in | iBench - real-time developers Hiring")
        se.Img(check=True).check_links()

        # Enter email and password with checking for update 'value' attribute and green checkmarks
        se.Find(NAME, "email").type(EMAIL).sleep(0.2).attr('value', EMAIL).out()
        se.parent(2).tag("span").attr('class', 'validation_status_ok')
        se.Find(NAME, "email").xpath_query().out("XPath")
        se.Find(NAME, "password").type(PASSW).sleep(0.2).attr('value', PASSW)
        se.parent(2).tag("span").attr('class', 'validation_status_ok')

        # se.Find(*lc_submit_button).click().sleep(2)  #click submit button
        se.Tag('button').click().sleep(2, 4)

        se.Wait(l_h1).text("Daily updates")
        se.curr_url("https://ibench.net/stats").title("Daily updates | iBench - real-time developers Hiring")
        se.Img(check=True).check_links()
        # sleep(10)

        # se.Find(NAME, "email").xpath_query().out("XPath")
        # se.Wait(l_h2).text("Log in")
        # se.Img(check=True)
        # se.Wait(l_h2).text("Login").click()

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

    def login_cookies(self):
        self.add_cookies()
        self.WD.get(self.url)
        sleep(20)
        # self.main_page()

    def registration(self):
        pass

    def recovery_password(self):
        pass

    def main(se):
        pass


if __name__ == "__main__":
    # iBench('Edge').foot_nav_menu()
    iBench().head_nav_menu()
    # iBench().login()
    print('FINISHED')
    sleep(10)
