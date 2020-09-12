# tweet-apex

## Installation
### Clone
Clone this repo to your local machine using :
```bash
git clone https://github.com/RadhiansyaZ/tweet-apex.git
```
### Install the dependencies
```bash
cd tweet-apex
pip install -r requirements.txt
```
### Run
```bash
python main.py
```

## Usage
### Deleting Tweets by Year
1. Download your data from 
> https://twitter.com/settings/your_twitter_data/data
2. Apply for a Twitter Developer Account
> https://developer.twitter.com
3. Create an Application.
4. Generate Authentication Credentials.
5. Store keys and tokens in somewhere safe.
6. Navigate to /data/ in your twitter data and copy tweet.js to tweet-apex directory.
7. Delete this part and save it as .json format. 
```python
window.YTD.tweet.part0 = 
```
8. Run the python file.