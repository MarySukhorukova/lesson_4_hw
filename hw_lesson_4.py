def change_name(func, *args):
    name = func.__name__.title().replace('_', ' ')
    print(name, *args, sep=' - ')


def open_browser(browser_name):
    change_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    change_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    change_name(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="unsplash.com")
find_registration_button_on_login_page(page_url="unsplash.com", button_text="Log in")