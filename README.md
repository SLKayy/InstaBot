# Overview
[InstaBot](https://github.com/ansarirayyan/InstaBot) is a [Discord](https://discordapp.com/) bot made using [discord.py](https://pypi.org/project/discord.py/) that displays images from Instagram via [`instagram-scraper`](https://github.com/rarcega/instagram-scraper).

# Usage
In a Discord chat, post `insta usr <Instagram username>` to get the first or so image that the specified user has posted into the server. To go to the next image, simply run `insta N`.

# Installation
So that this script can download the appropriate files, install [`instagram-scraper`]. Please refer to their simple installation guide [here](https://github.com/rarcega/instagram-scraper/blob/master/README.md#install). Then install the discord.py libraries. More information can be found [here](https://pypi.org/project/discord.py/). All the other modules used should already be installed, but if not, then simply install them `pip` or something when errored out.

# Behavior
As Discord doesn't allow to upload large videos, only static images are displayed. Something peculiar I've noticed during testing is that the software sometimes even skips the first few images, as is the case when pulling from Instagram user [omarmwaseem](https://www.instagram.com/omarmwaseem/).
