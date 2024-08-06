from seleniumpagefactory.Pagefactory import PageFactory


class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'let_me_hack_btn': ('XPATH', '//*[@id="collapseBanner"]/div/div[3]/div[2]/button'),
        'book_this_room_btn': ('XPATH', '//*[@id="root"]/div/div/div[4]/div/div/div[3]/button'),
        'name_inp': ('ID', 'name'),
        'email_inp': ('ID', 'email'),
        'phone_inp': ('ID', 'phone'),
        'subject_inp': ('ID', 'subject'),
        'message_inp': ('ID', 'description'),
        'submit_btn': ('ID', 'submitContact')
    }

    def click_let_me_hack_btn(self):
        self.let_me_hack_btn.click()

    def click_book_this_room_btn(self):
        self.book_this_room_btn.click()

    def input_name(self):
        self.name_inp.set_text("Test")

    def input_email(self):
        self.email_inp.set_text("Test")

    def input_phone(self):
        self.phone_inp.set_text("123456789")

    def input_subject(self):
        self.subject_inp.set_text("Test subject")

    def input_message(self):
        self.message_inp.set_text("Test message")

    def click_submit_btn(self):
        self.submit_btn.click()
