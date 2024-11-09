# Self Building Space-Exploration Factory Changelog

Download Blueprints from [here](https://github.com/bcwhite-code/brians-blueprints/releases/)

## 0.6.43

- Un-merged chests in orbit-side of space elevator.

## 0.6.42

- Removed latch from OWS that provides minor benefit but can cause failures.

## 0.6.41

- Fixed mall comment and rotate inserter for LTN assembler.

## 0.6.40

- Fixed bad loader direction in Substrates Block.

## 0.6.39

- Removed blue belts from ## 480MW reactor block.

## 0.6.38

- Simplified some logic in the Off-World Supply.
- Fixed OWS problem where construction train would not fully unload.
- Connected power in LDS (beryl).

## 0.6.37

- Fixed lamps in Elevator blueprints (that were mistakenly LTN inputs).

## 0.6.36

- Added elevator blueprint to allow use of SLS "depot" for extended train grid.
- Un-merged chests in Cryonite.

## 0.6.35

- Added space rail blocks and Elevator interface.
- Moved Elevator blueprints to separate book.
- Removed power switch from Belts.
- Connected power to Modules.
- Moved dish in Off-World Supply so it doesn't stop from riding the rocket.

## 0.6.34

- Added side balancers to core processing block stations.
- Fixed Mall recycling station.
- Fixed stashing of 3 reactors in 10GW block.

## 0.6.33

- Changed block control from power switch to blocked outputs for least UPS impact.

## 0.6.32

- Fixed science-export train station in Basic Science.
- Fixed belt direction in Barrelling.

## 0.6.31

- Removed LTN parts from Colony Request combinators.
- Removed nanobots from Colony Home combinators.

## 0.6.30

- Un-merged chests in Mall.
- Added missing power poles and fixed blue belt in Bricks & Glass.
- Fixed Basic Cores to require len=6 trains.
- Fixed self-build of Nuclear (## 480MW).
- Added missing prod3 modules to Refinery solid fuel.
- Many other small fixes.

## 0.6.29

- Fixed corrupted Concrete block.

## 0.6.28

- Added landfill output to Concrete block.
- Replaced missing green wire to P.Gas in Refinery.
- Fixed provide thresholds for walls in War.

## 0.6.27

- Retry race condition preventing some SLS rockets from getting loaded with capsules. (Can be applied over existing so long as it gets to place scaffolding.)

## 0.6.26

- Restored stations in SLS Orbit.
- Fixed/simplified science station in Basic Science.
- Removed LTN Content Readers from Colony Home (they register requests from all planets).

## 0.6.25

- Improved SLS Orbit with individual provider stations, up to 12.

## 0.6.24

- Fixed deadlock potential with quarter blocks.
- Included fixed block outline (since SBF book isn't yet updated).

Completely compatible with ## 0.6.23 and before but REMOVE ANY CONFLICTING SIGNAL when placing new version.

## 0.6.23

- Heat Shields (via Iridium)!
- Doubled capacity of basic Heat Shields block.

## 0.6.22

- Glass (pyroflux)!
- Small antimatter reactor (4GW)!
- Taught q-block construction about pylon power.
- Added two more (empty) tracks to Colony Home depot hub.
- Fixed provide priority of red-circuits block.
- Fixed chest limits on requesters in depot hub.

## 0.6.21

- Proflux Smelter and Foundry!
- Improved glass priority in LDS blocks.

## 0.6.20

- New Space Launch System (space elevator) using LTN/SE mod!
- Fixed unconnected science export station in Basic Science.

## 0.6.19

- Rocket Fuel!
- Pyroflux!
- Fixed corner case in SLS down-bound supply.
- Fixed steel belt (now red) in basic LDS.

## 0.6.18

- Spaceship support!
- Methane gas from methane ice!
- Changed basic LDS to take glass if available.
- Changed beryllium LDS to have lower priority if network has abundance of glass.

## 0.6.17

- LDS using beryllium (43/s)!
- Fixed down-bound requests in Space Launch System (i.e. elevator).

## 0.6.16

- Wood Recycling!
- Rocket Sections via beryllium!
- Fixed fuel station in Recycling Pad.
- Improved rocket fuel supply in Colony, Home.

## 0.6.15

- Added methane barrelling recipe to Barrelling.

## 0.6.14

- Space Elevator!!!
- Changed glass provider station to 4-car (for compatibility with Space Elevator).

## 0.6.13

- Moved landing pad in Colony Home for better recovery of crashed rockets.
- Added wood recycling (to green circuits) to Mall.
- Have Refinery accept 4-car coal trains.
- Fixed hold of 3 reactors in 10GW nuke.

## 0.6.12

- Fixed UG belt in Belts.
- Added more bots to phase#1 of Refinery.
- Fixed water requester and motors in Basic Science.
- Moved coal buffer chest inside logistic zone in Mall.
- Removed waterfill from War.

## 0.6.11

- Fixed reporting of contents to LTN in bulk supply station of Colony Home.
- Fixed power control of Scrap Recycling block.
- Added casting machine to Mall.
- Added scrap and compromised capsule recycling to Mall.
- Added block for Material Testing Packs.

## 0.6.10

- Fixed Mall supply station not unloading no-longer-needed items.
- Moved cargo-pod recycling from Recycling Pad to Rocket Sections.

## 0.6.9

- Added 4 more depot stations to Colony Home plus extra 8-car train and a 1-tanker train. Two empty slots.
- Moved water station in Colony Home to free up "parking" track.
- Fixed (again) rocket-fuel request in Colony Home.
- Improved Off-World Supply small-load launch delay.
- Added cargo-pod recycling to Recycling Pad.

## 0.6.8

- Vulcanite processing now exports enriched vulcanite.
- Added second bulk fluids station to Colony Home.
- Added beam power receivers.

## 0.6.7

- Added beaconized Foundary.
- Fixed rocket-fuel request from Colony Home.
- Improved resource requesting of Off-World Supply.
- Added missing power pole to coal-fired Smelter.

## 0.6.6

- Fixed bad waterfill in Belts and Barrelling.

## 0.6.5

- Fixed grid alignment of LDS.
- Separated chests in Nav-Sats so they won't merge.

## 0.6.4

- Restored missing wire connections to LTN stops in Basic Science.
- Off-World Supply remembers if an item was available in bulk even if it currently is not.

## 0.6.3

- Reduced module levels in Starter Circuits.
- Increased LDS buffer from 10k to 25k.
- Fixed direction of underground belt for lubricant barrels.

## 0.6.2

- Quarter-block construction now waits for recycling to complete before notifying.
- Restored missing wire in Mall.
- Removed test combinators in Off-World Supply.
- Fixed inserter filters in Bulk Launcher.
- Improved cleanup of crashed rockets in Bulk Receiver.

## 0.6.1

- Completely rebuilt for Space-Exploration v## 0.6!
- Rewritten instructions.
- New numbering scheme for versions.

## 0.10

- Low-Density Structures!
- Nuclear (10GW)!
- Circuits (x3)!
- Bricks & Glass!
- Fixed gears to multi-cylinder engines in Mall.

## 0.9

- Fixed Refinery light-oil cracking (removed extra UG pipe).

## 0.8

- Solar (## 128MW)!
- Kovarex/Nuclear (## 2.4GW)!
- Modules!
- Imported construction sites.
- Added "mall" accounting to Belts.
- Better production prioritization in Refinery.
- Removed unnecessary balancers from Refinery.
- Hub alert for low bot count (attrition).

## 0.7

- Depot Hub!
- Multi-Mine!

## 0.6

- Refinery!
- Foundry (electric)!
- Fixed pumpjack in Mall.
- Fixed Belts production cutoff and LTN config.

## 0.5

- Added Belt q-block.
- Fixed some loaders in Basic Science (should be red).
- Added solid fuel to Mall (mostly so doesn't stall from full methane).

## 0.4

- More steel and fixed greens in Basic Science.
- Mall no longer wastes local lubricant on large motors.

## 0.3

- Added small amounts of sulfur and sulfuric acid production to Basic Science.

## 0.2

- Fixed pump power and station settings in steam half-block.

## 0.1

- First release with some helpful bootstrap blueprints as well as blocks for "home", "basic science", "smelter", and "starter circuits"
