#!/bin/bash
set -xe

# Create config structure
mkdir -p /config/custom_components

# Symlink integration
ln -sf /workspaces/ha-homeseer/custom_components/homeseer /config/custom_components/homeseer 

# Copy config files
cp /workspaces/ha-homeseer/.devcontainer/config/configuration.yaml /config/configuration.yaml

pip install homeassistant

### Hass run command
alias hass='hass -c /config'

### Enable stopping startup until debugger is started
export HA_DEBUG=True

ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime
echo "America/New_York" > /etc/timezone

# Install git hooks
ln -sf /workspaces/ha-homeseer/.devcontainer/scripts/pre-commit \
       /workspaces/ha-homeseer/.git/hooks/pre-commit
chmod +x /workspaces/ha-homeseer/.devcontainer/scripts/pre-commit
git config --global --add safe.directory /workspaces/ha-homeseer
echo "✓ Git hooks installed"

