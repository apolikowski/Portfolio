from seleniumpagefactory.Pagefactory import PageFactory


class BookView(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'today_btn': ('XPATH', '//button[text()="Today"]'),
        'back_btn': ('XPATH', '//button[text()="Back"]'),
        'next_btn': ('XPATH', '//button[text()="Next"]'),
        'firstname_inp': ('NAME', 'firstname'),
        'lastname_inp': ('NAME', 'lastname'),
        'email_inp': ('NAME', 'email'),
        'phone_inp': ('NAME', 'phone'),
        'book_btn': ('CLASS', 'btn btn-outline-primary float-right book-room'),
        'cancel_btn': ('CLASS', 'btn btn-outline-danger float-right book-room'),
        'room_booking_section': ('XPATH', '//*[@id="root"]/div/div/div[4]/div/div[2]')
    }

    def click_book_this_room_btn(self):
        self.book_this_room_btn.click()
