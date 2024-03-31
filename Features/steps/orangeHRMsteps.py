from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('launch chrom browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    
    print("Chrom browser launched")

@when('open OrangeHRM homepage')
def Navigate_to_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Navigating to OrangeHRM homepage")

@then('verify that the logo present on page')
def Verify_the_logo(context):
    orange_logo = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']")
    assert orange_logo.is_displayed()
    print("Verifying the presence of the logo on the page")

@then('close browser')
def Close_browser(context):
    context.driver.close()
    print("Closing the browser")
