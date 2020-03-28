# Finbot API

This repo contains the API for a chatbot, Ubb, that trains an Natural Language Processing (NLP) model and teaches about personal finance. Built as a group for the final project at Makers Academy. You can access the frontend of the project here.

## Learning Journey

This was the team's first experience with Python, Django, Natural Language Processing, Tensorflow, and NLTK. It was also the team's first time 

## AI Model for Bot

The bot logic was built using [NLTK](https://www.nltk.org/), a Python library for NLP, which we used to [tokenize](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html) and [stem](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) a set of intents. We trained the bot by passing that pre-proccessed-data through a neural net using Tensorflow/[TFLearn](http://tflearn.org/).

The bot can predict the correct intent based on a user input. The user input is then tokenized/stemmed (i.e. create a 'bag of words') and then the model returns a response for the intent that most closely matches the user input.

Finally, the bot returns a response related to that intent.

Once this context is set, the bot also asks the user if they would like more information. If the user says yes, the bot responds with a few reading resources. These resources are curated links from trustworthy sources. 

If the bot does not understand or if the user is unsure about what to ask, the bot prompts the user with a list of topics that the user can ask about.

## The Team

[Meghan Iankov](https://github.com/meghaniankov) | [Niki Manoledaki](https://github.com/nikimanoledaki) | [Bassel Al-Sayed](https://github.com/basselalsayed) | [Shadi Khazaei](https://github.com/shadz22) | [Emily Spencer](https://github.com/emilyjspencer)

## Deployed App

Frontend: https://finbot-fe.herokuapp.com/ 
API: https://finbot--api.herokuapp.com/

## Getting Started

### 1. Install the software needed to run the program

- Install a version of Python 3 - we recommend Python 3.6, but the program can run witha any version of Python 3. Many of us have Python 3.7.6 installed on our local machines.
- Install TensorFlow 1.13.1
- Install Django
- Install NLTK

### 2. Install all other dependencies

After cloning the repo, run:

```
$ pip3 install
```

## Running the program

### Start Server

```
$ python3 manage.py runserver
```

## Built With

* Python
* Django
* Tensorflow
* TFLearn
* NLTK (Natural Language Toolkit)
