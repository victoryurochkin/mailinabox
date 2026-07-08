# Русификация Mail-in-a-Box

Цель: глубокая русификация форка Mail-in-a-Box для проекта fnkd.ru.

## Что переводим

- установщик `setup/*.sh`;
- веб-панель управления `management/templates/*.html`;
- пользовательские тексты backend `management/*.py`;
- инструкции, guide-страницы, README и справочные тексты;
- письма и уведомления администратора;
- видимые пользователю сообщения CLI.

## Что не переводим

- имена Linux-пакетов;
- systemd unit names;
- пути файловой системы;
- имена Python-функций, классов и переменных;
- DNS/SPF/DKIM/DMARC/TLS/SMTP/IMAP технические ключи;
- nginx/postfix/dovecot директивы;
- URL, API paths и YAML schema keys;
- upstream protocol names.

## Правило коммитов

Русификацию делать маленькими атомарными коммитами:

1. setup installer;
2. management templates;
3. management backend messages;
4. mail/device guides;
5. documentation;
6. final audit cleanup.
