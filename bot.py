from gzip import READ
import os, sys
import json
import logging
import random
from pathlib import Path
from time import sleep

import praw
from prawcore.exceptions import OAuthException, Forbidden

import app
from store import dump_pickled, read_pickled_set

submission_reply_list = ["Nice", "up up", "nice job", "friend!", "user", "I like the creativity!", "Very Nice"]

logging.basicConfig(handlers=[logging.StreamHandler()],
                    level=logging.INFO,
                    format='%(asctime)s %(threadName)-12s %(levelname).4s %(message)s',
                    datefmt='%a %d %H:%M:%S')

current_dir = Path(os.path.dirname(os.path.abspath(__file__)))

class RedditClient:

    def __init__(self):
            self.user_agent = 'Autovote2 by /u/ajmccrory1'
            self.count = 0
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
                    self.passed_submissions = read_pickled_set(f"submissions={self.username}.pickle")

                    if reddit.user.me() == self.username:
                        print('---> Logged into Reddit as {0}.'.format(reddit.user.me()))
                    else:
                        raise OAuthException
                except(OAuthException, Forbidden) as e:
                    print('---> Failed login due to {0}: invalid credentials.'.format(type(e).__name__))
                    sys.exit()


    def work_on_subreddit(self, sub_reddit: str, **generator_kwargs):
        if 'limit' not in generator_kwargs:
            with open('credentials.json') as request:
                data = json.load(request)
                Number = data['Number']
                generator_kwargs['limit'] = Number
        try:
            submissions = list(self.reddit.subreddit(sub_reddit).new(**generator_kwargs))
            for submission in submissions:
                self._process_submission(submission)

        except Exception as ex:
            error_message = str(ex)
            self._retry_rate_limited_failure(error_message, self.work_on_subreddit, sub_reddit, **generator_kwargs)

        finally:
            dump_pickled(self.passed_submissions, f"submissions--{self.username}.pickle")

    
    def _process_submission(self, submission):
        submission_id = submission.id
        if submission_id not in self.passed_submissions:
            comments = submission.comments.list()
            if len(comments) < 12:
                submission_reply = random.choice(submission_reply_list)
                submission.upvote()
                submission.reply(submission_reply)
                logging.info(f"Processed '{submission.title}'")

    def _retry_rate_limited_failure(self, error_msg, func, *args, **kwargs):
      error_msg = error_msg.lower()
      search_term = "try again in "
      if search_term in error_msg:
          minute_idx = error_msg.index(search_term) + len(search_term)
          if error_msg[minute_idx].isdigit():
              digits = [error_msg[minute_idx]]
              if error_msg[minute_idx + 1].isdigit():
                  digits.append(error_msg[minute_idx + 1])
              wait_time_in_min = int(''.join(digits))
              logging.info(f"{self.username} will attempt a second run after waiting for {wait_time_in_min} minutes")
              wait_time_sec = wait_time_in_min * 60
              sleep(random.randint(wait_time_sec + 10))
              func(*args, **kwargs)


def main():
    client = RedditClient()
    with open('credentials.json') as creds:
        data = json.load(creds)
        sub_reddit = data['subreddit_name']
    try:
        client.work_on_subreddit(sub_reddit)
    except ValueError:
        pass
    finally:
        return app.actions_performed()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
