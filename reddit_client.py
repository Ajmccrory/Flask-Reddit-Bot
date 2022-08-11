import sys
import json
import time

import app
import praw

from prawcore.exceptions import OAuthException, Forbidden

class RedditClient:
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
            self.client_id = self.client_secret = self.username = self.password = self.user_agent = None

            with open('credentials.json') as credentials:

                data = json.load(credentials)
                self.client_id = data["client_id"]
                self.client_secret = data["client_secret"]
                self.username = data["user_name"]
                self.password = data["password"]
                try:

                    self.user = praw.Reddit (
                                            user_agent=self.user_agent,
                                            client_id=self.client_id,
                                            client_secret=self.client_secret,
                                            password=self.password,
                                            username=self.username
                        )

                    if self.user.user.me() == self.username:
                        print('---> Logged into Reddit as {0}.'.format(self.user.user.me()))
                        vote_request = vote_request()
                        return vote_request
                    else:
                        raise OAuthException
                except(OAuthException, Forbidden) as e:
                    print('---> Failed login due to {0}: invalid credentials.'.format(type(e).__name__))
                    sys.exit()

    def prompt_user(start_time):
            if int(start_time) <= 900:
                return app.actions_performed()


    def vote_request(self):       
        with open('credentials.json') as request:
            data = json.load(request)
            Number = int(data["Number"])
            redditor = data["redditor"]
            try:
                upvote_target = redditor
                Number = int(Number)
                for comment in self.prog_bar(self.user.redditor(upvote_target).comments.new(
                    limit=Number)):
                    comment.upvote()
            except:
                    print('Failed to upvote user: {0}. Check your inputs and try again.'.format(upvote_target))
    
def main():
    start_time = time.time()
    client = RedditClient()
    while client.keep_alive:
        try:
            client.vote_request()
        except ValueError:
            pass
        client.keep_alive = client.prompt_user(start_time)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
