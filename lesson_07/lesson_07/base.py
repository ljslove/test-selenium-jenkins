
class base():
    def __init__(self,driver):
        self.driver=driver

    def by_id(self,id):
        return self.driver.find_element_by_id(id)

    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    def by_css(self,css):
        return self.driver.find_element_by_css_selector(css)

    def by_xpth(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    def excute_js(self,js):
        self.driver.execute_script(js);
