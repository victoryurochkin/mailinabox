#!/usr/bin/env python3
from pathlib import Path

p = Path("management/templates/sync-guide.html")
s = p.read_text()

replacements = {
    '<h2>Contacts &amp; Calendar Synchronization</h2>':
    '<h2>Синхронизация контактов и календаря</h2>',

    '<p>This box can hold your contacts and calendar, just like it holds your email.</p>':
    '<p>Этот сервер может хранить ваши контакты и календарь так же, как хранит вашу почту.</p>',

    '<h4>In your browser</h4>':
    '<h4>В браузере</h4>',

    '<p>You can edit your contacts and calendar from your web browser.</p>':
    '<p>Контакты и календарь можно редактировать из веб-браузера.</p>',

    '<thead><tr><th scope="col">For...</th> <th scope="col">Visit this URL</th></tr></thead>':
    '<thead><tr><th scope="col">Для...</th> <th scope="col">Откройте этот URL</th></tr></thead>',

    '<tr><td>Contacts</td> <td><a href="https://{{hostname}}/cloud/contacts">https://{{hostname}}/cloud/contacts</a></td></tr>':
    '<tr><td>Контакты</td> <td><a href="https://{{hostname}}/cloud/contacts">https://{{hostname}}/cloud/contacts</a></td></tr>',

    '<tr><td>Calendar</td> <td><a href="https://{{hostname}}/cloud/calendar">https://{{hostname}}/cloud/calendar</a></td></tr>':
    '<tr><td>Календарь</td> <td><a href="https://{{hostname}}/cloud/calendar">https://{{hostname}}/cloud/calendar</a></td></tr>',

    '<p>Log in settings are the same as with <a href="#mail-guide">mail</a>: your\n\t\t\tcomplete email address and your mail password.</p>':
    '<p>Параметры входа такие же, как для <a href="#mail-guide">почты</a>: полный email-адрес и пароль от почты.</p>',

    '<h4>On your mobile device</h4>':
    '<h4>На мобильном устройстве</h4>',

    '<p>If you set up your <a href="#mail-guide">mail</a> using Exchange/ActiveSync,\n\t\t\tyour contacts and calendar should already be syncing to your device!</p>':
    '<p>Если вы настроили <a href="#mail-guide">почту</a> через Exchange/ActiveSync, контакты и календарь уже должны синхронизироваться с устройством.</p>',

    '<p>Otherwise, the app below can synchronize your contacts and calendar to your Android phone.</p>':
    '<p>В противном случае приложение ниже может синхронизировать контакты и календарь с Android-телефоном.</p>',

    '<tr><td><a href="https://play.google.com/store/apps/details?id=at.bitfire.davdroid">DAVx⁵</a> (paid)</td> <td><a href="https://f-droid.org/packages/at.bitfire.davdroid/">DAVx⁵</a> (free)</td></tr>':
    '<tr><td><a href="https://play.google.com/store/apps/details?id=at.bitfire.davdroid">DAVx⁵</a> (платно)</td> <td><a href="https://f-droid.org/packages/at.bitfire.davdroid/">DAVx⁵</a> (бесплатно)</td></tr>',

    '<p>Use the following settings:</p>':
    '<p>Используйте следующие параметры:</p>',

    '<tr><td>Account Type</td> <td>CardDAV or CalDAV</td></tr>':
    '<tr><td>Тип учётной записи</td> <td>CardDAV или CalDAV</td></tr>',

    '<tr><td>Server Name</td> <td>{{hostname}}</td></tr>':
    '<tr><td>Имя сервера</td> <td>{{hostname}}</td></tr>',

    '<tr><td>Use SSL</td> <td>Yes</td></tr>':
    '<tr><td>Использовать SSL</td> <td>Да</td></tr>',

    '<tr><td>Username</td> <td>Your complete email address.</td></tr>':
    '<tr><td>Имя пользователя</td> <td>Полный email-адрес.</td></tr>',

    '<tr><td>Password</td> <td>Your mail password.</td></tr>':
    '<tr><td>Пароль</td> <td>Пароль от почты.</td></tr>',
}

for old, new in replacements.items():
    if old not in s:
        print(f"WARN: not found: {old[:120]}")
    s = s.replace(old, new)

p.write_text(s)
print("Changed file: management/templates/sync-guide.html")
