# How to Use
The majority of people are likely here because they want to easily access the Scratch API!

## Commands
/<user>/pfp (returns the profile picture of a user)
/<user>/favorite (returns the most recent project a user favorited)
/<project>/thumbnail (returns the thumbnail of a project)

## How to Access

It's quite simple, really.

For python users:
```
import requests
requests.get("api.scratchstatus.org/rgantzos/pfp/")
```

It works in node.js too, I just don't know much about node.js yet xD

# How it Works
The server that we use to display short pieces of the Scratch API is built on python. You can view the main.py file in this repository, it has all the code there. We would like credit if you do choose to use it, though.
