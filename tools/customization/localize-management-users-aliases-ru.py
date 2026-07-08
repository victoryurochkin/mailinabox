#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "management/templates/users.html": {
        "<h2>Users</h2>": "<h2>Пользователи</h2>",
        "<h3>Add a mail user</h3>": "<h3>Добавить почтового пользователя</h3>",
        "Add an email address to this system. This will create a new login username/password.": "Добавьте email-адрес в систему. Для него будет создана отдельная учётная запись и пароль.",

        '<label class="sr-only" for="adduserEmail">Email address</label>': '<label class="sr-only" for="adduserEmail">Email-адрес</label>',
        'id="adduserEmail" placeholder="Email Address"': 'id="adduserEmail" placeholder="Email-адрес"',
        '<label class="sr-only" for="adduserPassword">Password</label>': '<label class="sr-only" for="adduserPassword">Пароль</label>',
        'id="adduserPassword" placeholder="Password"': 'id="adduserPassword" placeholder="Пароль"',
        '<option value="">Normal User</option>': '<option value="">Обычный пользователь</option>',
        '<option value="admin">Administrator</option>': '<option value="admin">Администратор</option>',
        '<label class="sr-only" for="adduserQuota">Quota</label>': '<label class="sr-only" for="adduserQuota">Квота</label>',
        'id="adduserQuota" placeholder="Quota"': 'id="adduserQuota" placeholder="Квота"',
        '<button type="submit" class="btn btn-primary">Add User</button>': '<button type="submit" class="btn btn-primary">Добавить пользователя</button>',

        'Passwords must be at least eight characters consisting of English letters and numbers only. For best results, <a href="#" onclick="return generate_random_password()">generate a random password</a>.': 'Пароль должен быть не короче восьми символов и состоять только из латинских букв и цифр. Лучше <a href="#" onclick="return generate_random_password()">сгенерировать случайный пароль</a>.',
        'Use <a href="#aliases">aliases</a> to create email addresses that forward to existing accounts.': 'Используйте <a href="#aliases">алиасы</a>, чтобы создавать email-адреса с пересылкой на существующие аккаунты.',
        'Administrators get access to this control panel.': 'Администраторы получают доступ к этой панели управления.',
        'User accounts cannot contain any international (non-ASCII) characters, but <a href="#aliases">aliases</a> can.': 'Учётные записи пользователей не могут содержать международные символы вне ASCII, но <a href="#aliases">алиасы</a> могут.',
        'Quotas may not contain any spaces, commas or decimal points. Suffixes of G (gigabytes) and M (megabytes) are allowed.  For unlimited storage enter 0 (zero)': 'Квоты не должны содержать пробелы, запятые или десятичные точки. Можно использовать суффиксы G (гигабайты) и M (мегабайты). Для неограниченного объёма укажите 0 (ноль).',

        "<h3>Existing mail users</h3>": "<h3>Существующие почтовые пользователи</h3>",
        "<th scope=\"col\" width=\"35%\">Email Address</th>": "<th scope=\"col\" width=\"35%\">Email-адрес</th>",
        '<th scope="col" class="row-center">Size</th>': '<th scope="col" class="row-center">Размер</th>',
        '<th scope="col" class="row-center">Used</th>': '<th scope="col" class="row-center">Использовано</th>',
        '<th scope="col" class="row-center">Quota</th>': '<th scope="col" class="row-center">Квота</th>',
        '<th scope="col">Actions</th>': '<th scope="col">Действия</th>',

        'title="Set Quota"': 'title="Изменить квоту"',
        '>set quota<': '>изменить квоту<',
        'title="Set Password"': 'title="Изменить пароль"',
        '>set password<': '>изменить пароль<',
        'title="Archive Account"': 'title="Архивировать аккаунт"',
        '>archive account<': '>архивировать аккаунт<',
        "To restore account, create a new account with this email address. Or to permanently delete the mailbox, delete the directory <tt></tt> on the machine.": "Чтобы восстановить аккаунт, создайте новый аккаунт с этим email-адресом. Чтобы окончательно удалить почтовый ящик, удалите каталог <tt></tt> на сервере.",

        "<h3>Mail user API (advanced)</h3>": "<h3>API почтовых пользователей (для опытных пользователей)</h3>",
        "Use your box&rsquo;s mail user API to add/change/remove users from the command-line or custom services you build.": "Используйте API почтовых пользователей, чтобы добавлять, изменять и удалять пользователей из командной строки или собственных сервисов.",
        "<p>Usage:</p>": "<p>Использование:</p>",
        "Brackets denote an optional argument. Please note that the POST body <code>parameters</code> must be URL-encoded.": "Квадратные скобки обозначают необязательный аргумент. Обратите внимание: тело POST-запроса <code>parameters</code> должно быть URL-кодировано.",
        "The email and password given to the <code>--user</code> option must be an administrative user on this system.": "Email и пароль, переданные в параметре <code>--user</code>, должны принадлежать административному пользователю этой системы.",
        '<h4 style="margin-bottom: 0">Verbs</h4>': '<h4 style="margin-bottom: 0">Команды</h4>',
        "<h4>Examples:</h4>": "<h4>Примеры:</h4>",
        "Try these examples. For simplicity the examples omit the <code>--user me@mydomain.com:yourpassword</code> command line argument which you must fill in with your administrative email address and password.": "Попробуйте эти примеры. Для простоты в них не указан аргумент <code>--user me@mydomain.com:yourpassword</code>; его нужно заполнить административным email-адресом и паролем.",

        "title='Remove Privilege'>remove privilege</a>": "title='Удалить привилегию'>удалить привилегию</a>",
        "title='Add Privilege'>make <span class='name'></span></a>": "title='Добавить привилегию'>назначить <span class='name'></span></a>",
        'show_modal_error("Add User", $("<pre/>").text(r));': 'show_modal_error("Добавить пользователя", $("<pre/>").text(r));',
        'show_modal_error("Add User", r);': 'show_modal_error("Добавить пользователя", r);',
        '"Set Password",': '"Изменить пароль",',
        "New Password:": "Новый пароль:",
        "Passwords must be at least eight characters and may not contain spaces.": "Пароль должен быть не короче восьми символов и не должен содержать пробелы.",
        "If you change your own password, you will be logged out of this control panel and will need to log in again.": "Если вы измените собственный пароль, сеанс в панели управления будет завершён, и потребуется войти заново.",
        '"Set Quota",': '"Изменить квоту",',
        "Set quota for": "Задать квоту для",
        "Quota:": "Квота:",
        "Quotas may not contain any spaces or commas.  Suffixes of G (gigabytes) and M (megabytes) are allowed.": "Квоты не должны содержать пробелы или запятые. Можно использовать суффиксы G (гигабайты) и M (мегабайты).",
        "For unlimited storage enter 0 (zero)": "Для неограниченного объёма укажите 0 (ноль).",
        '"Archive User",': '"Архивировать пользователя",',
        "Are you sure you want to archive": "Вы уверены, что хотите архивировать",
        "The user's mailboxes will not be deleted (you can do that later), but the user will no longer be able to log into any services on this machine.": "Почтовые ящики пользователя не будут удалены, это можно сделать позже. Но пользователь больше не сможет входить в сервисы на этом сервере.",
        '"Archive",': '"Архивировать",',
        '"Modify Privileges"': '"Изменение привилегий"',
        "You cannot remove the admin privilege from yourself.": "Нельзя удалить административную привилегию у самого себя.",
        'var add_remove1 = add_remove.charAt(0).toUpperCase() + add_remove.substring(1);': 'var add_remove1 = (add_remove == "add") ? "Добавить" : "Удалить";',
        'Are you sure you want to " + add_remove + " the " + priv + " privilege for': 'Вы уверены, что хотите " + ((add_remove == "add") ? "добавить" : "удалить") + " привилегию " + priv + " для',
        '"Random Password"': '"Случайный пароль"',
        "Here, try this:": "Можно использовать этот вариант:",
    },

    "management/templates/aliases.html": {
        "<h2>Aliases</h2>": "<h2>Алиасы</h2>",
        "<h3>Add a mail alias</h3>": "<h3>Добавить почтовый алиас</h3>",
        "Aliases are email forwarders. An alias can forward email to a <a href=\"#users\">mail user</a> or to any email address.": "Алиасы — это почтовые перенаправления. Алиас может пересылать почту <a href=\"#users\">почтовому пользователю</a> или на любой email-адрес.",
        "To use an alias or any address besides your own login username in outbound mail, the sending user must be included as a permitted sender for the alias.": "Чтобы отправлять исходящую почту от имени алиаса или другого адреса, отправляющий пользователь должен быть добавлен в список разрешённых отправителей для этого алиаса.",

        ">Regular<": ">Обычный<",
        ">Domain Alias<": ">Алиас домена<",
        "A catch-all alias captures all otherwise unmatched email to a domain.": "Catch-All алиас принимает всю почту домена, которая не совпала с другими адресами.",
        "A domain alias forwards all email to the same user at another domain.": "Алиас домена пересылает всю почту на соответствующего пользователя в другом домене.",
        '<label for="addaliasAddress" class="col-sm-1 control-label">Alias</label>': '<label for="addaliasAddress" class="col-sm-1 control-label">Алиас</label>',
        '<label for="addaliasForwardsTo" class="col-sm-1 control-label">Forwards To</label>': '<label for="addaliasForwardsTo" class="col-sm-1 control-label">Пересылать на</label>',
        '<label for="addaliasSenders" class="col-sm-1 control-label">Permitted Senders</label>': '<label for="addaliasSenders" class="col-sm-1 control-label">Разрешённые отправители</label>',
        "Any mail user listed in the Forwards To box can send mail claiming to be from": "Любой почтовый пользователь из поля «Пересылать на» может отправлять почту от имени",
        "the alias address": "адреса алиаса",
        "any address on the alias domain": "любого адреса в домене алиаса",
        "Only these mail users can send mail claiming to be from": "Только эти почтовые пользователи могут отправлять почту от имени",
        'placeholder="one user per line or separated by commas"': 'placeholder="один пользователь на строку или через запятую"',
        '<button id="add-alias-button" type="submit" class="btn btn-primary">Add Alias</button>': '<button id="add-alias-button" type="submit" class="btn btn-primary">Добавить алиас</button>',
        '<button id="alias-cancel" class="btn btn-default hidden" onclick="aliases_reset_form(); return false;">Cancel</button>': '<button id="alias-cancel" class="btn btn-default hidden" onclick="aliases_reset_form(); return false;">Отмена</button>',

        "<h3>Existing mail aliases</h3>": "<h3>Существующие почтовые алиасы</h3>",
        'aria-label="Actions"': 'aria-label="Действия"',
        "<th scope=\"col\"> Alias<br></th>": "<th scope=\"col\"> Алиас<br></th>",
        "<th scope=\"col\"> Forwards To</th>": "<th scope=\"col\"> Пересылать на</th>",
        "<th scope=\"col\"> Permitted Senders</th>": "<th scope=\"col\"> Разрешённые отправители</th>",
        'title="Edit Alias"': 'title="Редактировать алиас"',
        'title="Remove Alias"': 'title="Удалить алиас"',

        "<h3>Mail aliases API (advanced)</h3>": "<h3>API почтовых алиасов (для опытных пользователей)</h3>",
        "Use your box&rsquo;s mail aliases API to add and remove mail aliases from the command-line or custom services you build.": "Используйте API почтовых алиасов, чтобы добавлять и удалять алиасы из командной строки или собственных сервисов.",
        "<p>Usage:</p>": "<p>Использование:</p>",
        "Brackets denote an optional argument. Please note that the POST body <code>parameters</code> must be URL-encoded.": "Квадратные скобки обозначают необязательный аргумент. Обратите внимание: тело POST-запроса <code>parameters</code> должно быть URL-кодировано.",
        "The email and password given to the <code>--user</code> option must be an administrative user on this system.": "Email и пароль, переданные в параметре <code>--user</code>, должны принадлежать административному пользователю этой системы.",
        '<h4 style="margin-bottom: 0">Verbs</h4>': '<h4 style="margin-bottom: 0">Команды</h4>',
        "<h4>Examples:</h4>": "<h4>Примеры:</h4>",
        "Try these examples. For simplicity the examples omit the <code>--user me@mydomain.com:yourpassword</code> command line argument which you must fill in with your email address and password.": "Попробуйте эти примеры. Для простоты в них не указан аргумент <code>--user me@mydomain.com:yourpassword</code>; его нужно заполнить вашим email-адресом и паролем.",

        'var title = (!is_alias_add_update) ? "Add Alias" : "Update Alias";': 'var title = (!is_alias_add_update) ? "Добавить алиас" : "Обновить алиас";',
        "$('#add-alias-button').text('Add Alias');": "$('#add-alias-button').text('Добавить алиас');",
        '"Remove Alias",': '"Удалить алиас",',
        '"Remove " + row_address + "?"': '"Удалить " + row_address + "?"',
        '"Remove",': '"Удалить",',
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
