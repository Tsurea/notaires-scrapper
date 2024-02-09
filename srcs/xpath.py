'''This file contains all the constant xpath that will be use in the script'''

next_xpath : str= '//a[@rel="next"]'
office_page_xpath : str = '//h2[contains(@class, "notary-card__title")]//a'
offices_xpath : str = '//article[contains(@class, "notary-card notary-card--office-sheet")]'

# Office page
# name of the office
name_xpath : str = '//div[contains(@class, "office-sheet__address-wrap")]//p'

# address
address_xpath : str = '//span[contains(@class, "address-line1")]'
postal_code_xpath : str = '//span[contains(@class, "postal-code")]'
locality_xpath : str = '//span[contains(@class, "locality")]'
country_xpath : str = '//span[contains(@class, "country")]'

website_xpath : str = '//div[contains(@class, "office-sheet__url")]//a'
phone_xpath : str = '//div[contains(@class, "office-sheet__phone")]//a'
language_xpath : str = '//div[contains(@class, "field-spoken-languages")]//div[contains(@class, "field__items")]'
email_xpath : str = '//div[contains(@class, "office-sheet__email")]//a'

# Employee info
employee_name_xpath : str = '//h2[contains(@class, "notary-card__title")]//span'
employee_mail_xpath : str = '//p[contains(@class, "notary-card__email")]//a'
employee_website_xpath : str = '//a[contains(@class, "notary-card__url")]'
employee_card_xpath : str = '//a[contains(@class, "notary-card--notary")]'
