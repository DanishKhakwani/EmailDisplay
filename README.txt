Make a web application which displays emails, and allows users to search for and display emails matching a variety of criteria.

Linked below are two Json files:
https://drive.google.com/open?id=0BycUrk3kLhXIQ1hJOVZrMW5ERDA
https://drive.google.com/open?id=0BycUrk3kLhXIaTNDZWp1YTJnMGs

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


Take inspiration from the look and feel of products like google mail or outlook. Alternatively, ebyou may design something entirely different (as long as it meets the requirements, is easy to use, and is well designed).

As mentioned in the previous email, provide following  two outputs:

1. All source code you used in the project, which you should email as a zip file to us.
2. A publicly accessible URL which hosts your web app. You should email us a link to this.
