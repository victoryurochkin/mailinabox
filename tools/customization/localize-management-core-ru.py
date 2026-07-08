#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "management/templates/index.html": {
        "{{hostname}} - Mail-in-a-Box Control Panel": "{{hostname}} - Панель управления Mail-in-a-Box",
        "Internet Explorer version 8 or any modern web browser is required to use this website, sorry.": "Для работы с этой панелью нужен Internet Explorer 8 или любой современный браузер.",
        "This is a <a href=\"https://mailinabox.email\">Mail-in-a-Box</a>.": "Это сервер <a href=\"https://mailinabox.email\">Mail-in-a-Box</a>.",
        "Close Dialog": "Закрыть окно",
        ">OK<": ">ОК<",
        ">Yes<": ">Да<",
    },

    "management/templates/login.html": {
        ">Email<": ">Email<",
        "placeholder=\"Email\"": "placeholder=\"Email\"",
        ">Password<": ">Пароль<",
        "placeholder=\"Password\"": "placeholder=\"Пароль\"",
        ">Code<": ">Код<",
        "placeholder=\"6-digit code\"": "placeholder=\"6-значный код\"",
        ">Sign in<": ">Войти<",
    },

    "management/templates/munin.html": {
        "<h2>Munin Monitoring</h2>": "<h2>Мониторинг Munin</h2>",
        "Opening munin in a new tab... You may need to allow pop-ups for this site.": "Munin открывается в новой вкладке... Возможно, для этого сайта нужно разрешить всплывающие окна.",
    },

    "management/templates/system-status.html": {
        "<h2>System Status Checks</h2>": "<h2>Проверки состояния системы</h2>",
        ">Reboot Box<": ">Перезагрузить сервер<",
        "This will reboot your Mail-in-a-Box <code>{{hostname}}</code>.": "Это перезагрузит ваш сервер Mail-in-a-Box <code>{{hostname}}</code>.",
        "Until the machine is fully restarted, your users will not be able to send and receive email, and you will not be able to connect to this control panel or with SSH. The reboot cannot be cancelled.": "Пока сервер полностью не перезапустится, пользователи не смогут отправлять и получать почту, а вы не сможете подключиться к панели управления или по SSH. Перезагрузку нельзя отменить.",
        "Please reload this page after a minute or so.": "Перезагрузите эту страницу примерно через минуту.",
        "The reboot command said:": "Команда перезагрузки вернула:",
    },
}

changed = []

for rel, mapping in REPLACEMENTS.items():
    p = Path(rel)
    text = p.read_text()
    original = text

    for old, new in mapping.items():
        if old not in text:
            print(f"WARN: not found in {rel}: {old}")
            continue
        text = text.replace(old, new)

    if text != original:
        p.write_text(text)
        changed.append(rel)

print("Changed files:")
for f in changed:
    print(f"  {f}")
