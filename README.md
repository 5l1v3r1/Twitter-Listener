# twitter_listener
Finds the most popular hashtags on twitter by listening to the Twitter live stream API for 10 min.

## How to use:
Enter the twitter_listener directory. Edit *config.py* to match your Twitter API credentials.

Enter:
```
source bin/activate
```
to create the virtualenv.

To generate a new report of top 10 hashtags, run:
```
python top_hashtags.py
```
The program will run for 10min and produce a report in *report.txt*.
