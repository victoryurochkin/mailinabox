#!/bin/bash
# Install the 'host', 'sed', and and 'nc' tools. This script is run before
# the rest of the system setup so we may not yet have things installed.
apt_get_quiet install bind9-host sed netcat-openbsd

# Stop if the PRIMARY_HOSTNAME is listed in the Spamhaus Domain Block List.
# The user might have chosen a name that was previously in use by a spammer
# and will not be able to reliably send mail. Do this after any automatic
# choices made above.
if host "$PRIMARY_HOSTNAME.dbl.spamhaus.org" > /dev/null; then
	echo
	echo "Выбранное имя сервера '$PRIMARY_HOSTNAME' находится в"
	echo "Spamhaus Domain Block List. См. http://www.spamhaus.org/dbl/"
	echo "и http://www.spamhaus.org/query/domain/$PRIMARY_HOSTNAME."
	echo
	echo "С этим доменным именем отправка почты будет невозможна, поэтому"
	echo "установка не может быть продолжена."
	echo
	exit 1
fi

# Stop if the IPv4 address is listed in the ZEN Spamhouse Block List.
# The user might have ended up on an IP address that was previously in use
# by a spammer, or the user may be deploying on a residential network. We
# will not be able to reliably send mail in these cases.
REVERSED_IPV4=$(echo "$PUBLIC_IP" | sed "s/\([0-9]*\).\([0-9]*\).\([0-9]*\).\([0-9]*\)/\4.\3.\2.\1/")
if host "$REVERSED_IPV4.zen.spamhaus.org" > /dev/null; then
	echo
	echo "IP-адрес $PUBLIC_IP находится в Spamhaus Block List."
	echo "См. http://www.spamhaus.org/query/ip/$PUBLIC_IP."
	echo
	echo "С этого сервера нельзя будет отправлять почту, поэтому установка"
	echo "не может быть продолжена."
	echo
	echo "Если возможно, назначьте этому серверу другой IP-адрес."
	echo "Многие IP-адреса домашних сетей находятся в блок-листах, поэтому Mail-in-a-Box"
	echo "обычно нельзя использовать на домашнем интернет-подключении."
	echo
	exit 1
fi

# Stop if we cannot make an outbound connection on port 25. Many residential
# networks block outbound port 25 to prevent their network from sending spam.
# See if we can reach one of Google's MTAs with a 5-second timeout.
if ! nc -z -w5 aspmx.l.google.com 25; then
	echo
	echo "Похоже, исходящая почта через порт 25 заблокирована вашей сетью."
	echo
	echo "С этого сервера нельзя будет отправлять почту, поэтому установка"
	echo "не может быть продолжена."
	echo
	echo "Многие домашние сети блокируют порт 25, чтобы заражённые"
	echo "устройства не могли рассылать спам. Была выполнена попытка подключения"
	echo "к почтовому серверу Google на порт 25, но соединение"
	echo "не установилось."
	echo
	exit 1
fi
