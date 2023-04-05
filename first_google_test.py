import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def set_browser():
    browser.open('https://www.google.com/')
    browser.driver.set_window_size(1024, 600)


def test_google_positive(set_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_negative(set_browser):
    browser.element('[name="q"]').should(be.blank).type('4334b344nffnvnmvmv999f9f9f92n2n22n2').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
