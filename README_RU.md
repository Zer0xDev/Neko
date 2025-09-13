
<img src="NekoLogo.png" width="150" height="150">

# Neko
Библиотека на Python для упрощения работы с нейросетями

# Что это?

Эта библиотека создана для упрощения работы с нейросетями

# Настройка

1. Откройте сайт openrouter.ai
2. Создайте или войдите в аккаунт
3. Выберите любую модель и скопируйте её название
4. Нажмите на кнопку 'Create API Key', затем скопируйте API ключ и сохраните его

# Installation

Скачайте папку neko и поместите в директорию с вашим проектом

# Пример работы

```bash
from neko import neko

answer = neko.chat.create(
    key="YOUR_API_KEY",
    model="model_name",
    prompt="Привет! Как дела?"
)

print(answer)
```
