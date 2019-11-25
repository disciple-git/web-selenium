

class GetElementBy:
    def __init__(self, driver):
        self.driver = driver

    def get_element_by(self, key):
        by = key.split('=')[0]
        value = key.split('=')[1]
        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element_by_name(value)
        elif by == 'classname':
            return self.driver.find_element_by_class_name(value)
        elif by == 'link':
            return self.driver.find_element_by_link_text(value)
        elif by == 'partial_link':
            return self.driver.find_element_by_partial_link_text(value)
        elif by == 'tag':
            return self.driver.find_element_by_tag_name(value)
        elif by == 'css_selector':
            return self.driver.find_element_by_css_selector(value)
        else:
            return self.driver.find_element_by_xpath(value)

