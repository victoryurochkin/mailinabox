#!/bin/bash
# Are we running as root?
if [[ $EUID -ne 0 ]]; then
	echo "Этот скрипт нужно запускать от root. Повторите запуск так:"
	echo
	echo "sudo $0"
	echo
	exit 1
fi

# Check that we are running on Ubuntu 22.04 LTS (or 22.04.xx).
# Pull in the variables defined in /etc/os-release but in a
# namespace to avoid polluting our variables.
source <(cat /etc/os-release | sed s/^/OS_RELEASE_/)
if [ "${OS_RELEASE_ID:-}" != "ubuntu" ] || [ "${OS_RELEASE_VERSION_ID:-}" != "22.04" ]; then
	echo "Mail-in-a-Box поддерживает установку только на Ubuntu 22.04. Сейчас используется:"
	echo
	echo "${OS_RELEASE_ID:-"Неизвестный дистрибутив Linux"} ${OS_RELEASE_VERSION_ID:-}"
	echo
	echo "Невозможно поддержать все варианты окружений, поэтому установка остановлена."
	exit 1
fi

# Check that we have enough memory.
#
# /proc/meminfo reports free memory in kibibytes. Our baseline will be 512 MB,
# which is 500000 kibibytes.
#
# We will display a warning if the memory is below 768 MB which is 750000 kibibytes
#
# Skip the check if we appear to be running inside of Vagrant, because that's really just for testing.
TOTAL_PHYSICAL_MEM=$(head -n 1 /proc/meminfo | awk '{print $2}')
if [ "$TOTAL_PHYSICAL_MEM" -lt 490000 ]; then
if [ ! -d /vagrant ]; then
	TOTAL_PHYSICAL_MEM=$(( TOTAL_PHYSICAL_MEM * 1024 / 1000 / 1000 ))
	echo "Для корректной работы Mail-in-a-Box требуется больше оперативной памяти."
	echo "Выделите сервер минимум с 512 МБ ОЗУ, рекомендуется 1 ГБ или больше."
	echo "На этом сервере обнаружено $TOTAL_PHYSICAL_MEM МБ ОЗУ."
	exit
fi
fi
if [ "$TOTAL_PHYSICAL_MEM" -lt 750000 ]; then
	echo "ПРЕДУПРЕЖДЕНИЕ: на сервере Mail-in-a-Box меньше 768 МБ ОЗУ."
	echo "         При высокой нагрузке система может работать нестабильно."
fi

# Check that tempfs is mounted with exec
MOUNTED_TMP_AS_NO_EXEC=$(grep "/tmp.*noexec" /proc/mounts || /bin/true)
if [ -n "$MOUNTED_TMP_AS_NO_EXEC" ]; then
	echo "Для Mail-in-a-Box каталог /tmp должен быть смонтирован с правом exec. Перемонтируйте /tmp с exec."
	exit
fi

# Check that no .wgetrc exists
if [ -e ~/.wgetrc ]; then
	echo "Mail-in-a-Box ожидает стандартные настройки wget, но найден файл ~/.wgetrc."
	exit
fi

# Check that we are running on x86_64 or i686 architecture, which are the only
# ones we support / test.
ARCHITECTURE=$(uname -m)
if [ "$ARCHITECTURE" != "x86_64" ] && [ "$ARCHITECTURE" != "i686" ]; then
	echo
	echo "ПРЕДУПРЕЖДЕНИЕ:"
	echo "Mail-in-a-Box тестировался только на платформах x86_64 и i686."
	echo "Архитектура $ARCHITECTURE может не поддерживаться."
	echo "Дальнейший запуск выполняется на ваш риск."
	echo
fi
