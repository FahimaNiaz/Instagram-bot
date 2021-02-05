from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys


#To login to your account
def login(driver, username, pw):
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    sleep(2)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(pw)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(2)
    driver.get("https://www.instagram.com/{0}/".format(username))
    return "successful"

#returns a list of people who you follow but do not follow you back
def get_unfollowers(driver, username):
    sleep(2)
    driver.get("https://www.instagram.com/{0}/".format(username))
    driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
    following =get_names(driver, username)
    driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
    followers =get_names(driver, username)
    not_following_back = [user for user in following if user not in followers]
    return not_following_back
#returns the list of followers or people we are following

def followers(driver, username):
    driver.get("https://www.instagram.com/{0}/".format(username))
    driver.find_element_by_partial_link_text("follower").click()
    sleep(2)
    followers =get_names(driver, username)
    my_followers = [user for user in followers]
    foll=[]
    foll.append(my_followers[0])
    return foll

#to give the list of people you follow
def following(driver,username):
    driver.get("https://www.instagram.com/{0}/".format(username))
    driver.find_element_by_partial_link_text("following").click()
    following =get_names(driver, username)
    my_following= [user for user in following]
    foll=[]
    foll.append(my_following[0:4])
    return foll

#sends an automated mesage to a list of users
def automate_message(driver, username, message, user):
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click() 
    sleep(2)
    for i in user: 
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i) 
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
        sleep(2)
        send= driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        send.send_keys(message)
        sleep(1)
        send.send_keys(Keys.RETURN)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        sleep(2)
    driver.get("https://www.instagram.com/{0}/".format(username))
    return "message sent"


def get_names(driver, username):
    sleep(3)
    scroll_box=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]") 
    last_h,h=0,1
    while last_h!=h:
        last_h=h
        sleep(3)
        h=driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
    links=scroll_box.find_elements_by_tag_name('a')
    names=[name.text for name in links if name.text != '']
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
    return names

#for the headless driver
def driver():
    firefox_binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
    #put the path where your firefox.exe is present in the line above
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless= True
    driver= webdriver.Firefox(executable_path="C:/Program Files/geckodriver.exe", options=fireFoxOptions, firefox_binary=firefox_binary)
    return driver#the executable path is where your geckodriver is present

#to logout
def logout(driver):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/hr').click()
    sleep(2)

#to like a number of posts in the given hashtag
def like_posts(driver, hashtag):
    driver.get('https://www.instagram.com/explore/tags/{0}/'.format(hashtag))
    sleep(2)
    for i in range(1,4):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[{0}]'.format(i)).click()
        sleep(3)
        driver.find_element_by_xpath("//article//section//button//*[@aria-label='Like']").click()
        driver.get('https://www.instagram.com/explore/tags/{0}/'.format(hashtag))
    
    return "liked pictures"

