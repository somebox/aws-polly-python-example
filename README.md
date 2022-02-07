# Generting lots of MP3s from Text with AWS Polly and Python

Part of a more complicated Art Project \
A simple example, with Python 3, boto3 AWS Polly \
Jeremy Seitz \
Luzern, Switzerland, Feb 2022


## Challenge

An artist friend had an gallery exhibit planned, themed around conversations with AI - specifically the GPT-3 chat bot. He managed to get an account set up with OpenAI, and was soon exchanging with GPT-3, asking questions about his art, his show, and intelligence in general. The AI even wrote his opening speech for him. 

The main gallery space where his paintings hung was quite vast. He asked me to record an audio experience of this human-AI conversation for his show, using a synthesized computer voice and a recording of his own. So I planned to set up several speakers, with the voices and some ambient sound. I needed to turn 25 paragraphs into audio files, and the quality had to be impressive.

## Solution

After some research I decided to use Amazon Polly to generate the answers to his questions. This repo contains a simple Python script which uses the service to generate MP3 files of each paragraph from the source text file. 

## Installation

To set your own AWS credentials, use `aws configure` via the command-line, or [read more about it here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

`pip3 install boto3`

`python3 run.py`

## Results

A fully-rendered conversation, post-processed as if it were in the gallery space: [mp3, 11:06](mp3/art1-questions-answers.mp3)

- Artist (questions): Edward Wright
- AI GPT-3: AWS Polly (English/Britan, Brian/Male, neural model)
- Shure SM7, Logic Audio X


