# NEBULA mainnet launch runbook (v10.24)

Run `python3 tools/launch_preflight.py` - every FAIL line must be cleared before the announcement.

## Code side (done in v10.24)
- mainnet/regtest split, new genesis, P2SH address fix, OrphanPool fix, SIGHASH_ALL-only OP_CHECKSIG,
  loopback bind defaults, random RPC password, TLS required by default.

## Things only you can do (in this order)
1. Choose the launch difficulty from your expected hashrate. If you change it: re-mine the genesis with
   `mine_genesis(bits)` and paste GENESIS_BITS / INITIAL_BITS / MAX_TARGET exponent / nonce / hash.
2. Foundation custody: create 3 keys on 3 DIFFERENT devices (hardware wallets), run
   `python3 tools/make_foundation_multisig.py 2 <pub1> <pub2> <pub3>`, put the address into FOUNDATION_ADDRESS
   AND `_GENESIS_ADDRESS_HARDCODED`, re-mine genesis (the merkle root changes), update the hash constants.
3. `pip install coincurve` on every node.
4a. First run `NEBULA_NETWORK=regtest python3 tools/local_testnet.py` (3 nodes on one machine, ~2-3 min).
4. Run a PUBLIC TESTNET (regtest-style params but real internet, several independent miners) for weeks:
   watch forks, reorgs, memory, restarts, peer bans. Fix what it shows.
5. Start real seed nodes on the seed hostnames (or change SEED_NODES / DNS_SEEDS to hosts you control).
6. Independent security audit (consensus, P2P, wallet, RPC/API). Fix findings. Re-run all tests.
7. After the chain has blocks: add checkpoints (e.g. every 1000 blocks, buried deeper than MAX_FORK_DEPTH).
8. Operators: NEBULA_NETWORK unset (mainnet), NEBULA_P2P_TLS=required, NEBULA_RPC_PASSWORD and NEBULA_API_KEY set,
   NEBULA_BIND left at 127.0.0.1 (use a reverse proxy with TLS for public APIs).

No code change can replace steps 4 and 6.

## v10.25 genesis premine
- Genesis pays 1,035,000 NBL to GENESIS_PREMINE_ADDRESS (see CHANGES_v10_25.txt). Prove the mnemonic restores that
  address BEFORE announcing; after launch the genesis can never change.
- Announce the premine publicly: it is on top of the 21,000,000 NBL mining schedule.
