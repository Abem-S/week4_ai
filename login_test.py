import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the login page
URL = "https://practicetestautomation.com/practice-test-login/"

# Login credentials
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"
INVALID_USERNAME = "wronguser"
INVALID_PASSWORD = "wrongpass"

# Setup Chrome
options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = uc.Chrome(options=options)
print("Browser launched successfully")

try:
    driver.get(URL)
    print("Page loaded")

    # Wait for username input
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    # ---- VALID LOGIN TEST ----
    driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.ID, "submit").click()

    try:
        # Wait for success message
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Logged In Successfully')]"))
        )
        print("Valid login test: PASSED ")
    except:
        print("Valid login test: FAILED ")

    driver.get(URL)
    time.sleep(2)

    # ---- INVALID LOGIN TEST ----
    driver.find_element(By.ID, "username").send_keys(INVALID_USERNAME)
    driver.find_element(By.ID, "password").send_keys(INVALID_PASSWORD)
    driver.find_element(By.ID, "submit").click()

    try:
        # Wait for error message
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "error"))
        )
        print("Invalid login test: PASSED ")
    except:
        print("Invalid login test: FAILED ")

finally:
    driver.save_screenshot("screenshot.png")
    driver.quit()
    print("Browser closed and screenshot saved")
