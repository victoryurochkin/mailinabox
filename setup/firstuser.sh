#!/bin/bash
# If there aren't any mail users yet, create one.
if [ -z "$(management/cli.py user)" ]; then
	# The output of "management/cli.py user" is a list of mail users. If there
	# aren't any yet, it'll be empty.

	# If we didn't ask for an email address at the start, do so now.
	if [ -z "${EMAIL_ADDR:-}" ]; then
		# In an interactive shell, ask the user for an email address.
		if [ -z "${NONINTERACTIVE:-}" ]; then
			input_box "Почтовый аккаунт" \
				"Let's create your first mail account.
				\n\nWhat email address do you want?" \
				"me@$(get_default_hostname)" \
				EMAIL_ADDR

			if [ -z "$EMAIL_ADDR" ]; then
				# user hit ESC/cancel
				exit
			fi
			while ! management/mailconfig.py validate-email "$EMAIL_ADDR"
			do
				input_box "Почтовый аккаунт" \
					"That's not a valid email address.
					\n\nWhat email address do you want?" \
					"$EMAIL_ADDR" \
					EMAIL_ADDR
				if [ -z "$EMAIL_ADDR" ]; then
					# user hit ESC/cancel
					exit
				fi
			done

		# But in a non-interactive shell, just make something up.
		# This is normally for testing.
		else
			# Use me@PRIMARY_HOSTNAME
			EMAIL_ADDR=me@$PRIMARY_HOSTNAME
			EMAIL_PW=12345678
			echo
			echo "Создание нового административного почтового аккаунта $EMAIL_ADDR с паролем $EMAIL_PW."
			echo
		fi
	else
		echo
		echo "Хорошо. Сейчас будет настроен аккаунт $EMAIL_ADDR. Этот аккаунт также"
		echo "получит доступ к панели управления сервера."
	fi

	# Create the user's mail account. This will ask for a password if none was given above.
	management/cli.py user add "$EMAIL_ADDR" ${EMAIL_PW:+"$EMAIL_PW"}

	# Make it an admin.
	hide_output management/cli.py user make-admin "$EMAIL_ADDR"

	# Create an alias to which we'll direct all automatically-created administrative aliases.
	management/cli.py alias add "administrator@$PRIMARY_HOSTNAME" "$EMAIL_ADDR" > /dev/null
fi
