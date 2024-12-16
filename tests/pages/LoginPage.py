import time

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.usernameLocator  = (By.ID, 'username_id')
        self.passwordLocator = (By.ID, 'password')
        self.loginButtonLocator = (By.ID, 'login')
        self.verificationTabLocator = (By.XPATH, '//a[@href="#/Verification"]')

    def loginWithValiCred(self, username: str, password: str):
        """
            @Test1.1 about this method loginWithValiCred()

            :param credentials: A dictionary containing 'username' and 'password' as keys.
            :type credentials: dict
            :description: Fills the username and password fields and clicks the sign-in button.
            :return: True if login is successful, False otherwise.
            :rtype: bool
            :author: Yaksha
        """
        self.driver.find_element(*self.usernameLocator).send_keys(username)
        self.driver.find_element(*self.passwordLocator).send_keys(password)
        self.driver.find_element(*self.loginButtonLocator).click()

    def scrollDownAndClickVerificationTab(self):
        """
            @Test1.2 about this method scroll_down_and_click_verification_tab()

            :param: None
            :description: Verifies the pharmacy tab, scrolls to it, and clicks it.
            :return: A string indicating the result of the action.
            :rtype: str
            :author: YAKSHA
        """
        try:
            verification_tab = self.driver.find_element(*self.verificationTabLocator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", verification_tab)
            verification_tab.click()
            self.waitForUrlContains("Verification/Inventory", 10)

        except Exception as e:
            raise e

    def verify_verification_page_url(self):
        """
            @Test1.3 about this method verify_verification_page_url()

            :param: None
            :description: Verifies the verification page URL.
            :return: A string indicating the result of the verification.
            :rtype: str
            :author: YAKSHA
        """
        try:
            url_to_verify = self.driver.current_url
            return url_to_verify
        except Exception as e:
            raise e

    def waitForUrlContains(self, expected_url_part, timeout):
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_url = self.driver.current_url
            if expected_url_part in current_url:
                return
            time.sleep(0.5)
        raise Exception(f"URL did not contain '{expected_url_part}' within {timeout} seconds.")
