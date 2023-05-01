from bs4 import BeautifulSoup
import requests
import pandas as pd

def webscraping():
    # If you would like to scrape for more days, however given that the web link format is exactly the same except the
    # number for the date, simply change the number in the `while iteration < 4:` to a number you'd like.

    # Required to keep track of the day (date).
    iteration = 0
    # To store the header columns.
    header_list = []
    # To store the number of daily COVID cases.
    covid_cases_list = []

    # Iterating only till 4th of March for the 5th of March the website is broken.
    # From 6th of March and on it's working well.
    while iteration < 4:
        # Required to store the complete table for the given day. As the iteration increases, the table is reset.
        table = []
        iteration += 1

        request_page = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-" +
                                    str(iteration) + "-martie-ora-13-00-2/")
        link = BeautifulSoup(request_page.text, "html.parser")
        main = link.find_all('div', attrs={'class': 'inside-article'})
        for obj in main:
            for table_index in obj.find_all('table'):
                for header in table_index.find_all('tr'):
                    table_list = [table_trs.get_text() for table_trs in header.find_all('td')]
                    # Appending to the `table` variable since I will iterate below through it to extract headers and
                    # number of COVID cases.
                    table.append(table_list)
                # Since there are 42 regions in Romania, and the website's table has 44, we will extract the number of
                # needed regions.
                for region in table[1:43]:
                    # Not the cleanest piece of code, but essentially I needed to introduce the if/else statement
                    # in order to separate the headers from the number of COVID cases.
                    if iteration > 1:
                        covid_cases_list.append(region[2])
                    else:
                        header_list.append(region[1])
                        covid_cases_list.append(region[2])
                break

    # Generating the column names depending on the dates scraped, i.e., "01.03", "02.03" for scraping 2 days only.
    date_columns = [f"0{i}.03" for i in range(1, iteration+1)]
    # Adding the two lists together so we can turn it into the column header of the dataframe.
    columns = ["NR. CRT", "Judet"] + date_columns
    # Since the values for all scraped days were inserted above with no clear separation for the days, we need to
    # split the list into a nested list after each 42nd element. Answer from: https://stackoverflow.com/a/15890829
    covid_cases_list = [covid_cases_list[x:x + 42] for x in range(0, len(covid_cases_list), 42)]
    # Creating a dataframe with the respective columns.
    df = pd.DataFrame(columns=columns)
    # Assigning the headers to the "Judet" column.
    df["Judet"] = header_list
    # Generating the range of numbers for the "NR. CRT" column.
    df["NR. CRT"] = range(1, 43)
    # Assigning each sublist from the nested list to the specific column, depending on which day it belongs to.
    # I do iteration + 1 because max. iteration from the while loop is 3, but we need 4 columns (days).
    for i in range(1, iteration + 1):
        # I do i - 1 because the list indexing starts from 0.
        df[f'0{i}.03'] = covid_cases_list[i-1]

    # Replacing the dot in numbers with empty string so that I can convert the columns into numeric type.
    # Answer from: https://stackoverflow.com/a/44176655
    df = df.replace('\.', '', regex=True)
    # Converting the columns from the third index to numeric.
    df.iloc[:, 2:] = df.iloc[:, 2:].apply(pd.to_numeric)
    # Calculating the totals of the COVID cases per day.
    df_sum = df.iloc[:, 2:].sum()
    # Transforming the totals into a row, where we append empty strings for the first two columns because there
    # is no meaningful sum for them.
    df.loc['Total'] = [''] * 2 + list(df_sum)

    print(df)

    # Writing the dataframe to excel.
    with pd.ExcelWriter('CazuriCovid.xlsx') as writer:
        df.to_excel(writer, index=False)


webscraping()
