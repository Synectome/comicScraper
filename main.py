from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import os
import datetime
from Comic import Comic


def save2file(data, name=None):
    file_path = str(datetime.datetime.now()) + ".txt"
    if name:
        file_path = name + '.txt'

    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")


def get_comics_urls(driver, max_number=None):
    comics_url_list = []
    comic_count = 0
    pageNumber = 1
    if not max_number:
        max_number = 99999999999999

    while comic_count <= max_number:
        current_pages_comic_list_element = driver.find_element(By.CLASS_NAME, "list-comic")
        # current_pages_comics_urls = current_pages_comic_list_element.find_elements(By.CLASS_NAME, "item")
        current_pages_comics_urls = current_pages_comic_list_element.find_elements(By.TAG_NAME, "a")
        print('number of comic items : ', len(current_pages_comics_urls))
        if len(current_pages_comics_urls) == 0:
            break
        comics_url_list += [element.get_attribute('href') for element in current_pages_comics_urls]
        comic_count += len(comics_url_list)

        # click next page button before repeating loop
        pageNumber += 1
        try:
            time.sleep(1)
            driver.get(url + "?page=" + str(pageNumber))
        except:
            break
    return comics_url_list


def setup():
    # Create a webdriver instance (for Chrome in this example)
    # driver = webdriver.Chrome()
    # or firefox
    firefox_options = Options()
    firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver


def read_comic_URLs_file(fp):
    comicurls = []
    # read the file, and navigate to each individual comic
    with open(fp, 'r') as file:
        for line in file:
            comicurls.append(line)
    return comicurls


def make_comic_obj(driver):
    comic_information_container = driver.find_element(By.CLASS_NAME, "barContent")
    title = comic_information_container.find_element(By.CLASS_NAME, "bigChar").text
    print("title is : ", title)
    comic = Comic(title)
    publisher = ""
    writer = ""
    artist = ""
    publication_date = ""
    completed = ""


if __name__ == "__main__":
    # URL to the site
    url = "https://readcomiconline.li/ComicList"
    comicURLsFileName = "ComicsURLs"
    cwd = os.getcwd()
    file_path = os.path.join(cwd, comicURLsFileName + ".txt")

    try:
        d = setup()

        if not os.path.exists(file_path):
            # there is no saved list of the Comic urls, so we need to do that
            d.get(url)
            comic_urls = get_comics_urls(d, 60)
            print("number of comic urls collected = ", len(comic_urls))
            save2file(comic_urls, comicURLsFileName)
        else:
            comic_urls = read_comic_URLs_file(file_path)

        for comic_url in comic_urls:
            # do something
            d.get(comic_url)
            make_comic_obj(d)
            break
        d.quit()
    finally:
        pass

