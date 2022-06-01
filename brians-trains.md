* Main documentation is [HERE](https://docs.google.com/document/d/1hfdz3PCpe91HOSuna6A650LsVmBjO8YACzxFemrQKqA/edit?usp=sharing). 
* Join the [discussion on Discord](https://discord.gg/hQnsXwpZ8A).
* [Auxiliary station blueprints](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy) make it much easier... if you're willing to install a few mods.
* [Self-Building Mega-Factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD) (a city-block layout book)

# Changelog

History, in brief.

## V4.20
* Updated non-LTN requester to properly export amount short.

## V4.19
* Added negative "0" channel amounts for request shortage.
* Set train-limit on depots so trains won't queue for them.

## V4.18
* Fixed (again) bad signals in 4-track "L".

## V4.17
* Fixed more bad signals in 4-track "L".

## V4.16
* Fixed bad signal in 4-track "L".

## V4.15
* Fixed weird present of two extra tanker cars in 8-tanker blueprint.

## V4.14
* Changed icons for "LTN Support" book so it won't get completely dropped if mod isn't installed.  Those blueprints can be adapted to non-LTN designs by changing the stops.

## V4.13
* Fixed LTN wiring in depot hubs' train fuel stations so it works with the "use signals" option.

## V4.12
* Fixed more wiring on train-fed LTN Depot.

## V4.11
* Fixed wiring on train-fed LTN Depot.

## V4.10
* Fixed missing red wires with fuel info on Logistics Depot Hub.
* Fixed some wiring on tanker stations.
* Increased requester "provide" threshold so ovefill can't change it into a provider.

## V4.9
* Fixed depot blueprints for Factorio 1.1 power lines.

## V4.8
* Restricted LTN network IDs so other networks can co-exist.  Stops are ID 255 (bits 0 to 7) and depots are ID 65535 (bits 0 to 15) to cover many options while leaving adequate unused bits for outside definition.

## V4.7
* Fixed green wire in 8-tanker requester

## V4.6
* Fixed wire in updated 8-car provider (left input).

## V4.5
* Improved non-LTN station designs. (see live doc).

## V4.4
* Added support for non-LTN use (see "Life without LTN" in live doc linked at top).
* [Combed](https://mods.factorio.com/mod/power-grid-comb) station electrical wires.

## V4.3
* Changed "average" dividers by one (96 -> 95 for providers, 96 -> 97 for requesters).  This eliminates the brief (1-2 items on one lane) stalls that occur at full speed.
* Removed extra rail from 2W U-turn.
* Saved with Factorio v1.1.5.  I hope that's not a problem for those still on 1.0.0.

## V4.2
* changed LTN station limits to use "stacks" instead of absolute amounts
* removed unnecessary chain signals; absolute grid makes them unnecessary
* added grid to double-exit blueprint

## V4.1
* cleaned schedule from player train
* made compatible with LTN "use signals"
* green wire now multiplexed
* add grid to station loops
* fixed alignment of stackers for 4-station loops

## V4.0
* Improved signaling on all "round" junctions lets trains get closer before stopping. Performance improvement is about 15%.
* Improved signalling on station loops also lets trains get closer while waiting and prioritizes moving trains over starting trains so as to not create logjams.
* Added "wide" double-track designs that can be later upgraded to quad-track without having to worry about the new outside track conflicting with existing stations.
* Added "city block" designs for all three rail sizes.
* Widened safe crossings to make it easier to drive vehicles.
* Added (non-LTN) station designs for player train and remote construction sites.
* Added blueprints for the train-rate display seen in my [video](https://youtu.be/gmV0mkNOkSA).

-----

**===> V3 Blueprints are incompatible with V2 blueprints! Do not mix them! <===**

## [V3.6](http://backgroundexposure.com/files/brians-trains-v3.txt)
 * Added missing red wire on 4 car provider (right input)
 * Use the "V3.6" link to get this version.

## V3.5
 * Subdivided blueprints into internal books of related designs.
 * Added missing 2-car to 4-blue requester stations.
 * Added blueprints for 2-tanker and 4-tanker trains.

## V3.4
 * Increased "siding" station track distance from main rail so "requester" stations will fit.
 * (Also provides better compatibility with "[aux](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy)" station designs.)

## V3.3
 * Fixed quad-rail placeholder so that all signals are present when two are crossed.
 * Removed unnecessary rails from quad-rail u-turn.

## V3.2
 * Added early LTN Depot that fuels engines from a coal train instead of logistics.

## V3.1
 * Stretched all station tracks to match new size.
 * Upgraded quad-rail high-capacity station to make use of new space.  Now 15% faster!  Sustained rates >42 trains per minute.

## V3.0
 * Rebuilt to 110x110 global, "absolute" grid for easier, error-free placement of track.
 * Junctions and straights are now the same size.

-----

## [V2.17](http://backgroundexposure.com/files/brians-trains-v2.txt)
 * Fixed default request amounts for 2-tanker and 4-tanker requestor stations.
 * Use the "V2.17" link to get this version if already started with V2 blueprints.

## V2.16
 * Added safe crossings (to avoid getting run over by speeding trains).

## V2.15

 * Changed "blue" requestor stations to mesh together when side-by-side.

## V2.14

 * Added 2 and 4-car fluid stations
 * Tested and saved with Factorio 0.18

## V2.13

* Fixed dead pump and request-amount-cut-off wiring in 8-tanker provider.
* Fixed signals on stub track.

## V2.12

* Added single-car, 2-blue, right-side requestor station.
* Fixed 8-car requestor to have default min train size of 8.

## V2.11

* Removed wall piece mistakenly included in quad-rail to double-rail junction.

## V2.10

* Added additional chain signals to quad-rail double-rail connection so it meshes properly with "placeholder".

## V2.9

* Added additional chain signals to quad-rail U-turn so it meshes properly with "placeholder".

## V2.8

* New high-throughput "straight" quad-rail junction… 10% more than v2.7!

## V2.7

* Fixed "X" placeholders in some stations.
* Stretched red and green wire along all rail sections.
* New quad-rail "loop" (upgrade) junction has 60% higher throughput!
* New quad-rail "straight" junction has 25% higher throughput than that!

## V2.6

* Fixed bad rail signal on 3x4+6 loop.
* Fixed bad combinator output on 1-car provider (right input)

## V2.5

* cleaned up tanker stations (removed excess pipe; fixed some wiring; added X to constant combinator)
* fixed some bad blueprint names

## V2.4

* added missing wires to 8-Car Requester (left output)

## V2.3

* removed roboports mistakenly included in a station "loop" blueprint

## V2.2

* updated for Factorio v0.17 (no actual changes were necessary)
* fixes to quad-rail designs (mostly more chain signals)
* fixed inconsistencies between station loop designs
* added text descriptions of designs
* first public release

## V2.1

* added 2-blue-per-car stations
* fixed some small problems such as misplaced signals
* first private release

## V2.0

* added quad-rail designs
* increased junction size to allow both double/quad junctions

-----

## V1.X

* standard chunk-based layout of rails
* fully operational stations, left & right feeds

## V0.X

* initial station designs
