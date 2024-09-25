# Exams & Holidays Analysis

Welcome to the Exams & Holidays Analysis project! This initiative combines exam schedules with holiday data in India to create a unique dataset that can be valuable for various stakeholders.

__API__: I used the Calendarific API to get holiday information for India.(https://calendarific.com/)

   __Purpose__: To compile a comprehensive list of holidays in India for 2024.

   __Why This API?__: Calendarific provides reliable and up-to-date holiday information across multiple countries.

__Web Scraping__: I scraped exam data from the Jagran Josh website (https://www.jagranjosh.com/exams).

   __Purpose__: To gather details about 2024 exams in India.

   __Why This Website?__: Jagran Josh is a trusted source for educational information in India, including exam schedules.

## Why Is This Dataset Valuable?

The dataset I created offers a unique combination of exam schedules and holiday information that isn’t readily available anywhere else in a clean format. Here’s why it matters:

__For Students and Educators__: It helps plan study schedules by identifying potential clashes between exams and holidays.

__Resource Management__: Educational institutions can better allocate resources by understanding when exams are scheduled relative to holidays.

__Policy Insights__: Education policymakers can use this data for informed decision-making regarding exam scheduling.

__Cultural Context__: It provides insights into how cultural events (holidays) intersect with educational milestones (exams).

## User Input for Clashes:
During execution, the script will ask if you want to see clashes between exams and holidays. 
If you input 'yes', it will display all instances where an exam date coincides with a holiday. 
Any other input will skip this step. 

This feature allows users to quickly identify potential conflicts in the schedule.

### This is how it looks:

<img width="679" alt="Screenshot 2024-09-25 at 1 08 52 PM" src="https://github.com/user-attachments/assets/6addae82-5a04-49d7-868b-5a989bccbe21">


## How to Run the Project

Getting started is easy! Just follow these steps:

 Clone the repository:
   
   git clone https://github.com/gunjan2713/Exam_HolidaysAnalysis

   cd Exam_HolidaysAnalysis

   python -m venv venv

   source .venv/bin/activate

   pip install -r requirements.txt

   python src/main.py
