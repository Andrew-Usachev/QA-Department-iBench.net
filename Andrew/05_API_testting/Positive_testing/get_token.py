from selen import *
from security import EMAIL, PASSW


class Get_token(Selen):

    def __init__(se, wd="Seleniumwire"):
        super().__init__(wd, headless=True)
        se.url = "https://ibench.net/login"
        se.ok_assert = True
        se.ok_print = False
        se.WD.maximize_window()

    def get(se):
        se.WD.get(se.url)
        se.Wait(l_h2).text("Log in")
        se.Find(NAME, "email").type(EMAIL).sleep(0.2)
        se.Find(NAME, "password").type(PASSW).sleep(0.2)
        se.Tag('button').click()
        se.Wait(l_h1)
        se.WD.get(se.url + 'stats')
        se.WD.refresh()
        reqs = se.WD.requests
        x_solt = ''
        for request in reqs:
            if "x-solt" not in request.headers:
                continue
            x_solt = request.headers["x-solt"]
            print("x-solt:", request.headers["x-solt"])
            break
        if not x_solt:
            print("x-solt not found!")
            exit()

        with open("Authorization.txt", "w") as file:
            file.write(x_solt)
        print("x_solt saved to file")


if __name__ == "__main__":
    Get_token().get()
