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

### *Sample Report*
```
24/09/17 18:59:21	24/09/17 19:9:21
teambillionaire	264
7	60
70	59
dalifinalista	24
antioch	19
taketheknee	18
micavicicontetrendy	16
vacature	15
1	14
boycottnfl	14
```
