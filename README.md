# Detourning the Web
#### ITP/NYU - Spring 2018 - Mondays from 6:30pm to 9:25pm
#### Sam Lavigne - lavigne@nyu.edu
#### [Sign up for office hours here](https://calendar.google.com/calendar/selfsched?sstoken=UUJjd182VklGYVlRfGRlZmF1bHR8Y2E5NDJlM2QyMmJiNDcwZDI0YzIyNGY1ZDdkOWIxZGY)

Detournement is the practice of "hijacking" cultural or artistic materials and reusing them to produce new works that both counter and explicate the original intent or ideology of the source material. In this class students will learn how to scrape massive quantities of material from the internet with Python, and then use that material to make satirical, critical and political projects. Each week we will cover a different web scraping technique, with production assignments relating to text, image and video.

***

## Schedule

### Week 1 - Jan 22
* Intro & ground rules
* HTML/CSS basics
 	* Tags, attributes, classes, ids, css selectors
* Using Chrome/Firefox developer tools
* the DOM: what it is and how to modify it
	* Editing a single element
	* Editing multiple elements
	* Editing subelements

#### WEEK 1 HOMEWORK
* **Project One: Critique three (3) websites by altering their content using Chrome/Firefox developer tools. Save screenshots and [post to the class homework wiki](https://github.com/antiboredom/detourning-the-web-2018/wiki).**
* Readings:
	* [A User’s Guide to Détournement](http://www.bopsecrets.org/SI/detourn.htm)
	* [Uncreative Writing, Chapter 2, Language as material](https://monoskop.org/media/text/goldsmith_2011_uncreative_writing/#filepos104950)

***

### Week 2 - Jan 29
* [opening video](https://www.youtube.com/watch?v=Id3G5UOl9lg)
* Screenshot presentations
* Command line basics
* Python basics
* Setting up our environments with pip and virtualenv
* Intro to web scraping with Beautiful Soup

#### WEEK 2 HOMEWORK
* Readings:
  * [The Infinity of Lists](http://linktocome.com)
* **Project Two - The List (Part 1): Scrape the web, and then create a list with the material you collect.**
 	* Your list should be text only.
 	* You list should be long

***

### Week 3 - Feb 5
* [opening video](https://www.youtube.com/watch?v=nbiEfr5FxEA)
* ~~More web scraping with Beautiful Soup~~
* Writing to a file
* Dictionaries
* JSON
	* writing to json
	* scraping from ajax/json
		* Fox News search
		* Instagram
* Primer on manipulating text with TextBlob
	* getting words
	* getting parts of speech
	* most common phrases


#### WEEK 3 HOMEWORK
* **Project Two - The List (Part 2): Create a physical version of your list: for example, print it on roll paper, make a book, make a website, make a projection, recite it, etc.**
* Readings:
	* [Fuck Off Google](https://events.ccc.de/congress/2014/Fahrplan/system/attachments/2530/original/fuckoffgoogleeng.pdf)
<!-- * **Project (due on week 5) - pick one:** -->
<!-- 	* Create a script that acts on your behalf online. -->
<!-- 	* Create a system that automatically manipulates images found online. -->

***

### Week 4 - Feb 12
* Project #2 due
* Downloading files
* Manipulating images
	* wth imagemagick
	* with Pillow
* Calling external commands using subprocess.call

#### WEEK 4 HOMEWORK
* Readings:
	* [A Hacker Manifesto](http://www.neme.org/texts/hacker-manifesto)
	* [How to write satire about current events](http://www.wikihow.com/Write-Satire-About-Current-Events)

***

### Week 5 - FEB 26
* Web scraping with Selenium and puppeteer


#### WEEK 5 HOMEWORK
* **Project Three - Image: Create a system that automatically manipulates images found online.**
* Readings:
	* [Caliban and the Witch](https://libcom.org/files/Caliban%20and%20the%20Witch.pdf) (chapter one)

***

### Week 6 - Mar 5
* Automating the online self
* `AJAX` and how to deal with it

***

### Week 7 - Mar 19
* Project #3 due

***

### Week 8 - Mar 26
* Bots


#### WEEK 8 HOMEWORK
* **Project Four - Make a simple bot**

***

### Week 9 - Apr 2
* Scraping and editing video
<!-- * Make a video using python -->
<!-- * Come in with an idea for your final project to be discussed on Mar 9 -->

#### WEEK 9 HOMEWORK
* **Prepare a proposal for your final project.**


***

### Week 10 - Apr 9
* Project proposals due
* TBD

***

### Week 11 - Apr 16
* Lab day

***

### Week 12 - Apr 23
* Final presentations

***

## Grading/Expectations

* Each of the four main projects is worth 20% of your grade, and class participation is 20%.
* More than one unexcused absence is grounds for failure :(
* But no one will fail.
* It's OK to show work that has sensitive or difficult content, but if you do so give everyone a quick heads up beforehand.
* We will be critiquing each others work in the class. Be honest but friendly when critiquing other students. When receiving critique please listen and take feedback seriously.
* Feel free to use your laptop in class to take notes or follow along when I'm covering programming topics. Please do not use your laptops to do stuff on social media unrelated to the class etc.
* The only time laptop use is strictly prohibited is when other students are presenting their work.
* Turn off your phones or put them on silent during class.
* No projects about Trump.

***

## Resources

### Learning Python
* [Learn Python The Hard Way by Zed Shaw](https://learnpythonthehardway.org/book/) (not actually hard)

### Command Line
* [Intro to Unix by Allison Parrish](http://www.decontextualize.com/teaching/rwet/introduction-and-unix-tutorial/)
* [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial)

### Scraping
* [Really nice web scraping tutorial](https://first-web-scraper.readthedocs.io/en/latest/)
* [Web Scraping from "Automate the Boring Stuff"](https://automatetheboringstuff.com/chapter11/)
* [Scrapy](https://scrapy.org/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Selenium](http://selenium-python.readthedocs.io/)
* [Splinter](http://splinter.readthedocs.io/en/latest/index.html)

### Text Parsing
* [Pattern](http://www.clips.ua.ac.be/pages/pattern-en)
* [TextBlob](https://textblob.readthedocs.io/)
* [NLTK](http://www.nltk.org/)
* [SpaCy](https://spacy.io/)

### Image
* [Pillow](https://pillow.readthedocs.io/en/4.0.x/)
* [ImageMagick](https://www.imagemagick.org/script/index.php)

### Audio
* [Sox](http://sox.sourceforge.net/)
* [Pydub](http://pydub.com/)

### Video
* [ffmpeg](https://ffmpeg.org/)
* [moviepy](http://zulko.github.io/moviepy/)
* [vidpy](http://antiboredom.github.io/vidpy/)
