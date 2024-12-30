import logging
from ..tests.common import *
from datetime import datetime, timedelta
import pytest
import time
from ..tests.pages.LoginPage import LoginPage
from ..tests.TestUtils import TestUtils
from ..tests.pages.VerificationPage import VerificationPage


logging.basicConfig(level=logging.INFO)


@pytest.mark.order(1)
def test_login(setup_driver, credentials, expected_data):
    """
        Precondition: User should be logged in and on the healthapp section.

        Steps:
        1. Login in the healthapp application.
        2. Scroll down the menu until verification.
        3. Click on the verification.

        Expected Result:
        The user should successfully navigate to the verification section.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        login_page = LoginPage(driver)
        username = credentials["username"]
        password = credentials["password"]
        login_page.loginWithValiCred(username, password)
        login_page.scrollDownAndClickVerificationTab()
        currentUrl = login_page.verify_verification_page_url()
        expectedUrl = expected_data["URL"]
        expected_url_exists = expectedUrl in currentUrl
        if expected_url_exists:
            passed = True
            test_obj.yakshaAssert("TestValidLogin", True, "functional")
            print("TestValidLogin = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestValidLogin", False, "functional")
            print("TestValidLogin = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "functional")
        print("TestValidLogin = Failed")
    assert passed


@pytest.mark.order(2)
def test_verify_verification_submodules(setup_driver):
    """
        Precondition: User should be logged in and on the Verification section.

        Steps:
        1. Click on the Verification Module drop-down arrow.
        2. Click on Order.

        Expected Result:
        The user should successfully access the Order section from the Verification Module.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)

        inventory_locator = verification_page_instance.get_page_bar_fixed_locator("Inventory")
        inventory_element = driver.find_element(*inventory_locator)
        is_inventory_element_displayed = inventory_element.is_displayed(), "Inventory submodule is not displayed"

        pharmacy_locator = verification_page_instance.get_page_bar_fixed_locator("Pharmacy")
        pharmacy_element = driver.find_element(*pharmacy_locator)
        is_pharmacy_element_displayed = pharmacy_element.is_displayed(), "Pharmacy submodule is not displayed"
        if (is_pharmacy_element_displayed and is_inventory_element_displayed):
            passed = True
            test_obj.yakshaAssert("TestVerifyVerificationSubModules", True, "functional")
            print("TestVerifyVerificationSubModules = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestVerifyVerificationSubModules", False, "functional")
            print("TestVerifyVerificationSubModules = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestVerifyVerificationSubModules", False, "functional")
        print("TestVerifyVerificationSubModules = Failed")
    assert passed


@pytest.mark.order(3)
def test_verify_inventory_tabs_and_buttons_are_displayed(setup_driver):
    """
        Precondition: User should be logged in and on the Verification section.

        Steps:
        1. Click on the Verification Module drop-down arrow.
        2. Click on Inventory.
        3. Click on Requisition.

        Expected Result:
        The user should successfully access the Requisition section from the Verification Module.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)

        is_requisition_tab_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_sub_nav_tab_locator("Requisition")), "Requisition tab is not displayed"

        is_purchase_request_tab_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_sub_nav_tab_locator(
                "Purchase Request")), "Purchase Request tab is not displayed"

        is_purchase_order_tab_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_sub_nav_tab_locator("Purchase Order")), "Purchase Order tab is not displayed"

        is_gr_quality_inspection_tab_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_sub_nav_tab_locator(
                "GR Quality Inspection")), "GR Quality Inspection tab is not displayed"

        is_pending_radio_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_radio_buttons_locator("pending")), "Pending radio button is not displayed"

        is_approved_radio_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_radio_buttons_locator("approved")), "Approved radio button is not displayed"

        is_rejected_radio_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_radio_buttons_locator("rejected")), "Rejected radio button is not displayed"

        is_all_radio_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_radio_buttons_locator("all")), "All radio button is not displayed"

        is_favourite_icon_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.favourite_or_star_icon()), "Favourite or star icon is not displayed"

        is_ok_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_ok_button_locator()), "OK button is not displayed"

        is_search_bar_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.search_bar_id()), "Search bar is not displayed"

        is_print_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_button_locators_by_text("Print")), "Print button is not displayed"

        is_first_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_button_locators_by_text("First")), "First button is not displayed"

        is_previous_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_button_locators_by_text("Previous")), "Previous button is not displayed"

        is_next_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_button_locators_by_text("Next")), "Next button is not displayed"

        is_last_button_displayed = verification_page_instance.is_element_displayed(
            verification_page_instance.get_button_locators_by_text("Last")), "Last button is not displayed"
        if (
                is_requisition_tab_displayed
                and is_purchase_request_tab_displayed
                and is_purchase_order_tab_displayed
                and is_gr_quality_inspection_tab_displayed
                and is_pending_radio_button_displayed
                and is_approved_radio_button_displayed
                and is_rejected_radio_button_displayed
                and is_all_radio_button_displayed
                and is_favourite_icon_displayed
                and is_ok_button_displayed
                and is_search_bar_displayed
                and is_print_button_displayed
                and is_first_button_displayed
                and is_previous_button_displayed
                and is_next_button_displayed
                and is_last_button_displayed
             ):
            passed = True
            test_obj.yakshaAssert("TestTabsAndButtonsVisibility", True, "functional")
            print("TestTabsAndButtonsVisibility = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestTabsAndButtonsVisibility", False, "functional")
            print("TestTabsAndButtonsVisibility = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestTabsAndButtonsVisibility", False, "functional")
        print("TestTabsAndButtonsVisibility = Failed")
    assert passed


@pytest.mark.order(4)
def test_verify_navigation_to_another_submodule_after_opening_inventory_section(setup_driver):
    """
        Precondition: User should be logged in and should be on the verification module.

        Steps:
        1. Click on the inventory.
        2. Click on the pharmacy.
        3. User should navigate to the pharmacy section from the inventory section.

        Expected Result:
        The user successfully navigates to the pharmacy section from the inventory section.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)
        is_selected_tab_active = verification_page_instance.verify_selected_tab_is_active_or_not(
            verification_page_instance.get_page_bar_fixed_locator("Pharmacy")
        ), "Pharmacy page is not active"
        if is_selected_tab_active:
            passed = True
            test_obj.yakshaAssert("TestTabSelectedOrNot", True, "functional")
            print("TestTabSelectedOrNot = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestTabSelectedOrNot", False, "functional")
            print("TestTabSelectedOrNot = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestTabSelectedOrNot", False, "functional")
        print("TestTabSelectedOrNot = Failed")
    assert passed


@pytest.mark.order(5)
def test_verify_navigation_of_tabs(setup_driver):
    """
        Precondition: User should be logged in and should be on the verification module.

        Steps:
        1. Click on the inventory.
        2. Click on the pharmacy.
        3. User should navigate to the pharmacy section from the inventory section.

        Expected Result:
        The user successfully navigates to the pharmacy section from the inventory section.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)
        can_navigate_between_tabs = verification_page_instance.verify_navigation_of_tabs(), "Purchase Request Tab is not active"
        if can_navigate_between_tabs:
            passed = True
            test_obj.yakshaAssert("TestNavigationBetweenTabs", True, "functional")
            print("TestNavigationBetweenTabs = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestNavigationBetweenTabs", False, "functional")
            print("TestNavigationBetweenTabs = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestNavigationBetweenTabs", False, "functional")
        print("TestNavigationBetweenTabs = Failed")
    assert passed


@pytest.mark.order(6)
def test_verify_search_data_by_date_filter(setup_driver):
    """
        Precondition: User should be logged in and should be on the Requisition section.

        Steps:
        1. Click on the "From" date.
        2. Select the "From" date.
        3. Click on the "To" date.
        4. Select the "To" date.
        5. Click on the "OK" button.

        Expected Result:
        The user successfully selects the date range and confirms the selection.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)

        current_date = datetime.now()
        date_7_days_ago = current_date - timedelta(days=7)

        date_format = "%d-%m-%Y"
        to_date = current_date.strftime(date_format)
        from_date = date_7_days_ago.strftime(date_format)

        is_date_within_range = verification_page_instance.verify_results_date_range_within_selected_range(from_date, to_date), \
            "The results are not within the selected date range"
        if is_date_within_range:
            passed = True
            test_obj.yakshaAssert("TestDateRangeFilterFunctionality", True, "functional")
            print("TestDateRangeFilterFunctionality = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestDateRangeFilterFunctionality", False, "functional")
            print("TestDateRangeFilterFunctionality = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestDateRangeFilterFunctionality", False, "functional")
        print("TestDateRangeFilterFunctionality = Failed")
    assert passed


@pytest.mark.order(7)
def test_verify_tool_tip_text(setup_driver, expected_data):
    """
        Precondition: User should be logged in and should be on the Inventory > Requisition section.

        Steps:
        1. Hover the mouse over the star/favourite icon.
        2. Verify that a tooltip with the text "Remember this date" appears when hovering over the star.

        Expected Result:
        The tooltip with the text "Remember this date" should appear when hovering over the star.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)
        favorite_icon_tooltip_as_expected = verification_page_instance.verify_tool_tip_text() == expected_data["favouriteIcon"]
        if favorite_icon_tooltip_as_expected:
            passed = True
            test_obj.yakshaAssert("TestFavoriteIconText", True, "functional")
            print("TestFavoriteIconText = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestFavoriteIconText", False, "functional")
            print("TestFavoriteIconText = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestFavoriteIconText", False, "functional")
        print("TestFavoriteIconText = Failed")
    assert passed


@pytest.mark.order(8)
def test_verify_dates_are_remembered_correctly(setup_driver):
    """
        Precondition: User should be logged in and should be on the Inventory > Requisition section.

        Steps:
        1. Hover the mouse over the star/favourite icon.
        2. Verify that a tooltip with the text "Remember this date" appears when hovering over the star.

        Expected Result:
        The tooltip with the text "Remember this date" should appear when hovering over the star.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)
        current_date = datetime.now()
        date_50_days_ago = current_date - timedelta(days=365)

        to_date = current_date.strftime('%d-%m-%Y')
        from_date = date_50_days_ago.strftime('%d-%m-%Y')

        # print(f"From Date: {from_date}, To Date: {to_date}")
        logging.info(f"From Date: {from_date}, To Date: {to_date}")
        time.sleep(5)

        starred_date_range_remembered = verification_page_instance.verify_dates_are_remembered_correctly(from_date, to_date)
        if starred_date_range_remembered:
            passed = True
            test_obj.yakshaAssert("TestStarredDateRangeRemembered", True, "functional")
            print("TestStarredDateRangeRemembered = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestStarredDateRangeRemembered", False, "functional")
            print("TestStarredDateRangeRemembered = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestStarredDateRangeRemembered", False, "functional")
        print("TestStarredDateRangeRemembered = Failed")
    assert passed


@pytest.mark.order(9)
def test_verify_result_data_is_as_per_the_selected_date_range(setup_driver):
    """
        Precondition: User should be logged in and should be on the verification module.

        Steps:
        1. Click on the data range button.
        2. Select "one week" option from the drop-down.
        3. Click on the "OK" button.

        Expected Result:
        The result data should match the selected date range.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)

        verification_page_instance.click_element(verification_page_instance.favourite_or_star_icon())

        # Select "Last 1 Week" from the Date Range Dropdown
        verification_page_instance.click_date_range_dropdown_and_select("Last 1 Week")

        # Get current date and the date 7 days ago
        current_date = datetime.now()
        date_7_days_ago = current_date - timedelta(days=365)

        # Format dates
        date_format = "%m-%d-%Y"
        to_date = current_date.strftime(date_format)
        from_date = date_7_days_ago.strftime(date_format)

        # Wait for data to load
        time.sleep(3)

        # Verify the results date range is within the selected range
        result_dates_within_selected_range = verification_page_instance.verify_the_results_date_range_is_within_the_selected_range(from_date, to_date)
        if result_dates_within_selected_range:
            passed = True
            test_obj.yakshaAssert("TestResultsAreAsPerSelectedDateRange", True, "functional")
            print("TestResultsAreAsPerSelectedDateRange = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestResultsAreAsPerSelectedDateRange", False, "functional")
            print("TestResultsAreAsPerSelectedDateRange = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestResultsAreAsPerSelectedDateRange", False, "functional")
        print("TestResultsAreAsPerSelectedDateRange = Failed")
    assert passed


@pytest.mark.order(10)
def test_verify_all_the_radio_buttons_are_selectable(setup_driver):
    """
        Precondition: User should be logged in and should be on the Verification module.

        Steps:
        1. Click on the "Pending" radio button from the List by Verification Status.
        2. Click on the "Approved" radio button from the List by Verification Status.
        3. Click on the "Rejected" radio button from the List by Verification Status.
        4. Click on the "All" radio button from the List by Verification Status.

        Expected Result:
        The user should be able to toggle through the verification status options (Pending, Approved, Rejected, All) successfully.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)

        # Click on the "pending" radio button and verify if it is selected
        pending_radio_clicked = verification_page_instance.click_radio_button_by_text("pending")
        pending_radio_selected = verification_page_instance.is_radio_button_selected("pending")

        # Click on the "approved" radio button and verify if it is selected
        approved_radio_clicked = verification_page_instance.click_radio_button_by_text("approved")
        approved_radio_selected = verification_page_instance.is_radio_button_selected("approved")

        # Click on the "rejected" radio button and verify if it is selected
        rejected_radio_clicked = verification_page_instance.click_radio_button_by_text("rejected")
        rejected_radio_selected = verification_page_instance.is_radio_button_selected("rejected")

        # Click on the "all" radio button and verify if it is selected
        all_radio_clicked = verification_page_instance.click_radio_button_by_text("all")
        all_radio_selected = verification_page_instance.is_radio_button_selected("all")

        # Click on "pending" again to reset the pre-condition for the next test case
        pending_radio_clicked_again = verification_page_instance.click_radio_button_by_text("pending")
        if (
            pending_radio_clicked
            and pending_radio_selected
            and approved_radio_clicked
            and approved_radio_selected
            and rejected_radio_clicked
            and rejected_radio_selected
            and all_radio_clicked
            and all_radio_selected
            and pending_radio_clicked_again
        ):
            passed = True
            test_obj.yakshaAssert("TestRadioButtonsClickable", True, "functional")
            print("TestRadioButtonsClickable = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestRadioButtonsClickable", False, "functional")
            print("TestRadioButtonsClickable = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestRadioButtonsClickable", False, "functional")
        print("TestRadioButtonsClickable = Failed")
    assert passed


@pytest.mark.order(11)
def test_verify_records_are_filtered_according_to_requisition_status(setup_driver):
    """
        Precondition: User should be logged in and should be on the Verification module.

        Steps:
        1. Click on the Requisition Status drop-down.
        2. Click on the "Active" drop-down option.

        Expected Result:
        The "Active" option should be successfully selected from the Requisition Status drop-down.
    """
    test_obj = TestUtils()
    try:
        verification_page_instance = VerificationPage(setup_driver)

        records_filtered_with_active_status = verification_page_instance.verify_records_are_filtered_according_to_requisition_status("active"), \
            "Records are not filtered according to the requisition status 'active'."
        if records_filtered_with_active_status:
            passed = True
            test_obj.yakshaAssert("TestActiveStatusFilter", True, "functional")
            print("TestActiveStatusFilter = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestActiveStatusFilter", False, "functional")
            print("TestActiveStatusFilter = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestActiveStatusFilter", False, "functional")
        print("TestActiveStatusFilter = Failed")
    assert passed


@pytest.mark.order(12)
def test_verify_requisition_page_for_record(setup_driver):
    """
        Precondition: User should be logged in and should be on the Verification module.

        Steps:
        1. Select the "All" radio button.
        2. Select the "All" drop-down option.
        3. Click on "FROM" and select "Jan 2020".
        4. Click on "TO" and select "March 2024".
        5. Click on the "OK" button.
        6. Click on the "View" button from the action column of a specific row.
        7. User should navigate to the Check and Verify Requisition page of the selected specific row.

        Expected Result:
        The user should successfully navigate to the Check and Verify Requisition page of the selected specific row.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)

        # Verify the "Inventory" tab is visited
        inventory_tab_visited = verification_page_instance.visit_tab("Inventory"), "Failed to visit 'Inventory' tab."

        # Click the "all" radio button
        all_radio_button_clicked = verification_page_instance.click_radio_button_by_text("all"), "Failed to click 'all' radio button."

        # Select "all" from the dropdown
        dropdown_value_all_selected = verification_page_instance.select_dropdown_value_by_text(
            "all"), "Failed to select 'all' from the dropdown."

        # Apply the date filter
        filter_applied = verification_page_instance.apply_date_filter("01-01-2020", "01-03-2024"), "Failed to apply date filter."

        # Get the requisition number of the first requisition and click the "View" button
        requisition_number_of_first_requisition = verification_page_instance.get_requisition_number_and_click_view_button_for_first_requisition()

        # Verify the requisition number from the report matches
        requisition_number_matches = verification_page_instance.get_requisition_number_from_the_report() == requisition_number_of_first_requisition, \
            "Requisition numbers do not match."

        # Click the "Back to Requisition List" button
        back_to_requisition_clicked = verification_page_instance.click_button_by_text(
            "Back to Requisition List"), "Failed to navigate back to requisition list."
        if (
            inventory_tab_visited
            and all_radio_button_clicked
            and dropdown_value_all_selected
            and filter_applied
            and requisition_number_matches
        ):
            passed = True
            test_obj.yakshaAssert("TestRequisitionNumberMatchesWithReport", True, "functional")
            print("TestRequisitionNumberMatchesWithReport = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestRequisitionNumberMatchesWithReport", False, "functional")
            print("TestRequisitionNumberMatchesWithReport = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestRequisitionNumberMatchesWithReport", False, "functional")
        print("TestRequisitionNumberMatchesWithReport = Failed")
    assert passed


@pytest.mark.order(13)
def test_verify_record_count_matches(setup_driver):
    """
        Precondition: User should be logged in and should be on the Requisition tab in the verification module.

        Steps:
        1. Click on the inventory section.
        2. Click on the "Purchase Request" sub-tab.
        3. Find and select the "All" radio button to view all records.
        4. Fetch and verify the result counts.
        5. The result count displayed at the bottom of the page should match the total record count.

        Expected Result:
        The result count displayed at the bottom of the page should match the total record count.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)
        verification_page_instance.click_element(verification_page_instance.get_sub_nav_tab_locator("Purchase Request"))
        # Apply the date filter
        verification_page_instance.apply_date_filter("01-01-2020", "01-03-2024"), "Failed to apply date filter."
        time.sleep(10)
        record_count_matches = verification_page_instance.verify_record_count_matches()
        if record_count_matches:
            passed = True
            test_obj.yakshaAssert("TestRecordCountMatches", True, "functional")
            print("TestRecordCountMatches = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestRecordCountMatches", False, "functional")
            print("TestRecordCountMatches = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestRecordCountMatches", False, "functional")
        print("TestRecordCountMatches = Failed")
    assert passed


@pytest.mark.order(14)
def test_verify_user_can_scroll_up_and_down(setup_driver):
    """
        Precondition: User should be logged in.

        Steps:
        1. Verify that the "Pending" radio button is visible.
        2. Scroll all the way to the bottom of the page.
        3. Verify that the "Previous" button is visible.
        4. Scroll all the way to the top of the page.
        5. Verify that the "Pending" radio button is still visible.

        Expected Result:
        The "Pending" radio button should be visible at both the top and bottom of the page, and the "Previous" button should be visible when scrolled to the bottom.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)
        # Assert that the pending radio button is visible
        pending_radio_visible = verification_page_instance.is_pending_radio_button_visible()

        # Scroll all the way down and verify
        scrolled_down = verification_page_instance.scroll_all_the_way_down()
        previous_button_visible = verification_page_instance.is_previous_button_visible()

        # Scroll all the way up and verify
        scrolled_up = verification_page_instance.scroll_all_the_way_up()
        pending_radio_visible_again = verification_page_instance.is_pending_radio_button_visible()
        if (
            pending_radio_visible
            and scrolled_down
            and previous_button_visible
            and scrolled_up
            and pending_radio_visible_again
        ):
            passed = True
            test_obj.yakshaAssert("TestScrollingAndFooterVisibility", True, "functional")
            print("TestScrollingAndFooterVisibility = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestScrollingAndFooterVisibility", False, "functional")
            print("TestScrollingAndFooterVisibility = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestScrollingAndFooterVisibility", False, "functional")
        print("TestScrollingAndFooterVisibility = Failed")
    assert passed


@pytest.mark.order(15)
def test_verify_required_field_error_message(setup_driver, expected_data):
    """
        Precondition: User should be logged in and should be on the Verification module.

        Steps:
        1. Navigate to the "Internal" section under Inventory.
        2. Click on "Purchase Request".
        3. Click on the "Create Purchase Request" button.
        4. Click on the "Request" button.

        Expected Result:
        The user should successfully create a purchase request.
    """
    test_obj = TestUtils()
    try:
        driver = setup_driver
        verification_page_instance = VerificationPage(driver)
        # Get the actual error message from the verification page
        actual_error_message = verification_page_instance.verify_required_field_error_message()

        # Fetch the expected error message from the JSON data
        expected_error_message = expected_data["itemNameReq"]

        # Assert that the actual error message matches the expected error message
        error_message_as_expected = actual_error_message == expected_error_message, f"Expected: {expected_error_message}, but got: {actual_error_message}"
        if error_message_as_expected:
            passed = True
            test_obj.yakshaAssert("TestErrorMessageIsAsExpected", True, "functional")
            print("TestErrorMessageIsAsExpected = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestErrorMessageIsAsExpected", False, "functional")
            print("TestErrorMessageIsAsExpected = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("TestErrorMessageIsAsExpected", False, "functional")
        print("TestErrorMessageIsAsExpected = Failed")
    assert passed
