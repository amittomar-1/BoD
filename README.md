## BoD: Sales and Data analysis made easy through voice

BoD is a voice-based Business Intelligence chatbot. It responds to user questions about data in a database, It converts the questions into backend database queries, and transforms the results into natural language responses.

## Features of BoD:
1. It keeps a track of the context of your questions.
2. BoD can respond to users' questions by converting them into queries for the backend database.
3. BoD can help you in your company's sales.
4. It is cost effective.

## Project Architechture 
Amazon S3[Stores database]
Amazon Athena [Runs queries on the database stored in S3]
AWS Lambda[Coinverts the questions into queries and then converts the result into NLP]
Amazon Lex [Provides Chatbot and voice]

![BoD Sales   Data Analysis Made Easy](https://user-images.githubusercontent.com/49426082/120067104-7a564180-c097-11eb-9d77-9446beddfd5b.png)

