#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "management/templates/index.html": {
        '<a href="#" class="dropdown-toggle" data-toggle="dropdown">System <b class="caret"></b></a>':
        '<a href="#" class="dropdown-toggle" data-toggle="dropdown">Система <b class="caret"></b></a>',

        '<li><a href="#system_status">Status Checks</a></li>':
        '<li><a href="#system_status">Проверки состояния</a></li>',

        '<li><a href="#tls">TLS (SSL) Certificates</a></li>':
        '<li><a href="#tls">TLS (SSL) сертификаты</a></li>',

        '<li><a href="#system_backup">Backup Status</a></li>':
        '<li><a href="#system_backup">Резервные копии</a></li>',

        '<li class="dropdown-header">Advanced Pages</li>':
        '<li class="dropdown-header">Расширенные страницы</li>',

        '<li><a href="#custom_dns">Custom DNS</a></li>':
        '<li><a href="#custom_dns">Пользовательские DNS-записи</a></li>',

        '<li><a href="#external_dns">External DNS</a></li>':
        '<li><a href="#external_dns">Внешний DNS</a></li>',

        '<li><a href="#mail-guide" class="if-logged-in-not-admin">Mail</a></li>':
        '<li><a href="#mail-guide" class="if-logged-in-not-admin">Почта</a></li>',

        '<a href="#" class="dropdown-toggle" data-toggle="dropdown">Mail &amp; Users <b class="caret"></b></a>':
        '<a href="#" class="dropdown-toggle" data-toggle="dropdown">Почта и пользователи <b class="caret"></b></a>',

        '<li><a href="#users">Users</a></li>':
        '<li><a href="#users">Пользователи</a></li>',

        '<li><a href="#aliases">Aliases</a></li>':
        '<li><a href="#aliases">Алиасы</a></li>',

        '<li><a href="#mfa">Two-Factor Authentication</a></li>':
        '<li><a href="#mfa">Двухфакторная аутентификация</a></li>',

        '<li><a href="#sync_guide" class="if-logged-in">Contacts/Calendar</a></li>':
        '<li><a href="#sync_guide" class="if-logged-in">Контакты/Календарь</a></li>',

        '<li><a href="#web" class="if-logged-in-admin">Web</a></li>':
        '<li><a href="#web" class="if-logged-in-admin">Веб</a></li>',

        '<div>Loading...</div>':
        '<div>Загрузка...</div>',

        'global_modal_state = 1; // Cancel':
        'global_modal_state = 1; // Отмена',

        '$("#global_modal .btn-default").show().text("Cancel");':
        '$("#global_modal .btn-default").show().text("Отмена");',

        '$(\'#global_modal .btn-default\').show().text("Cancel");':
        '$(\'#global_modal .btn-default\').show().text("Отмена");',

        'show_modal_error("Error", data.message);':
        'show_modal_error("Ошибка", data.message);',

        'show_modal_error("Error", "Something went wrong, sorry.")':
        'show_modal_error("Ошибка", "Что-то пошло не так.")',
    },

    "management/templates/login.html": {
        '<p class="subtitle">Log in here for your Mail-in-a-Box control panel.</p>':
        '<p class="subtitle">Войдите здесь в панель управления Mail-in-a-Box.</p>',

        '<label for="inputEmail3" class="col-sm-3 control-label">Email</label>':
        '<label for="inputEmail3" class="col-sm-3 control-label">Email-адрес</label>',

        'id="loginEmail" placeholder="Email"':
        'id="loginEmail" placeholder="Email-адрес"',

        'show_modal_error("Login Failed", "Enter your email address.", function()':
        'show_modal_error("Ошибка входа", "Введите email-адрес.", function()',

        'show_modal_error("Login Failed", "Enter your email password.", function()':
        'show_modal_error("Ошибка входа", "Введите пароль от почты.", function()',

        'show_modal_error("Login Failed", "Incorrect two factor authentication token.");':
        'show_modal_error("Ошибка входа", "Неверный код двухфакторной аутентификации.");',

        'show_modal_error("Login Failed", response.reason)':
        'show_modal_error("Ошибка входа", response.reason)',

        'show_modal_error("Login Failed", "You are not an administrator on this system.")':
        'show_modal_error("Ошибка входа", "Вы не являетесь администратором этой системы.")',
    },

    "management/templates/system-status.html": {
        '<p style="line-height: 125%"><small>(When enabled, status checks phone-home to check for a new release of Mail-in-a-Box.)</small></p>':
        '<p style="line-height: 125%"><small>(Если включено, проверки состояния обращаются к внешнему сервису, чтобы проверить наличие новой версии Mail-in-a-Box.)</small></p>',

        "$('#system-checks tbody').html(\"<tr><td colspan='2' class='text-muted'>Loading...</td></tr>\")":
        "$('#system-checks tbody').html(\"<tr><td colspan='2' class='text-muted'>Загрузка...</td></tr>\")",
    },

    "management/templates/welcome.html": {
        '<p class="subtitle">Welcome to your Mail-in-a-Box control panel.</p>':
        '<p class="subtitle">Добро пожаловать в панель управления Mail-in-a-Box.</p>',
    },

    "management/templates/users.html": {
        "# Adds a new email user":
        "# Добавляет нового почтового пользователя",

        "# Removes a email user":
        "# Удаляет почтового пользователя",

        "# Adds admin privilege to an email user":
        "# Назначает пользователю права администратора",

        "# Removes admin privilege from an email user":
        "# Удаляет у пользователя права администратора",

        "$('#user_table tbody').html(\"<tr><td colspan='2' class='text-muted'>Loading...</td></tr>\")":
        "$('#user_table tbody').html(\"<tr><td colspan='2' class='text-muted'>Загрузка...</td></tr>\")",

        "n.find('.box-size').attr('title', 'Mailbox size is unkown')":
        "n.find('.box-size').attr('title', 'Размер почтового ящика неизвестен')",

        'show_modal_error("Remove User", $("<pre/>").text(r));':
        'show_modal_error("Архивировать пользователя", $("<pre/>").text(r));',

        'show_modal_error("Remove User", r);':
        'show_modal_error("Архивировать пользователя", r);',
    },

    "management/templates/aliases.html": {
        'Only forward mail to addresses handled by this Mail-in-a-Box, since mail forwarded by aliases to other domains may be rejected or filtered by the receiver. To forward mail to other domains, create a mail user and then log into webmail for the user and create a filter rule to forward mail.':
        'Пересылайте почту только на адреса, обслуживаемые этим Mail-in-a-Box. Почта, пересылаемая алиасами на другие домены, может быть отклонена или отфильтрована получателем. Чтобы пересылать почту на другие домены, создайте почтового пользователя, войдите в webmail от его имени и настройте правило фильтрации для пересылки.',

        "# Adds a new alias":
        "# Добавляет новый алиас",

        "# Removes an alias":
        "# Удаляет алиас",

        "$('#alias_table tbody').html(\"<tr><td colspan='2' class='text-muted'>Loading...</td></tr>\")":
        "$('#alias_table tbody').html(\"<tr><td colspan='2' class='text-muted'>Загрузка...</td></tr>\")",

        "'you@yourdomain.com (incoming email address)'":
        "'you@yourdomain.com (входящий email-адрес)'",

        "'@yourdomain.com (incoming catch-all domain)'":
        "'@yourdomain.com (входящий catch-all домен)'",

        'show_modal_error(title, "You did not enter any permitted senders.");':
        'show_modal_error(title, "Вы не указали разрешённых отправителей.");',

        "$('#add-alias-button').text('Update');":
        "$('#add-alias-button').text('Обновить');",
    },

    "management/templates/system-backup.html": {
        '<th scope="col" colspan="2">When</th>':
        '<th scope="col" colspan="2">Когда</th>',

        '<th scope="col">Type</th>':
        '<th scope="col">Тип</th>',

        '<th scope="col">Deleted in...</th>':
        '<th scope="col">Удаление через...</th>',
    },
}

changed = []

for rel, mapping in REPLACEMENTS.items():
    p = Path(rel)
    s = p.read_text()
    original = s

    for old, new in mapping.items():
        if old not in s:
            print(f"WARN: not found in {rel}: {old[:120]}")
            continue
        s = s.replace(old, new)

    if s != original:
        p.write_text(s)
        changed.append(rel)

print("Changed files:")
for f in changed:
    print(f"  {f}")
