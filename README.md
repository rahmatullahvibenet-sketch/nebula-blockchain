# NEBULA (NBL)

NEBULA is an experimental, Bitcoin-style proof-of-work blockchain written in Python (with an optional C accelerator for
hashing). It has a fixed supply schedule, UTXO accounting, P2PKH / P2SH / multisig scripts, BIP39/BIP32/BIP44 HD wallets
and an encrypted (TLS) peer-to-peer layer.

> **Status: pre-launch, experimental software. It has NOT had an independent security audit.**
> Do not put money you cannot afford to lose into anything built on this code. Nothing here is investment advice and
> nobody promises that NBL will ever have a market value.

## Try it in 3 minutes

```bash
git clone https://github.com/rahmatullahvibenet-sketch/nebula-blockchain
cd nebula-blockchain
python3 tests/test_genesis_premine_v1025.py     # rebuilds both genesis blocks, checks hash / PoW / premine
python3 tests/test_lwma_v1025.py                # difficulty algorithm checks
python3 tools/local_testnet.py --quick          # 4 real nodes over TLS on YOUR machine: mining, a signed payment,
                                                # a late joiner syncing from scratch, a fork and a re-org

```

**What this proves, and what it does not.** These runs use the `regtest` network on one machine (127.0.0.1). They show
that the consensus code, the P2P layer and chain reorganisation work. They do **not** show that nodes on different
networks find each other over the internet: there is no public testnet and no seed node yet.

**Where a review would help most:** the LWMA difficulty code, genesis/premine handling, signature validation
(low-S, DER parsing), and the reorg policy. If you find a flaw, please open an issue (or message privately for security)

**New here? Start with [REVIEW.md](REVIEW.md): a 30-minute guide to the files and functions worth reading.**

## Key parameters

| Item | Value |
|---|---|
| Ticker / decimals | NBL / 9 |
| Consensus | Proof of work, double SHA-256 |
| Target block time | 10 minutes |
| Difficulty adjustment | per-block LWMA (60-block window, max 2x change per block); easiest allowed difficulty is 2^20 hashes/block, launch difficulty is 2^28 |
| Block reward | 50 NBL, halving every 210,000 blocks |
| Mining supply | 21,000,000 NBL (`MAX_SUPPLY`) |
| Coinbase maturity | 100 blocks |
| Miner share of the block reward | **100%** (no foundation or developer cut) |
| Address derivation | BIP44 path `m/44'/2025'/0'/0/n` |
| Default P2P port | 8333 |
| Networks | `mainnet` (default) and `regtest` (test network with trivial difficulty) |

## Run a node and connect to others

```bash
python3 nebula_v10_24.py node --port 8333                          # start a node
python3 nebula_v10_24.py node --peers 203.0.113.10:8333             # connect to a node you know (comma-separated list)
python3 nebula_v10_24.py node --mine --addr <YOUR_ADDRESS> --peers HOST:PORT
```

Inside a running node, `connect HOST:PORT` dials another node and `peers` lists the connected ones.
At start-up a node also downloads `seeds.txt` from this repository (set `NEBULA_SEEDS_URL=off` to disable it).

**There are no public seed nodes yet**, so right now nodes only find each other if you give them an address. Most home
connections cannot accept inbound connections (NAT), so a connection needs one side with a public IP (or a port forward / tunnel).
**If you have a public IP or a VPS and can keep a node running, please open an issue with your `host:port`** and it will be
added to `seeds.txt`.
## Genesis block and premine (public and verifiable)

The genesis coinbase transaction has two outputs:

1. 50 NBL genesis reward to the genesis address `NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx`.
2. **A premine of 1,035,000 NBL** to `NYeuFNDnykFEhKWQnCCPeyFQFEKX2qs1oh`.

The premine is on top of the 21,000,000 NBL mining schedule (about 4.9% of it); total ever created is therefore
22,035,000 NBL. It is part of the genesis block itself, so every node verifies it and any explorer will show it.
Like every coinbase output it can only be spent after 100 blocks.

Genesis message: *"NEBULA — Financial Freedom for All Humanity — No Government. No Bank. No Permission. — 2025/03/16"*

| Network | Genesis hash |
|---|---|
| mainnet | `0000000176dc3448fe722a3c91994bcc144901aa72785f377c44ee43166ba5f1` |
| regtest | `00000c766872ca090644312f2fefc4453664c59ff89181af204d36a7323313dd` |

Anyone can check these: `python3 tests/test_genesis_premine_v1025.py` rebuilds both genesis blocks from the code and
verifies hash, proof of work, merkle root and the premine output.

## Requirements

* Python 3.10+ (developed and tested with 3.13)
* Optional, recommended: `pip install coincurve` (fast secp256k1; otherwise a slow pure-Python fallback is used)
* Optional: `gcc` (a C hashing/mining accelerator is compiled automatically when available)

## Running

```bash
python3 nebula_v10_24.py --help
```

Useful options: `--mine`, `--addr <reward address>`, `--datadir`, `--port`, `--api-port`, `--threads`.
The network is chosen with the environment variable `NEBULA_NETWORK` (`mainnet` by default, or `regtest`).

Safe defaults: HTTP API and explorers listen on `127.0.0.1` only (set `NEBULA_BIND` to expose them); the RPC password is
random unless `NEBULA_RPC_PASSWORD` is set; `NEBULA_API_KEY` is generated if not set.

## Testing on your own machine (test network)

```bash
export NEBULA_NETWORK=regtest
python3 tools/mine_to_address.py <YOUR_ADDRESS> 101   # mine test blocks (worthless test coins) to your address
python3 tools/send_test.py --check-only               # check that your 12 words give the expected address
python3 tests/test_genesis_premine_v1025.py           # genesis / premine checks
python3 tests/test_lwma_v1025.py                      # difficulty algorithm checks
python3 tools/local_testnet.py                        # 3 real nodes, a late joiner, a fork and a re-org
```

The test suites live in `tests/` (consensus, reorg policy, P2SH, storage, wiring, P2P with TLS, genesis/premine).

## Wallet safety

* Your 12-word recovery phrase is the only copy of your keys. Write it on paper, keep two copies in different places.
* Never type it into a chat, an email, a website, a screenshot or a file, and never commit it to a repository.
* Never commit anything from `nebula_data/` (it contains node TLS keys). `.gitignore` already excludes it.

## Known limitations

See `LAUNCH_RUNBOOK.md` and `CHANGES_v10_2x.txt`. In short: no public testnet yet, no checkpoints yet, seed nodes are not
running yet, no external audit, and P2SH spending from the wallet UI has not been tested end to end.

## Contributing

Bug reports and security findings are welcome. Please report suspected vulnerabilities privately to the maintainer
before opening a public issue.

## License

MIT, see `LICENSE`.
