
import random

from time import sleep

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "ru.aton.financeapp",
    "appActivity": "ru.aton.finance.activity.LoginActivity",
    "app": "C:\\Users\\root\\PycharmProjects\\challenge-aton-line\\src\\apk\\atonline.apk"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
touch = TouchAction(driver)
driver.implicitly_wait(10)


# ================ Initial activity ================

print('Initial activity\n')

try:
    # Tap on "Next" button 3 times
    for index in range(3):
        driver.find_element_by_id("ru.aton.financeapp:id/showcaseNextOrStartBtn").click()
    # Tap on "Skip" button 1 time
    driver.find_element_by_id("ru.aton.financeapp:id/showcaseSkipBtn").click()
    # Tap on "OK" button 1 time
    driver.find_element_by_id("ru.aton.financeapp:id/tvTopButton").click()
except Exception as error_msg:
    print(error_msg)


# ================ Some user actions ================

print('Some user actions\n')

try:
    # Tap on "Show all ideas" button
    driver.find_element_by_id("ru.aton.financeapp:id/glass_case_all_ideas_button").click()
    # Scroll gallery
    for index in range(3):
        sleep(2)
        touch.long_press(x=508, y=1472, duration=1000).move_to(x=528, y=492).release().perform()
    # Tap on "Back" button upper left
    driver.find_element_by_id("ru.aton.financeapp:id/iconLeft").click()
    # Scroll gallery
    for index in range(3):
        sleep(2)
        touch.long_press(x=1009, y=1458, duration=1000).move_to(x=88, y=1441).release().perform()
    # Tap on last item
    # touch.tap(x=980, y=1440).perform()
except Exception as error_msg:
    print(error_msg)


# ================ Login try ================

print('Login try\n')

try:
    # Tap on "Enter" button upper center
    driver.find_element_by_id("ru.aton.financeapp:id/screen_login_glass_case_button").click()
    # Enter random Phone Number and tap "Login" button
    random_phone = random.randint(0000000, 9999999)
    driver.find_element_by_id("ru.aton.financeapp:id/loginOrPhone").send_keys(7000, random_phone)
    driver.find_element_by_id("ru.aton.financeapp:id/loginButton").click()
    # Enter invalid smsCode
    driver.find_element_by_id("ru.aton.financeapp:id/smsCode").send_keys("0000")
    # Assert SMS Title
    sms_title = driver.find_element_by_id("ru.aton.financeapp:id/smsTitle").get_attribute("text")
    print(sms_title)
    assert sms_title == "НЕВЕРНЫЙ КОД ДОСТУПА", "SMS Title doesn't match"
    print('\nSMS Title Successfully Asserted\n')

except Exception as error_msg:
    print(error_msg)


# ================ Observe results ================

sleep(2)

# ================ Clean device after test ================

print('Cleaning Device\n')

# Close app
driver.close_app()

# Remove app from device
driver.remove_app('ru.aton.financeapp')
sleep(4)

# Close driver session
driver.quit()

print('Test Ended')
