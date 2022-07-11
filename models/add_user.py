import os
from urllib.parse import urlparse
testenv = os.environ['PYTEST_BASE_URL']  # Global Test BASE URL - note:pytest_base_url not really working
from faker import Faker


class AddUser:

    def __init__(self,page):
        '''Init setup page and baseurl from page'''

        self.page = page
        self.add_user = page.locator("id=cp_master_srt_employee_id_lbl_sort_label")

        #create pase url of page for navigation

        self.base_url = urlparse(page.url)
        self.base_url = self.base_url.scheme + '://' + self.base_url.hostname
        print(self.base_url)

    def navigate(self):
        '''navigate to people page'''

        self.page.goto(self.base_url + "/workforce/people")
        self.page.wait_for_load_state('domcontentloaded')

        assert self.page.wait_for_selector("id=cp_master_srt_employee_id_lbl_sort_label")

        self.page.click("id=cp_master_lbtn_new")

        assert self.page.wait_for_selector("id=cp_master_txt_first_name__add")

    def add_new_user(self):
        '''add new user'''

        fakeperson = Faker()

        self.page.fill("id=cp_master_txt_first_name__add", fakeperson.first_name())
        self.page.fill("id=cp_master_txt_last_name__add", fakeperson.last_name())
        self.page.fill("id=cp_master_txt_employee_job_title__add", fakeperson.job())
        self.page.click("id=cp_master_lbtn_save__add")

