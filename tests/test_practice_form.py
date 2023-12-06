from selene.support.shared import browser
from selene import have, be, command
import os



def test_student_registration_form_smoke():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test@test.com')
    browser.all('[for^=gender-radio]').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('7727231131')
    browser.element('#dateOfBirthInput').click()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1997"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#subjectsInput').should(be.blank).type('eng').press_enter()
    browser.all('[for^=hobbies-checkbox-1]').element_by(have.exact_text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/sea.jpg'))
    browser.element('#currentAddress').type('Minsk,\nBelarus')
    browser.element('.css-yk16xz-control').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').perform(command.js.click)


    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'John Doe',
            'test@test.com',
            'Male',
            '7727231131',
            '20 July,1997',
            'English',
            'Sports',
            'sea.jpg',
            'Minsk, Belarus',
            'NCR Noida'
        )
    )



    ...