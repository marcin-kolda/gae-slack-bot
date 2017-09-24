[![Build Status](https://travis-ci.org/marcin-kolda/gae-slack-bot.svg?branch=master)](https://travis-ci.org/marcin-kolda/gae-slack-bot)
[![Coverage Status](https://coveralls.io/repos/github/marcin-kolda/gae-slack-bot/badge.svg?branch=master)](https://coveralls.io/github/marcin-kolda/gae-slack-bot?branch=master)
# gae-slack-bot
[Google App Engine](https://cloud.google.com/appengine/) Python [Slack bot](https://api.slack.com/bot-users) example based on [Slack Events API](https://api.slack.com/events-api).

# How it works?

![Architecture diagram](diagram.jpg)

This bot uses [Slack Events API](https://api.slack.com/events-api) to subscribe to selected events and reply via [Slack Web API](https://api.slack.com/web).

# Features

This a proof of concept Slack bot example, which:
* repeats every message in direct conversation or channels to which bot is invited,
* verifies all incoming messages with [Slack verification token](https://api.slack.com/events-api#subscriptions), 
* can run for free within [GCP Free Tier](https://cloud.google.com/free/) if there is a small traffic,
* can automatically scale for larger traffic (requires enabling billing).
