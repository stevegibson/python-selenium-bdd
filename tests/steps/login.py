from behave import when
from pages.login_page import login_page


@when(u'I log in using the standard username and password')
def step_impl_login(context):
    login_page.login('standard_user', 'secret_sauce')
