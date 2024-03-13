import requests
from twilio.rest import Client

def get_word() -> str:
    """
    :return: a message which contains the word of the day, its definition, word type, and example.
    """

    API_KEY = 'YOUR_KEY'

    url = f'http://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        return "Error: Failed to fetch data from Wordnik API."
    
    daily_word = data["word"]
    word_def = data["definitions"][0]["text"]
    word_type = data["definitions"][0]["partOfSpeech"]
    word_example = data["examples"][0]["text"]

    final_message = f"""\
    Good Morning :)

    The word of the day is: {daily_word}.

    {daily_word} is a {word_type}, which means: {word_def}

    In a sentence:
    {word_example}
    """

    return final_message


def send_word() -> None:

    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'

    # initialise twilio client
    client = Client(account_sid, auth_token)

    # twilio and recipient phone number
    from_phone_number='+16122607874' # my twilio number
    to_phone_number='+#AREACODE#NUMBER'

    # message body
    message_body = get_word()

    # sending message
    message = client.messages.create(
        from_ = from_phone_number,
        body = message_body,
        to = to_phone_number
    )

if __name__ == "__main__":
    send_word()

# TODO: 'crontab -e' and then 0 8 * * * /usr/bin/python3 /path/to/your/script.py