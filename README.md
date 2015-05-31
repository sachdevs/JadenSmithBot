# JadenSmithBot
Markov chain bot, states built using Jaden's tweets <br>
Since Jaden deleted his account, I just copy pasted his famous tweets from different websites<br>
If you want to make a bot for someone else usomg tweet_scraper, simply run a sed command with the following regex and change file extension to *.txt:
```
\d+,\d+-\d+-\d+\s\d+:\d+:\d+,
```
Replace that with nothing, then remove the first line of the text manually and you should be ready to go!
Or you can modify the program to just interpret csv files... (probably easier to do that :P)<br>
I am actually quite disappointed that Jaden Smith no longer has his account. Training this bot against 69 lines of text seems too little. I may switch to another person if it doesnt work out.
EDIT: So the chain generator and text gen is finished. Examples can be found in sampleJadenOut.txt It didnt work out too well, but I will upload a more formal readme in the coming days.
<h3>Dependencies</h3>
-Tweepy (for tweet scraper)
