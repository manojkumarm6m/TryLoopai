import os
import re
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from qa.pages.LoginPage import LoginLoc
from qa.utilities import ExcelUtils
from qa.pages.ReversalPage import Reversal

folder_path = "./../ExcelFiles"
file_name = "transactions_data.xlsx"

# Get the absolute path of the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, folder_path, file_name)
wait = None

sum_total = []
grand_total = []


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestLogin(LoginLoc):

    def login(self, un='qa-engineer-assignment@test.com', pwd='QApassword123$'):
        """
        This test verifies that a user is able to successfully log in to the application with valid credentials

        :param un: Username from Excel file
        :param pwd: Password from Excel file
        """
        self.enter_data(By.ID, self.email, un)
        self.enter_data(By.ID, self.password, pwd)
        self.click_element(By.XPATH, self.login_button)

    @pytest.mark.parametrize("un, pwd", ExcelUtils.get_data_from_excel(file_path, "LoginTestData"))
    def test_login(self, un, pwd):
        self.login(un, pwd)
        self.click_element(By.XPATH, Reversal.chargebacks)
        self.click_element(By.XPATH, Reversal.history_by_store)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, self.length_xpath)))
        e = self.driver.find_elements(By.XPATH, self.length_xpath)
        l = len(e)
        print("length of months is = ", l)

        for j in range(1, l + 1):
            flag = True
            ind = []
            while flag:
                dynamic_xpath = self.base_xpath.format(j)
                elements = self.driver.find_elements(By.XPATH, dynamic_xpath)

                for i in elements:
                    cleaned_text = re.sub('[^0-9.]', '', i.text)
                    value = float(cleaned_text)
                    ind.append(value)
                    # print(value)

                next_button = self.wait_for_element_and_hover((By.XPATH, self.next_button))
                if next_button:
                    next_button.click()
                else:
                    flag = False
            sum_total.append(round(sum(ind), 2))
            self.click_on_previous((By.XPATH, self.previous_button))

    @pytest.mark.parametrize("un, pwd", ExcelUtils.get_data_from_excel(file_path, "LoginTestData"))
    def test_grand_total(self, un, pwd):
        self.login(un, pwd)
        self.click_element(By.XPATH, Reversal.chargebacks)
        self.click_element(By.XPATH, Reversal.history_by_store)
        grand_total_xpath = '//tr[@class="MuiTableRow-root css-1u3yjyd-MuiTableRow-root"]//td[@class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-439gbi-MuiTableCell-root"]'
        wait = WebDriverWait(self.driver, 60)
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, grand_total_xpath)))
        for i in elements:
            cleaned_text = re.sub('[^0-9.]', '', i.text)
            value = float(cleaned_text)
            grand_total.append(value)
        print(sum_total)
        print(grand_total)
        assert sum_total == grand_total

    @pytest.mark.parametrize("un, pwd", ExcelUtils.get_data_from_excel(file_path, "LoginTestData"))
    def test_generate_csv_file(self, un, pwd):
        global order_type, order_id, order_state, lost_sale, net_payout, payout_id, payout_date
        self.login(un, pwd)
        self.click_element(By.XPATH, Reversal.chargebacks)
        self.click_element(By.XPATH, self.transactions)
        self.wait_for_element_and_hover((By.XPATH, self.location)).click()
        self.click_element(By.XPATH, self.clear)
        self.click_element(By.XPATH, self.alchemy)
        self.click_element(By.XPATH, self.buffet)
        self.click_element(By.XPATH, self.apply)
        self.wait_for_element_and_hover((By.XPATH,  self.market_place)).click()
        self.click_element(By.XPATH, self.clear)
        self.click_element(By.XPATH, self.grab_hub)

        self.click_element(By.XPATH, self.apply_button)
        table = self.driver.find_element(By.XPATH, "//table")

        # Find all the rows in the table
        rows = table.find_elements(By.XPATH, ".//tr")

        # Create a list to store the extracted data
        data = []
        for row in rows[1:]:
            # Find all the cells in the current row
            cells = row.find_elements(By.XPATH, ".//td")

            # Check if there are enough cells in the row
            if len(cells) >= 8:
                # Extract the text from each cell
                order_id = cells[0].text
                location = cells[1].text
                order_state = cells[2].text
                order_type = cells[3].text
                lost_sale = cells[4].text
                net_payout = cells[5].text
                payout_id = cells[6].text
                payout_date = cells[7].text
            elif len(cells) <= 5:
                order_type = cells[0].text
                lost_sale = cells[1].text
                net_payout = cells[2].text
                payout_id = cells[3].text
                payout_date = cells[4].text

            # Create a dictionary for the current row
            row_data = {
                'Order ID': order_id,
                'Location': location,
                'Order State': order_state,
                'Type': order_type,
                'Lost Sale': lost_sale,
                'Net Payout': net_payout,
                'Payout ID': payout_id,
                'Payout Date': payout_date
            }

            data.append(row_data)

        # Write the data to the CSV file
        csv_file = 'output.csv'
        # Define the fieldnames for the CSV file
        fieldnames = ['Order ID', 'Location', 'Order State', 'Type', 'Lost Sale', 'Net Payout', 'Payout ID',
                      'Payout Date']

        with open(csv_file, 'w', newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(data)

