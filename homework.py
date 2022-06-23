
def string_name(func):
    print('Имя функции:\n', '',  func.__name__ )
    if func.__code__.co_varnames:
        print('Аргументы функции:')
    else:
        print('Аргументов нет')
    for arg in func.__code__.co_varnames:
        print('  ' + arg)


def open_browser(browser, version):
    pass


def go_to_companyname_homepage(company_name, region):
    pass


def find_registration_button_on_login_page():
    pass


functions = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
for s in functions:
    string_name(s)
