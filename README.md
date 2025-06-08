# 🧪 QA Selenium Checkout Demo

This is a UI automation test project using **Selenium WebDriver (Python)** that simulates a complete user checkout process on [SauceDemo](https://www.saucedemo.com/). It is designed as a QA portfolio project to demonstrate automation skills, DOM interaction, wait handling, and test verification.

## ✅ What the script does

1. Opens the Chrome browser
2. Logs in with demo credentials (`standard_user`)
3. Adds two products to the shopping cart
4. Proceeds to checkout
5. Fills in customer info and confirms total price
6. Asserts that the order is successfully completed

## 📂 Files

- `saucedemo_checkout_flow.py` — The main Selenium automation script
- `demo.mp4` *(optional)* — Recorded video of the full test run (can be added for visual demonstration)

## 💻 Technologies Used

- Python 3
- Selenium WebDriver
- ChromeDriver
- SauceDemo (public test site)

## 📷 Sample Output
- [Step 1] Opening SauceDemo login page...
- [OK] Logged in successfully
- [OK] Products added.
- [INFO] Order total: Total: $43.18
- [PASS] Order completed successfully.


## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Download ChromeDriver and update the path in the script.
3. Run the script:
   python saucedemo_checkout_flow.py

## 📌 Author

Zepeng Yu — [LinkedIn](https://www.linkedin.com/in/zepeng-yu) | [GitHub](https://github.com/ComeonZeming)

---
