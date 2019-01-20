import time
from lesson_07.base import base
from lesson_07.LoginTest import LoginTest
class SearchTest(base):
    def leave_place(self):
        return self.by_id("notice01")

    def arrive_place(self):
        return self.by_id("notice08")

    def data(self):
        return self.by_id("dateObj")

    def search_button(self):
        return self.by_id("searchbtn")

    def search(self,leave,arrive,date):
        time.sleep(5)
        self.leave_place().clear()
        self.leave_place().send_keys(leave);
        self.arrive_place().clear()
        self.arrive_place().send_keys(arrive);
        time.sleep(5)
        self.excute_js("document.getElementById('dateObj').removeAttribute('readonly')")
        self.data().clear()
        self.data().send_keys(date)
        self.search_button().click()
        time.sleep(10)

