#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import webbrowser
import subprocess
import smtplib
from twilio.rest import Client
import pyttsx3
import wikipedia
import tweepy
import webbrowser
import json
from datetime import datetime


# In[5]:



# Function to clear the terminal screen
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Function to send an email
def send_email():
    # Your email configuration
    # Set up your email, password, and SMTP server
    email_address = "your_email@gmail.com"
    password = "your_password"
    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(email_address, password)

        to_address = input("Enter the recipient's email address: ")
        subject = input("Enter the email subject: ")
        message = input("Enter the email message: ")

        email_content = f"Subject: {subject}\n\n{message}"
        server.sendmail(email_address, to_address, email_content)
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()

# Function to send an SMS using Twilio
def send_sms():
    # Your Twilio account SID, authentication token, and Twilio phone number
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    twilio_phone_number = "your_twilio_phone_number"

    try:
        client = Client(account_sid, auth_token)

        to_phone_number = input("Enter the recipient's phone number: ")
        message = input("Enter the SMS message: ")

        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=to_phone_number
        )

        print(f"SMS sent successfully! SID: {message.sid}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to get current trends on Twitter
def get_twitter_trends():
    # Set up your Twitter API credentials
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        trends = api.trends_place(id=1)  # Worldwide trends
        print("Current Twitter Trends:")
        for trend in trends[0]['trends']:
            print(f"- {trend['name']}")

    except tweepy.TweepError as e:
        print(f"An error occurred: {str(e)}")

# Function to get top posts for a hashtag on Twitter
def get_top_posts_for_hashtag():
    # Set up your Twitter API credentials
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    hashtag = input("Enter the hashtag: ")

    try:
        tweets = api.search(q=hashtag, count=10, result_type="popular")

        print(f"Top 10 posts for #{hashtag}:")
        for i, tweet in enumerate(tweets):
            print(f"{i + 1}. {tweet.text}")

    except tweepy.TweepError as e:
        print(f"An error occurred: {str(e)}")

# Function to get data from a Wikipedia page
def get_wikipedia_data():
    topic = input("Enter the topic: ")
    try:
        result = wikipedia.summary(topic, sentences=3)
        print(f"Wikipedia summary for {topic}:\n{result}")

    except wikipedia.WikipediaException as e:
        print(f"An error occurred: {str(e)}")

# Function to open a web page
def open_webpage():
    url = input("Enter the URL: ")
    webbrowser.open(url)

# Function to control the speaker volume
def control_speaker_volume():
    volume = int(input("Enter the volume level (0 to 100): "))
    # Your code to control speaker volume goes here


# In[ ]:


# Main program loop
while True:
    clear_screen()

    print("Menu:")
    print("1. Notepad")
    print("2. Chrome")
    print("3. WhatsApp")
    print("4. Email")
    print("5. SMS")
    print("6. Twitter Trends")
    print("7. Top Posts for Hashtag")
    print("8. Wikipedia Data")
    print("9. Open Webpage")
    print("10. Control Speaker Volume")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subprocess.run(["notepad.exe"])
    elif choice == "2":
        subprocess.run(["chrome.exe"])
    elif choice == "3":
        # Add your code to open WhatsApp
        pass
    elif choice == "4":
        send_email()
    elif choice == "5":
        send_sms()
    elif choice == "6":
        get_twitter_trends()
    elif choice == "7":
        get_top_posts_for_hashtag()
    elif choice == "8":
        get_wikipedia_data()
    elif choice == "9":
        open_webpage()
    elif choice == "10":
        control_speaker_volume()
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    input("Press Enter to continue...")


# In[ ]:




