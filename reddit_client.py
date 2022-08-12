import sys
import os
import json
import time

import app
import praw

from prawcore.exceptions import OAuthException, Forbidden

sub_id = ""

class RedditClient:
    start = time.time()
    user = None
    keep_alive = True
    prog_bar = time.time()
    valid = {
        "yes": True,
        "y": True,
        "Y": True,
        "ye": True,
        }

    def __init__(self):
            '''This is the constructor of the RedditClient instance.
             When supplied with correct set of credentials, it will initialize an
            instance of the Reddit object using PRAW.
             Created instance is then assigned to the user variable for later use.
                Returns:
            None
                 Raises:
            OAuthException:     If authentication fails using OAuth2.
            Forbidden:          If username is None.
            KeyError:           If dictionary keys are not found.

        '''
            self.user_agent = 'Autovote2 by /u/ajmccrory1'
            self.client_id = self.client_secret = self.username = self.password = None

            with open('credentials.json') as credentials:

                data = json.load(credentials)
                self.client_id = data["client_id"]
                self.client_secret = data["client_secret"]
                self.username = data["user_name"]
                self.password = data["password"]
                try:

                    reddit = praw.Reddit (
                                            client_id=self.client_id,
                                            client_secret=self.client_secret,
                                            password=self.password,
                                            user_agent=self.user_agent,
                                            username=self.username,
                        )
       

                    if reddit.user.me() == self.username:
                        print('---> Logged into Reddit as {0}.'.format(reddit.user.me()))
                    else:
                        raise OAuthException
                except(OAuthException, Forbidden) as e:
                    print('---> Failed login due to {0}: invalid credentials.'.format(type(e).__name__))
                    sys.exit()

    def prompt_user(self, user_input):
            return user_input in self.valid


    def vote_request(self):       
        with open('credentials.json') as request:
            data = json.load(request)
            comment_id = data['comment_id']
            try:
                comment_id = comment_id
                comment = self.comment(comment_id)
                comment.upvote()
            except:
                print('Failed to upvote user: {0}. Check your inputs and try again.'.format(comment_id))
    
def main():
    client = RedditClient()
    while client.keep_alive:
        try:
            client.vote_request()
        except ValueError:
            pass
        client.keep_alive = client.prompt_user(input(
            'would you like to perform another actions[y/n]\n?'
        ))
    print('Goodbye!')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        app.actions_performed()
