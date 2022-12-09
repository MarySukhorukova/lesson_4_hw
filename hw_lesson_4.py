def сorrecting_name(func, *args):
    name = func.__name__.title().replace('_', ' ')
    print(name, *args, sep=' - ')


def open_browser(browser_name):
    сorrecting_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    сorrecting_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    сorrecting_name(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="unsplash.com")
find_registration_button_on_login_page(page_url="unsplash.com", button_text="Log in")
