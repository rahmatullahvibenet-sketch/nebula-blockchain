#!/usr/bin/env bash
# Run a NEBULA node that keeps itself alive (restarts after a crash) and, optionally, opens a public tunnel.
#   bash tools/run_seed.sh                 # node on port 8333 + free tunnel via serveo.net (needs: pkg install openssh)
#   NEBULA_TUNNEL=none bash tools/run_seed.sh    # node only (you have a public IP / port forward)
#   PORT=9000 bash tools/run_seed.sh
# Stop everything with Ctrl+C. Logs: seed_logs/node.log and seed_logs/tunnel.log
cd "$(dirname "$0")/.." || exit 1
PORT="${PORT:-8333}"
TUNNEL="${NEBULA_TUNNEL:-serveo}"
mkdir -p seed_logs
command -v termux-wake-lock >/dev/null 2>&1 && termux-wake-lock    # Termux: keep the phone awake

pids=""
cleanup() { for p in $pids; do pkill -P "$p" 2>/dev/null; kill "$p" 2>/dev/null; done; command -v termux-wake-unlock >/dev/null 2>&1 && termux-wake-unlock; exit 0; }
trap cleanup INT TERM

if [ "$TUNNEL" = "serveo" ]; then
  if ! command -v ssh >/dev/null 2>&1; then echo "ssh not found. In Termux run: pkg install -y openssh"; exit 1; fi
  ( while true; do
      echo "$(date '+%F %T') tunnel starting" >> seed_logs/tunnel.log
      ssh -o LogLevel=VERBOSE -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes \
          -o StrictHostKeyChecking=accept-new -N -R "$PORT:localhost:$PORT" serveo.net >> seed_logs/tunnel.log 2>&1
      echo "$(date '+%F %T') tunnel ended, retrying in 15 s" >> seed_logs/tunnel.log
      sleep 15
    done ) &
  pids="$pids $!"
  echo "Tunnel: your public address should be  serveo.net:$PORT  (check: tail seed_logs/tunnel.log)"
fi

echo "Node: starting on port $PORT (it restarts automatically if it stops). Ctrl+C to stop."
( while true; do
    echo "$(date '+%F %T') node starting" >> seed_logs/node.log
    python3 nebula_v10_24.py node --port "$PORT" < /dev/null >> seed_logs/node.log 2>&1
    echo "$(date '+%F %T') node stopped, restarting in 5 s" >> seed_logs/node.log
    sleep 5
  done ) &
pids="$pids $!"

# Simple status line every minute
while true; do
  sleep 60 & wait $!
  echo "$(date '+%H:%M') running | node log: $(grep -c 'New block' seed_logs/node.log 2>/dev/null) blocks seen | $(tail -n1 seed_logs/node.log | cut -c1-70)"
done
