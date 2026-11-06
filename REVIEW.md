# Reviewing NEBULA in about 30 minutes

NEBULA is experimental and **not audited**. This page tells a reviewer where to look first, so you do not have to read
the whole repository. Everything here is checkable: if something below is wrong, please open an issue.

**Heads-up about size.** `nebula_v10_24.py` is a very large single file (about 95,000 lines). Most of it is optional
feature modules ("groups") that I have not audited and that are not part of the checks below. Start with the places
listed here. Line numbers are for this version of the file; search for the function name if they drift.

## 1. Run the checks (5 minutes)

```bash
git clone https://github.com/rahmatullahvibenet-sketch/nebula-blockchain
cd nebula-blockchain
python3 tests/test_genesis_premine_v1025.py     # rebuilds both genesis blocks (hash, PoW, merkle root, premine)
python3 tests/test_lwma_v1025.py                # difficulty algorithm
python3 tools/local_testnet.py --quick          # 4 real nodes over TLS on one machine (about 2 minutes)
```

These run on the `regtest` network on one machine. They do not show that nodes find each other over the internet.

## 2. Read these functions (20 minutes)

| Area | Where (in `nebula_v10_24.py`) | What to check |
|---|---|---|
| Difficulty (LWMA) | `lwma_next_bits` (about line 1268), `bits_to_target`, `target_to_bits` (about 1241) | Weighting, clamps (solvetime in [1, 6T], at most 2x change per block, cap at `MAX_TARGET`), rounding, timestamp games, behaviour right after genesis |
| Genesis and premine | `build_genesis_coinbase` (about 2441), `GENESIS_PREMINE_*` (about 376) | 1,035,000 NBL output in the genesis coinbase; the two genesis hashes in `README.md` |
| Signature checks | `Secp256k1.verify` (about 476), `ECDSA.verify` (about 630) | Low-S rule, range checks on r and s, public key on curve, DER parsing (`sig_from_der`), consistency with and without `coincurve` |
| Block acceptance and reorg | `NEBULABlockchain.add_block` (about 2567), `MAX_FORK_DEPTH` (about 2472) | Fork handling, reorg depth limit, rollback and re-apply of the UTXO set, side-chain storage limits |
| Block reward | `mining_reward` (about 1300) | Halving every 210,000 blocks, 21M cap |

Relevant tests: `tests/test_consensus_core.py`, `tests/test_reorg_policy_v1022.py`, `tests/test_p2sh_v1023.py`,
`tests/test_storage_v1020.py`.

## 3. Questions I would especially like answered

1. Can two honest nodes ever compute different `bits` for the same chain (for example because of integer rounding)?
2. Is there any way to get a block with a high-S or malformed-DER signature accepted?
3. Can a reorg leave the UTXO set in a state that differs from replaying the chain from genesis?
4. Is the timestamp rule strong enough against difficulty manipulation?

## 4. Known problems (so you do not have to rediscover them)

- `tests/test_network_v1024.py` passes 11 of 12 checks. The same failure happens on the original code, before my
  recent network changes.
- Some start-up warnings appear in optional modules (for example a `PeerAddressBook` name error in the network init).
  They have not affected the tests above, but they are not fixed yet.
- No public testnet and no seed nodes yet; P2P tests run on one machine.
- Genesis premine of 1,035,000 NBL (public, in the genesis block).

## 5. How to report

Open a GitHub issue (use a template). For a security problem, please use GitHub's private vulnerability reporting
(Security tab, "Report a vulnerability") instead of a public issue.
