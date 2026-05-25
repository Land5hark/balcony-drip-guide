# Secrets Vault

> **I SEE THIS BEFORE EVERY SESSION. DO NOT LOSE IT.**

## Vault Location
`/home/linuxlite/.openclaw/workspace/secrets/workspace-secrets.kdbx`

## Vault Master Password
`<REDACTED — memorized by owner and stored in KeePassXC>`

## Tool
KeePassXC (installed: `keepassxc-cli` v2.4.3)

## Entries

### Spiike ProtonMail
- **Entry name:** `Spiike ProtonMail`
- **Username:** `Spiike.ops@proton.me`
- **Password:** `<REDACTED — retrieve from KeePassXC vault>`
- **URL:** `https://mail.proton.me`
- **Notes:** Full service email for Spike. Double-i in username was accidental.

## How to Retrieve a Password
```bash
keepassxc-cli show /home/linuxlite/.openclaw/workspace/secrets/workspace-secrets.kdbx "Spiike ProtonMail"
# Then enter master password when prompted
```

## Created
2026-05-22 by Spike after user directive.
