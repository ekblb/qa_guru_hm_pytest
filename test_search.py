from selene import browser, be, have

def test_ecosia_success_search(open_and_close_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_ecosia_unsuccess_search(open_and_close_browser):
    browser.element('[name="q"]').should(be.blank).type('ewrwrwrrwrw23020103021-31031').press_enter()
    browser.element('html').should(have.text('Unfortunately we didn’t find any results for “ewrwrwrrwrw23020103021-31031'))


