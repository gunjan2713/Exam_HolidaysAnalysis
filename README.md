Exams & Holidays Analysis

Welcome to the Exams & Holidays Analysis project! This initiative combines exam schedules with holiday data in India to create a unique dataset that can be valuable for various stakeholders.

Data Sources

API: I used the Calendarific API to get holiday information for India.(https://calendarific.com/)

   Purpose: To compile a comprehensive list of holidays in India for 2024.

   Why This API?: Calendarific provides reliable and up-to-date holiday information across multiple countries.

Web Scraping: I scraped exam data from the Jagran Josh website (https://www.jagranjosh.com/exams).

   Purpose: To gather details about 2024 exams in India.

   Why This Website?: Jagran Josh is a trusted source for educational information in India, including exam schedules.

Why Is This Dataset Valuable?

The dataset I created offers a unique combination of exam schedules and holiday information that isn’t readily available anywhere else in a clean format. Here’s why it matters:

For Students and Educators: It helps plan study schedules by identifying potential clashes between exams and holidays.

Resource Management: Educational institutions can better allocate resources by understanding when exams are scheduled relative to holidays.

Policy Insights: Education policymakers can use this data for informed decision-making regarding exam scheduling.

Cultural Context: It provides insights into how cultural events (holidays) intersect with educational milestones (exams).

How to Run the Project

Getting started is easy! Just follow these steps:

 Clone the repository:
   
   git clone https://github.com/gunjan2713/Exam_HolidaysAnalysis

   cd Exam_HolidaysAnalysis

   python -m venv venv

   source .venv/bin/activate

   pip install -r requirements.txt

   python src/main.py
