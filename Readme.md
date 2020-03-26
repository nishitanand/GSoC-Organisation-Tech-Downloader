<h1>GSoC Organisation and Tech Downloader</h1>


While applying for GSoC, students have to see which organisations were selected in which year and which organisations used the same language and tech stack as they are proficient in.

So for this, they have to spend hours looking at the web pages of all the organisations and this is a very tiring task.

This project helps them by giving them the list of all the organisations that used a given tech stack / language in a given year.

User first has to input the year that they want to search for and then enter which language or tech stack they want to search for.
Eg- python, java, django, flask, javascript, NLP etc.


This Program then scrapes the GSoC Archive website and searches for all the organisations which used that tech stack in the year enteerd by the user. It then uses BeautifulSoup library and Requests library and does web scrapping on the website.

It then uses File Handling to write the details to a text file. Along with the language/tech stack entered by the user, the program saves all the languages and tech stacks used by those organisations in that year as well as the number of organisations using that tech stack / language.


To use it, first write this command in the command line

pip install -r requirements.txt

or (for Mac)

pip3 install -r requirements.txt

and then to run the file write

python GSoC-Org-Tech-Downloader.py

or (for Mac)

python3 GSoC-Org-Tech-Downloader.py

