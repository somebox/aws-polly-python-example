# Reads paragraphs from a text file, and requests an MP3 rendering using AWS Amazon Polly, as separate files.
# The numbering is automatic.
# AWS credentials should be stored in ~/.aws using the standard way for boto3.

import boto3

polly_client = boto3.Session(
                region_name='eu-central-1').client('polly')

f = open('doc/answers.txt', 'r')
data = f.read()
questions = data.split("\n")

for i, question in enumerate(questions):
    print(i, question[0:40])
    response = polly_client.synthesize_speech(VoiceId='Brian',
               OutputFormat='mp3', 
               Text = question,
               Engine = 'neural')
    mp3 = open("answer"+str(i)+".mp3", 'wb')
    mp3.write(response['AudioStream'].read())
    mp3.close()
    print(" chars: "+response['RequestCharacters'])
