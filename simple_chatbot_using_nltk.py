# install nltk

from nltk.chat.util import Chat , reflections

pairs = [
    [
        r'my name is (.*)',
        ['Hello %1 , It was nice meeting you ?'],
    ],
    [
        r'what is your name', 
        ['My name is epic and i am an chatbot'],
    ],
    [
        r'how are you ',
        ['I am fine \n What you doing ?'],
    ],
    [
        r'i am (.*)',
        ['Cool i love doing %1'],
    ],
    [
        r'(.*) age?',
        ['MAN i am an chatbot and you are asking me that question . '],
    ],
    [
        r'quit',
        ['It was nice talking to you , see you later , BBYE!'] ,
    ],
]

def epicbot():
    print('Hello i am epic and i am an chatbot . \nenter quit to exit the chat bot')
    chat = Chat(pairs , reflections)
    chat.converse()

if __name__ == '__main__':
    epicbot()