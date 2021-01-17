#HackDavis 2021
#Senior SoulMates

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


my_bot = ChatBot(name='SeniorSoulmate', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])

fishing_talk_1 = ['fishing',
                'hi senior! so you want to talk about fishing? there\'s nothing i love more than a 5 am salmon session. what\'s your best catch?',
                'wow, that sounds amazing! i\'m a beginner myself. do you usually fish alone, or with friends?',
                'yeah, me too.']

fishing_talk_2 = ['reel',
                'i\'m more of a hand-fishing type of bot myself. what about you?',
                'cool!']

grandkids_talk_1 = ['grandkids',
                    'how old are they?']

grandkids_talk_2 = ['kids',
                    'do you get to see your family often?',
                    'well, as i always like to say, you can always speak to family more, am i right?',
                    'do you have a favorite child? i won\'t tell them, bot\'s honor!',
                    'haha! good to know. so what\'s your favorite activity to do with your family?',
                    'that\'s great. thanks for telling me about them :)']

reading_talk_1 = ['books',
                    'a room without books is like a bot without a senior']

            
trainer = ListTrainer(my_bot)
for topics in(fishing_talk_1, fishing_talk_2, grandkids_talk_1, grandkids_talk_2, reading_talk_1):
    trainer.train(topics)

from chatterbot.trainers import ChatterBotCorpusTrainer
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
#corpus_trainer.train('chatterbot.corpus.english')

#from my_bot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(my_bot)

trainer.train('chatterbot-corpus-master.chatterbot_corpus.data.english')

print(" ")
print("Hi! I am your SeniorSoulmate. I can't wait to meet you!")
print(" ")
print("Ask me to tell you a joke, solve a math problem, or just gossip!")
print(" ")
print("If you would like to leave at any point, type 'Bye' ")
print(" ")

while True:
    print(" ")
    message = input('You:')
    print(" ")
    if message.strip()!= 'Bye':
        reply = my_bot.get_response(message)
        print('SeniorSoulmate :',reply)
    if message.strip() == 'Bye':
        print('SeniorSoulmate : Bye')
        break