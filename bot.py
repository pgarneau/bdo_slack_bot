import os
import time

import autoit
import pyscreenshot
import slackclient

import game_input
import window
import worker

SLACK_TOKEN = 'xoxb-242539638209-FEc64GplHlZrKJp9kTyZVph6'
BOT_NAME = 'bdo_bot'
BOT_USER = 'U74FVJS65'
IMAGE_FILE_NAME = 'bdo_ss.png'

slack_client = slackclient.SlackClient(SLACK_TOKEN)

def is_for_me(event):
    type = event.get('type')

    if type and type == 'message' and not (event.get('user') == BOT_USER):
        if '<@{user}>'.format(user=BOT_USER) in event.get('text').strip().split():
            return True

def upload_image(channel):
    pyscreenshot.grab_to_file(IMAGE_FILE_NAME)
    slack_client.api_call('files.upload', filename=IMAGE_FILE_NAME, channels=channel,
                          file=open(IMAGE_FILE_NAME, 'rb'))

def post_message(message, channel):
    slack_client.api_call('chat.postMessage', channel=channel, text=message,
                          as_user=True)

def handle_message(message, user, channel):
    words = [word.lower() for word in message.strip().split()]
    if len(words) >= 2:
        if words[1] == "status":
            upload_image(channel)

        elif words[1] == "process":
            print('processing...')

        elif words[1] == "store":
            print('storing...')
            game_input.get_pos()

        elif words[1] == "workers":
            worker.reset_workers()

        else:
            title = window.focus_bdo()
            autoit.control_send(title, "", words[1])
#            print('testing...')
#            post_message(message='Hello!', channel=channel)

def run():
    if slack_client.rtm_connect():
        print('[.] Bot is on')
        # Focus BDO
        window.focus_bdo()
        while True:
            event_list = slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    if is_for_me(event):
                        handle_message(message=event.get('text'),
                                       user=event.get('user'),
                                       channel=event.get('channel'))
                        time.sleep(1)
                    else:
                        print('')

if __name__=='__main__':
    run()

