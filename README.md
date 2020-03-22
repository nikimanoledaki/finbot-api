# Finbot API

This repo contains the API for a chatbot, Ubb, that trains an Natural Language Processing (NLP) model and teaches about personal finance. Built as a group for the final project at Makers Academy. You can access the frontend of the project here.

## Learning Journey

This was the team's first experience with Python, Django, Natural Language Processing, Tensorflow, and NLTK. It was also the team's first time 

## AI Model for Bot

The bot logic was built using [NLTK](https://www.nltk.org/), a Python library for NLP, which we used to [tokenize](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html) and [stem](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) a set of intents. We trained the bot by passing that pre-proccessed-data through a neural net using Tensorflow/[TFLearn](http://tflearn.org/).

We could then predict the correct intent based on a user input. The user input would be tokenized/stemmed (i.e. create a 'bag of words') and then the model would return the intent that most closely matched the input.

Finally, the bot returned a response related to that intent.

## The Team

[Meghan Iankov](https://github.com/meghaniankov) | [Niki Manoledaki](https://github.com/nikimanoledaki) | [Bassel Al-Sayed](https://github.com/basselalsayed) | [Shadi Khazaei](https://github.com/shadz22) | [Emily Spencer](https://github.com/emilyjspencer)

## Deployed App

Frontend: https://finbot-fe.herokuapp.com/ 
API: https://finbot--api.herokuapp.com/

## Getting Started

### 1. Install Python 3.6

### 2. Install all other dependencies

After cloning the repo, run:

```
pip install
```

## Running the program

### Start Server

```sh
$ python3 manage.py runserver
```

## Built With

* Python
* Django
* Tensorflow
* TFLearn
* NLTK (Natural Language Toolkit)
