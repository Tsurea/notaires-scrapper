from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse
import os
import sys

@dataclass
class Business:
    name: str = None
    address: str = None
    website: str = None
    language: str = None
    email: str = None

@dataclass
class Employee:
    name: str = None
    phone: str = None
    email: str = None
    website: str = None

@dataclass
class EmployeeList:
    employee_list: list[Employee] = field(default_factory=list)
    save_at = 'output'

    def dataframe(self):
        """transform business_list to pandas dataframe

        Returns: pandas dataframe
        """
        return pd.json_normalize(
            (asdict(business) for business in self.business_list), sep="_"
        )

    def save_to_excel(self, filename):
        """saves pandas dataframe to excel (xlsx) file

        Args:
            filename (str): filename
        """

        if not os.path.exists(self.save_at):
            os.makedirs(self.save_at)
        self.dataframe().to_excel(f"output/{filename}.xlsx", index=False)

    def save_to_csv(self, filename):
        """saves pandas dataframe to csv file

        Args:
            filename (str): filename
        """

        if not os.path.exists(self.save_at):
            os.makedirs(self.save_at)
        self.dataframe().to_csv(f"output/{filename}.csv", index=False)

@dataclass
class BusinessList:
    """holds list of Business objects,
    and save to both excel and csv
    """
    business_list: list[Business] = field(default_factory=list)
    save_at = 'output'

    def dataframe(self):
        """transform business_list to pandas dataframe

        Returns: pandas dataframe
        """
        return pd.json_normalize(
            (asdict(business) for business in self.business_list), sep="_"
        )

    def save_to_excel(self, filename):
        """saves pandas dataframe to excel (xlsx) file

        Args:
            filename (str): filename
        """

        if not os.path.exists(self.save_at):
            os.makedirs(self.save_at)
        self.dataframe().to_excel(f"output/{filename}.xlsx", index=False)

    def save_to_csv(self, filename):
        """saves pandas dataframe to csv file

        Args:
            filename (str): filename
        """

        if not os.path.exists(self.save_at):
            os.makedirs(self.save_at)
        self.dataframe().to_csv(f"output/{filename}.csv", index=False)

def main():
    ########
    # input 
    ########
    
    # read search from arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="url website")
    args = parser.parse_args()
        
    ###########
    # scraping
    ###########
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(args.url, timeout=60000)
        # wait is added for dev phase. can remove it in production
        page.wait_for_timeout(5000)

        business_list = BusinessList()

        next_xpath = '//a[@rel="next"]'
        office_page_xpath = '//h2[contains(@class, "notary-card__title")]//a'
        next = page.locator(next_xpath)
        while next.count() > 0:
            try:
                offices_xpath = '//article[contains(@class, "notary-card notary-card--office-sheet")]'

                for office in page.locator(offices_xpath).all():
                    office.locator(office_page_xpath).click()
                    page.wait_for_timeout(5000)
                    page.go_back()
                    pass
                next.click()

                next = page.locator(next_xpath)
            except Exception as e:
                print(f'Error occured: {e}')
        
        #########
        # output
        #########
        business_list.save_to_excel(f"notaire_{search_for}".replace(' ', '_'))
        business_list.save_to_csv(f"notaire_{search_for}".replace(' ', '_'))

        browser.close()


if __name__ == "__main__":
    main()
