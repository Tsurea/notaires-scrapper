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
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(args.url, timeout=60000)
        # wait is added for dev phase. can remove it in production
        page.wait_for_timeout(500)

        business_list = BusinessList()

        next = page.locator(next_xpath)
        i : int = 0
        while next.count() > 0 or i < 1:
            if (next.count() == 0):
                i += 1
            try:

                for office in page.locator(offices_xpath).all():
                    office.locator(office_page_xpath).click()
                    page.wait_for_timeout(500)

                    business = Business()
                    if page.locator(name_xpath).count() > 0:
                        business.name = page.locator(name_xpath).all()[0].inner_text()
                    else:
                        business.name = ""
                    print(business.name)
                    if page.locator(address_xpath).count() > 0:
                        business.address = page.locator(address_xpath).all()[0].inner_text()
                    else:
                        business.address = ""
                    if page.locator(postal_code_xpath).count() > 0:
                        business.postal_code = page.locator(postal_code_xpath).all()[0].inner_text()
                    else:
                        business.postal_code = ""
                    if page.locator(locality_xpath).count() > 0:
                        business.locality = page.locator(locality_xpath).all()[0].inner_text()
                    else:
                        business.locality = ""
                    if page.locator(locality_xpath).count() > 0:
                        business.locality = page.locator(locality_xpath).all()[0].inner_text()
                    else:
                        business.locality = ""
                    if page.locator(country_xpath).count() > 0:
                        business.country = page.locator(country_xpath).all()[0].inner_text()
                    else:
                        business.country = ""

                    if page.locator(website_xpath).count() > 0:
                        business.website = page.locator(website_xpath).all()[0].inner_text()
                    else:
                        business.website = ""
                    if page.locator(language_xpath).count() > 0:
                        business.language = page.locator(language_xpath).all()[0].inner_text()
                    else:
                        business.language = ""
                    if page.locator(email_xpath).count() > 0:
                        business.email = page.locator(email_xpath).all()[0].get_attribute('href')[7:]
                    else:
                        business.email = ""
                    if page.locator(phone_xpath).count() > 0:
                        business.phone = page.locator(phone_xpath).all()[0].inner_text()
                    else:
                        business.phone = ""
                    business_list.business_list.append(business)
                    page.go_back()
                if (next.count() > 0):
                    next.click()
                    page.wait_for_timeout(500)
                next = page.locator(next_xpath)
            except Exception as e:
                print(f'Error occured: {e}')
        
        #########
        # output
        #########
        business_list.save_to_excel(f"notaire_paris".replace(' ', '_'))
        business_list.save_to_csv(f"notaire_paris".replace(' ', '_'))

        browser.close()

if __name__ == "__main__":
    main()
