# Email Display

A simple web-app to search the emails stored in a database using sender id,
recipient id or between specified to/from dates.

### Tools
- Python 3
- Django 1.9.5

### Setup
> Initialize database
```
./manage.py migrate
```
> Load the data stored in ids.json and emails.json using custom command
```
./manage.py loadjson
```

### Todos
* Front-end work
* Use form class to create search forms

The first file, ids.json, maps string identifiers of people to their name (note that name can sometimes be an email address, but that this is irrelevant for this assignment, and all names regardless of appearance can be considered as names).

The second file, emails.json, is a JSON array containing data for every email in the data set. Each email object has the following fields:
- subject: a string, subject of the email.
- content: a string, the full-text content of the email.
- timeSent: an integer which represents a time value, the canonical date/time representation in javascript (e.g. see http://www.2ality.com/2014/02/time-values.html)
- senderId: a string ID of the sender, who will have an entry in ids.json.
- recipientIds: an array with IDs of the email recipients, who will each have entries in ids.json.

With this data, the task is to:
1. Create an SQL database which stores all email data. Any variant of SQL is fine, but non-relational databases like MongoDB are disallowed.
2. Create a web application which interfaces with your SQL database and allows users to search for emails matching certain criteria (see "Email Search Requirements" below), and to display a particular email (see "Email Display Requirements" below)

Email Search Requirements:
1. Users should be able to search for a list of emails by the name of the sender.
2. Users should be able to search for a list of emails by the name of the recipient.
3. Users should be able to search for a list of emails which were sent within a particular date range.

Email Display Requirements:
After selecting an email from a list of searched emails, a user should be able to:
1. See the name of the sender.
2. See the names of the recipients.
3. See the time the email was sent.
4. See the subject of the email.
5. See the full content of the email.
