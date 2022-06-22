def open_browser():
    pass


def go_to_companyname_homepage():
    pass


def find_registration_button_on_login_page():
    pass


i = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
for s in i:
    string_name = s.__name__
    print(string_name)
