#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "setup/bootstrap.sh": {
        "Support is ending for Ubuntu 18.04.": "Поддержка Ubuntu 18.04 завершается.",
        "Please immediately begin to migrate your data to": "Пожалуйста, как можно скорее начните перенос данных на",
        "a new machine running Ubuntu 22.04. See:": "новый сервер с Ubuntu 22.04. Подробнее:",
        "Ubuntu 14.04 is no longer supported.": "Ubuntu 14.04 больше не поддерживается.",
        "The last version of Mail-in-a-Box supporting Ubuntu 14.04 will be installed.": "Будет установлена последняя версия Mail-in-a-Box с поддержкой Ubuntu 14.04.",
        "This script may be used only on a machine running Ubuntu 14.04, 18.04, or 22.04.": "Этот скрипт можно запускать только на сервере с Ubuntu 14.04, 18.04 или 22.04.",
        "This script must be run as root. Did you leave out sudo?": "Этот скрипт нужно запускать от root. Возможно, вы забыли sudo?",
        "Installing git . . .": "Установка git . . .",
        "Downloading Mail-in-a-Box $TAG. . .": "Загрузка Mail-in-a-Box $TAG . . .",
        "Updating Mail-in-a-Box to $TAG . . .": "Обновление Mail-in-a-Box до $TAG . . .",
        "Update failed. Did you modify something in $PWD?": "Обновление не удалось. Возможно, вы изменяли файлы в $PWD?",
    },

    "setup/preflight.sh": {
        "This script must be run as root. Please re-run like this:": "Этот скрипт нужно запускать от root. Повторите запуск так:",
        "Mail-in-a-Box only supports being installed on Ubuntu 22.04, sorry. You are running:": "Mail-in-a-Box поддерживает установку только на Ubuntu 22.04. Сейчас используется:",
        "Unknown linux distribution": "Неизвестный дистрибутив Linux",
        "We can't write scripts that run on every possible setup, sorry.": "Невозможно поддержать все варианты окружений, поэтому установка остановлена.",
        "Your Mail-in-a-Box needs more memory (RAM) to function properly.": "Для корректной работы Mail-in-a-Box требуется больше оперативной памяти.",
        "Please provision a machine with at least 512 MB, 1 GB recommended.": "Выделите сервер минимум с 512 МБ ОЗУ, рекомендуется 1 ГБ или больше.",
        "This machine has $TOTAL_PHYSICAL_MEM MB memory.": "На этом сервере обнаружено $TOTAL_PHYSICAL_MEM МБ ОЗУ.",
        "WARNING: Your Mail-in-a-Box has less than 768 MB of memory.": "ПРЕДУПРЕЖДЕНИЕ: на сервере Mail-in-a-Box меньше 768 МБ ОЗУ.",
        "         It might run unreliably when under heavy load.": "         При высокой нагрузке система может работать нестабильно.",
        "Mail-in-a-Box has to have exec rights on /tmp, please mount /tmp with exec": "Для Mail-in-a-Box каталог /tmp должен быть смонтирован с правом exec. Перемонтируйте /tmp с exec.",
        "Mail-in-a-Box expects no overrides to wget defaults, ~/.wgetrc exists": "Mail-in-a-Box ожидает стандартные настройки wget, но найден файл ~/.wgetrc.",
        "WARNING:": "ПРЕДУПРЕЖДЕНИЕ:",
        "Mail-in-a-Box has only been tested on x86_64 and i686 platform": "Mail-in-a-Box тестировался только на платформах x86_64 и i686.",
        "architectures. Your architecture, $ARCHITECTURE, may not work.": "Архитектура $ARCHITECTURE может не поддерживаться.",
        "You are on your own.": "Дальнейший запуск выполняется на ваш риск.",
    },

    "setup/questions.sh": {
        "Installing packages needed for setup...": "Установка пакетов, необходимых для настройки...",
        "Mail-in-a-Box Installation": "Установка Mail-in-a-Box",
        "Your Email Address": "Ваш email-адрес",
        "Hostname": "Имя сервера",
        "Public IP Address": "Публичный IPv4-адрес",
        "IPv6 Address (Optional)": "IPv6-адрес (необязательно)",
        "I could not determine the IP or IPv6 address of the network interface": "Не удалось определить IP или IPv6-адрес сетевого интерфейса",
        "for connecting to the Internet. Setup must stop.": "для подключения к Интернету. Установка будет остановлена.",
        "Primary Hostname: $PRIMARY_HOSTNAME": "Основное имя сервера: $PRIMARY_HOSTNAME",
        "Public IP Address: $PUBLIC_IP": "Публичный IPv4-адрес: $PUBLIC_IP",
        "Public IPv6 Address: $PUBLIC_IPV6": "Публичный IPv6-адрес: $PUBLIC_IPV6",
        "Private IP Address: $PRIVATE_IP": "Приватный IPv4-адрес: $PRIVATE_IP",
        "Private IPv6 Address: $PRIVATE_IPV6": "Приватный IPv6-адрес: $PRIVATE_IPV6",
        "Mail-in-a-Box Version: $(git describe --always)": "Версия Mail-in-a-Box: $(git describe --always)",
    },

    "setup/functions.sh": {
        "FAILED: $*": "ОШИБКА: $*",
        "Download of $URL did not match expected checksum.": "Контрольная сумма загруженного файла $URL не совпала с ожидаемой.",
        "Found:": "Получено:",
        "Expected:": "Ожидалось:",
    },

    "setup/start.sh": {
        "Waiting for the Mail-in-a-Box management daemon to start...": "Ожидание запуска службы управления Mail-in-a-Box...",
        "Mail-in-a-Box uses Let's Encrypt to provision free SSL/TLS certificates": "Mail-in-a-Box использует Let's Encrypt для выпуска бесплатных SSL/TLS-сертификатов",
        "to enable HTTPS connections to your box. We're automatically": "для включения HTTPS-подключений к вашему серверу. Установка автоматически",
        "agreeing you to their subscriber agreement. See https://letsencrypt.org.": "принимает пользовательское соглашение Let's Encrypt. Подробнее: https://letsencrypt.org.",
        "Your Mail-in-a-Box is running.": "Ваш Mail-in-a-Box запущен.",
        "Please log in to the control panel for further instructions at:": "Войдите в панель управления для дальнейших инструкций:",
        "If you have a DNS problem put the box's IP address in the URL": "Если есть проблема с DNS, используйте IP-адрес сервера в URL",
        "(https://$PUBLIC_IP/admin) but then check the TLS fingerprint:": "(https://$PUBLIC_IP/admin), но обязательно проверьте TLS-отпечаток:",
        "You will be alerted that the website has an invalid certificate. Check that": "Браузер предупредит о недействительном сертификате. Проверьте, что",
        "the certificate fingerprint matches:": "отпечаток сертификата совпадает:",
        "Then you can confirm the security exception and continue.": "После этого можно подтвердить исключение безопасности и продолжить.",
    },

    "setup/system.sh": {
        "Adding a swap file to the system...": "Добавление swap-файла в систему...",
        "ERROR: Swap allocation failed": "ОШИБКА: не удалось выделить swap.",
        "Installing add-apt-repository...": "Установка add-apt-repository...",
        "Updating system packages...": "Обновление системных пакетов...",
        "Installing system packages...": "Установка системных пакетов...",
        "Setting timezone to UTC.": "Установка часового пояса UTC.",
        "Initializing system random number generator...": "Инициализация системного генератора случайных чисел...",
        "Creating SSH key for backup…": "Создание SSH-ключа для резервного копирования…",
        "Opening alternate SSH port $port.": "Открытие альтернативного SSH-порта $port.",
    },

    "setup/network-checks.sh": {
        "The hostname you chose '$PRIMARY_HOSTNAME' is listed in the": "Выбранное имя сервера '$PRIMARY_HOSTNAME' находится в",
        "Spamhaus Domain Block List. See http://www.spamhaus.org/dbl/": "Spamhaus Domain Block List. См. http://www.spamhaus.org/dbl/",
        "and http://www.spamhaus.org/query/domain/$PRIMARY_HOSTNAME.": "и http://www.spamhaus.org/query/domain/$PRIMARY_HOSTNAME.",
        "You will not be able to send mail using this domain name, so": "С этим доменным именем отправка почты будет невозможна, поэтому",
        "setup cannot continue.": "установка не может быть продолжена.",
        "The IP address $PUBLIC_IP is listed in the Spamhaus Block List.": "IP-адрес $PUBLIC_IP находится в Spamhaus Block List.",
        "See http://www.spamhaus.org/query/ip/$PUBLIC_IP.": "См. http://www.spamhaus.org/query/ip/$PUBLIC_IP.",
        "You will not be able to send mail using this machine, so setup": "С этого сервера нельзя будет отправлять почту, поэтому установка",
        "cannot continue.": "не может быть продолжена.",
        "Associate a different IP address with this machine if possible.": "Если возможно, назначьте этому серверу другой IP-адрес.",
        "Many residential network IP addresses are listed, so Mail-in-a-Box": "Многие IP-адреса домашних сетей находятся в блок-листах, поэтому Mail-in-a-Box",
        "typically cannot be used on a residential Internet connection.": "обычно нельзя использовать на домашнем интернет-подключении.",
        "Outbound mail (port 25) seems to be blocked by your network.": "Похоже, исходящая почта через порт 25 заблокирована вашей сетью.",
        "Many residential networks block port 25 to prevent hijacked": "Многие домашние сети блокируют порт 25, чтобы заражённые",
        "machines from being able to send spam. I just tried to connect": "устройства не могли рассылать спам. Была выполнена попытка подключения",
        "to Google's mail server on port 25 but the connection did not": "к почтовому серверу Google на порт 25, но соединение",
        "succeed.": "не установилось.",
    },

    "setup/dns.sh": {
        "Installing nsd (DNS server)...": "Установка nsd (DNS-сервер)...",
        "Generating DNSSEC signing keys...": "Генерация ключей подписи DNSSEC...",
    },

    "setup/web.sh": {
        "Removing apache...": "Удаление Apache...",
        "Installing Nginx (web server)...": "Установка Nginx (веб-сервер)...",
    },

    "setup/mail-postfix.sh": {
        "Installing Postfix (SMTP server)...": "Установка Postfix (SMTP-сервер)...",
    },

    "setup/mail-dovecot.sh": {
        "Installing Dovecot (IMAP server)...": "Установка Dovecot (IMAP-сервер)...",
    },

    "setup/mail-users.sh": {
        "Creating new user database: $db_path": "Создание новой базы пользователей: $db_path",
    },

    "setup/dkim.sh": {
        "Installing OpenDKIM/OpenDMARC...": "Установка OpenDKIM/OpenDMARC...",
    },

    "setup/spamassassin.sh": {
        "Installing SpamAssassin...": "Установка SpamAssassin...",
    },

    "setup/ssl.sh": {
        "Creating initial SSL certificate and perfect forward secrecy Diffie-Hellman parameters...": "Создание первичного SSL-сертификата и параметров Diffie-Hellman для Perfect Forward Secrecy...",
    },

    "setup/management.sh": {
        "Installing Mail-in-a-Box system management daemon...": "Установка системной службы управления Mail-in-a-Box...",
    },

    "setup/munin.sh": {
        "Installing Munin (system monitoring)...": "Установка Munin (мониторинг системы)...",
    },

    "setup/zpush.sh": {
        "Installing Z-Push (Exchange/ActiveSync server)...": "Установка Z-Push (сервер Exchange/ActiveSync)...",
    },

    "setup/webmail.sh": {
        "Installing Roundcube (webmail)...": "Установка Roundcube (веб-почта)...",
    },

    "setup/nextcloud.sh": {
        "Installing Nextcloud (contacts/calendar)...": "Установка Nextcloud (контакты/календарь)...",
        "Upgrading to Nextcloud version $version": "Обновление Nextcloud до версии $version",
        "Contacts app archive did not unpack to /usr/local/lib/owncloud/apps/contacts.": "Архив приложения Contacts не распаковался в /usr/local/lib/owncloud/apps/contacts.",
        "Calendar app archive did not unpack to /usr/local/lib/owncloud/apps/calendar.": "Архив приложения Calendar не распаковался в /usr/local/lib/owncloud/apps/calendar.",
        "Trying ownCloud upgrade again to work around ownCloud upgrade bug...": "Повторная попытка обновления ownCloud для обхода ошибки обновления...",
        "...which seemed to work.": "...похоже, это сработало.",
        "Upgrading Nextcloud --- backing up existing installation, configuration, and database to directory to $BACKUP_DIRECTORY...": "Обновление Nextcloud --- резервное копирование текущей установки, конфигурации и базы данных в каталог $BACKUP_DIRECTORY...",
        "Upgrades from Mail-in-a-Box prior to v0.28 (dated July 30, 2018) with Nextcloud < 13.0.6 (you have ownCloud 8 or 9) are not supported. Upgrade to Mail-in-a-Box version v0.30 first. Setup will continue, but skip the Nextcloud migration.": "Обновления с Mail-in-a-Box старее v0.28 (30 июля 2018) при Nextcloud < 13.0.6 (у вас ownCloud 8 или 9) не поддерживаются. Сначала обновитесь до Mail-in-a-Box v0.30. Установка продолжится, но миграция Nextcloud будет пропущена.",
        "Upgrades from Mail-in-a-Box prior to v0.28 (dated July 30, 2018) with Nextcloud < 13.0.6 (you have ownCloud 10, 11 or 12) are not supported. Upgrade to Mail-in-a-Box version v0.30 first. Setup will continue, but skip the Nextcloud migration.": "Обновления с Mail-in-a-Box старее v0.28 (30 июля 2018) при Nextcloud < 13.0.6 (у вас ownCloud 10, 11 или 12) не поддерживаются. Сначала обновитесь до Mail-in-a-Box v0.30. Установка продолжится, но миграция Nextcloud будет пропущена.",
        "Upgrades from Mail-in-a-Box prior to v60 with Nextcloud 19 or earlier are not supported. Upgrade to the latest Mail-in-a-Box version supported on your machine first. Setup will continue, but skip the Nextcloud migration.": "Обновления с Mail-in-a-Box старее v60 при Nextcloud 19 или ниже не поддерживаются. Сначала обновитесь до последней версии Mail-in-a-Box, поддерживаемой на этом сервере. Установка продолжится, но миграция Nextcloud будет пропущена.",
    },

    "setup/firstuser.sh": {
        "Mail Account": "Почтовый аккаунт",
        "Creating a new administrative mail account for $EMAIL_ADDR with password $EMAIL_PW.": "Создание нового административного почтового аккаунта $EMAIL_ADDR с паролем $EMAIL_PW.",
        "Okay. I'm about to set up $EMAIL_ADDR for you. This account will also": "Хорошо. Сейчас будет настроен аккаунт $EMAIL_ADDR. Этот аккаунт также",
        "have access to the box's control panel.": "получит доступ к панели управления сервера.",
    },
}

changed_files = []

for rel_path, replacements in REPLACEMENTS.items():
    path = Path(rel_path)
    if not path.exists():
        raise SystemExit(f"ERROR: file not found: {rel_path}")

    text = path.read_text()
    original = text

    for old, new in replacements.items():
        if old not in text:
            print(f"WARN: not found in {rel_path}: {old}")
            continue
        text = text.replace(old, new)

    if text != original:
        path.write_text(text)
        changed_files.append(rel_path)

print("Changed files:")
for f in changed_files:
    print(f"  {f}")
