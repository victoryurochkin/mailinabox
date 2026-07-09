#!/usr/bin/env python3
from pathlib import Path

p = Path("management/templates/system-backup.html")
s = p.read_text()

replacements = {
    "<h2>Backup Status</h2>":
    "<h2>Состояние резервного копирования</h2>",

    "<p>The box makes an incremental backup each night. You can store the backup on any Amazon Web Services S3-compatible service, or other options.</p>":
    "<p>Сервер каждую ночь создаёт инкрементную резервную копию. Резервные копии можно хранить в любом S3-совместимом сервисе Amazon Web Services или в других поддерживаемых вариантах.</p>",

    "<h3>Configuration</h3>":
    "<h3>Конфигурация</h3>",

    '<label for="backup-target-type" class="col-sm-2 control-label">Backup to:</label>':
    '<label for="backup-target-type" class="col-sm-2 control-label">Хранить резервные копии:</label>',

    '<option value="off">Nowhere (Disable Backups)</option>':
    '<option value="off">Нигде (отключить резервное копирование)</option>',

    '<option value="local">Local</option>':
    '<option value="local">Локально</option>',

    '<option value="rsync">rsync over SSH</option>':
    '<option value="rsync">rsync через SSH</option>',

    '<option value="s3">S3 Compatible Storage</option>':
    '<option value="s3">S3-совместимое хранилище</option>',

    '<option value="b2">Backblaze B2</option>':
    '<option value="b2">Backblaze B2</option>',

    "Backups are stored on this machine&rsquo;s own hard disk. You are responsible for periodically using SFTP (FTP over SSH) to copy the backup files from <tt class=\"backup-location\"></tt> to a safe location. These files are encrypted, so they are safe to store anywhere.":
    "Резервные копии хранятся на локальном диске этого сервера. Вам нужно периодически копировать файлы резервных копий из <tt class=\"backup-location\"></tt> в безопасное место через SFTP (FTP поверх SSH). Эти файлы зашифрованы, поэтому их можно безопасно хранить в любом месте.",

    "Separately copy the encryption password from <tt class=\"backup-encpassword-file\"></tt> to a safe and secure location. You will need this file to decrypt backup files.":
    "Отдельно скопируйте пароль шифрования из <tt class=\"backup-encpassword-file\"></tt> в безопасное место. Этот файл понадобится для расшифровки резервных копий.",

    "Backups synced to a remote machine using rsync over SSH, with local":
    "Резервные копии синхронизируются на удалённый сервер через rsync поверх SSH, с локальными",

    "they are safe to store anywhere.":
    "их можно безопасно хранить в любом месте.",

    "Separately copy the encryption":
    "Отдельно скопируйте пароль шифрования",

    '<label for="backup-target-rsync-host" class="col-sm-2 control-label">Hostname</label>':
    '<label for="backup-target-rsync-host" class="col-sm-2 control-label">Hostname</label>',

    '<label for="backup-target-rsync-path" class="col-sm-2 control-label">Path</label>':
    '<label for="backup-target-rsync-path" class="col-sm-2 control-label">Путь</label>',

    '<label for="backup-target-rsync-user" class="col-sm-2 control-label">Username</label>':
    '<label for="backup-target-rsync-user" class="col-sm-2 control-label">Имя пользователя</label>',

    '<label for="ssh-pub-key" class="col-sm-2 control-label">Public SSH Key</label>':
    '<label for="ssh-pub-key" class="col-sm-2 control-label">Публичный SSH-ключ</label>',

    "Copy the Public SSH Key above, and paste it within the <tt>~/.ssh/authorized_keys</tt>":
    "Скопируйте публичный SSH-ключ выше и вставьте его в <tt>~/.ssh/authorized_keys</tt>",

    '>Copy<':
    '>Копировать<',

    "Backups are stored in an S3-compatible bucket. You must have an AWS or other S3 service account already.":
    "Резервные копии хранятся в S3-совместимом bucket. У вас уже должна быть учётная запись AWS или другого S3-совместимого сервиса.",

    "You MUST manually copy the encryption password from <tt class=\"backup-encpassword-file\"></tt> to a safe and secure location. You will need this file to decrypt backup files. It is <b>NOT</b> stored in your S3 bucket.":
    "Вы ОБЯЗАТЕЛЬНО должны вручную скопировать пароль шифрования из <tt class=\"backup-encpassword-file\"></tt> в безопасное место. Этот файл понадобится для расшифровки резервных копий. Он <b>НЕ</b> хранится в S3 bucket.",

    '<label for="backup-target-s3-host-select" class="col-sm-2 control-label">S3 Region</label>':
    '<label for="backup-target-s3-host-select" class="col-sm-2 control-label">Регион S3</label>',

    '<label for="backup-target-s3-host" class="col-sm-2 control-label">S3 Host / Endpoint</label>':
    '<label for="backup-target-s3-host" class="col-sm-2 control-label">S3 Host / Endpoint</label>',

    '<label for="backup-target-s3-region-name" class="col-sm-2 control-label">S3 Region Name <span style="font-weight: normal">(if required)</span></label>':
    '<label for="backup-target-s3-region-name" class="col-sm-2 control-label">Имя региона S3 <span style="font-weight: normal">(если требуется)</span></label>',

    '<label for="backup-target-s3-path" class="col-sm-2 control-label">S3 Bucket &amp; Path</label>':
    '<label for="backup-target-s3-path" class="col-sm-2 control-label">S3 Bucket и путь</label>',

    '<label for="backup-target-user" class="col-sm-2 control-label">S3 Access Key</label>':
    '<label for="backup-target-user" class="col-sm-2 control-label">S3 Access Key</label>',

    '<label for="backup-target-pass" class="col-sm-2 control-label">S3 Secret Access Key</label>':
    '<label for="backup-target-pass" class="col-sm-2 control-label">S3 Secret Access Key</label>',

    'Backups are stored in a <a href="https://www.backblaze.com/" target="_blank" rel="noreferrer">Backblaze</a> B2 bucket. You must have a Backblaze account already.':
    'Резервные копии хранятся в bucket <a href="https://www.backblaze.com/" target="_blank" rel="noreferrer">Backblaze</a> B2. У вас уже должна быть учётная запись Backblaze.',

    "You MUST manually copy the encryption password from <tt class=\"backup-encpassword-file\"></tt> to a safe and secure location. You will need this file to decrypt backup files. It is NOT stored in your Backblaze B2 bucket.":
    "Вы ОБЯЗАТЕЛЬНО должны вручную скопировать пароль шифрования из <tt class=\"backup-encpassword-file\"></tt> в безопасное место. Этот файл понадобится для расшифровки резервных копий. Он НЕ хранится в bucket Backblaze B2.",

    '<label for="backup-target-b2-user" class="col-sm-2 control-label">B2 Application KeyID</label>':
    '<label for="backup-target-b2-user" class="col-sm-2 control-label">B2 Application KeyID</label>',

    '<label for="backup-target-b2-pass" class="col-sm-2 control-label">B2 Application Key</label>':
    '<label for="backup-target-b2-pass" class="col-sm-2 control-label">B2 Application Key</label>',

    '<label for="backup-target-b2-bucket" class="col-sm-2 control-label">B2 Bucket</label>':
    '<label for="backup-target-b2-bucket" class="col-sm-2 control-label">B2 Bucket</label>',

    '<label for="min-age" class="col-sm-2 control-label">Retention Days:</label>':
    '<label for="min-age" class="col-sm-2 control-label">Срок хранения, дней:</label>',

    '>Save<':
    '>Сохранить<',

    "<h3>Available backups</h3>":
    "<h3>Доступные резервные копии</h3>",

    "<p>The backup location currently contains the backups listed below. The total size of the backups is currently <span id=\"backup-total-size\"></span>.</p>":
    "<p>В текущем расположении резервных копий найдены копии из списка ниже. Их общий размер сейчас составляет <span id=\"backup-total-size\"></span>.</p>",

    'show_modal_error("Backup Error", $("<pre/>").text(r.error));':
    'show_modal_error("Ошибка резервного копирования", $("<pre/>").text(r.error));',

    "Backups are turned off.":
    "Резервное копирование отключено.",

    'show_modal_error("Backup configuration", $("<p/>").text(r), function() { if (r == "OK") show_system_backup(); });':
    'show_modal_error("Конфигурация резервного копирования", $("<p/>").text(r), function() { if (r == "OK") show_system_backup(); });',

    'show_modal_error("Backup configuration", $("<p/>").text(r));':
    'show_modal_error("Конфигурация резервного копирования", $("<p/>").text(r));',
}

for old, new in replacements.items():
    if old not in s:
        print(f"WARN: not found: {old[:120]}")
    s = s.replace(old, new)

p.write_text(s)
print("Changed file: management/templates/system-backup.html")
