from datetime import datetime
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VerificationPage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_bar_fixed_locator(self, nav_bar_name):
        return By.XPATH, f"//ul[@class='page-breadcrumb']/li/a[@href='#/Verification/{nav_bar_name}']"

    def get_sub_nav_tab_locator(self, sub_nav_name):
        return By.XPATH, f"//div[@class='sub-navtab']/ul/li/a[text()='{sub_nav_name}']"

    def favourite_or_star_icon(self):
        return By.XPATH, f"//i[contains(@class,'icon-favourite')]"

    def get_ok_button_locator(self):
        return By.XPATH, f"//button[@class='btn green btn-success']"

    def search_bar_id(self):
        return By.ID, f"quickFilterInput"

    def get_button_locators_by_text(self, button_name):
        return By.XPATH, f"//button[contains(text(),'{button_name}')]"

    def get_radio_buttons_locator(self, radio_button_name):
        return (By.XPATH, f"//input[@value='{radio_button_name}']/../span")

    def get_calendar_from_dropdown_locator(self):
        return (By.XPATH, "(//input[@id='date'])[1]")

    def get_calendar_to_dropdown_locator(self):
        return (By.XPATH, "(//input[@id='date'])[2]")

    def get_actual_requested_on_dates(self):
        return (By.XPATH, "//div[@col-id='RequisitionDate']/span[not(contains(@class,'hidden'))]")

    def get_date_range_button(self):
        return By.CSS_SELECTOR, "td [data-hover='dropdown']"

    def get_anchor_tag_locator_by_text(self, anchor_tag_name):
        return By.XPATH, f"//a[contains(text(),'{anchor_tag_name}')]"

    def verify_requisition_dropdown(self):
        return By.XPATH, "//div[contains(text(),'Requisition Status:')]/../div/select"

    def get_req_status(self):
        return By.CSS_SELECTOR, "div[ref='eCenterContainer'] div[col-id='RequisitionStatus']"

    def get_requisition_status_dropdown_locator(self):
        return (By.XPATH, "//div[text()=' Requisition Status: ']/..//select")

    def get_requisition_number_locators_for_all_requisitions(self):
        return By.XPATH, "//div[@col-id='RequisitionNo' and @role='gridcell']"

    def get_requisition_number_locator_from_the_report(self):
        return (By.XPATH, "//div[text()='Requisition No:']/b")

    def get_result_count_locator(self):
        return (By.CSS_SELECTOR, "div[class='page-items']")

    def get_first_view_button(self):
        return (By.XPATH, '(//a[text()="View"])[1]')

    def get_total_record_count(self):
        return (By.CSS_SELECTOR, "span[ref='eSummaryPanel'] span[ref='lbRecordCount']")

    def get_inventory_locator(self):
        return (By.XPATH, "//a[@href='#/Inventory']")

    def get_inventory_page_bar_fixed_locator(self, nav_bar_name):
        return (By.XPATH, f"//ul[contains(@class,'page-breadcrumb')]/li/a[@href='#/Inventory/{nav_bar_name}']")

    def get_locator_by_id(self, id_name):
        return (By.ID, id_name)

    def get_item_name_required_msg(self):
        return (By.XPATH, "//div[contains(text(),'Item is required')]")

    def verify_selected_tab_is_active_or_not(self, element):
        """
        @Test4 Verifies if the selected tab is active.

        :param element: The locator tuple (e.g., By.ID, "tab_locator") used to find the tab element.
        :type element: tuple
        :description: Checks if the specified tab element is displayed, clicks it, retrieves its "class" attribute,
                      and verifies if it contains the "active" keyword to determine if the tab is active.
        :return: True if the tab is active, False otherwise.
        :rtype: bool
        """
        try:
            if self.is_element_displayed(element):
                tabs = self.driver.find_element(*element)
                tabs.click()  # Highlighting removed
                locator_attribute_value = tabs.get_attribute("class")
                return "active" in locator_attribute_value
        except Exception as e:
            raise e
        return False

    def is_element_displayed(self, locator):
        """
        @Test3 Checks if a web element is displayed on the page.

        :param locator: The locator tuple (e.g., By.ID, "element_id") used to find the element.
        :type locator: tuple
        :description: Attempts to locate the element using the provided locator and checks if it is displayed on the page.
        :return: True if the element is displayed, False otherwise.
        :rtype: bool
        """
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    def verify_navigation_of_tabs(self):
        """
        @Test5 Verifies the navigation and activation of tabs.

        :description: Checks if the "Inventory" page bar is displayed and clicks it. Then navigates through the
                      "Requisition" and "Purchase Request" sub-navigation tabs. Verifies if the "Purchase Request" tab
                      becomes active after clicking, based on its "class" attribute, and finally returns to the
                      "Requisition" tab.
        :return: None
        """
        is_active = False
        try:
            if self.is_element_displayed(self.get_page_bar_fixed_locator("Inventory")):
                self.driver.find_element(*self.get_page_bar_fixed_locator("Inventory")).click()
                self.driver.find_element(*self.get_sub_nav_tab_locator("Requisition")).click()

                purchase_request_tab = self.driver.find_element(*self.get_sub_nav_tab_locator("Purchase Request"))
                purchase_request_tab.click()

                locator_attribute_value = purchase_request_tab.get_attribute("class")
                print(f"locatorAttributeValue > {locator_attribute_value}")

                is_active = "active" in locator_attribute_value

                self.driver.find_element(*self.get_sub_nav_tab_locator("Requisition")).click()
        except Exception as e:
            raise e

        return is_active

    def verify_results_date_range_within_selected_range(self, from_date: str, to_date: str) -> bool:
        """
        @Test6 Verifies that the results' dates are within the selected date range.

        :param from_date: The start date of the range in the format "dd-mm-yyyy".
        :type from_date: str
        :param to_date: The end date of the range in the format "dd-mm-yyyy".
        :type to_date: str
        :description: Converts the provided date range into `datetime` objects and compares each date from the
                      filtered results to ensure they fall within the specified range. If any date is outside the range,
                      or if parsing fails, the method returns False.
        :return: True if all dates are within the specified range, False otherwise.
        :rtype: bool
        :raises Exception: If an unexpected error occurs during the verification process.
        """
        try:
            date_format = "%d-%m-%Y"
            input_format = "%Y-%m-%d"

            from_date_obj = datetime.strptime(from_date, date_format)
            to_date_obj = datetime.strptime(to_date, date_format)

            actual_dates_after_filter_applied = self.driver.find_elements(*self.get_actual_requested_on_dates())

            for date_element in actual_dates_after_filter_applied:
                date_text = date_element.text

                try:
                    parsed_date = datetime.strptime(date_text, input_format)
                    formatted_date = datetime.strptime(parsed_date.strftime(date_format), date_format)

                except ValueError:
                    print(f"Date parsing failed for: {date_text}")
                    return False

                if formatted_date < from_date_obj or formatted_date > to_date_obj:
                    return False

            return True

        except Exception as e:
            raise Exception(f"An error occurred during date range verification: {str(e)}")

    def verify_tool_tip_text(self):
        """
        @Test7 Verifies and retrieves the tooltip text of an element.

        :description: Locates the tooltip element (e.g., favorite or star icon), hovers over it to trigger the tooltip,
                      and retrieves the tooltip text from the element's 'title' attribute.
        :return: The tooltip text as a string.
        :rtype: str
        :raises Exception: If an error occurs while locating the element or fetching the tooltip text.
        """
        tool_tip_value = ""
        try:
            # Find the tooltip element (favourite or star icon)
            tool_tip_element = self.driver.find_element(*self.favourite_or_star_icon())

            # Hover over the element to trigger the tooltip (if needed)
            ActionChains(self.driver).move_to_element(tool_tip_element).perform()

            # Get the 'title' attribute to fetch the tooltip text
            tool_tip_value = tool_tip_element.get_attribute("title")
            print(f"Tool tip title: {tool_tip_value}")

        except Exception as e:
            raise e

        return tool_tip_value

    def verify_dates_are_remembered_correctly(self, from_date, to_date):
        """
        @Test8 Verifies if the selected date range is remembered correctly.

        :param from_date: The "from" date in the format "dd-mm-yyyy".
        :type from_date: str
        :param to_date: The "to" date in the format "dd-mm-yyyy".
        :type to_date: str
        :description: Sets the "from" and "to" dates using dropdowns, navigates between tabs, and retrieves the remembered dates
                      to ensure they match the initially selected values. Returns True if the dates are remembered correctly.
        :return: True if the remembered dates match the selected dates, False otherwise.
        :rtype: bool
        :raises Exception: If any error occurs during the date verification process.
        """
        try:
            # Split the fromDate and toDate into day, month, and year components
            from_day, from_month, from_year = from_date.split("-")
            to_day, to_month, to_year = to_date.split("-")

            # Locate the date dropdowns and OK button
            from_date_dropdown = self.driver.find_element(*self.get_calendar_from_dropdown_locator())
            to_date_dropdown = self.driver.find_element(*self.get_calendar_to_dropdown_locator())
            ok_button = self.driver.find_element(*self.get_ok_button_locator())

            time.sleep(5)
            # Set the "from" date
            from_date_dropdown.send_keys(from_day)
            from_date_dropdown.send_keys(from_month)
            from_date_dropdown.send_keys(from_year)

            time.sleep(5)

            # Set the "to" date
            # to_date_dropdown.send_keys(to_day)
            # to_date_dropdown.send_keys(to_month)
            # to_date_dropdown.send_keys(to_year)

            time.sleep(5)

            # Locate and click the tooltip (if applicable)
            tooltip = self.driver.find_element(*self.favourite_or_star_icon())
            tooltip.click()

            time.sleep(5)

            # Click the OK button
            ok_button.click()

            # Navigate to Pharmacy tab and back to Inventory tab
            pharmacy_tab = self.driver.find_element(*self.get_page_bar_fixed_locator("Pharmacy"))
            pharmacy_tab.click()

            inventory_tab = self.driver.find_element(*self.get_page_bar_fixed_locator("Inventory"))
            inventory_tab.click()

            requisition_tab = self.driver.find_element(*self.get_sub_nav_tab_locator("Requisition"))
            requisition_tab.click()

            # Wait for the OK button to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.get_ok_button_locator())
            )

            # Construct the actual dates from the selected components
            actual_from_date = f"{from_day}-{from_month}-{from_year}"
            actual_to_date = f"{to_day}-{to_month}-{to_year}"

            print(f"Actual from date: {actual_from_date}")
            print(f"Actual to date: {actual_to_date}")

            # Verify if the remembered dates match the expected dates
            if actual_from_date == from_date and actual_to_date == to_date:
                print("Returned true")
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def click_element(self, locator):
        elementToClick = self.driver.find_element(*locator)
        elementToClick.click()

    def click_date_range_dropdown_and_select(self, value_to_select):
        """
        @Test9 Clicks the date range dropdown and selects a specified value.

        :param value_to_select: The value to be selected from the dropdown (e.g., "Last 1 Week").
        :type value_to_select: str
        :description: Repeatedly clicks the date range dropdown and selects the desired value until the value is
                      successfully selected (verified by the "selected-range" class attribute). Finally, clicks the OK button.
        :return: True if the specified value is successfully selected, False otherwise.
        :rtype: bool
        :raises Exception: If an error occurs during the selection process.
        """
        try:
            # Find and click the Date Range button
            # date_range_button = self.driver.find_element(*self.get_date_range_button())
            # date_range_button.click()
            #
            # # Find and click the value to select (e.g., "Last 1 Week")
            # value_to_select_element = self.driver.find_element(
            #     *self.get_anchor_tag_locator_by_text(value_to_select))
            # value_to_select_element.click()

            while True:
                # Perform actions in the loop
                date_range_button = self.driver.find_element(*self.get_date_range_button())
                date_range_button.click()

                # Find and click the value to select
                value_to_select_element = self.driver.find_element(
                    *self.get_anchor_tag_locator_by_text(value_to_select))
                value_to_select_element.click()

                # Check if the class attribute is 'ABC'
                if value_to_select_element.get_attribute("class") == "selected-range":
                    is_value_selected = True
                    break  # Exit the loop when the condition is met

            # Optionally click the Date Range button again (based on the Java code)
            # date_range_button.click()

            # Ensure the value is selected by checking the class attribute
            # is_value_selected = "selected-range" in value_to_select_element.get_attribute("class")

            # Find and click the OK button
            ok_button = self.driver.find_element(*self.get_ok_button_locator())
            ok_button.click()

            return is_value_selected

        except Exception as e:
            raise e

    def click_radio_button_by_text(self, radio_button_text):
        """
        @Test10.1 @Test12.2 Clicks a radio button based on its associated text.

        :param radio_button_text: The visible text associated with the radio button to be clicked.
        :type radio_button_text: str
        :description: Locates the radio button corresponding to the provided text using a locator and clicks it.
        :return: True if the radio button is successfully clicked, False otherwise.
        :rtype: bool
        :raises Exception: If an error occurs while locating or interacting with the radio button.
        """
        try:
            # Find the radio button using the locator and click it
            radio_button_to_click = self.driver.find_element(*self.get_radio_buttons_locator(radio_button_text))
            radio_button_to_click.click()
            return True
        except Exception as e:
            raise e

    def is_radio_button_selected(self, radio_button_text):
        """
        @Test10.2 Checks if a radio button is selected based on its associated text.

        :param radio_button_text: The visible text associated with the radio button to be verified.
        :type radio_button_text: str
        :description: Locates the radio button corresponding to the provided text and uses JavaScript to check
                      the content of the `::after` pseudo-element to determine if the radio button is selected.
        :return: True if the radio button is selected, False otherwise.
        :rtype: bool
        :raises Exception: If an error occurs during the verification process.
        """
        try:
            print(f"Started {radio_button_text}")
            radio_button_selected = False
            js = self.driver.execute_script  # Get JavaScript Executor

            # Find the radio button element
            radio_button_to_verify = self.driver.find_element(*self.get_radio_buttons_locator(radio_button_text))

            # JavaScript to get the content of the ::after pseudo-element
            script = "return window.getComputedStyle(arguments[0], '::after').getPropertyValue('content');"
            content = js(script, radio_button_to_verify)

            # Check if the content is not empty
            if content:
                print("The span element contains the ::after pseudo-element. complete")
                radio_button_selected = True
            else:
                print("The span element does not contain the ::after pseudo-element.")
                radio_button_selected = False

            return radio_button_selected
        except Exception as e:
            raise e

    def verify_the_results_date_range_is_within_the_selected_range(self, from_date, to_date):
        try:
            # Define date formatters
            date_format = "%m-%d-%Y"
            input_date_format = "%Y-%m-%d"

            # Parse the 'from' and 'to' dates
            from_date_obj = datetime.strptime(from_date, date_format).date()
            to_date_obj = datetime.strptime(to_date, date_format).date()

            # Get the actual dates after filter has been applied
            actual_dates_after_filter_applied = self.driver.find_elements(
                *self.get_actual_requested_on_dates())

            # Iterate through the date elements and check if they are within the specified range
            for date_element in actual_dates_after_filter_applied:
                date_text = date_element.text

                try:
                    # Try parsing the date in 'yyyy-MM-dd' format
                    date = datetime.strptime(date_text, input_date_format).date()
                except ValueError:
                    print(f"Date parsing failed for: {date_text}")
                    return False

                # Check if the parsed date is within the selected range
                if date < from_date_obj or date > to_date_obj:
                    return False

            return True
        except Exception as e:
            raise e

    def verify_records_are_filtered_according_to_requisition_status(self, status):
        """
        @Test11 Verifies that records are filtered correctly according to the specified requisition status.

        :param status: The requisition status to filter and verify (e.g., "Approved", "Pending").
        :type status: str
        :description: Selects the specified status from a dropdown, waits for the filtered results to load, and checks
                      that all displayed requisition statuses in the table match the given status. If any status does not match
                      or no records are found, the method raises an exception.
        :return: True if all requisition statuses match the specified status, False otherwise.
        :rtype: bool
        :raises Exception: If an error occurs during the filtering or verification process.
        """
        try:
            self.apply_date_filter("01-01-2020", "01-03-2024")
            # Locate the dropdown element
            dropdown_element = self.driver.find_element(*self.verify_requisition_dropdown())

            # Select the option with the given status
            from selenium.webdriver.support.ui import Select
            dropdown = Select(dropdown_element)
            dropdown.select_by_value(status)
            time.sleep(10)

            print(f"Selected the '{status}' option from the dropdown.")

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.get_req_status())
            )

            # Locate all the requisition status elements in the table
            req_status_elements = self.driver.find_elements(*self.get_req_status())
            print(f"Number of status elements: {len(req_status_elements)}")

            if req_status_elements:
                # Verify all statuses match the given status
                for status_element in req_status_elements:
                    status_text = status_element.text.strip()
                    if status_text.lower() != status.lower():
                        print(f"Found a status that does not match '{status}': {status_text}")
                        return False

                print(f"All requisition statuses match '{status}'.")
                return True
            else:
                raise Exception("No requisition status records found.")
        except Exception as e:
            raise Exception(f"Failed to verify requisition statuses: {str(e)}") from e

    def visit_tab(self, tab_text):
        """
        @Test12.1 Navigates to a specified tab and verifies its URL.

        :param tab_text: The visible text of the tab to visit.
        :type tab_text: str
        :description: Locates the tab element using the provided text, clicks it, navigates to the "Requisition" sub-tab,
                      and verifies if the current URL contains the text "Inventory".
        :return: True if the current URL contains "Inventory", False otherwise.
        :rtype: bool
        :raises Exception: If an error occurs while navigating to the tab or verifying the URL.
        """
        try:
            # Locate the tab element
            tab_to_visit = self.driver.find_element(*self.get_page_bar_fixed_locator("Inventory"))
            tab_to_visit.click()

            requisition_tab = self.driver.find_element(*self.get_sub_nav_tab_locator("Requisition"))
            requisition_tab.click()

            # Verify if the current URL contains "Inventory"
            return "Inventory" in self.driver.current_url

        except Exception as e:
            raise Exception(f"Failed to visit the tab '{tab_text}'") from e

    def select_dropdown_value_by_text(self, option_to_select):
        """
        @Test12.3 Selects a value from a dropdown menu based on the provided text and verifies the selection.

        :param option_to_select: The value to be selected from the dropdown.
        :type option_to_select: str
        :description: Locates the dropdown element, selects the specified value, and verifies if the selected value
                      matches the expected option by comparing the text.
        :return: True if the specified value is successfully selected, False otherwise.
        :rtype: bool
        :raises Exception: If an error occurs during the selection or verification process.
        """
        try:
            # Locate the dropdown element
            dropdown_element = self.driver.find_element(*self.get_requisition_status_dropdown_locator())

            # Create a Select object and select the desired value
            dropdown = Select(dropdown_element)
            dropdown.select_by_value(option_to_select)

            # Verify if the selected value matches the expected value
            selected_option = dropdown.first_selected_option
            selected_text = selected_option.text.lower()

            return option_to_select.lower() in selected_text

        except Exception as e:
            raise Exception(f"Failed to select the dropdown value '{option_to_select}'") from e

    def apply_date_filter(self, from_date, to_date):
        """
        @Test12.4 Applies a date filter by selecting the specified date range.

        :param from_date: The start date of the range in the format "dd-mm-yyyy".
        :type from_date: str
        :param to_date: The end date of the range in the format "dd-mm-yyyy".
        :type to_date: str
        :description: Splits the provided date range into day, month, and year components, inputs the values into the
                      respective date dropdowns, and confirms the selection by clicking the OK button.
        :return: True if the date filter is successfully applied, False otherwise.
        :rtype: bool
        :raises Exception: If an error occurs while applying the date filter.
        """
        try:
            # Split the dates into day, month, and year components
            from_day, from_month, from_year = from_date.split("-")
            to_day, to_month, to_year = to_date.split("-")

            # Locate the dropdowns and the OK button
            from_date_dropdown = self.driver.find_element(*self.get_calendar_from_dropdown_locator())
            to_date_dropdown = self.driver.find_element(*self.get_calendar_to_dropdown_locator())
            ok_button = self.driver.find_element(*self.get_ok_button_locator())

            # Input the from-date values
            from_date_dropdown.click()
            from_date_dropdown.send_keys(from_day)
            from_date_dropdown.send_keys(from_month)
            from_date_dropdown.send_keys(from_year)

            # Input the to-date values
            to_date_dropdown.click()
            to_date_dropdown.send_keys(to_day)
            to_date_dropdown.send_keys(to_month)
            to_date_dropdown.send_keys(to_year)
            
            # Click the OK button
            ok_button.click()

            return True
        except Exception as e:
            raise Exception(f"Failed to apply date filter: {str(e)}")

    def get_requisition_number_and_click_view_button_for_first_requisition(self):
        """
        @Test12.5 Retrieves the first requisition number and clicks the corresponding "View" button.

        :description:
          - Waits for requisitions to load.
          - Locates and retrieves the list of requisition numbers.
          - Extracts the text of the first requisition number.
          - Locates and clicks the "View" button corresponding to the first requisition.

        :return: The first requisition number as a string.
        :rtype: str
        :raises Exception: If an error occurs while retrieving the requisition number or clicking the "View" button.
        """
        try:
            time.sleep(5)
            # Get all requisition numbers using the locator method
            all_requisition_numbers = self.driver.find_elements(
                *self.get_requisition_number_locators_for_all_requisitions())

            # Highlight and get the text of the first requisition number
            expected_requisition_number = all_requisition_numbers[0].text

            # Get all view buttons using the locator method
            view_buttons = self.driver.find_elements(*self.get_anchor_tag_locator_by_text("View"))

            # Highlight and click the first view button
            view_buttons[0].click()

            return expected_requisition_number
        except Exception as e:
            raise Exception(f"Failed to get requisition number and click 'View' button: {str(e)}")

    def get_requisition_number_from_the_report(self):
        """
        @Test12.6 Retrieves the requisition number from the report.

        :description:
          - Locates the requisition number element within the report.
          - Extracts and returns the text content of the requisition number after stripping whitespace.

        :return: The requisition number as a string.
        :rtype: str
        :raises Exception: If an error occurs while locating or retrieving the requisition number.
        """
        try:
            actual_requisition_number = self.driver.find_element(
                *self.get_requisition_number_locator_from_the_report()).text.strip()
            return actual_requisition_number
        except Exception as e:
            raise e

    def click_button_by_text(self, button_text):
        """
        @Test12.7 Clicks a button identified by its text.

        :param button_text: The visible text of the button to click.
        :type button_text: str
        :description:
          - Locates a button using an XPath expression that matches the provided text.
          - Clicks the located button.

        :return: True if the button is clicked successfully.
        :rtype: bool
        :raises Exception: If the button is not found or an error occurs while clicking it.
        """
        try:
            button_to_click = self.driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
            button_to_click.click()
        except Exception as e:
            print("Either the button was not found or encountered an error while clicking!")
            raise e
        return True

    def verify_record_count_matches(self):
        """
        @Test13 Verifies that the displayed result count matches the total record count.

        :description:
          - Navigates to the "Purchase Request" tab.
          - Selects the "All" radio button to display all records.
          - Waits for the result count and first view button to load.
          - Fetches the result count displayed at the bottom of the page.
          - Extracts and compares the shown result count with the total record count.

        :return: True if the displayed result count matches the total record count, otherwise False.
        :rtype: bool
        :raises Exception: If an error occurs during the verification process.
        """
        try:
            # Click on "Purchase Request"
            self.driver.find_element(*self.get_sub_nav_tab_locator("Purchase Request")).click()

            # Select "All" radio button
            all_radio_button = self.driver.find_element(*self.get_radio_buttons_locator("all"))
            all_radio_button.click()
            print("Selected the 'All' radio button.")

            # Wait for the results to load
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.get_result_count_locator())
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.get_first_view_button())
            )

            # Fetch the result count shown at the bottom of the page
            result_count_element = self.driver.find_element(*self.get_result_count_locator())
            result_count_text = result_count_element.text
            print(f"Result count text: {result_count_text}")

            # Split the text to extract the actual result count
            actual_result_count_text = result_count_text.split(" ")[3]

            total_records_element = self.driver.find_element(*self.get_total_record_count())
            expected_total_records_count = total_records_element.text

            # Convert result count and total record count to integers
            shown_result_count = int(actual_result_count_text)
            total_record_count = int(expected_total_records_count)

            print(f"Shown Result Count: {shown_result_count}")
            print(f"Total Record Count: {total_record_count}")

            # Verify that the counts match
            return shown_result_count == total_record_count
        except Exception as e:
            raise Exception("Failed to verify that the shown result count matches the total record count") from e

    def is_pending_radio_button_visible(self):
        """
        @Test14.1 @Test14.5 Checks if the "Pending" radio button is visible on the page.

        :description:
          - Locates the "Pending" radio button using the specified locator.
          - Returns True if the radio button is displayed, otherwise False.

        :return: True if the "Pending" radio button is visible, otherwise False.
        :rtype: bool
        :raises Exception: If an error occurs while locating or checking the visibility of the radio button.
        """
        try:
            pending_radio_button = self.driver.find_element(*self.get_radio_buttons_locator("pending"))
            return pending_radio_button.is_displayed()
        except Exception as e:
            raise Exception("Error checking if pending radio button is visible") from e

    def scroll_all_the_way_down(self):
        """
        @Test14.2 Scrolls the page all the way down to the bottom.

        :description:
          - Executes a JavaScript command to scroll the page to the bottom.

        :return: True if the page was successfully scrolled down.
        :rtype: bool
        :raises Exception: If an error occurs while attempting to scroll the page.
        """
        try:
            js = self.driver.execute_script
            js("window.scrollTo(0, document.body.scrollHeight);")
            return True
        except Exception as e:
            raise Exception("Error scrolling all the way down") from e

    def is_previous_button_visible(self):
        """
        @Test14.3 Checks if the "Previous" button is visible on the page.

        :description:
          - Locates the "Previous" button using the specified locator.
          - Returns True if the button is displayed, otherwise False.

        :return: True if the "Previous" button is visible, otherwise False.
        :rtype: bool
        :raises Exception: If an error occurs while locating or checking the visibility of the "Previous" button.
        """
        try:
            previous_button = self.driver.find_element(*self.get_button_locators_by_text("Previous"))
            return previous_button.is_displayed()
        except Exception as e:
            raise Exception("Error verifying visibility of the 'Previous' button") from e

    def scroll_all_the_way_up(self):
        """
        @Test14.4 Scrolls the page all the way to the top.

        :description:
          - Executes a JavaScript command to scroll the page to the top (coordinates 0, 0).
          - Returns True if the scroll action is successful.

        :return: True if the page scrolls to the top successfully.
        :rtype: bool
        :raises Exception: If an error occurs while scrolling to the top of the page.
        """
        try:
            js = self.driver.execute_script
            js("window.scrollTo(0, 0);")
            return True
        except Exception as e:
            raise Exception("Error while scrolling to the top of the page") from e

    def verify_required_field_error_message(self):
        """
        @Test15.1 Verifies the error message for a required field (Item Name) on the Purchase Request form.

        :description:
          - Scrolls to the Inventory tab, clicks it, and navigates through several tabs.
          - Clicks the 'Create Purchase Request' button and checks if the required field error message for the Item Name is displayed.
          - Returns the text of the error message displayed for the Item Name field.

        :return: The error message text for the Item Name field.
        :rtype: str
        :raises Exception: If an error occurs while navigating through the tabs or retrieving the error message.
        """
        item_name_message_text = ""
        try:
            # Scroll to the inventory tab and click it
            inventory_tab = self.driver.find_element(*self.get_inventory_locator())
            self.driver.execute_script("arguments[0].scrollIntoView(true);", inventory_tab)
            inventory_tab.click()

            # Navigate through tabs and click on required elements
            self.driver.find_element(*self.get_inventory_page_bar_fixed_locator("InternalMain")).click()
            self.driver.find_element(*self.get_sub_nav_tab_locator("Purchase Request")).click()
            self.driver.find_element(*self.get_button_locators_by_text("Create Purchase Request")).click()

            self.driver.find_element(*self.get_locator_by_id("RequestPORequisition")).click()

            # Retrieve the error message for item name
            item_name_message_element = self.driver.find_element(*self.get_item_name_required_msg())
            print(f"Item Name message text: {item_name_message_element.text}")
            item_name_message_text = item_name_message_element.text

            return item_name_message_text

        except Exception as e:
            raise Exception(f"Error occurred while verifying required field error message: {e}")
