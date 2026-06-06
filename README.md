# Python Exercises

مجموعه‌ای از مسائل الگوریتمی از سطح مبتدی تا پیشرفته — همراه با پیاده‌سازی راه‌حل در پایتون.

A collection of algorithm exercises from beginner to advanced, with Python solutions.

**Browse online:** [amirmahdikahdouii.github.io/Python-Exercises](https://amirmahdikahdouii.github.io/Python-Exercises/)

## Repository structure

```
Python-Exercises/
├── catalog/problems.yaml    # metadata: category, difficulty, tags
├── problems/
│   ├── 001-count-n-digit-primes/
│   │   ├── README.md        # problem statement (Persian)
│   │   └── solution.py
│   └── ...
├── scripts/
│   ├── migrate.py
│   └── generate_hugo_content.py
└── .github/workflows/deploy-website.yml
```

Each problem lives in `problems/NNN-slug/` where `NNN` is the original question number (Q-1 → 001).

## How to practice

1. Clone this repository.
2. Browse problems on the [website](https://amirmahdikahdouii.github.io/Python-Exercises/) or in [`catalog/problems.yaml`](catalog/problems.yaml).
3. Open a problem's `README.md` and implement your own solution.
4. Compare with `solution.py` (or `solution.go` for problem #85).

## Categories

Problems are tagged by topic and difficulty in `catalog/problems.yaml`:

| Category | Examples |
|----------|----------|
| math | primes, divisors, palindromes |
| strings | ciphers, digit manipulation |
| arrays | statistics, merging, filtering |
| search | binary search variants |
| sorting | bubble sort, bead sort |
| dp | knapsack, fibonacci |
| greedy | stock profit, book buying |
| crypto | Caesar cipher, OTP |
| simulation | elevator, games |
| combinatorics | subsets, combinations |
| data-structures | sets, frequency maps |
| graphs | parity, grid problems |
| io | Go reader exercise (#85) |

## Website

The Hugo site (PaperMod theme) lives on the [`website`](https://github.com/Amirmahdikahdouii/Python-Exercises/tree/website) branch. Pushing to `master` or `website` triggers automatic deployment to GitHub Pages.

## Contributing

To add a new problem:

1. Create `problems/NNN-your-slug/` with `README.md` and `solution.py`.
2. Add an entry to `catalog/problems.yaml`.
3. Push to `master` — the site rebuilds automatically.

## Contact

Questions or collaboration: [Telegram](https://t.me/Amir_mahdi_kahdouii)
