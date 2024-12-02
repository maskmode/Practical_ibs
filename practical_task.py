from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))

try:
    driver.get("http://google.com/ncr")
    print("Шаг 1: Открыта страница http://google.com/ncr")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenide")
    search_box.send_keys(Keys.RETURN)
    print("Шаг 2: Выполнен поиск по слову 'selenide'")

    first_result_link = WebDriverWait(driver, 20).until(  # Увеличил время ожидания
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "selenide.org"))
    ).get_attribute("href")

    if first_result_link and "selenide.org" in first_result_link:
        print("Шаг 3: Первый результат — ссылка на сайт selenide.org")
    else:
        print("Шаг 3: Первый результат не соответствует ссылке на сайт selenide.org")

    try:
        first_image = WebDriverWait(driver, 5).until(  # Увеличиваем время ожидания
            EC.presence_of_element_located((By.XPATH, "(//img)[1]"))
        )
        first_image_src = first_image.get_attribute("src")

        if first_image_src and "selenide" in first_image_src:
            print("Шаг 5: Первое изображение связано с сайтом selenide.org")
        else:
            print("Шаг 5: Первое изображение не связано с сайтом selenide.org")
    except Exception as e:
        print(f"Шаг 5: Ошибка при получении первого изображения - {e}")

    images_link = driver.find_element(By.LINK_TEXT, "All")
    images_link.click()
    print("Шаг 6: Вернулись в раздел поиска Все")

    first_result_link = WebDriverWait(driver, 20).until(  # Увеличил время ожидания
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "selenide.org"))
    ).get_attribute("href")

    if first_result_link and "selenide.org" in first_result_link:
        print("Шаг 7: Первый результат снова ссылка на сайт selenide.org")
    else:
        print("Шаг 7: Первый результат не соответствует ссылке на сайт selenide.org")

finally:
    driver.quit()
