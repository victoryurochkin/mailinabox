#!/usr/bin/env bash
set -Eeuo pipefail

OUT="/root/mailinabox-russian-localization-audit-$(date +%F_%H-%M-%S).txt"

{
  echo "Mail-in-a-Box Russian localization audit"
  echo "Generated: $(date)"
  echo "Repo: $(pwd)"
  echo

  echo "=== Git ==="
  git status --short
  git log --oneline --decorate -5
  echo

  echo "=== Candidate user-facing files ==="
  find \
    setup \
    management \
    conf \
    tools \
    tests \
    api \
    . \
    -path ./.git -prune -o \
    -type f \
    \( \
      -name "*.sh" -o \
      -name "*.py" -o \
      -name "*.html" -o \
      -name "*.md" -o \
      -name "*.txt" -o \
      -name "*.yml" -o \
      -name "*.xml" -o \
      -name "*.conf" \
    \) \
    -print | sort
  echo

  echo "=== Setup visible strings: echo / read / printf ==="
  grep -RInE '^[[:space:]]*(echo|read|printf)|hide_output|input_box|message_box|confirm_box|echo_box' setup \
    --exclude-dir=.git || true
  echo

  echo "=== Management UI templates visible text ==="
  grep -RInE '<title>|<h[1-6]|<p>|<label|<button|placeholder=|value=|aria-label=|alt=|title=' management/templates \
    --exclude-dir=.git || true
  echo

  echo "=== Management Python user-facing strings ==="
  grep -RInE 'raise ValueError|return "|return '\''|print\(|json_response|status|message|description|Exception|RuntimeError' management \
    --include='*.py' \
    --exclude-dir=.git || true
  echo

  echo "=== Mail/config/profile visible text ==="
  grep -RInE 'Mail-in-a-Box|email|mail|calendar|contacts|setup|configure|configuration|administrator|password|login|user|domain|backup|restore|status|security|DNS|SSL|TLS|SMTP|IMAP|Nextcloud|Roundcube' \
    conf api tools README.md CHANGELOG.md security.md \
    --exclude-dir=.git || true
  echo

  echo "=== Hardcoded English words in likely user-facing files ==="
  grep -RInE '\b(Welcome|Installing|Upgrading|Setting up|Checking|Error|ERROR|Warning|WARNING|Success|Done|Please|Enter|Choose|Select|Configure|Configuration|Status|Backup|Restore|Login|Password|Email|Mail|Contacts|Calendar|User|Users|Domain|Domains|DNS|SSL|Certificate|Certificates|Security|System|Admin|Administrator|Management|Control Panel)\b' \
    setup management conf tools api README.md security.md \
    --exclude-dir=.git || true

} | tee "$OUT"

echo
echo "Audit saved to: $OUT"
