# impressJokeBot
This is a basic chabot application where the user has option to choose the category from which he/she wishes to read the joke from.
the bot can be found in telegram with username as :**@ImpressJokeBot**

### Added features :
- 3 jokes category (currently with sample jokes for each category).
- implemented Jokes category as separate button.
- Number of calls to each of the button is recorded in database.
- Number of button click by each user is also recorded.

##### Database used : 
Heroku Postgres

##### Queries to access database from terminal:
```
psql --host=ec2-44-195-247-84.compute-1.amazonaws.com --port=5432 --username=xvoubscwvklvcz --password --dbname=d139gatk9hl0m0
```
password is : 7ce04d575f56974e709cc249b91bd0cc96036e7b83237fc373803faeda1ec5e2

- To access the table storing the clicks count :
```
select * from clicks;
```
- To access the table storing button click by each user:
```
select * from user_details;
```

