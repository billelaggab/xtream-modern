#!/bin/bash
# Xtream Codes Modern - Clear Logs Script
# Based on xtreamui-things/clearlogs.sh

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Xtream Codes Modern - Log Cleaner${NC}"
echo "====================================="

# Log directories to clean
LOG_DIRS=(
    "/var/log/nginx"
    "/var/log/mysql"
    "/var/log/xtream"
    "/home/xtreamcodes/iptv_xtream_codes/logs"
)

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}This script must be run as root${NC}"
   exit 1
fi

# Function to clear log directory
clear_logs() {
    local dir=$1
    if [[ -d "$dir" ]]; then
        echo -e "Clearing logs in: ${YELLOW}$dir${NC}"
        find "$dir" -type f -name "*.log" -delete
        find "$dir" -type f -name "*.log.*" -delete
        echo -e "${GREEN}Done${NC}"
    else
        echo -e "${YELLOW}Directory not found: $dir${NC}"
    fi
}

# Clear each log directory
for dir in "${LOG_DIRS[@]}"; do
    clear_logs "$dir"
done

# Clear journal logs (systemd)
echo -e "Clearing journal logs older than 7 days..."
journalctl --vacuum-time=7d

echo -e "\n${GREEN}All logs cleared successfully!${NC}"