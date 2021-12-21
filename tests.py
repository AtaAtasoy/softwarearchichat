from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

valid_username = get_random_string(8)
valid_password = get_random_string(12)
valid_email = get_random_string(8) + "@gmail.com"

valid_username2 = get_random_string(8)
valid_password2 = get_random_string(12)
valid_email2 = get_random_string(8) + "@gmail.com"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://localhost:8000/accounts/register")
assert browser.title == "Register Page"

username = browser.find_element(By.XPATH, '//*[@id="id_username"]')
email = browser.find_element(By.XPATH, '//*[@id="id_email"]')
password = browser.find_element(By.XPATH, '//*[@id="id_password1"]')
password2 = browser.find_element(By.XPATH, '//*[@id="id_password2"]')
register_btn = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/form/input[6]')

username.send_keys(valid_username)
email.send_keys(valid_email)
password.send_keys(valid_password)
password2.send_keys(valid_password)
register_btn.click()
WebDriverWait(browser, timeout=10).until(EC.title_is("Chat Rooms"))
print("REGISTERED ", valid_username, " SUCCESSFULLY")
browser.get("http://localhost:8000/accounts/logout")
assert browser.title == "Login Page"
print("LOGGED OUT ", valid_username, " SUCCESSFULLY")


browser.get("http://localhost:8000/accounts/register")
assert browser.title == "Register Page"

username = browser.find_element(By.XPATH, '//*[@id="id_username"]')
email = browser.find_element(By.XPATH, '//*[@id="id_email"]')
password = browser.find_element(By.XPATH, '//*[@id="id_password1"]')
password2 = browser.find_element(By.XPATH, '//*[@id="id_password2"]')
register_btn = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/form/input[6]')

username.send_keys(valid_username2)
email.send_keys(valid_email2)
password.send_keys(valid_password2)
password2.send_keys(valid_password2)
register_btn.click()
WebDriverWait(browser, timeout=10).until(EC.title_is("Chat Rooms"))
print("REGISTERED ", valid_username2, " SUCCESSFULLY")

browser.get("http://localhost:8000/accounts/logout")
assert browser.title == "Login Page"
print("LOGGED OUT ", valid_username2, " SUCCESSFULLY")


username = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[2]")
password = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[3]")
submit = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/button")

username.send_keys(valid_username)
password.send_keys(valid_password)
submit.click()

WebDriverWait(browser, timeout=10).until(EC.title_is("Chat Rooms"))
assert browser.title == "Chat Rooms"
print("LOGGED ", valid_username, " IN SUCCESSFULLY")

WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)

contact = browser.find_element(By.LINK_TEXT, valid_username2)
contact_name = contact.text
contact.click()
WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)
chat_room_title = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/span").text
assert contact_name == chat_room_title == valid_username2
print("OPENED CHAT WITH ", valid_username2, " SUCCESSFULLY")


message_box = browser.find_element(By.XPATH, '//*[@id="message_input"]')
send_button = browser.find_element(By.XPATH, '//*[@id="chat-message-submit"]')
message_box.send_keys("This is a test message")
send_button.click()
message_table = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div/div[1]')
browser.implicitly_wait(5)
assert "This is a test message" in message_table.text
print("SENT MESSAGE SUCCESSFULLY")

browser.get("http://localhost:8000/accounts/logout")
WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)
print("LOGGED OUT ", valid_username, " SUCCESSFULLY")

username = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[2]")
password = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[3]")
submit = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/button")

username.send_keys(valid_username2)
password.send_keys(valid_password2)
submit.click()
WebDriverWait(browser, timeout=10).until(EC.title_is("Chat Rooms"))
assert browser.title == "Chat Rooms"
print("LOGGED ", valid_username2, " IN SUCCESSFULLY")

WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)
contact = browser.find_element(By.LINK_TEXT, valid_username)
contact_name = contact.text
contact.click()
chat_room_title = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/span").text
assert chat_room_title == valid_username == contact_name
print("OPENED CHAT WITH ", valid_username, " SUCCESSFULLY")


message_table = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div/div[1]')
assert "This is a test message" in message_table.text
print("RECEIVED THE MESSAGE ", valid_username, " SUCCESSFULLY")

browser.close()