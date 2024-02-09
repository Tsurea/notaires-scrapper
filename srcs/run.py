from playwright.sync_api import sync_playwright
import pandas as pd
import argparse
import os
import sys

from employee import Employee, EmployeeList
from business import Business, BusinessList
from xpath import *

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
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(args.url, timeout=60000)
        # wait is added for dev phase. can remove it in production
        page.wait_for_timeout(5000)

        business_list = BusinessList()

        next = page.locator(next_xpath)
        while next.count() > 0:
            try:

                for office in page.locator(offices_xpath).all():
                    office.locator(office_page_xpath).click()
                    page.wait_for_timeout(5000)
                    business = Business()
                    
                    business_list.business_list.append(business)
                    page.go_back()
                    pass
                next.click()
                page.wait_for_timeout(5000)
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
