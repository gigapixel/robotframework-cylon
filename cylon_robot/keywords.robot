*** Settings ***
Library  cylon_robot.WebLibrary


*** Keywords ***
I browse to '${url}'
    I_browse_to_url  ${url}

I browse to [${ref}]
    I_browse_to_ref  ${ref}

I enter '${value}' to [${ref}]
    I_enter_value_to_ref  ${value}  ${ref}

I click [${ref}]
    I_click_ref  ${ref}

I see [${ref}] @${attr} contains '${expect}'
    I_see_ref_attr_contains_expect  ${ref}  ${attr}  ${expect}
