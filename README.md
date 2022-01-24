# smart-revise-bot
![Preview](https://i.imgur.com/okgz66Z.gif)


# Introduction
https://smartrevise.online/ is a multiple choice question revision website used by school students from the UK to revise for their Computer Science GCSE or A-level exams.

# Prerequisites
- Google Chrome (chromedriver added to PATH) 
- Python 3.9+ (https://www.python.org/downloads/)
- Selenium

To install selenium, open your terminal and paste the following line:
```
pip install selenium
```

To add chromedriver to PATH, follow this tutorial: 
https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/

# Starting the bot
In a terminal, execute start_bot.py with the appropiate arguments.
```
usage: start_bot.py [-h] -e EMAIL -p PASSWORD -l LINK [-H HEADLESS] [-L LIMIT]

Automatically answer questions on smartrevise.online

options:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        The email of your account on smartrevise.online
  -p PASSWORD, --password PASSWORD
                        The password of your account on smartrevise.online
  -l LINK, --link LINK  The number at the end of the link where you answer
                        questions
  -H HEADLESS, --headless HEADLESS
                        Run in headless mode? True/False
  -L LIMIT, --limit LIMIT
                        How many questions to answer?
```

Example usage: `python start_bot.py -e your_account_email@provider.com -p your_password -l 3 -L 100`

# The -l link argument
Log into smartrevise.online, go to your course and answer a question. When you look at the link of the page, you should see something like this:
```
https://smartrevise.online/student/revise/Question/26
```

The -l argument is 26 in this case, for other courses that number is different.

# How it works
This bot is possible due to the 'I don't know' button the website offers. It clicks the button, stores the correct answer, and when it comes across that question again, it will answer it correctly.

# Afterword 
This bot was made out of boredom. As Craig and Dave, the creators of the website, put it - you are "only cheating yourself if you don't use the application properly", as "it can't learn about your strong & weak areas". They are right, I do not suggest that you use it for homework or whatever, it was made just for fun.
I have had the code for this bot for quite some time, but I only now decided to make it public because I received an email from the Mark Plowman, the tehnical director of smartrevise and CraignDave Ltd, stating that my bot is "the most successful one we've seen to date" and that he is curious to see the source code.

This bot was made with absolutely NO ILL INTENT and I am not responsible for how this code is used by other parties.




