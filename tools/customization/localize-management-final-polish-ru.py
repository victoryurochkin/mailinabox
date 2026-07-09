#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "management/templates/index.html": {
        '<li><a href="#mail-guide">Instructions</a></li>':
        '<li><a href="#mail-guide">Инструкция</a></li>',

        '<li class="dropdown-header">Your Account</li>':
        '<li class="dropdown-header">Ваша учётная запись</li>',

        '<li class="if-logged-in"><a href="#" onclick="do_logout(); return false;" style="color: white">Log out</a></li>':
        '<li class="if-logged-in"><a href="#" onclick="do_logout(); return false;" style="color: white">Выйти</a></li>',

        '// the custom DNS api sends raw POST/PUT bodies --- prevent URL-encoding':
        '// API пользовательских DNS-записей отправляет сырые тела POST/PUT — не URL-кодируем их',

        '// Remove locally stored credentials':
        '// Удаляем локально сохранённые учётные данные',
    },

    "management/templates/login.html": {
        '// Login succeeded but user might not be authorized!':
        '// Вход выполнен, но пользователь может быть не авторизован!',

        '// Login succeeded.':
        '// Вход выполнен.',

        '// Save the new credentials.':
        '// Сохраняем новые учётные данные.',

        '// Reset any saved credentials.':
        '// Сбрасываем сохранённые учётные данные.',
    },

    "management/templates/system-status.html": {
        '<div><a onclick="return enable_privacy(!current_privacy_setting)" href="#"><span>Enable/Disable</span> New-Version Check</a></div>':
        '<div><a onclick="return enable_privacy(!current_privacy_setting)" href="#"><span>Включить/отключить</span> проверку новых версий</a></div>',

        "summary.append($('<span class=\"summary-error\"/>').text(`${count_by_status['error']} ${error_symbol} Error, `));":
        "summary.append($('<span class=\"summary-error\"/>').text(`${count_by_status['error']} ${error_symbol} ошибок, `));",

        "// successful reboots don't produce any output; the output must be HTML-escaped":
        "// успешная перезагрузка не возвращает вывод; вывод должен быть HTML-экранирован",
    },

    "management/templates/users.html": {
        "n.find('.quota').text((user.quota == '0') ? 'unlimited' : user.quota);":
        "n.find('.quota').text((user.quota == '0') ? 'без ограничений' : user.quota);",
    },

    "management/templates/aliases.html": {
        '<span class="domainalias text-muted">Enter just the part of an email address starting with the @-sign.</span>':
        '<span class="domainalias text-muted">Введите только часть email-адреса, начиная со знака @.</span>',

        "$('#addaliasForwardsTo').attr('placeholder', 'one address per line or separated by commas');":
        "$('#addaliasForwardsTo').attr('placeholder', 'один адрес на строку или через запятую');",

        "$('#addaliasForwardsTo').attr('placeholder', '@otherdomain.com (forward to other domain)');":
        "$('#addaliasForwardsTo').attr('placeholder', '@otherdomain.com (домен назначения пересылки)');",
    },

    "management/templates/ssl.html": {
        'placeholder="-----BEGIN CERTIFICATE-----&#xA;stuff here&#xA;-----END CERTIFICATE-----"':
        'placeholder="-----BEGIN CERTIFICATE-----&#xA;содержимое сертификата&#xA;-----END CERTIFICATE-----"',

        'placeholder="-----BEGIN CERTIFICATE-----&#xA;stuff here&#xA;-----END CERTIFICATE-----&#xA;-----BEGIN CERTIFICATE-----&#xA;more stuff here&#xA;-----END CERTIFICATE-----"':
        'placeholder="-----BEGIN CERTIFICATE-----&#xA;содержимое сертификата&#xA;-----END CERTIFICATE-----&#xA;-----BEGIN CERTIFICATE-----&#xA;содержимое промежуточного сертификата&#xA;-----END CERTIFICATE-----"',
    },

    "management/templates/custom-dns.html": {
        'Введите hostname, которому нужно делегировать этот поддомен.':
        'Введите имя хоста, которому нужно делегировать этот поддомен.',

        'После настройки укажите ниже hostname вторичного DNS-сервера провайдера, а не его IP-адрес.':
        'После настройки укажите ниже имя хоста вторичного DNS-сервера провайдера, а не его IP-адрес.',

        '<label for="secondarydnsHostname" class="col-sm-1 control-label">Hostname</label>':
        '<label for="secondarydnsHostname" class="col-sm-1 control-label">Имя хоста</label>',

        'добавьте перед hostname, IP-адресом или подсетью префикс':
        'добавьте перед именем хоста, IP-адресом или подсетью префикс',
    },

    "management/templates/system-backup.html": {
        '<label for="backup-target-rsync-host" class="col-sm-2 control-label">Hostname</label>':
        '<label for="backup-target-rsync-host" class="col-sm-2 control-label">Имя хоста</label>',

        '<label for="backup-target-s3-host" class="col-sm-2 control-label">S3 Host / Endpoint</label>':
        '<label for="backup-target-s3-host" class="col-sm-2 control-label">Хост / endpoint S3</label>',

        '<label for="backup-target-s3-path" class="col-sm-2 control-label">S3 Bucket и путь</label>':
        '<label for="backup-target-s3-path" class="col-sm-2 control-label">Бакет S3 и путь</label>',

        '<label for="backup-target-user" class="col-sm-2 control-label">S3 Access Key</label>':
        '<label for="backup-target-user" class="col-sm-2 control-label">Ключ доступа S3</label>',

        '<label for="backup-target-pass" class="col-sm-2 control-label">S3 Secret Access Key</label>':
        '<label for="backup-target-pass" class="col-sm-2 control-label">Секретный ключ доступа S3</label>',

        '<label for="backup-target-b2-user" class="col-sm-2 control-label">B2 Application KeyID</label>':
        '<label for="backup-target-b2-user" class="col-sm-2 control-label">ID ключа приложения B2</label>',

        '<label for="backup-target-b2-pass" class="col-sm-2 control-label">B2 Application Key</label>':
        '<label for="backup-target-b2-pass" class="col-sm-2 control-label">Ключ приложения B2</label>',

        '<label for="backup-target-b2-bucket" class="col-sm-2 control-label">B2 Bucket</label>':
        '<label for="backup-target-b2-bucket" class="col-sm-2 control-label">Бакет B2</label>',

        'Резервные копии хранятся в S3-совместимом bucket.':
        'Резервные копии хранятся в S3-совместимом бакете.',

        'Он <b>НЕ</b> хранится в S3 bucket.':
        'Он <b>НЕ</b> хранится в бакете S3.',

        'Резервные копии хранятся в bucket <a href="https://www.backblaze.com/" target="_blank" rel="noreferrer">Backblaze</a> B2.':
        'Резервные копии хранятся в бакете <a href="https://www.backblaze.com/" target="_blank" rel="noreferrer">Backblaze</a> B2.',

        'Он НЕ хранится в bucket Backblaze B2.':
        'Он НЕ хранится в бакете Backblaze B2.',
    },
}

changed = []

for rel, mapping in REPLACEMENTS.items():
    p = Path(rel)
    s = p.read_text()
    original = s

    for old, new in mapping.items():
        if old not in s:
            print(f"WARN: not found in {rel}: {old[:140]}")
            continue
        s = s.replace(old, new)

    if s != original:
        p.write_text(s)
        changed.append(rel)

print("Changed files:")
for f in changed:
    print(f"  {f}")
