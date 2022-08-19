def product_info_scraper(link: str, tab_no: int):
    driver.switch_to.window(driver.window_handles[tab_no % 2])
    driver.get(f"{link}")
    time.sleep(3.5)
    single_page_products_list = WebDriverWait(driver=driver, timeout=10).until(method=single_page_products_list_finder)
    for product in single_page_products_list:
        data = {}
        try:
            product_url = product.find_element(by=By.CSS_SELECTOR, value="a[class='itemlink']")
            data["url"] = product_url.get_attribute('href')
            if not db.contains(Todo.url == str(data['url'])):
                db.insert(data)
                print(data)
            else:
                print(f"Already Exists {product_url.get_attribute('href')}")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    import time
    from dotenv import dotenv_values
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from tinydb import TinyDB, Query

    config = dotenv_values(dotenv_path='./.env')
    db = TinyDB("./db_files/yoox_product_url.json")
    Todo = Query()

    options = uc.ChromeOptions()
    driver = uc.Chrome(driver_executable_path=config['DRIVER_PATH'], options=options)
    driver.get(config['BASE_URL'])
    driver.implicitly_wait(time_to_wait=2)
    driver.switch_to.new_window(type_hint='tab')
    single_page_products_list_finder = ec.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div[class='itemData text-center']")
    )

    from_page = int(config['START_PAGE'])
    to_page = int(config['END_PAGE'])

    for page_number in range(from_page, to_page + 1):
        url = f"{config['PAGE_URL']}{page_number}"
        try:
            product_info_scraper(url, page_number)
        except Exception as exception:
            print(exception)

    driver.close()
    print("Finished")
