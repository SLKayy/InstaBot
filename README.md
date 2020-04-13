# Overview
[InstaBot](https://github.com/ansarirayyan/InstaBot) is a [Discord](https://discordapp.com/) bot made using [discord.py](https://pypi.org/project/discord.py/) that displays images from Instagram via [`instagram-scraper`](https://github.com/rarcega/instagram-scraper).

# Usage
Here lies a list of commands that can be used to operate the bot:

| Command | Description |
| :----------------: |:----------------:|
| `insta usr <username>` | Searches for the pics of specified username |
| `insta tag <tag name> <max number>` | Searches for a certain amount of pics pertaining to a particular tag |
| `insta N` | Goes on to next image of your latest search |
| `insta reload_usr <username>` | Fetches all the images again of a particular username for an up-to-date local copy |
| `insta reload_tag <tag name> <max number>` | Fetches a certain number of all the images again of a particular tag name for an up-to-date local copy |
| `insta ls` | Lists all the usernames of which you have data already downloaded |

If no `<max number>` paramater is specified, it will default to downloading posts. If a user desires so, he or she can pass a different parameter in a later fetch than they did during the initial one.

# Installation
So that this script can download the appropriate files, install [`instagram-scraper`]. Please refer to their simple installation guide [here](https://github.com/rarcega/instagram-scraper/blob/master/README.md#install). Then install the discord.py libraries. More information can be found [here](https://pypi.org/project/discord.py/). All the other modules used should already be installed, but if not, then simply install them via `pip` (or `git`, or another alternative method of installation) when errored out.

# Running
This program is written in Python 3.

UNIX or UNIX-liked:
```
python3 main.py
```

On Windows:
```
py main.py
```

# Behavior and Limitations

* As Discord doesn't allow to upload large videos, only static images are displayed. Something peculiar I've noticed during testing is that the software sometimes even skips the first few images, as is the case when pulling from Instagram user [omarmwaseem](https://www.instagram.com/omarmwaseem/) on occasion.
* As of the time of the writing of this document, `instagram-scraper` does not allow the use of non-UTF-8 in searches, but there is an [open issue](https://github.com/rarcega/instagram-scraper/issues/83) (though outstanding for a couple of years) on its GitHub repository.
* The first time you pull info from a tag or user, it might take a while, as it's first downloading the files. But afterwards, it will generally be a lot faster to upload for viewing purposes, right in Discord.
