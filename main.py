import requests
import json
import time
from datetime import datetime
from pushbullet import Pushbullet

# Set up Pushbullet API
api_key = 'o.FUzJu4AoGKuYoaCNq8LQ2X1EbcoXcsC'
pb = Pushbullet(api_key)

# Set up Merriam-Webster API
dictionary_key = '71fa8603-0f6c-4ac2-b598-6cb9e56a69b'
dictionary_url = 'https://www.dictionaryapi.com/api/v3/references/learners/json/white?key=' + dictionary_key


def get_new_word_and_meaning():
    # Get a new word and its meaning from the Merriam-Webster API
    response = requests.get(dictionary_url)
    print(response.json())
    data = response.json()

    # Parse the data to extract the word and its meaning
    new_word = data[0]['hwi']['hw']
    meaning = data[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]

    return new_word, meaning

#new_word, meaning = get_new_word_and_meaning()
#print(new_word, meaning)


def send_push_notification(title, message):
    # Send a Pushbullet notification with the specified title and message
     print(f'Sending Pushbullet notification: {title} - {message}')
     push = pb.push_note(title, message)

# Schedule the script to run at 8:00 AM every day
while True:
    now = datetime.now()
    if now.hour == 8 and now.minute == 0:
        # Get a new word and its meaning
        new_word, meaning = get_new_word_and_meaning()

        # Send a Pushbullet notification with the new word and its meaning
        title = 'New Word Alert!'
        message = f'The meaning of "{new_word}" is: {meaning}'
        send_push_notification(title, message)

    # Wait for 1 minute before checking the time again
    time.sleep(60)


    # Wait for 1 minute before checking the time again
    
