import os

from .log import *
from .world import *
from .repository import *


class WebLibrary(object):

    def cylon_setup(self):
        repository.load_references()
        world.open_browser()

    def cylon_teardown(self):
        world.close_browser()

    ##->I browse to '${url}'
    def I_browse_to_url(self, url):
        url = repository.replace_refs(url)
        try:
            world.driver.get(url)
        except TimeoutException:
            log.error("page load timeout")

    ##->I browse to [${ref}]
    def I_browse_to_ref(self, ref):
        url = repository.get_ref_value(ref)
        try:
            world.driver.get(url)
        except TimeoutException:
            log.error("page load timeout")

    ##->I enter '${value}' to [${ref}]
    def I_enter_value_to_ref(self, value, ref):
        value = repository.replace_refs(value)
        element = world.find_element(ref)
        element.send_keys(value)

    ##->I click [${ref}]
    def I_click_ref(self, ref):
        element = world.find_element(ref)
        try:
            element.click()
        except TimeoutException:
            log.error("page load timeout (after click)")

    ##->I see [${ref}] @attr contains '${expect}'
    def I_see_ref_attr_contains_expect(self, ref, attr, expect):
        expect = repository.replace_refs(expect)
        element = world.find_element(ref)
        actual = element.get_attribute(attr)

        if expect not in actual:
            log.fail(actual, expect)
