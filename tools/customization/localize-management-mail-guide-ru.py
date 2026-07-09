#!/usr/bin/env python3
from pathlib import Path

p = Path("management/templates/mail-guide.html")
s = p.read_text()

replacements = {
    '<h2 style="margin-bottom: 0">Checking and Sending Mail</h2>':
    '<h2 style="margin-bottom: 0">Проверка и отправка почты</h2>',

    '<h3>Webmail</h3>':
    '<h3>Веб-почта</h3>',

    '<p>Webmail lets you check your email from any web browser. Your webmail site is:</p>':
    '<p>Веб-почта позволяет проверять почту из любого браузера. Адрес вашей веб-почты:</p>',

    '<p>Your username is your whole email address.</p>':
    '<p>Имя пользователя — полный email-адрес.</p>',

    '<h3>Mobile/desktop apps</h3>':
    '<h3>Мобильные и настольные приложения</h3>',

    '<h4>Automatic configuration</h4>':
    '<h4>Автоматическая настройка</h4>',

    '<p>iOS and macOS only: Open <a style="font-weight: bold" href="https://{{hostname}}/mailinabox.mobileconfig">this configuration link</a> on your iOS device or on your Mac desktop to easily set up mail (IMAP/SMTP), Contacts, and Calendar. Your username is your whole email address.</p>':
    '<p>Только для iOS и macOS: откройте <a style="font-weight: bold" href="https://{{hostname}}/mailinabox.mobileconfig">эту ссылку конфигурации</a> на устройстве iOS или Mac, чтобы быстро настроить почту (IMAP/SMTP), Контакты и Календарь. Имя пользователя — полный email-адрес.</p>',

    '<h4>Manual configuration</h4>':
    '<h4>Ручная настройка</h4>',

    '<p>Use the following settings when you set up your email on your phone, desktop, or other device:</p>':
    '<p>Используйте следующие параметры при настройке почты на телефоне, компьютере или другом устройстве:</p>',

    '<tr><th scope="col">Option</th> <th scope="col">Value</th></tr>':
    '<tr><th scope="col">Параметр</th> <th scope="col">Значение</th></tr>',

    '<tr><th scope="row">Protocol/Method</th> <td>IMAP</td></tr>':
    '<tr><th scope="row">Протокол/метод</th> <td>IMAP</td></tr>',

    '<tr><th scope="row">Mail server</th> <td>{{hostname}}</td>':
    '<tr><th scope="row">Почтовый сервер</th> <td>{{hostname}}</td>',

    '<tr><th scope="row">IMAP Port</th> <td>993</td></tr>':
    '<tr><th scope="row">Порт IMAP</th> <td>993</td></tr>',

    '<tr><th scope="row">IMAP Security</th> <td>SSL or TLS</td></tr>':
    '<tr><th scope="row">Безопасность IMAP</th> <td>SSL или TLS</td></tr>',

    '<tr><th scope="row">SMTP Port</th> <td>465</td></tr>':
    '<tr><th scope="row">Порт SMTP</th> <td>465</td></tr>',

    '<tr><th scope="row">SMTP Security</td> <td>SSL or TLS</td></tr>':
    '<tr><th scope="row">Безопасность SMTP</td> <td>SSL или TLS</td></tr>',

    '<tr><th scope="row">Username:</th> <td>Your whole email address.</td></tr>':
    '<tr><th scope="row">Имя пользователя:</th> <td>Полный email-адрес.</td></tr>',

    '<tr><th scope="row">Password:</th> <td>Your mail password.</td></tr>':
    '<tr><th scope="row">Пароль:</th> <td>Пароль от почты.</td></tr>',

    '<p>In addition to setting up your email, you&rsquo;ll also need to set up <a href="#sync_guide">contacts and calendar synchronization</a> separately.</p>':
    '<p>Кроме настройки почты, отдельно нужно настроить <a href="#sync_guide">синхронизацию контактов и календаря</a>.</p>',

    '<p>As an alternative to IMAP you can also use the POP protocol: choose POP as the protocol, port 995, and SSL or TLS security in your mail client. The SMTP settings and usernames and passwords remain the same. However, we recommend you use IMAP instead.</p>':
    '<p>В качестве альтернативы IMAP можно использовать протокол POP: выберите POP как протокол, порт 995 и защиту SSL или TLS в почтовом клиенте. Параметры SMTP, имена пользователей и пароли остаются теми же. Однако мы рекомендуем использовать IMAP.</p>',

    '<h4>Exchange/ActiveSync settings</h4>':
    '<h4>Параметры Exchange/ActiveSync</h4>',

    '<p>On iOS devices, devices on this <a href="https://github.com/Z-Hub/Z-Push/wiki/Compatibility">compatibility list</a>, or using Outlook 2007 or later on Windows 7 and later, you may set up your mail as an Exchange or ActiveSync server. However, we&rsquo;ve found this to be more buggy than using IMAP as described above. If you encounter any problems, please use the manual settings above.</p>':
    '<p>На устройствах iOS, устройствах из этого <a href="https://github.com/Z-Hub/Z-Push/wiki/Compatibility">списка совместимости</a>, а также в Outlook 2007 и новее на Windows 7 и новее можно настроить почту как Exchange- или ActiveSync-сервер. Однако этот вариант обычно менее стабилен, чем IMAP, описанный выше. Если возникнут проблемы, используйте ручные параметры выше.</p>',

    '<tr><th scope="row">Server</th> <td>{{hostname}}</td></tr>':
    '<tr><th scope="row">Сервер</th> <td>{{hostname}}</td></tr>',

    '<tr><th scope="row">Options</th> <td>Secure Connection</td></tr>':
    '<tr><th scope="row">Параметры</th> <td>Защищённое соединение</td></tr>',

    '<p>Your device should also provide a contacts list and calendar that syncs to this box when you use this method.</p>':
    '<p>При использовании этого метода устройство также должно предоставить список контактов и календарь, которые синхронизируются с этим сервером.</p>',

    '<h3>Other information about mail on your box</h3>':
    '<h3>Дополнительная информация о почте на сервере</h3>',

    '<h4>Greylisting</h4>':
    '<h4>Greylisting</h4>',

    '<p>Your box uses a technique called greylisting to cut down on spam. Greylisting works by initially rejecting mail from people you haven&rsquo;t received mail from before. Legitimate mail servers will attempt redelivery shortly afterwards, but the vast majority of spam gets tricked by this. If you are waiting for an email from someone new, such as if you are registering on a new website and are waiting for an email confirmation, please be aware there will be a minimum of 3 minutes delay, depending how soon the remote server attempts redelivery.</p>':
    '<p>Сервер использует технологию greylisting для снижения количества спама. Greylisting сначала временно отклоняет почту от отправителей, от которых вы раньше не получали письма. Легитимные почтовые серверы вскоре повторят доставку, а большая часть спама на этом отсеивается. Если вы ждёте письмо от нового отправителя, например подтверждение регистрации на сайте, учитывайте минимальную задержку около 3 минут. Фактическая задержка зависит от того, как быстро удалённый сервер повторит доставку.</p>',

    '<h4>+tag addresses</h4>':
    '<h4>Адреса с +tag</h4>',

    '<p>Every incoming email address also receives mail for <code>+tag</code> addresses. If your email address is <code>you@yourdomain.com</code>, you&rsquo;ll also automatically get mail sent to <code>you+anythinghere@yourdomain.com</code>. Use this as a fast way to segment incoming mail for your own filtering rules without having to create aliases in this control panel.</p>':
    '<p>Каждый входящий email-адрес также принимает почту для адресов с <code>+tag</code>. Например, если ваш адрес <code>you@yourdomain.com</code>, вы автоматически получите письма, отправленные на <code>you+anythinghere@yourdomain.com</code>. Это быстрый способ разделять входящую почту для собственных правил фильтрации без создания алиасов в панели управления.</p>',

    '<h4>Use only this box to send as you</h4>':
    '<h4>Используйте только этот сервер для отправки от вашего имени</h4>',

    '<p>Your box sets strict email sending policies for your domain names to make it harder for spam and other fraudulent mail to claim to be you. Only this machine is authorized to send email on behalf of your domain names. If you use any other service to send email as you, it will likely get spam filtered by recipients.</p>':
    '<p>Сервер задаёт строгие политики отправки почты для ваших доменов, чтобы спаму и мошенническим письмам было сложнее выдавать себя за вас. Только этот сервер авторизован отправлять почту от имени ваших доменов. Если вы используете другой сервис для отправки почты от вашего имени, такие письма, скорее всего, будут отфильтрованы получателями как спам.</p>',
}

for old, new in replacements.items():
    if old not in s:
        print(f"WARN: not found: {old[:120]}")
    s = s.replace(old, new)

p.write_text(s)
print("Changed file: management/templates/mail-guide.html")
