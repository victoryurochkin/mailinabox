#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "management/templates/custom-dns.html": {
        "<h2>Custom DNS</h2>": "<h2>Пользовательские DNS-записи</h2>",
        "<p>It is possible to set custom DNS records on domains hosted here.</p>": "<p>Для доменов, размещённых на этом сервере, можно задавать пользовательские DNS-записи.</p>",
        "<h3>Set custom DNS records</h3>": "<h3>Настроить пользовательские DNS-записи</h3>",
        "<p>You can set additional DNS records, such as if you have a website running on another server, to add DKIM records for external mail providers, or for various confirmation-of-ownership tests.</p>": "<p>Можно добавить дополнительные DNS-записи: например, для сайта на другом сервере, DKIM-записи внешних почтовых провайдеров или проверок владения доменом.</p>",

        '<label for="customdnsQname" class="col-sm-1 control-label">Name</label>': '<label for="customdnsQname" class="col-sm-1 control-label">Имя</label>',
        'id="customdnsQname" placeholder="subdomain"': 'id="customdnsQname" placeholder="поддомен"',
        '<label for="customdnsType" class="col-sm-1 control-label">Type</label>': '<label for="customdnsType" class="col-sm-1 control-label">Тип</label>',
        '<label for="customdnsValue" class="col-sm-1 control-label">Value</label>': '<label for="customdnsValue" class="col-sm-1 control-label">Значение</label>',
        '<button type="submit" class="btn btn-primary">Set Record</button>': '<button type="submit" class="btn btn-primary">Сохранить запись</button>',
        'aria-label="Actions"': 'aria-label="Действия"',

        'data-hint="Enter an IPv4 address (i.e. a dotted quad, such as 123.456.789.012).  The \'local\' alias sets the record to this box\'s public IPv4 address."': 'data-hint="Введите IPv4-адрес, например 123.456.789.012. Алиас \'local\' установит запись в публичный IPv4-адрес этого сервера."',
        'data-hint="Enter an IPv6 address.  The \'local\' alias sets the record to this box\'s public IPv6 address."': 'data-hint="Введите IPv6-адрес. Алиас \'local\' установит запись в публичный IPv6-адрес этого сервера."',
        'data-hint="Enter a CA that can issue certificates for this domain in the form of FLAG TAG VALUE. (0 issuewild &quot;letsencrypt.org&quot;)"': 'data-hint="Введите центр сертификации, которому разрешено выпускать сертификаты для этого домена, в формате FLAG TAG VALUE. Например: 0 issuewild &quot;letsencrypt.org&quot;."',
        'data-hint="Enter another domain name followed by a period at the end (e.g. mypage.github.io.)."': 'data-hint="Введите другое доменное имя с точкой в конце, например mypage.github.io."',
        'data-hint="Enter arbitrary text."': 'data-hint="Введите произвольный текст."',
        'data-hint="Enter record in the form of PRIORITY DOMAIN., including trailing period (e.g. 20 mx.example.com.)."': 'data-hint="Введите запись в формате PRIORITY DOMAIN. с точкой в конце, например 20 mx.example.com."',
        'data-hint="Enter record in the form of PRIORITY WEIGHT PORT TARGET., including trailing period (e.g. 10 10 5060 sip.example.com.)."': 'data-hint="Введите запись в формате PRIORITY WEIGHT PORT TARGET. с точкой в конце, например 10 10 5060 sip.example.com."',
        'data-hint="Enter record in the form of ALGORITHM TYPE FINGERPRINT."': 'data-hint="Введите запись в формате ALGORITHM TYPE FINGERPRINT."',
        'data-hint="Enter a hostname to which this subdomain should be delegated to"': 'data-hint="Введите hostname, которому нужно делегировать этот поддомен."',

        "A (IPv4 address)": "A (IPv4-адрес)",
        "AAAA (IPv6 address)": "AAAA (IPv6-адрес)",
        "CAA (Certificate Authority Authorization)": "CAA (авторизация центров сертификации)",
        "CNAME (DNS forwarding)": "CNAME (DNS-перенаправление)",
        "TXT (text record)": "TXT (текстовая запись)",
        "MX (mail exchanger)": "MX (почтовый обменник)",
        "SRV (service record)": "SRV (служебная запись)",
        "SSHFP (SSH fingerprint record)": "SSHFP (отпечаток SSH)",
        "NS (DNS subdomain delegation)": "NS (делегирование DNS-поддомена)",

        "<h3>Using a secondary nameserver</h3>": "<h3>Использование вторичного DNS-сервера</h3>",
        "<p>If your TLD requires you to have two separate nameservers, you can either set up <a href=\"#external_dns\">external DNS</a> and ignore the DNS server on this box entirely, or use the DNS server on this box but add a secondary (aka &ldquo;slave&rdquo;) nameserver.</p>": "<p>Если доменная зона требует два отдельных DNS-сервера, можно либо настроить <a href=\"#external_dns\">внешний DNS</a> и полностью игнорировать DNS-сервер этого Mail-in-a-Box, либо использовать DNS-сервер на этом сервере и добавить вторичный DNS-сервер.</p>",
        "<p>If you choose to use a secondary nameserver, you must find a secondary nameserver service provider. Your domain name registrar or virtual cloud provider may provide this service for you. Once you set up the secondary nameserver service, enter the hostname (not the IP address) of <em>their</em> secondary nameserver in the box below.</p>": "<p>Если вы используете вторичный DNS-сервер, нужно выбрать провайдера такой услуги. Её может предоставлять регистратор домена или облачный провайдер. После настройки укажите ниже hostname вторичного DNS-сервера провайдера, а не его IP-адрес.</p>",
        '<label for="secondarydnsHostname" class="col-sm-1 control-label">Hostname</label>': '<label for="secondarydnsHostname" class="col-sm-1 control-label">Hostname</label>',
        '<button type="submit" class="btn btn-primary">Update</button>': '<button type="submit" class="btn btn-primary">Обновить</button>',
        "Clear the input field above and click Update to use this machine itself as secondary DNS, which is the default/normal setup.": "Очистите поле выше и нажмите «Обновить», чтобы использовать сам этот сервер как вторичный DNS. Это стандартная настройка по умолчанию.",

        "<h3>Custom DNS API</h3>": "<h3>API пользовательских DNS-записей</h3>",
        "<p>Use your box&rsquo;s DNS API to set custom DNS records on domains hosted here. For instance, you can create your own dynamic DNS service.</p>": "<p>Используйте DNS API этого сервера для настройки пользовательских DNS-записей доменов, размещённых здесь. Например, так можно создать собственный сервис динамического DNS.</p>",
        "<p>Usage:</p>": "<p>Использование:</p>",
        "<p>(Brackets denote an optional argument.)</p>": "<p>Квадратные скобки обозначают необязательный аргумент.</p>",
        "<h4>Verbs</h4>": "<h4>Команды</h4>",
        '<th scope="col"> Verb</th> <th scope="col"> Usage</th>': '<th scope="col"> Метод</th> <th scope="col"> Использование</th>',
        "<h4>Parameters</h4>": "<h4>Параметры</h4>",
        '<th scope="col"> Parameter </th> <th scope="col"> Value </th>': '<th scope="col"> Параметр </th> <th scope="col"> Значение </th>',
        "<p>Strict <a href=\"http://tools.ietf.org/html/rfc4408\">SPF</a> and <a href=\"https://datatracker.ietf.org/doc/draft-kucherawy-dmarc-base/?include_text=1\">DMARC</a> records will be added to all custom domains unless you override them.</p>": "<p>Строгие записи <a href=\"http://tools.ietf.org/html/rfc4408\">SPF</a> и <a href=\"https://datatracker.ietf.org/doc/draft-kucherawy-dmarc-base/?include_text=1\">DMARC</a> будут добавлены ко всем пользовательским доменам, если вы не переопределите их вручную.</p>",
        "<h4>Examples:</h4>": "<h4>Примеры:</h4>",
        "Try these examples. For simplicity the examples omit the <code>--user me@mydomain.com:yourpassword</code> command line argument which you must fill in with your email address and password.": "Попробуйте эти примеры. Для простоты в них не указан аргумент <code>--user me@mydomain.com:yourpassword</code>; его нужно заполнить вашим email-адресом и паролем.",

        'show_modal_error("Secondary DNS", $("<pre/>").text(data));': 'show_modal_error("Вторичный DNS", $("<pre/>").text(data));',
        'show_modal_error("Secondary DNS", $("<pre/>").text(err));': 'show_modal_error("Вторичный DNS", $("<pre/>").text(err));',
        'show_modal_error("Custom DNS", $("<pre/>").text(data));': 'show_modal_error("Пользовательские DNS-записи", $("<pre/>").text(data));',
        'show_modal_error("Custom DNS (Error)", $("<pre/>").text(err));': 'show_modal_error("Пользовательские DNS-записи — ошибка", $("<pre/>").text(err));',
    },

    "management/templates/external-dns.html": {
        "<h2>External DNS</h2>": "<h2>Внешний DNS</h2>",
        "<p>Although your box is configured to serve its own DNS, it is possible to host your DNS elsewhere &mdash; such as in the DNS control panel provided by your domain name registrar or virtual cloud provider &mdash; by copying the DNS zone information shown in the table below into your external DNS server&rsquo;s control panel.</p>": "<p>Хотя этот сервер настроен для самостоятельного обслуживания DNS, DNS можно разместить в другом месте — например, в панели DNS регистратора домена или облачного провайдера. Для этого скопируйте информацию DNS-зоны из таблицы ниже во внешнюю DNS-панель.</p>",
        "<p>If you do so, you are responsible for keeping your DNS entries up to date! If you previously enabled DNSSEC on your domain name by setting a DS record at your registrar, you will likely have to turn it off before changing nameservers.</p>": "<p>В этом случае вы самостоятельно отвечаете за актуальность DNS-записей. Если ранее для домена был включён DNSSEC через DS-запись у регистратора, скорее всего, его нужно отключить перед сменой nameserver-ов.</p>",
        "<h3>Download zonefile</h3>": "<h3>Скачать zonefile</h3>",
        "<p>You can download your zonefiles here or use the table of records below.</p>": "<p>Здесь можно скачать zonefile или использовать таблицу записей ниже.</p>",
        '<label for="downloadZonefile" class="control-label sr-only">Zone</label>': '<label for="downloadZonefile" class="control-label sr-only">Зона</label>',
        '<button type="submit" class="btn btn-primary">Download</button>': '<button type="submit" class="btn btn-primary">Скачать</button>',
        "<h3>Records</h3>": "<h3>Записи</h3>",
        'show_modal_error("Download Zonefile", $("<pre/>").text(data));': 'show_modal_error("Скачать zonefile", $("<pre/>").text(data));',
        'show_modal_error("Download Zonefile (Error)", $("<pre/>").text(err));': 'show_modal_error("Скачать zonefile — ошибка", $("<pre/>").text(err));',
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
