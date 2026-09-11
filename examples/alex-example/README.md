# Example workspace: Alex Rivera (fictional)

A filled workspace so you can see the shape and try the differ without real data.

```bash
cd examples/alex-example
python3 ../../scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/cv.txt --label CV
../../scripts/verify_kernel.sh .
```

Expected: the differ reports a FACT difference on Fintra dates (Jan vs Feb 2022), a CHANGED
bullet (4 s vs 4.1 s), and MISSING bullets (design system, SEPA payout flow). `accepted.md`
makes the headline difference silent.
