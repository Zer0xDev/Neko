
<img src="NekoLogo.png" width="150" height="150">

# Neko
Python Library for Easy Work with AI

# What is this?

This library was created to simplify working with AI

# Setup

1. Open the openrouter.ai website
2. Register or log in to your account
3. Select any model and copy its name
4. Click on 'Create API Key', then enter a name and copy the API key

# Installation

Download the neko folder and place it in your project directory

# Example

```bash
from neko import neko

answer = neko.chat.create(
    key="YOUR_API_KEY",
    model="model_name",
    prompt="Hello! How are you?"
)

print(answer)
```
