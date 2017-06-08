# Medium Scraper

#### Description
This code contains a scrapper that given tags stores the top articles related.

#### Language
Python 3

#### Requirements
1. Install python dependencies with `pip install -r requirements.txt`.
2. Install PhantomJS with `npm -g install phantomjs-prebuilt`.
3. Install Mongo.

#### How to run
1. Run mongo `sudo mongod`
2. Create a `.env` file. You can use `.env.example`
2. Set a list of initial tags `seeds = ['python', 'machine learning']`.
3. Create an instance of `Spider` with your initial seeds `Spider(seeds)`.
