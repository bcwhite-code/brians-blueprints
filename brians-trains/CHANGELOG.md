# Brian's Train Changelog

History, in brief.

Download Blueprints from [here](https://github.com/bcwhite-code/brians-blueprints/releases/)

## v5.0.27

- Add Cybersyn headers, support hub, and trains.
- Some reorganization of the book.
- Fix city-block roboport mix-ins.
- Fix station priorities for 8-car bodies.
- Fix green wire for double-station 4-car loop.


## v5.0.26

- Add "inactivity 1s" to depot stop for fuel train (or it won't fuel).
- Add missing wire to Depot Hub fuel station.

## v5.0.25

- New fueling mechanism for trains.

The Depot Hub now no longer has a separate "BT Fuel" station on the side. Instead, trains are fueled directly at the Depot stops. (Reason is in the doc.)

The train templates no longer include the BT:Refuel interrupt but that will not affect existing trains (or any such trains added in the future). That shouldn't be a problem.

The old fueling stations will continue to work but are unlikely to be used given that trains will be constantly topped-up every time they visit a Depot.

If the existing Depot Hubs are not updated then trains will continue to get fueled with the old method which will cause trains to become stuck if the fuel type is ever changed (the reason why this fueling change was required in the first place).

## v5.0.24

- Route train-request signal via train-stop so it can't go out until the stop is built.

## v5.0.23

- Fixed station name of 8-car "merged" provider.
- Moved signal in Depot Hub to fit in short block.
- Try to make station build instructions more clear.

## v5.0.22

- Fixed configuration of merged stations. (Just apply over existing ones.)
- Increased height of 8-car loops by 1-rail so that stations fit inside.

## v5.0.21

- Added merged-chest stations, both provide and request. The loading blueprints for them is further down the sub-book. You may have to adapt them for whatever "loader" technology is being used.

## v5.0.20

- New Depot Hub fuel station that can fill backward-facing engines. This is necessary if your factory has reversible "stub" stops as they can cause trains servicing them to get permanently stalled at the fueling station.

## v5.0.18

- Remove erroneous red wires from "Rail for Stations" blueprints.

## v5.0.16

- Fix bug in requester headers that could cause negative requests if station is overfilled.

Old headers still work but if the station is overfilled, like from it being full and the request reduced, they will start requesting a negative number of trains which can mess things up elsewhere.

## v5.0.15

- Fixed remaining old-rail blueprints.
- Added red & green wires to all rail-for-station blueprints, shortening them by 1 in the process.

## v5.0.14

- Fix reversed underground belt in 1-car-provider-right.
- Add some train stops to some station loops.

## v5.0.13

- Fixed fluid-provider header to properly handle number of trains.

## v5.0.12

- Fixed some bad logic in the Depot Hub where it was looking at the wrong channel.

## v5.0.11

- Add "limited loading" support to all providers.

Both the headers and the stations have changed. If you use new headers with old stations, just change the PVD amount in the config combinator from 1 to 1000000000 (or any number larger than is contained in a full train).

Note regarding limited loading:

> The calculated number of allowed trains is based on full trains. Thus, even if you set the load limit to 1/4 of a train, it won't call a train until there is enough material for a full one.
>
> If you don't want that... In the top line of the constant combinator add a negative stacks S (for items) or negative units F (for fluids) of the amount to be left free in a train, then a T (for items) or G (for fluids) of the positive same number.
>
> Do not change the S, T, F, or G in the bottom section as that will affect all stations of that type & length.
>
> Keep in mind that by reducing these limits, the station has capacity for more trains which means you need to have additional stacker space to support them or limit the loading of the station. For items, this can be done by blocking off additional slots in the first chest.

## v5.0.10

- Fixed feedback on fluid-requester header.
- Fixed BT:idle interrupt like shown above.

**You'll want to make the same change to your build or you may find trains stuck at a bad station that requested but won't unload.**

## v5.0.9

- Fix some stations

## v5.0.8

- Added missing rail segments to 3-station loops.
- Fixed fluid requester header.

To fix the fluid header, remove the conflicting combinator before re-placing the header. Nothing else should need changing.

Again, two version of the blueprint, the main one exported from git with Fatul and the `-direct` one the export string from Factorio.

## v5.0.7

- Fixed some bad track in one requester station.
- Fixed missing blueprint parameter in another station.
- Turned off "read train contents" in all requester stations.

Note: If a requester is high-traffic, you can turn that on to have the train go directly back to the provider rather than making an intermediate visit to a depot (where it might be scheduled for a different item).
I've updated the 5.0.7 release to have two files:
5.0.7 which was imported into git using Fatul then re-exported.
5.0.7-direct which is the string direct from Factorio.
If you use the former, please let me know any blueprint problems. Fatul has need some updates for F2.

## v5.0.6

This is a **BREAKING CHANGE** over previous 5.0.x releases. Before applying anything new, you must:

- remove all trains
- remove all circuit entities from all stations
- remove all circuit entities from the Depot Hub
- remove the "multiplex controller"

To use this new version:

- place the new "Vanilla Controller" (it can sit in junction)
- place new station headers
- place new stations overtop old ones; these are parameterized blueprints and will prompt for the item/fluid being provided/requested
- for requesters, set the negative request amount in the combinator (the order of these probably no longer matters even though the instructions say so)
- drop new trains (don't forget to fuel backward-facing engines)

## v5.0.5

- Improved requester stations are shorter and have fewer splitters.
- Depot Hub is now smaller (but has no functional changes).

You'll need a Depot Hub. And exactly one "Multiplexer Control" (from the Xtra sub-book) wired via red to the train grid.

The trains should start in "automatic" mode so it should just launch after giving it some fuel. Since the first Depot Hub won't yet have a functioning fuel station, you'll have to fully fuel the train.

Do NOT mix 1-car and 1-car-reversible in the same factory. Use only one or the other depending on your needs.

There's probably more but I can't think of it right now.

I'VE DONE ONLY LIMITED TESTING

## v5.0.3

- Fixed all "stack" inserters to be "bulk".
- Fixed filter setting on requester stations.
- Fixed pump enables and filters on fluid stations.
- Updated "header" blueprints.
- Probably have to re-place ones from 5.0.2.

## v5.0.2

- Updated all sizes of provider and requester station.
- Updated train templates to use F2 schedules.

## v5.0.0

- Updates for Factorio 2.x. A work-in-progress. Not for the faint-of-heart.

## v4.26

- Changed provider divisors back to multiples of 12 to simplify and fix non-LTN mixins.

## v4.25

- Fixed a bad splitter in 1-car right-output requester station.

## v4.24

- New symmetrical quad-rail non-loop intersection with left-turn avoidance.
- Add "congestion control" mix-in for quad-rail 4-way "loop" junctions. (Read blueprint comment.)

## v4.23

- Added missing red wire in 4-car provider (right).
- Added red+green from LTN lamp to pole for easier debugging.
- Added priority placeholders to station configs.

## v4.22

- Added landfill under all BT rail blueprints

## v4.21

- Changed requester station divisor back to actual chest count (no performance improvement from off-by-one)
- Changed station-rail exit signal to chain-signal so trains can't exit and immediately block the main track.

## v4.20

- Updated non-LTN requester to properly export amount short.

## v4.19

- Added negative "0" channel amounts for request shortage.
- Set train-limit on depots so trains won't queue for them.

## v4.18

- Fixed (again) bad signals in 4-track "L".

## v4.17

- Fixed more bad signals in 4-track "L".

## v4.16

- Fixed bad signal in 4-track "L".

## v4.15

- Fixed weird present of two extra tanker cars in 8-tanker blueprint.

## v4.14

- Changed icons for "LTN Support" book so it won't get completely dropped if mod isn't installed. Those blueprints can be adapted to non-LTN designs by changing the stops.

## v4.13

- Fixed LTN wiring in depot hubs' train fuel stations so it works with the "use signals" option.

## v4.12

- Fixed more wiring on train-fed LTN Depot.

## v4.11

- Fixed wiring on train-fed LTN Depot.

## v4.10

- Fixed missing red wires with fuel info on Logistics Depot Hub.
- Fixed some wiring on tanker stations.
- Increased requester "provide" threshold so overfill can't change it into a provider.

## v4.9

- Fixed depot blueprints for Factorio 1.1 power lines.

## v4.8

- Restricted LTN network IDs so other networks can co-exist. Stops are ID 255 (bits 0 to 7) and depots are ID 65535 (bits 0 to 15) to cover many options while leaving adequate unused bits for outside definition.

## v4.7

- Fixed green wire in 8-tanker requester

## v4.6

- Fixed wire in updated 8-car provider (left input).

## v4.5

- Improved non-LTN station designs. (see live doc).

## v4.4

- Added support for non-LTN use (see "Life without LTN" in live doc linked at top).
- [Combed](https://mods.factorio.com/mod/power-grid-comb) station electrical wires.

## v4.3

- Changed "average" dividers by one (96 -> 95 for providers, 96 -> 97 for requesters). This eliminates the brief (1-2 items on one lane) stalls that occur at full speed.
- Removed extra rail from 2W U-turn.
- Saved with Factorio v1.1.5. I hope that's not a problem for those still on 1.0.0.

## v4.2

- changed LTN station limits to use "stacks" instead of absolute amounts
- removed unnecessary chain signals; absolute grid makes them unnecessary
- added grid to double-exit blueprint

## v4.1

- cleaned schedule from player train
- made compatible with LTN "use signals"
- green wire now multiplexed
- add grid to station loops
- fixed alignment of stackers for 4-station loops

## v4.0

- Improved signaling on all "round" junctions lets trains get closer before stopping. Performance improvement is about 15%.
- Improved signalling on station loops also lets trains get closer while waiting and prioritizes moving trains over starting trains so as to not create logjams.
- Added "wide" double-track designs that can be later upgraded to quad-track without having to worry about the new outside track conflicting with existing stations.
- Added "city block" designs for all three rail sizes.
- Widened safe crossings to make it easier to drive vehicles.
- Added (non-LTN) station designs for player train and remote construction sites.
- Added blueprints for the train-rate display seen in my [video](https://youtu.be/gmv0mkNOkSA).

## [v3.6](http://backgroundexposure.com/files/brians-trains-v3.txt)

- Added missing red wire on 4 car provider (right input)
- Use the "v3.6" link to get this version.

## v3.5

- Subdivided blueprints into internal books of related designs.
- Added missing 2-car to 4-blue requester stations.
- Added blueprints for 2-tanker and 4-tanker trains.

## v3.4

- Increased "siding" station track distance from main rail so "requester" stations will fit.
- (Also provides better compatibility with "[aux](https://factorioprints.com/view/-M5PZvxZvXEZnmg4v7Hy)" station designs.)

## v3.3

- Fixed quad-rail placeholder so that all signals are present when two are crossed.
- Removed unnecessary rails from quad-rail u-turn.

## v3.2

- Added early LTN Depot that fuels engines from a coal train instead of logistics.

## v3.1

- Stretched all station tracks to match new size.
- Upgraded quad-rail high-capacity station to make use of new space. Now 15% faster! Sustained rates >42 trains per minute.

## v3.0

**v3 Blueprints are incompatible with v2 blueprints! Do not mix them!**

- Rebuilt to 110x110 global, "absolute" grid for easier, error-free placement of track.
- Junctions and straights are now the same size.

## [v2.17](http://backgroundexposure.com/files/brians-trains-v2.txt)

- Fixed default request amounts for 2-tanker and 4-tanker requestor stations.
- Use the "v2.17" link to get this version if already started with v2 blueprints.

## v2.16

- Added safe crossings (to avoid getting run over by speeding trains).

## v2.15

- Changed "blue" requestor stations to mesh together when side-by-side.

## v2.14

- Added 2 and 4-car fluid stations
- Tested and saved with Factorio 0.18

## v2.13

- Fixed dead pump and request-amount-cut-off wiring in 8-tanker provider.
- Fixed signals on stub track.

## v2.12

- Added single-car, 2-blue, right-side requestor station.
- Fixed 8-car requestor to have default min train size of 8.

## v2.11

- Removed wall piece mistakenly included in quad-rail to double-rail junction.

## v2.10

- Added additional chain signals to quad-rail double-rail connection so it meshes properly with "placeholder".

## v2.9

- Added additional chain signals to quad-rail U-turn so it meshes properly with "placeholder".

## v2.8

- New high-throughput "straight" quad-rail junction… 10% more than v2.7!

## v2.7

- Fixed "X" placeholders in some stations.
- Stretched red and green wire along all rail sections.
- New quad-rail "loop" (upgrade) junction has 60% higher throughput!
- New quad-rail "straight" junction has 25% higher throughput than that!

## v2.6

- Fixed bad rail signal on 3x4+6 loop.
- Fixed bad combinator output on 1-car provider (right input)

## v2.5

- cleaned up tanker stations (removed excess pipe; fixed some wiring; added X to constant combinator)
- fixed some bad blueprint names

## v2.4

- added missing wires to 8-Car Requester (left output)

## v2.3

- removed roboports mistakenly included in a station "loop" blueprint

## v2.2

- updated for Factorio v0.17 (no actual changes were necessary)
- fixes to quad-rail designs (mostly more chain signals)
- fixed inconsistencies between station loop designs
- added text descriptions of designs
- first public release

## v2.1

- added 2-blue-per-car stations
- fixed some small problems such as misplaced signals
- first private release

## v2.0

- added quad-rail designs
- increased junction size to allow both double/quad junctions

## v1.X

- standard chunk-based layout of rails
- fully operational stations, left & right feeds

## v0.X

- initial station designs
