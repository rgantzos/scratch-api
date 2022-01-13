# How to Use
The majority of people are likely here because they want to easily access the Scratch API!

## Commands
```
/<user>/pfp/ (returns the profile picture of a user)
/<user>/favorite/ (returns the most recent project a user favorited)
/<project>/thumbnail/ (returns the thumbnail of a project)
/<user>/follower-count/ (returns the follower count of a user)
/<user>/project/ (returns the project ID of a user's most recent project)
/<user>/scratchteam/ (returns whether or not a user is on the Scratch Team)
/<user>/id/ (returns the ID of a user)
/<user>/join-date/ (returns the join date of a user)
/<project>/views/ (returns the view count of a project)
/<project>/loves/ (returns the love count of a project)
/<project>/favorites/ (returns the favorites count of a project)
/<project>/remixes/ (returns the remix count of a project)
/<project>/studio/followers/ (returns the follower count of a studio)
/<project>/studio/host-id/ (returns the host ID of a studio)
/<project>/studio/managers/ (returns the manager count of a studio)
/<project>/studio/comments/ (returns the comment count of a studio)
/<project>/title/ (returns the title of a project)
/<project>/remix-check/ (returns whether or not a project is a remix)
/<project>/modified/ (returns when a project was last modified)
/<project>/shared/ (returns when a project was last shared)
/<project>/created/ (returns when a project was created)
```

## How to Access

It's quite simple, really.

For python users:
```
import requests
requests.get("api.scratchstatus.org/rgantzos/pfp/").text
```

It works in node.js too, I just don't know much about node.js yet xD

# How it Works
The server that we use to display short pieces of the Scratch API is built on python. You can view the main.py file in this repository, it has all the code there. We would like credit if you do choose to use it, though.

# More
For more documentation, you can always go to the [Official YouTube Channel](https://www.youtube.com/channel/UC-kD7mi3Dpht3lW0bVytkMw/)!
