# Introduction

A [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) ("FSM") is a standard mechanism for implementing complex behavior.

"It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can
change from one state to another in response to some inputs; the change from one state to another is called a
transition."

The FSM implemented here has up to 9 unique states (plus a "reset" state) and can be controlled by up to 23 different inputs. It even has status lights and some basic error checking.

_Why use an external general-purpose FSM instead of just implementing it yourself with more basic logic?_ Because it turns out that designing circuits to manage state is surprisingly complex with exacting timing requirements and plenty of "gotcha" edge cases. Factorio does not make it easy to change circuits or even move existing combinators whereas adjustments to the FSM require only changes to constants in combinators and comparators.

For help, [join the Discord channel](https://discord.gg/yBDwZPY2CH).

## Control

The FSM interface is handled completely by a red wire to the central substation, optionally via an empty constant-combinator on one side. Both inputs and outputs share this wire.

### Outputs

- **0-9**: Set to "1" when the corresponding state is active.
- **X**: Flag indicating if the state is continuing (1=continuing, 0=changing).
- **Y**: The number of ticks the current state has been active.
- **Z**: The binary-encoded state number (state "0" is 1, state "1" is 2, state "2" is 4, etc.).

With these, it's easy to define actions based on being in a particular state just by checking the value of "Z" or by multiplying other values by the "0" through "9" signals. It's even easy to act based on any arbitrary set of states by doing "**(&nbsp;Z&nbsp;AND**&nbsp;_number_&nbsp;**)&nbsp;>&nbsp;0**" with two combinators (where _number_ is the binary **OR** of the desired state numbers).

The "X" signal is of particular importance as it precedes a state change by one tick. This allows inputs to be cleared so they can't affect a transition from the _upcoming_ state to a different one. This timing is essential if the "hold" time is disabled (see below) and it's generally useful for clearing latched "one-shot" (aka "pulse") signals.

_Tip: To strip undesired signals, have a constant combinator with large negative values for all unwanted signals. Send that on a green wire along with the main red wire to an "**each > 0**" combinator._

### Inputs

- **A-W**: Arbitrary conditions 1 through 23 (default: >0 is true, <=0 is false).

The red wire does not have to be clean and constant values can be added to it via the constant combinator on one side. It's fine to have these signals (and others) be used for things outside of the FSM. The configuration of the FSM will determine which signals have any effect and exactly what those effects will be.

The default configuration has a 1/10th second "hold" time requirement (aka "debounce") on these signals. This avoids spurious state changes that can happen due to instability of the outside logic from imperfect propagation of signals but it means that intentional one-tick pulses cannot cause state changes. See the Cookbook for how to handle these.

## Configuration

Now comes the difficult part. The behavior of the FSM is controlled by 18 constant combinators along the bottom. Each of the nine states has nine "mask" values and nine "match" values, though in general most of them are left as zeros.

The numbers are binary encoded signal sets with "A" being 1, "B" being 2, "C" being 4, "D" being 8, etc. When the input signals specified by the "mask" have the value specified by the "match", the FSM will move to the matching state. This is most easily explained with some examples. (Note that the "match" values must actually be expressed as the _negative_ of the desired value.)

```md
From state#1, go to state#2 when "A" is true:
state#1: mask#2=1, match#2=-1

From state#2, go to state#3 when both "B" and "C" are true:
state#2: mask#3=6, match#3=-6

From state#3, go to state#4 if "D" is true or state#5 if "E" is true or state#1 if "A" is false:
state#3: mask#1=25, match#1=0, mask#4=25, match#4=-9, mask#5=25, match#5=-17
```

Note that in the last case, the "mask" defines all relevant signals for all three cases and thus the "match" exactly defines what all three signals must be for each transition. It's important to do it this way (and not check only a single bit for each choice) so that there can never be an ambiguous result. As defined, both "D" and "E" being true will cause no transition because that combination matches no configuration. If each was defined with a mask of a single bit, the FSM would not know which was the correct choice. If that happens, the FSM will lock down and signal an error to the user.

If it were important that the FSM always return to state#1 when "A" goes false regardless of the state of the other signals, then it would be defined as such:

```text
state#3: mask#1=1, match#1=0, mask#4=25, match#4=-9, mask#5=25, match#5=-17
```

By changing the mask for the state#1 transition, the FSM will always choose that when "A" is false regardless of the other signals. This is only safe, however, because all other choices have masks that include "A" and matches that require it to be true.

The conditions for each input signal can also be changed. The default is ">0" but can be anything and is configurable on a per-signal basis. Even the signal being checked can be changed but internally they're always "A" through "W".

Lastly, in the combinator at the center beside the substation power, there is a "hold time". The "H" value is the number of game ticks (1/60th second) that the signals must align before a state transition will take place. The default value of 6 (1/10th second) will generally prevent state transitions due to spurious signals that occur during stabilization of the outside logic. Set it higher if needed. If set to zero or one, even one-shot "pulse" signals will cause state changes. **Don't change any other values!**

## Turning it On

Once configured, go to that constant combinator in the center and flip it "on". The FSM will immediately go to the "0" (reset) state and remain there for one "hold time" before automatically advancing to state "1". It's not possible to programmatically transition back to the reset state; only power-cycling the combinator can cause that.

Along the bottom, lamps indicate the currently active state, 1-9. The lamp in the center shows the current status of the FSM:

- **red**: Turned off.
- **green**: Active and stable.
- **yellow**: Active and transitioning states, including the hold time.

## Cookbook

Some useful recipes for outside the FSM. Contributions welcome!

### Pulse Latch

If eliminating the "hold time" is undesirable (and it generally is), using a "one-shot" (aka "pulse") signal won't work without help.

To enact transitions with pulses, create a decider combinator "**S = _inputvalue_ when X > 0**" with signal "S" on the red wire coming from the pulse generator, connecting to _both_ the input and output of the combinator, and continuing to the FSM.

Note that this latch will be cleared on any state transition, not necessarily a transition that made use of the signal.

### Timed Transitions

Create a decider combinator with "**S = 1 when W ≥ _n_**". Connect both input and output to the red wire of the FSM. This will activate signal **S** whenever the FSM has been in the current state longer than **_n_** ticks. It's possible to have multiple timers each setting a different signal and configuring different states to transition based on different timers.

## Final Notes

The FSM is a complex set of logic and, as such, it is not instantaneous. It takes about 10 ticks (1/6th second) to enact a state transition (on top of the configured "hold" time) once all the necessary signals align.

If not all nine states are being used, later logic columns (from the constant combinators up through the ">" and "\*" pairs just below the substation) can be simply removed without damaging the machine. Also from the line of "=" combinators near the top. Only states "1" and "2" are required.

Similarly, if not all 23 inputs are being used (and really, who would?), the later ">" and "«" pairs associated with those signals can also be removed.

In both cases, however, it must be the entire tail that is removed. It isn't allowed to remove state "4" while keeping state "5" or to remove signal "C" while keeping signal "D".
