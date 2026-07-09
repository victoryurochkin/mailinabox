#!/usr/bin/env python3
from pathlib import Path

REPLACEMENTS = {
    "management/templates/ssl.html": {
        "<h2>TLS (SSL) Certificates</h2>": "<h2>TLS (SSL) сертификаты</h2>",

        "<p>A TLS (formerly called SSL) certificate is a cryptographic file that proves to anyone connecting to a web address that the connection is secure between you and the owner of that address.</p>":
        "<p>TLS-сертификат, ранее называвшийся SSL-сертификатом, — это криптографический файл, который подтверждает пользователю, подключающемуся к веб-адресу, что соединение защищено между ним и владельцем этого адреса.</p>",

        "<p>You need a TLS certificate for this box&rsquo;s hostname ({{hostname}}) and every other domain name and subdomain that this box is hosting a website for (see the list below).</p>":
        "<p>TLS-сертификат нужен для hostname этого сервера ({{hostname}}), а также для каждого домена и поддомена, для которого этот сервер размещает сайт. Список приведён ниже.</p>",

        "<h3>Provision certificates</h3>": "<h3>Выпустить сертификаты</h3>",
        ">Provision<": ">Выпустить<",

        '<p>A TLS certificate can be automatically provisioned from <a href="https://letsencrypt.org/" target="_blank">Let&rsquo;s Encrypt</a>, a free TLS certificate provider, for:<br>':
        '<p>TLS-сертификат можно автоматически выпустить через <a href="https://letsencrypt.org/" target="_blank">Let&rsquo;s Encrypt</a>, бесплатного поставщика TLS-сертификатов, для:<br>',

        "<h3>Certificate status</h3>": "<h3>Состояние сертификатов</h3>",

        '<p style="margin-top: 1.5em">Certificates expire after a period of time. All certificates will be automatically renewed through <a href="https://letsencrypt.org/" target="_blank">Let&rsquo;s Encrypt</a> 14 days prior to expiration.</p>':
        '<p style="margin-top: 1.5em">Сертификаты имеют срок действия. Все сертификаты будут автоматически продлеваться через <a href="https://letsencrypt.org/" target="_blank">Let&rsquo;s Encrypt</a> за 14 дней до истечения срока.</p>',

        "<th scope=\"col\">Domain</th>": "<th scope=\"col\">Домен</th>",
        "<th scope=\"col\">Certificate Status</th>": "<th scope=\"col\">Состояние сертификата</th>",
        "<th scope=\"col\">Actions</th>": "<th scope=\"col\">Действия</th>",

        '<h3 id="ssl_install_header">Install certificate</h3>': '<h3 id="ssl_install_header">Установить сертификат</h3>',

        "<p>If you don't want to use our automatic Let's Encrypt integration, you can give any other certificate provider a try. You can generate the needed CSR below.</p>":
        "<p>Если вы не хотите использовать автоматическую интеграцию с Let&rsquo;s Encrypt, можно использовать другого поставщика сертификатов. Ниже можно сгенерировать необходимый CSR.</p>",

        "<p>Which domain are you getting a certificate for?</p>":
        "<p>Для какого домена вы получаете сертификат?</p>",

        "<p>(A multi-domain or wildcard certificate will be automatically applied to any domains it is valid for besides the one you choose above.)</p>":
        "<p>Мультидоменный или wildcard-сертификат будет автоматически применён ко всем доменам, для которых он действителен, помимо выбранного выше.</p>",

        "<p>What country are you in? This is required by some TLS certificate providers. You may leave this blank if you know your TLS certificate provider doesn't require it.</p>":
        "<p>В какой стране вы находитесь? Некоторые поставщики TLS-сертификатов требуют это поле. Можно оставить пустым, если ваш поставщик сертификатов его не требует.</p>",

        "<p>You will need to provide the certificate provider this Certificate Signing Request (CSR):</p>":
        "<p>Передайте поставщику сертификата этот Certificate Signing Request (CSR):</p>",

        "<p><small>The CSR is safe to share. It can only be used in combination with a secret key stored on this machine.</small></p>":
        "<p><small>CSR безопасно передавать поставщику. Он может использоваться только вместе с секретным ключом, который хранится на этом сервере.</small></p>",

        "<p>The certificate provider will then provide you with a TLS/SSL certificate. They may also provide you with an intermediate chain. Paste each separately into the boxes below:</p>":
        "<p>После этого поставщик выдаст TLS/SSL-сертификат. Также он может выдать промежуточную цепочку сертификатов. Вставьте каждый блок отдельно в поля ниже:</p>",

        '<p style="margin-bottom: .5em">TLS/SSL certificate:</p>':
        '<p style="margin-bottom: .5em">TLS/SSL-сертификат:</p>',

        '<p style="margin-bottom: .5em">TLS/SSL intermediate chain (if provided):</p>':
        '<p style="margin-bottom: .5em">Промежуточная цепочка TLS/SSL, если предоставлена:</p>',

        "<p>After you paste in the information, click the install button.</p>":
        "<p>После вставки данных нажмите кнопку установки.</p>",

        ">Install<": ">Установить<",

        "Install Certificate": "Установить сертификат",
        "Replace Certificate": "Заменить сертификат",

        'show_modal_error("TLS Certificate Installation", "Certificate has been installed. Check that you have no connection problems to the domain.", function() { show_ssl(); $(\'#csr_info\').slideUp(); });':
        'show_modal_error("Установка TLS-сертификата", "Сертификат установлен. Проверьте, что подключение к домену работает без проблем.", function() { show_ssl(); $(\'#csr_info\').slideUp(); });',

        'show_modal_error("TLS Certificate Installation", status);':
        'show_modal_error("Установка TLS-сертификата", status);',

        'show_modal_error("TLS Certificate Provisioning", "There were no domain names to provision certificates for.");':
        'show_modal_error("Выпуск TLS-сертификата", "Нет доменных имён, для которых можно выпустить сертификаты.");',
    },

    "management/templates/mfa.html": {
        "<h2>Two-Factor Authentication</h2>": "<h2>Двухфакторная аутентификация</h2>",

        "When two-factor authentication is enabled, you will be prompted to enter a six digit code from an":
        "Когда двухфакторная аутентификация включена, при входе потребуется вводить шестизначный код из",

        "Enabling two-factor authentication does not protect access to your email":
        "Включение двухфакторной аутентификации не защищает доступ к вашей почте",

        "Enabling two-factor authentication on this page only limits access to this control panel. Remember that most websites allow you to":
        "Включение двухфакторной аутентификации на этой странице ограничивает только доступ к панели управления. Помните, что большинство сайтов позволяют",

        "<h3>Setup Instructions</h3>": "<h3>Инструкция по настройке</h3>",

        '<p>1. Install <a href="https://freeotp.github.io/">FreeOTP</a> or <a href="https://www.pcworld.com/article/3225913/what-is-two-factor-authentication-and-which-2fa-apps-are-best.html">any':
        '<p>1. Установите <a href="https://freeotp.github.io/">FreeOTP</a> или <a href="https://www.pcworld.com/article/3225913/what-is-two-factor-authentication-and-which-2fa-apps-are-best.html">любое',

        "other two-factor authentication app</a> that supports TOTP.</p>":
        "другое приложение двухфакторной аутентификации</a> с поддержкой TOTP.</p>",

        '<p style="margin-bottom: 0">2. Scan the QR code in the app or directly enter the secret into the app:</p>':
        '<p style="margin-bottom: 0">2. Отсканируйте QR-код в приложении или вручную введите секретный ключ:</p>',

        '<label for="totp-setup-label" style="font-weight: normal">3. Optionally, give your device a label so that you can remember what device you set it up on:</label>':
        '<label for="totp-setup-label" style="font-weight: normal">3. При желании задайте метку устройства, чтобы помнить, где настроена двухфакторная аутентификация:</label>',

        'placeholder="my phone"': 'placeholder="мой телефон"',

        '<label for="totp-setup-token" style="font-weight: normal">4. Use the app to generate your first six-digit code and enter it here:</label>':
        '<label for="totp-setup-token" style="font-weight: normal">4. Сгенерируйте первый шестизначный код в приложении и введите его здесь:</label>',

        'placeholder="6-digit code"': 'placeholder="6-значный код"',

        "When you click Enable Two-Factor Authentication, you will be logged out of the control panel and will have to log in":
        "После нажатия «Включить двухфакторную аутентификацию» сеанс в панели управления будет завершён, и потребуется войти",

        "again, now using your two-factor authentication app.</p>":
        "снова, уже с использованием приложения двухфакторной аутентификации.</p>",

        ">Enable Two-Factor Authentication<": ">Включить двухфакторную аутентификацию<",

        "Two-factor authentication is active for your account<span id=\"mfa-device-label\"></span>.":
        "Двухфакторная аутентификация активна для вашей учётной записи<span id=\"mfa-device-label\"></span>.",

        "You will have to log into the admin panel again after disabling two-factor authentication.":
        "После отключения двухфакторной аутентификации потребуется снова войти в панель управления.",

        ">Disable Two-Factor Authentication<": ">Отключить двухфакторную аутентификацию<",

        'img.alt = "QR code, scan this in your authenticator app"':
        'img.alt = "QR-код, отсканируйте его в приложении аутентификации"',

        'code.innerHTML = `Secret: ${provisioned_totp.secret}`;':
        'code.innerHTML = `Секретный ключ: ${provisioned_totp.secret}`;',
    },
}

changed = []

for rel, mapping in REPLACEMENTS.items():
    p = Path(rel)
    s = p.read_text()
    original = s

    for old, new in mapping.items():
        if old not in s:
            print(f"WARN: not found in {rel}: {old[:100]}")
            continue
        s = s.replace(old, new)

    if s != original:
        p.write_text(s)
        changed.append(rel)

print("Changed files:")
for f in changed:
    print(f"  {f}")
