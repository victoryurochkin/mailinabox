# Русификация Mail-in-a-Box

Цель: русифицированный fork Mail-in-a-Box для проекта fnkd.ru с минимальным риском регрессий.

## Статус

Закрыто:

- исправлена установка Nextcloud Contacts/Calendar;
- русифицирован установщик `setup/*.sh` и `setup/migrate.py`;
- русифицированы основные шаблоны панели управления `management/templates/*.html`;
- добавлены audit/localization scripts в `tools/customization/`;
- создан финальный тег `v76-fnkd-management-ui-russian-localization-final`.

Не переводилось массово:

- backend/API/CLI сообщения в `management/*.py`;
- OpenAPI schema `api/mailinabox.yml`;
- технические конфиги и протокольные шаблоны.

Причина: эти строки часто используются во внутренних API, проверках, CLI, тестах и интеграциях. Массовый перевод повышает риск сломать совместимость. Их стоит переводить только точечно, если конкретная английская строка реально появляется пользователю в панели или в установщике.

## Что переводим

- видимые сообщения установщика;
- видимые HTML-шаблоны панели управления;
- публичные статические страницы;
- fork-specific README/CHANGELOG/CONTRIBUTING;
- конкретные backend-строки только при подтверждённой видимости пользователю.

## Что не переводим

- имена Linux-пакетов;
- systemd unit names;
- пути файловой системы;
- имена Python-функций, классов и переменных;
- DNS/SPF/DKIM/DMARC/TLS/SMTP/IMAP технические ключи;
- nginx/postfix/dovecot директивы;
- URL, API paths и YAML schema keys;
- upstream protocol names.

## Контроль после изменений

```bash
bash -n setup/*.sh
python3 -m py_compile setup/migrate.py management/*.py tools/customization/*.py
find setup management tools -type d -name '__pycache__' -prune -exec rm -rf {} +
git status --short
```

## Правило коммитов

Русификацию делать маленькими атомарными коммитами:

1. setup installer;
2. management templates;
3. final template polish;
4. documentation;
5. backend/API/CLI only by confirmed need.
