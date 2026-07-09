#!/usr/bin/env python3
from pathlib import Path

p = Path("management/templates/web.html")
s = p.read_text()

replacements = {
    "<h2>Static Web Hosting</h2>":
    "<h2>Статический веб-хостинг</h2>",

    '<p>This machine is serving a simple, static website at <a href="https://{{hostname}}">https://{{hostname}}</a> and at all domain names that you set up an email user or alias for.</p>':
    '<p>Этот сервер обслуживает простой статический сайт по адресу <a href="https://{{hostname}}">https://{{hostname}}</a>, а также на всех доменах, для которых вы создали почтового пользователя или алиас.</p>',

    "<h3>Uploading web files</h3>":
    "<h3>Загрузка файлов сайта</h3>",

    "<p>You can replace the default website with your own HTML pages and other static files. This control panel won&rsquo;t help you design a website, but once you have <tt>.html</tt> files you can upload them following these instructions:</p>":
    "<p>Вы можете заменить сайт по умолчанию своими HTML-страницами и другими статическими файлами. Эта панель управления не помогает разрабатывать сайт, но когда у вас уже есть файлы <tt>.html</tt>, их можно загрузить по инструкции ниже:</p>",

    '<li>Ensure that any domains you are publishing a website for have no problems on the <a href="#system_status">Status Checks</a> page.</li>':
    '<li>Убедитесь, что у доменов, для которых вы публикуете сайт, нет проблем на странице <a href="#system_status">Проверки состояния</a>.</li>',

    '<li>On your personal computer, install an SSH file transfer program such as <a href="https://filezilla-project.org/">FileZilla</a> or <a href="https://man.openbsd.org/scp.1">scp</a>.</li>':
    '<li>На своём компьютере установите программу для передачи файлов по SSH, например <a href="https://filezilla-project.org/">FileZilla</a> или <a href="https://man.openbsd.org/scp.1">scp</a>.</li>',

    '<li>Log in to this machine with the file transfer program. The server is <strong>{{hostname}}</strong>, the protocol is SSH or SFTP, and use the <strong>SSH login credentials</strong> that you used when you originally created this machine at your cloud host provider. This is <strong>not</strong> what you use to log in either for email or this control panel. Your SSH credentials probably involves a private key file.</li>':
    '<li>Подключитесь к этому серверу через программу передачи файлов. Сервер: <strong>{{hostname}}</strong>, протокол: SSH или SFTP. Используйте <strong>SSH-учётные данные</strong>, которые применялись при создании сервера у облачного провайдера. Это <strong>не</strong> логин и пароль от почты или панели управления. Скорее всего, SSH-доступ использует файл приватного ключа.</li>',

    '<li>Upload your <tt>.html</tt> or other files to the directory <tt>{{storage_root}}/www/default</tt> on this machine. They will appear directly and immediately on the web.</li>':
    '<li>Загрузите файлы <tt>.html</tt> или другие файлы в каталог <tt>{{storage_root}}/www/default</tt> на этом сервере. Они сразу станут доступны через веб.</li>',

    '<li>The websites set up on this machine are listed in the table below with where to put the files for each website.</li>':
    '<li>Сайты, настроенные на этом сервере, перечислены в таблице ниже вместе с каталогами, куда нужно загружать файлы каждого сайта.</li>',

    'aria-label="Actions"':
    'aria-label="Действия"',

    '<p>To add a domain to this table, create a dummy <a href="#users">mail user</a> or <a href="#aliases">alias</a> on the domain first and see the <a href="https://mailinabox.email/guide.html#domain-name-configuration">setup guide</a> for adding nameserver records to the new domain at your registrar (but <i>not</i> glue records).</p>':
    '<p>Чтобы добавить домен в эту таблицу, сначала создайте для него фиктивного <a href="#users">почтового пользователя</a> или <a href="#aliases">алиас</a>. Также смотрите <a href="https://mailinabox.email/guide.html#domain-name-configuration">руководство по настройке</a> о добавлении nameserver-записей для нового домена у регистратора, но <i>не</i> glue-записей.</p>',

    "show_change_web_root(this)'>Change</button>":
    "show_change_web_root(this)'>Изменить</button>",

    'show_modal_error("Web Update", data, function() { show_web() });':
    'show_modal_error("Обновление веб-настроек", data, function() { show_web() });',

    "'Change Root Directory for ' + domain":
    "'Изменить корневой каталог для ' + domain",

    "'<p>You can change the static directory for <tt>' + domain + '</tt> to:</p> <p><tt>' + root + '</tt></p> <p>First create this directory on the server. Then click Update to scan for the directory and update web settings.</p>'":
    "'<p>Можно изменить статический каталог для <tt>' + domain + '</tt> на:</p> <p><tt>' + root + '</tt></p> <p>Сначала создайте этот каталог на сервере. Затем нажмите «Обновить», чтобы просканировать каталог и обновить веб-настройки.</p>'",

    "'Update',":
    "'Обновить',",
}

for old, new in replacements.items():
    if old not in s:
        print(f"WARN: not found: {old[:120]}")
    s = s.replace(old, new)

p.write_text(s)
print("Changed file: management/templates/web.html")
