# webpy

Send webhooks easily across discord, e.t.c with webpy!

Currently tested on:
- Discord Webhook (https://discordapp.com/developers)


# Installation

Install the package:
`pip install webpy`

and thats it!



# Usage

as webpy is still in `beta` more features will be added but this is one example:

```python

from webpy import Webhook

webhook = Webhook("your url goes here")
webhook.sendmsg("this message is sent from `webpy`")
```


Done! and when you run it you should see an output:

**Discord**:

![discord output]("discord.png")



**Others**:

```json

{
    "content": "Hello World!"
}


```



