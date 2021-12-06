from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def initial_config(date):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    url = f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{date}-ianuarie-ora-13-00/"
    browser.get(url)
    return browser


def get_data(browser):
    table = browser.find_element(By.TAG_NAME, 'table')

    data_list = table.text.split('\n')

    header = browser.find_element(By.TAG_NAME, "tr").text.split('\n')
    dictionary = {i: [] for i in header}
    print(header)

    for j in range(0, len(header)):
        for i in range(len(header) + int(j), len(data_list), len(header)):
            dictionary[header[int(j)]].append(data_list[i])
        print()
    print(dictionary)

    return pd.DataFrame(dictionary)


def write_data(df, date):
    with pd.ExcelWriter(f'covid_cases_scraping_{date}.xlsx') as writer:
        df.to_excel(writer, sheet_name=f"covid_{date}_nov", index=False, encoding="utf-16")


def main():
    for date in range(14, 21):
        browser = initial_config(date)
        df = get_data(browser)
        write_data(df, date)

    browser.close()


if __name__ == "__main__":
    main()
