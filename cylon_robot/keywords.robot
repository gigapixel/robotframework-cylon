*** Settings ***
Library  cylon_robot.WebLibrary


*** Keywords ***
I open browser '${browser}'
    open_browser  ${browser}

I close browser
    close_browser

I browse to '${url}'
    browse_to_url  ${url}

I browse to [${ref}]
    browse_to_ref  ${ref}


I enter '${value}' to [${ref}]
    enter_value_to_ref  ${value}  ${ref}

I click [${ref}]
    click_ref  ${ref}

I check [${ref}]
    check_ref  ${ref}

I uncheck [${ref}]
    uncheck_ref  ${ref}

I select '${text}' text in [${ref}]
    select_text_in_ref  ${ref}  ${text}

I select '${value}' value in [${ref}]
    select_value_in_ref  ${ref}  ${value}


I see [${ref}] text contains '${expect}'
    verify_ref_text_contains_expect  ${ref}  ${expect}

I see [${ref}] @${attr} contains '${expect}'
    verify_ref_attr_contains_expect  ${ref}  ${attr}  ${expect}

I see [${ref}] is checked
    verify_ref_is_checked  ${ref}

I see [${ref}] is unchecked
    verify_ref_is_unchecked  ${ref}
