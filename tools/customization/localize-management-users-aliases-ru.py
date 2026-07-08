#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "management/templates/users.html": {
        "<h2>Users</h2>": "<h2>Пользователи</h2>",
        "<h3>Add a mail user</h3>": "<h3>Добавить почтового пользователя</h3>",
        "Add an email address to this system. This will create a new login username/password.": "Добавьте email-адрес в систему. Для него будет создана отдельная учётная запись и пароль.",
        "Email address": "Email-адрес",
        "Email Address": "Email-адрес",
        "Password": "Пароль",
        "Normal User": "Обычный пользователь",
        "Administrator": "Администратор",
        "Quota": "Квота",
        "Add User": "Добавить пользователя",
        "<h3>Existing mail users</h3>": "<h3>Существующие почтовые пользователи</h3>",
        "Set Quota": "Изменить квоту",
        "Set Password": "Изменить пароль",
        "Archive Account": "Архивировать аккаунт",
        "<h3>Mail user API (advanced)</h3>": "<h3>API почтовых пользователей (для опытных пользователей)</h3>",
        "Use your box&rsquo;s mail user API to add/change/remove users from the command-line or custom services you build.": "Используйте API почтовых пользователей, чтобы добавлять, изменять и удалять пользователей из командной строки или собственных сервисов.",
        "<p>Usage:</p>": "<p>Использование:</p>",
        "Brackets denote an optional argument. Please note that the POST body <code>parameters</code> must be URL-encoded.": "Квадратные скобки обозначают необязательный аргумент. Обратите внимание: тело POST-запроса <code>parameters</code> должно быть URL-кодировано.",
        "The email and password given to the <code>--user</code> option must be an administrative user on this system.": "Email и пароль, переданные в параметре <code>--user</code>, должны принадлежать административному пользователю этой системы.",
        "Verbs": "Команды",
        "Examples:": "Примеры:",
        "Try these examples. For simplicity the examples omit the <code>--user me@mydomain.com:yourpassword</code> command line argument which you must fill in with your administrative email address and password.": "Попробуйте эти примеры. Для простоты в них не указан аргумент <code>--user me@mydomain.com:yourpassword</code>; его нужно заполнить административным email-адресом и паролем.",
        "Remove Privilege": "Удалить привилегию",
        "remove privilege": "удалить привилегию",
        "Add Privilege": "Добавить привилегию",
        "make <span class='name'></span>": "назначить <span class='name'></span>",
        "Set a new password for": "Задать новый пароль для",
        "New Password:": "Новый пароль:",
        "Passwords must be at least eight characters and may not contain spaces.": "Пароль должен быть не короче восьми символов и не должен содержать пробелы.",
        "Set quota for": "Задать квоту для",
        "Quotas may not contain any spaces or commas.  Suffixes of G (gigabytes) and M (megabytes) are allowed.": "Квоты не должны содержать пробелы или запятые. Можно использовать суффиксы G (гигабайты) и M (мегабайты).",
        "For unlimited storage enter 0 (zero)": "Для неограниченного объёма укажите 0 (ноль).",
        "Are you sure you want to archive": "Вы уверены, что хотите архивировать",
        "The user's mailboxes will not be deleted (you can do that later), but the user will no longer be able to log into any services on this machine.": "Почтовые ящики пользователя не будут удалены, это можно сделать позже. Но пользователь больше не сможет входить в сервисы на этом сервере.",
        "Are you sure you want to ": "Вы уверены, что хотите ",
        " the ": " привилегию ",
        " privilege for": " для",
        "Random Password": "Случайный пароль",
        "Here, try this:": "Можно использовать этот вариант:",
    },

    "management/templates/aliases.html": {
        "<h2>Aliases</h2>": "<h2>Алиасы</h2>",
        "<h3>Add a mail alias</h3>": "<h3>Добавить почтовый алиас</h3>",
        "Aliases are email forwarders. An alias can forward email to a <a href=\"#users\">mail user</a> or to any email address.": "Алиасы — это почтовые перенаправления. Алиас может пересылать почту <a href=\"#users\">почтовому пользователю</a> или на любой email-адрес.",
        "To use an alias or any address besides your own login username in outbound mail, the sending user must be included as a permitted sender for the alias.": "Чтобы отправлять исходящую почту от имени алиаса или другого адреса, отправляющий пользователь должен быть добавлен в список разрешённых отправителей для этого алиаса.",
        "Regular": "Обычный",
        "Catch-All": "Catch-All",
        "Domain Alias": "Алиас домена",
        "Alias": "Алиас",
        "Forwards To": "Пересылать на",
        "Permitted Senders": "Разрешённые отправители",
        "one user per line or separated by commas": "один пользователь на строку или через запятую",
        "Add Alias": "Добавить алиас",
        "Cancel": "Отмена",
        "<h3>Existing mail aliases</h3>": "<h3>Существующие почтовые алиасы</h3>",
        "Actions": "Действия",
        "Edit Alias": "Редактировать алиас",
        "Remove Alias": "Удалить алиас",
        "<h3>Mail aliases API (advanced)</h3>": "<h3>API почтовых алиасов (для опытных пользователей)</h3>",
        "Use your box&rsquo;s mail aliases API to add and remove mail aliases from the command-line or custom services you build.": "Используйте API почтовых алиасов, чтобы добавлять и удалять алиасы из командной строки или собственных сервисов.",
        "<p>Usage:</p>": "<p>Использование:</p>",
        "Brackets denote an optional argument. Please note that the POST body <code>parameters</code> must be URL-encoded.": "Квадратные скобки обозначают необязательный аргумент. Обратите внимание: тело POST-запроса <code>parameters</code> должно быть URL-кодировано.",
        "The email and password given to the <code>--user</code> option must be an administrative user on this system.": "Email и пароль, переданные в параметре <code>--user</code>, должны принадлежать административному пользователю этой системы.",
        "Verbs": "Команды",
        "Examples:": "Примеры:",
        "Try these examples. For simplicity the examples omit the <code>--user me@mydomain.com:yourpassword</code> command line argument which you must fill in with your email address and password.": "Попробуйте эти примеры. Для простоты в них не указан аргумент <code>--user me@mydomain.com:yourpassword</code>; его нужно заполнить вашим email-адресом и паролем.",
    },
}

changed = []

for rel, mapping in REPLACEMENTS.items():
    p = Path(rel)
    s = p.read_text()
    original = s

    for old, new in mapping.items():
        if old not in s:
            print(f"WARN: not found in {rel}: {old}")
            continue
        s = s.replace(old, new)

    if s != original:
        p.write_text(s)
        changed.append(rel)

print("Changed files:")
for f in changed:
    print(f"  {f}")
