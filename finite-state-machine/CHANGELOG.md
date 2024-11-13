# Finite State Machine Changelog

## v1.2

- Added constant combinator at one edge as an alternate red-wire connection point and to support constants being added to signals.

## v1.1

- Changed definition of X output to allow it to clear inputs before they can affect the upcoming state.
- Synchronized timing of inputs vs current state (which is why an X "precursor" is essential).
- Re-ordered input circuits to make it cleaner to remove those not used.

## v1.0

- First public release.
