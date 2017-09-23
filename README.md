[![Build Status](https://travis-ci.org/marcin-kolda/gae-slack-bot.svg?branch=master)](https://travis-ci.org/marcin-kolda/gae-slack-bot)
[![Coverage Status](https://coveralls.io/repos/github/marcin-kolda/gae-slack-bot/badge.svg?branch=master)](https://coveralls.io/github/marcin-kolda/gae-slack-bot?branch=master)
# gae-slack-bot
Google App Engine Slack bot using Event API

# Configuration

App required GCP billing enabled to use [Python Sockets API](https://cloud.google.com/appengine/docs/standard/python/sockets/),
as traffic from sockets is billed as [outgoing bandwidth](https://cloud.google.com/appengine/docs/pricing#Billable_Resource_Unit_Costs).
Sockets API is required for [python-slackclient](https://github.com/slackapi/python-slackclient).