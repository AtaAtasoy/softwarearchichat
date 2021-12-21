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
browser.get("http://localhost:8000/accounts/logout")
assert browser.title == "Login Page"

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
browser.get("http://localhost:8000/accounts/logout")
assert browser.title == "Login Page"

username = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[2]")
password = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[3]")
submit = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/button")

username.send_keys(valid_username)
password.send_keys(valid_password)
submit.click()

WebDriverWait(browser, timeout=10).until(EC.title_is("Chat Rooms"))
assert browser.title == "Chat Rooms"

WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)

contact = browser.find_element(By.LINK_TEXT, valid_username2)
contact_name = contact.text
contact.click()
WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)
chat_room_title = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/span").text
assert contact_name == chat_room_title == valid_username2

message_box = browser.find_element(By.XPATH, '//*[@id="message_input"]')
send_button = browser.find_element(By.XPATH, '//*[@id="chat-message-submit"]')
message_box.send_keys("This is a test message")
send_button.click()

browser.get("http://localhost:8000/accounts/logout")
WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)

username = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[2]")
password = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/input[3]")
submit = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/form/button")

username.send_keys(valid_username2)
password.send_keys(valid_password2)
submit.click()
WebDriverWait(browser, timeout=10).until(EC.title_is("Chat Rooms"))
assert browser.title == "Chat Rooms"

WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located)
contact = browser.find_element(By.LINK_TEXT, valid_username)
contact_name = contact.text
contact.click()
chat_room_title = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/span").text
assert chat_room_title == valid_username == contact_name

message_table = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div/div[1]')
assert "This is a test message" in message_table.text

browser.close()

