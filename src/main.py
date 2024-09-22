import requests
from bs4 import BeautifulSoup
import pandas as pd

# Api url and key
API_KEY = 'sZ99pMnNtUwwYHWit8H4PnEfWWz6vkMy'
HOLIDAYS_URL = f'https://calendarific.com/api/v2/holidays?api_key={API_KEY}'
# Url for the exams page to scrape
EXAMS_URL = 'https://www.jagranjosh.com/exams'

# function to scrape exam  data
def scrape_exams(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    # list to store exam data
    exams = []
    for exam in soup.find_all('li'):
        name_tag = exam.find('h3', class_='ExamsLanding_ExamTypes__vr7ED')
        if name_tag:
            # extract the text out of name tag
            exam_name = name_tag.text.strip()
        else:
            exam_name = "No exam name available"
        date_tag = exam.find_all('p')
        #   extract exam date
        if len(date_tag) > 1:
            exam_date = date_tag[1].text.strip()
        else:
            exam_date = "No exam date available"
         # add the details to the list above
        exams.append([exam_name, exam_date])
# making a detaframe for the data
    df = pd.DataFrame(exams, columns=['Exam Name', 'Exam Date'])
#    cleaning the data: removing the name with missing exam name or missing date
    df = df[(df['Exam Name'] != "No exam name available") & (df['Exam Date'] != "No exam date available")]
  #       changing the date format
    df['Exam Date'] = pd.to_datetime(df['Exam Date'], format='%A, %b %d, %Y', errors='coerce')
    return df

# fetching holiays data from calendarific api
def fetch_holidays(year, country):
  # defining paramters
    params = {
        'year': year, 
        'country': country
        }
    response = requests.get(HOLIDAYS_URL, params=params)
    return response.json()['response']['holidays'] if response.status_code == 200 else None
# parsing holiday data
def parse_holidays(holidays, country):
    holiday_data = []
    for holiday in holidays:
# getting name,date,type and state of the holiday
        holiday_name = holiday.get('name', 'Unknown Holiday')
        # if data is not available, fill the second choice 
        holiday_date = holiday['date']['iso']
        holiday_type = holiday.get('type', 'Unknown Type')
        holiday_states = holiday.get('locations', ['All'])
# appends holidays data
        holiday_data.append([holiday_name, country, holiday_states, holiday_type, holiday_date])
    # create a dataframe of holidays
    df = pd.DataFrame(holiday_data, columns=['Holiday', 'Country', 'State', 'Type', 'Date'])
        # changing the date format
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
    return df



def combine_data(exam_df, holidays_df):
  #  combining data based on the exam
    df = pd.merge(exam_df, holidays_df, how='outer', left_on='Exam Date', right_on='Date')
  # creating one date column out of two and merging them in ascending order
    df['Combined Date'] = df['Exam Date'].combine_first(df['Date'])
    # sorting df
    df = df.sort_values('Combined Date').reset_index(drop=True)
# create two new columns: one for exams and one for holidays
    df['Exams'] = df['Exam Name'].fillna('No Exam')
    df['Holidays'] = df['Holiday'].fillna('Not a Holiday')
  # all country column defaulting to india
    df['Country'] = 'India'
    df['Holiday Type'] = df['Type'].fillna('N/A')
# return a dataframe of combined data
    return df[['Combined Date', 'Exams', 'Holidays', 'Country', 'Holiday Type']]

def check_clashes(df):

  # input from user
    user_input = input("Do you want to know where there is a clash between an exam and a holiday? (yes/no): ").strip().lower()
# if answer is yes
    if user_input == 'yes':
  #  check if exams column and holidays column fot some row is not null
        clashes = df[(df['Exams']!="No Exam") & (df['Holidays']!='Not a Holiday')]
# if there are clashes
        if not clashes.empty:
            print("Here are the rows where there is a clash between an exam and a holiday:")
          # return the datafame with clashes
            return pd.DataFrame(clashes)  
        else:
            print("There are no clashes between exams and holidays.")
          
    else:
        print("You chose not to check for clashes.")

# Main Execution

# calling fetch_holidays function inside parse_holidays function to get the dataframe of holidays
holidays_df = parse_holidays(fetch_holidays(year=2024, country='IN'), 'IN')
# calling scrape_exams function to get the exams dataframe
exam_df = scrape_exams(EXAMS_URL)

# if there are elements in  both the dataframes
if exam_df is not None and not holidays_df.empty:
  # create a final dataframe by calling combine function
    df_final = combine_data(exam_df, holidays_df)
    df_final.head(100).to_csv('ExamHolidays.csv', index=False)
  # check for the clashes
    clashes_df = check_clashes(df_final.head(100))
    print(clashes_df)
    # print(df_final)
df_loaded = pd.read_csv('ExamHolidays.csv')
# clashes_df 
# df_final
