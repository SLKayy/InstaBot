# Overview
[InstaBot](https://github.com/ansarirayyan/InstaBot) is a [Discord](https://discordapp.com/) bot made using [discord.py](https://pypi.org/project/discord.py/) that displays images from Instagram via [`instagram-scraper`](https://github.com/rarcega/instagram-scraper).

# Usage
Here lies a list of commands that can be used to operate the bot:


# Installation
So that this script can download the appropriate files, install [`instagram-scraper`]. Please refer to their simple installation guide [here](https://github.com/rarcega/instagram-scraper/blob/master/README.md#install). Then install the discord.py libraries. More information can be found [here](https://pypi.org/project/discord.py/). All the other modules used should already be installed, but if not, then simply install them via `pip` (or `git`, or another alternative method of installation) when errored out. This program is written for Python 3.

# Running
UNIX or UNIX-liked:
```
python3 main.py
```

On Windows:
```
py main.py
```

# Behavior
As Discord doesn't allow to upload large videos, only static images are displayed. Something peculiar I've noticed during testing is that the software sometimes even skips the first few images, as is the case when pulling from Instagram user [omarmwaseem](https://www.instagram.com/omarmwaseem/). Also, as of the time of the writing of this document, `instagram-scraper` does not allow the use of non-UTF-8 in searches, but there is an [open issue](https://github.com/rarcega/instagram-scraper/issues/83) (though outstanding for a couple of years) on its GitHub repository.
