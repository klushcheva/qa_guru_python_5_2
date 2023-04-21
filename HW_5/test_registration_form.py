from selene import browser, have, command
import os


def test_registration_form():
    browser.open('/automation-practice-form')

    browser.element('[id=firstName]').type('Ivan')
    browser.element('[id=lastName]').type('Petrov')
    browser.element('[id=userEmail]').type('i.petrov@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id=userNumber]').type('1234567890')

    browser.element('[id=dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option:nth-child(90)').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option:nth-child(4)').click()
    browser.element('.react-datepicker__day--013').click()

    browser.element('[id="subjectsInput"]').type('E')
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('[id=uploadPicture]').send_keys(os.getcwd() + '/picture.jpeg')

    browser.element('[id = currentAddress]').type('Baker street, 221b')
    browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
    browser.element('[id="state"').click()
    browser.element('[id="react-select-3-option-2"]').should(have.text('Haryana')).click()
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').should(have.text('Karnal')).click()

    browser.element('[id="submit"]').perform(command.js.scroll_into_view)
    browser.element('[id=submit]').press_enter()

    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Ivan Petrov', 'Student Email i.petrov@mail.ru', 'Gender Male', 'Mobile 1234567890',
        'Date of Birth 13 April,1989', 'Subjects English', 'Hobbies Reading',
        'Picture picture.jpeg', 'Address Baker street, 221b', 'State and City Haryana Karnal'))
