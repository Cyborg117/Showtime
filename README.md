# Showtime 

![image](https://user-images.githubusercontent.com/33039708/145700797-59c102fc-487a-42e7-9ebf-c8aead8028e0.png) 

A Minor Project made in Python using Tkinter for frontend which fetches Data about Movies/TV-Series from an Online Database and uses the OMDB REST API and pyImdb to show Information about movies. 

Give a Star if you liked it!! 

# Concept

## API
API is the acronym for `Application Programming Interface`, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you're using an API. It is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software.

## REST APIs
REST is an acronym for `REpresentational State Transfer` and an architectural style for distributed hypermedia systems. It is designed to take advantage of existing protocols. While REST can be used over nearly any protocol, it usually takes advantage of HTTP when used for Web APIs. This means that developers do not need to install libraries or additional software in order to take advantage of a REST API design.

## OMDb API
The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by Community.

## JSON
JSON or `JavaScript Object Notation` is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate.
JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

JSON is built on two structures:

1. A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
2. An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

These are universal data structures. Virtually all modern programming languages support them in one form or another. It makes sense that a data format that is interchangeable with programming languages also be based on these structures.

# Requirements
1. OMDb API Key - http://www.omdbapi.com/apikey.aspx
2. IMDbPY library

# How to use 
1. Write in Terminal `pip install -r requirements.txt`
2. Create your Own OMDb API Key from here - http://www.omdbapi.com/apikey.aspx 
3. Run Showtime.py and add the Key and Click Verify
4. Now a keyfile.txt File will be Created in which your API KEY is stored and used for getting Data

# Features
1. `Getdata` - It will Fetch the Data, Parse it and Show it to you on the basis of Movie Name or Movie ID (imdb)
2. `Movie Id` - It will search Movie Id using the Movie Name Provided
3. `Keyword` - It will Search the movie Using Keywords and also find Related Keywords
4. `Top 250` - It will get the Top 250 Movies from Imdb
5. `Bottom 100` - It will get the Bottom 100 Movies from Imdb

# Screenshots

![image](https://user-images.githubusercontent.com/33039708/145715934-da31c6d6-3a8b-4771-99c9-c6d06b4fc36d.png) ![image](https://user-images.githubusercontent.com/33039708/145715996-cc964267-1c09-44a5-9b9e-a389acf45cd9.png)

![image](https://user-images.githubusercontent.com/33039708/145716058-6487b043-3e8e-4ed4-a4ea-c73070e8343f.png)

![image](https://user-images.githubusercontent.com/33039708/145715163-a5919dbb-2036-4ecb-a25f-2b0880387e6c.png)

# V3
1. Fetching Data about Celebrities and Production Houses (soon)
2. Add Code to Get API KEY from the GUI itself using requests (soon)
3. Adding Threads to fetch data Simultaneously (soon)
4. Fix Beaking GUI (soon)
5. Add history and the Option to Star Movies (soon)

# Request a Feature
If you want me to add a Particular Feature in the Source then

1. Goto Issues and Create a New Issue
2. There Select a Feature Request Template and Click Get Started
3. Write Accordingly
4. OR Contact me at hrithikraj137@gmail.com
