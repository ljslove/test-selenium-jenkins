import HTMLTestRunner
import unittest
from ddt import ddt,data,file_data,unpack
from selenium import webdriver
from lesson_07.LoginTest import LoginTest
from lesson_07.SearchTest import SearchTest
import time;


@ddt
class HtmlReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        cls.driver = webdriver.Chrome(path)
        cls.driver.get("https://passport.ctrip.com/user/login?")

    @data({"name":"16638705015","password":"ljs201709"})
    @unpack
    def test_01(self,name,password):
        logintest=LoginTest(self.driver);
        logintest.login(name,password)
        url=self.driver.current_url
        self.assertEqual(url,"http://my.ctrip.com/home/myinfo.aspx")
    @data({"leave":"上海","arrive":"杭州","date":"2019-02-09"})
    @unpack
    def test_02(self,leave,arrive,date):
        self.driver.get("http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
        time.sleep(40)
        searchtest=SearchTest(self.driver)
        searchtest.search(leave,arrive,date)
        url1 = self.driver.current_url
        self.assertEqual(url1, "http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")

    @data({"leave": "南京", "arrive": "无锡", "date": "2019-02-10"})
    @unpack
    def test_03(self,leave, arrive, date):
        self.driver.get("http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
        time.sleep(40)
        searchtest = SearchTest(self.driver)
        searchtest.search(leave, arrive, date)
        url1 = self.driver.current_url
        self.assertEqual(url1, "http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit();


if __name__=="__main__":

    test_dir = r"G:\python+selenium\code\lesson_07"
    tests = unittest.defaultTestLoader.discover(test_dir, pattern="HtmlReport.py", top_level_dir=None)
    fp = open(r"G:\python+selenium\report\rep.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="自动化测试报告")
    runner.run(tests)
    fp.close();





