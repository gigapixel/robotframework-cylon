import time

from selenium import webdriver
from selenium.common.exceptions import *

from .log import *
from .repository import *


class world:
    driver = None
    timeout = 10

    @classmethod
    def open_browser(cls, browser):
        if browser == "chrome":
            cls.driver = webdriver.Chrome()
        elif browser == "firefox":
            cls.driver = webdriver.Firefox()
        else:
            log.info("the '%s' browser is not supported" % browser)
            return

        cls.driver.implicitly_wait(cls.timeout)
        cls.driver.set_page_load_timeout(cls.timeout)


    @classmethod
    def close_browser(cls):
        if cls.driver is None:
            return
        for handle in cls.driver.window_handles:
            cls.driver.switch_to_window(handle)
            cls.driver.close()


    @classmethod
    def find_element(cls, ref):
        selector = repository.extract_ref(ref)

        try:
            if selector.startswith('//'):
                element = cls.driver.find_element_by_xpath(selector)
            else:
                element = cls.driver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            log.error("element not found %s" % ref)

        return element


    @classmethod
    def find_elements(cls, ref):
        selector = cls.get_ref_value(ref)

        try:
            if selector.startswith('//'):
                elements = cls.driver.find_elements_by_xpath(selector)
            else:
                elements = cls.driver.find_elements_by_css_selector(selector)
        except NoSuchElementException:
            log.error("elements not found %s" % ref)

        return elements


    @classmethod
    def wait_element_present(cls, element):
        for n in range(cls.timeout):
            if element.is_displayed():
                time.sleep(1)
                return element
            time.sleep(1)

        log.error("element not present")
