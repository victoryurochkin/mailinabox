Mail-in-a-Box
=============

Этот репозиторий является русифицированным fork проекта Mail-in-a-Box на базе upstream v76. Основная цель fork — установка и эксплуатация Mail-in-a-Box с русскоязычным установщиком и русскоязычной панелью управления.

Основные отличия fork:

* исправлена установка Nextcloud Contacts и Calendar через закреплённые release assets;
* русифицированы сообщения установщика `setup/*.sh` и `setup/migrate.py`;
* русифицированы основные HTML-шаблоны панели управления `management/templates/*.html`;
* добавлены вспомогательные audit/localization tools в `tools/customization/`;
* backend/API/CLI строки массово не переводились намеренно, чтобы не повышать риск регрессий во внутренних API, проверках и интеграциях.

Рекомендуемая установка fork:

```bash
git clone https://github.com/mail-in-a-box/mailinabox
cd mailinabox
sudo setup/start.sh
```

---
