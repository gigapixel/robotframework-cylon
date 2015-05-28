import os

from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select as to_select

from .log import *
from .world import *
from .repository import *


class keywords(object):

    def cylon_setup(self):
        repository.load_references()
        world.open_browser("chrome")


    def cylon_teardown(self):
        world.close_browser()


    def load_all_references(self):
        repository.load_references()

    ##->I open browser '${browser}'
    def open_browser(self, browser):
        world.open_browser(browser)

    ##->I close browser
    def close_browser(self):
        world.close_browser()

    ##->I browse to '${url}'
    def browse_to_url(self, url):
        url = repository.replace_refs(url)
        try:
            world.driver.get(url)
        except TimeoutException:
            log.error("page load timeout")

    ##->I browse to [${ref}]
    def browse_to_ref(self, ref):
        url = repository.extract_ref(ref)
        try:
            world.driver.get(url)
        except TimeoutException:
            log.error("page load timeout")

    ##->I enter '${value}' to [${ref}]
    def enter_value_to_ref(self, value, ref):
        value = repository.replace_refs(value)
        element = world.find_element(ref)

        try:
            element.send_keys(value)
        except ElementNotVisibleException:
            log.error("element not visible %s" % ref)

    ##->I click [${ref}]
    def click_ref(self, ref):
        element = world.find_element(ref)
        element = world.wait_element_present(element)

        try:
            element.click()
        except TimeoutException:
            log.error("page load timeout (after click link)")


    def check_ref(self, ref):
        element = world.find_element(ref)
        element = world.wait_element_present(element)

        checkbox = element
        if element.tag_name != 'input':
            checkbox = element.find_element_by_tag_name("input")

        if checkbox.is_selected():
            return

        try:
            element.click()
        except ElementNotVisibleException:
            log.error("element not visible %s" % ref)


    def uncheck_ref(self, ref):
        element = world.find_element(ref)
        element = world.wait_element_present(element)

        checkbox = element
        if element.tag_name != 'input':
            checkbox = element.find_element_by_tag_name("input")

        if not checkbox.is_selected():
            return

        try:
            element.click()
        except ElementNotVisibleException:
            log.error("element not visible %s" % ref)


    def select_text_in_ref(self, ref, text):
        text = repository.replace_refs(text)
        element = world.find_element(ref)
        try:
            to_select(element).select_by_visible_text(text)
        except NoSuchElementException:
            log.error("not found option with text '%s'" % text)


    def select_value_in_ref(self, ref, value):
        value = repository.replace_refs(value)
        element = world.find_element(ref)
        try:
            to_select(element).select_by_value(value)
        except NoSuchElementException:
            log.error("not found option with value '%s'" % value)


    def verify_ref_text_contains_expect(self, ref, expect):
        expect = repository.replace_refs(expect)
        element = world.find_element(ref)
        actual = element.text

        if expect not in actual:
            log.fail(actual, expect)

    ##->I see [${ref}] @attr contains '${expect}'
    def verify_ref_attr_contains_expect(self, ref, attr, expect):
        expect = repository.replace_refs(expect)
        element = world.find_element(ref)
        actual = element.get_attribute(attr)

        if expect not in actual:
            log.fail(actual, expect)


    def verify_ref_is_checked(self, ref):
        element = world.find_element(ref)
        if not element.is_selected():
            log.fail('unchecked', 'checked')


    def verify_ref_is_unchecked(self, ref):
        element = world.find_element(ref)
        if element.is_selected():
            log.fail('checked', 'unchecked')
