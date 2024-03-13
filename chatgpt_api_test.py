import ipywidgets as widgets
from IPython.display import display
from textblob import TextBlob
import openai

from google.colab import userdata

api_key = userdata.get('API_KEY')

# Ключ API для OpenAI
openai.api_key = api_key


def on_button_clicked(b):
    text = text_input.value
    sentiment = determine_sentiment(text)
    style = 'batman' if sentiment == 'positive' else 'joker'
    response = generate_response(style, text)
    output.clear_output()
    with output:
        print(f"Ответ ({style}): {response}")


def determine_sentiment(text):
    blob = TextBlob(text)
    return 'positive' if blob.sentiment.polarity > 0 else 'negative'


def generate_response(style, text):
    prompt = f"{style}: {text}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


text_input = widgets.Textarea(
    value='',
    placeholder='Введите ваш текст здесь',
    description='Текст:',
    disabled=False
)

button = widgets.Button(description="Отправить")
output = widgets.Output()

button.on_click(on_button_clicked)

display(text_input, button, output)
