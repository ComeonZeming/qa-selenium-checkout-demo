from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import datetime
import tempfile
import shutil

# === Chrome Setup ===
chrome_driver_path = r"C:\QAProject\chromedriver.exe"
chrome_options = Options()

# Disable automation banners and password manager popups
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

# Use temporary user profile to avoid Chrome login/popup noise
user_data_dir = tempfile.mkdtemp()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Launch browser with options
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

print("=" * 60)
print(f"[START] Script started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

try:
    # Step 1: Open the SauceDemo login page
    print("\n[Step 1] Opening SauceDemo login page...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)

    # Step 2: Login with standard_user credentials
    print("[Step 2] Logging in...")
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    print("[OK] Logged in successfully")
    time.sleep(3)

    # Step 3: Add 2 products to the cart
    print("[Step 3] Adding products to cart...")

    def add_to_cart(product_id, remove_id):
        driver.find_element(By.ID, product_id).click()
        wait.until(EC.presence_of_element_located((By.ID, remove_id)))
        time.sleep(1)

    add_to_cart("add-to-cart-sauce-labs-backpack", "remove-sauce-labs-backpack")
    add_to_cart("add-to-cart-sauce-labs-bike-light", "remove-sauce-labs-bike-light")
    print("[OK] Products added.")
    time.sleep(3)

    # Step 4: Go to cart page
    print("[Step 4] Opening cart page...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)

    # Step 5: Check cart contents
    print("[Step 5] Verifying items in cart...")
    wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    print(f"[INFO] {len(cart_items)} item(s) found in cart.")
    for i, item in enumerate(cart_items, 1):
        print(f"[Item {i}]\n{item.text}\n")
    time.sleep(3)

    # Step 6: Proceed to checkout
    print("[Step 6] Proceeding to checkout...")
    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)

    # Step 7: Fill in checkout form
    print("[Step 7] Entering customer information...")
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("David")
    driver.find_element(By.ID, "last-name").send_keys("Yu")
    driver.find_element(By.ID, "postal-code").send_keys("77001")
    time.sleep(1)
    driver.find_element(By.ID, "continue").click()
    print("[OK] Checkout form submitted.")
    time.sleep(3)

    # Step 8: Review summary
    print("[Step 8] Reviewing order summary...")
    summary = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    print(f"[INFO] Order total: {summary.text}")
    time.sleep(3)

    # Step 9: Finish checkout
    print("[Step 9] Completing the order...")
    driver.find_element(By.ID, "finish").click()
    complete = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    assert "THANK YOU FOR YOUR ORDER" in complete.text.upper()
    print("[PASS] Order completed successfully.")
    time.sleep(3)

except TimeoutException as te:
    print(f"[ERROR] Timeout: {te}")
except Exception as e:
    print(f"[ERROR] Unexpected failure: {e}")
finally:
    input("\n[INFO] Press Enter to close the browser...")
    driver.quit()
    shutil.rmtree(user_data_dir, ignore_errors=True)
    print("[DONE] Browser closed")
    print("=" * 60)
    print(f"[END] Finished at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
