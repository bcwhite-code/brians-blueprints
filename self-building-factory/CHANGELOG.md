# Self Building Factory Changelog

Download Blueprints from [here](https://github.com/bcwhite-code/brians-blueprints/releases/)

## v5.0.50

- Include "all required items" on med power pole of Construction Site.
- Saved with latest Factorio version.

## v5.0.49

- Restored dropped red wire in .48 Science block.

## v5.0.48

- Fix Science so additional labs will fit. Also improve sushi-belt cycling.
- Move config of rail support & ramp in Red Mall to separate combinator so it doesn't break non-SA play.
- Add missing efficiency modules to Solar Parts.

## v5.0.47

- Still more spoilage-stall fixes to agricultural science.

## v5.0.46

- Fix spoilage stalls in agricultural science.

## v5.0.45

- Fix stall of nutrient feed to sulfur production in Gleba agricultural science.

## v5.0.44

- Fix space science so recycling of asteroid chunks doesn't clog.
- Add extraction of spoilage from rocket-fuel chamber.

## v5.0.43

- Fix space science to filter some inserters. Also make it able to be rotated 90 degrees.
- Fix filters for extraction from collectors on The UPS (ship).

## v5.0.42

- Fix Fulgora scrap recycling bootstrap of items provided to logistics network.
- Add burning of spoilage to Red Mall.

## v5.0.41

- Do request-exclusion in HOME a different way and tag different train lengths near speakers.
- Fix some problems in the agricultural-science print, including bottlenecks and fuel output.
- Removed unnecessary pumps from 10GW reactor.
- Turn on crafting of turrets in Red Mall (since needed for space travel).
- Update basic space science to support full 45/min.
- Update The UPS (ship) to buffer more water, use less ammo, jettison spoilage, and schedules.

## v5.0.40

- Add requester chest for artillery to Red Mall.
- Fix BOM for Refinery construction.
- Fix Home to not completely exclude depleted nuclear fuel cell trains.

## v5.0.39

- Fix stall of red science when yellow is behind in Science block.
- Enable all weapons in Red Mall.
- Add Vulcanus science rocket.

## v5.0.38

- Updated Rocketry block with multiple cargo rockets (still WIP). Force-build will not update.
- Add small requests for guns and lasers because they'll be needed for ships.
- Add new ship: The UPS (Universal Pack Ship)

## v5.0.37

- Fix Supply station of Fulgora recycling.
- Improve performance of Fulgoa mall.
- Add buffering of science, activated with arrival of Space science, to Science block.

## v5.0.36

- Bypass "finished" speaker for signal in Construction Site so will work even without it.
- Replace Fusion with Fisson for personal in Red Mall.
- Improve storage ability of ammo buffering in Hammerhead ship.
- Remove "full rocket only" circuit in Rocketry Block that wasn't tested and caused problems.
- Add recycling, train supply, and automall for Fulgora.

## v5.0.35

- Removed extra blueprints that shouldn't have been there.
- Improved module support of Red Mall.

## v5.0.34

- Change smelters to determine the ore from the plate rather than a separate parameter.
- Fix (finally?) the "supply" station of Solar Parts.

## v5.0.33

- Change all provider stations to be single-train at a time.
- Handle "spiolage" of agriculture science packs in Science.
- Disable alarm for empty uranium fuel cells in Home.
- Keep LDS recycling from consuming all steel in Quality.

## v5.0.32

- Fix Construction Site "recycling" that could loop back some items forever.
- Remove some leftover prototype assemblers from Red Mall.
- Fix Solar Parts "supply" station counting of loaded items.
- Limit all Starter Circuits outputs to a single train.
- Add 10GW reactor (self-building).

## v5.0.31

- Add "depots full" alarm to Home block.
- Add elevated rail assemblers to Red Mall.
- Change all L3 modules to L2 modules in Red Mall, Starter Circuits, Refinery, and Solar Parts.

## v5.0.30

- Set water request in reactor.
- Add assemblers for science labs to Science.
- Remove methane pump for sulfur in Science.
- Fix bad belt and some filters in Quality.

## v5.0.29

- Restored full roundabout corner junctions on blocks (or don't get straight-through when adjacent).

## v5.0.28

- Fix Construction Site missing combinators by removing non-std signals from default but making them easy to add locally.
- Restore landing pad to Science blueprint.
- Add (very slow) production of L2 productivity modules to Science to fill labs.
- Better purging of excess plates in Quality block before recycling begins.

## v5.0.27

- Add prod2 modules to science labs in Science block.
- Add WIP "quality" block (self-building).
- Add signal-sorter from Alex Leonheart to WIP Rocketry (completely untested).

## v5.0.26

- Add 35/s basic circuits block. (self-building)
- Add 90/s advanced circuits block. (self-building)
- Add 12/s processors block. (self-building)

## v5.0.23

- Add train counting for depots to Home and Hubs.
- Fix supply of small-stack items in Red Mall Supply.
- Fix wiring on Solar Parts. Add more instruction to bp comment.
- Fix chest locked-slots for greens in Starter Circuits.
- Add "Rocketry" block to WIP (self-building).

## v5.0.22

- Fix U-235 line to nuclear fuel in Nuclear 2.4GW.
- Change "special" trains to go to Depot stops between every transfer. This fixes both launch and stalls at stations.
- Add Solar Parts block for Advanced Solar. (self-building).

- If you're having trouble with Special Trains then add another `BT Depot` stop at the beginning or end with a `inactivity 1s` condition.

## v5.0.21

- Improved Supply logic in Red Mall. (see below)
- Fixed missing requests for new F2 items in Red Mall. (regression)
- Add "build" area to Home.
- Add new alerts to Home.
- Fix missing green wires in Home.
- Fix signals and train-limits for Refinery output fluids.
- Add filters to inserters removing fuel.
- Add electric smelter (self-building).
- Add electric foundry (self-building).

- Before applying the new Home blueprint, completely remove the "parking" track on one side. After that, the new print should merge without conflict.

- Before applying the new Mall blueprint, you must remove some logic at the Supply station. Remove these gates and just the gates; leave power, station, chests, etc. Don't leave any gates that you can see in the image. Then apply the new print to restore functionality.

![Remove logic at supply station](./assets/sbf%20v5.0.21%20breaking%20change.png)

## v5.0.20

- Fix some wiring in Home block.
- Add "build" area in Home block.
- Add filters to all fuel requesters so they can't unload bad things.

- The new Home block should place safely over the existing one but remove the "parking" track on the one side first.

- In that new area, you can drop train blueprints and the bots will build them. You still have to drop fuel into them manually when you want them to go. A single stack of coal half-dropped (ctrl-click) in each engine (starting with any back-facing engines) should do the trick.

## v5.0.19

- Fix acid station name in Starter Circuits.
- Fix direction of underground battery belt in Refinery.
- Fix setting for selection-combinators in Red Mall.
- Fix unloading of uranium trains in Red Mall.
- Add fueling of construction train to Red Mall.

## v5.0.18

- Fix acid pipe in Starter Circuits.
- Add Refinery (self-building).

## v5.0.17

- Update Depot Hub prints for new fueling method and moved out of WIP.

## v5.0.16

- Update Home block to match new fueling of trains in BT v5.0.25.
- Update special-train schedules for new fueling.
- Fix extraction of science from landing-pad in IS block.

- The existing Home block will continue to work but there will be problems when updating the fuel to something better. (See BT doc for details as to why.)

## v5.0.15

- Minor improvements to Construction Site.
- Moved Depot Hub prints to WIP book. (See BT thread for details.)
- Add Nuclear (2.4GW) w/ Kovarex block. (self-building)

## v5.0.12

- Add back another lost wire to Construction Site. (Can also be merged with .10 or .11 versions.)

## v5.0.11

- Restored missing wire from train-stop (read contents) to combinator. (Can be applied over existing 5.0.10 Site.)

## v5.0.10

- Fix Construction Site for "extra" items like landfill. Should now handle blocks placed on water. The request for Cliff Explosives is now off by default but easy to turn on in a const combinator near the tail of the station. (Will not overlay; only for new builds.)
- Fix recycler in Mall: red chests -> yellow chests
- Improve schedule of construction train with time limits.
- Add Starter Circuits block (self-building).

## v5.0.9

- Fix Construction Site request of "extra' things like landfill and cliff-explosives.
- Add coal-fired smelter for iron and copper plates. (self-building)

## v5.0.7

- Fixed construction instructions in Solar Block.

## v5.0.6

- SELF-BUILDING!
- Solar block (128MW)
- Updated Mall (with self-build parts) -- should place over existing with no conflict though there is one corner rail that you'll have to fill in by hand because the roboports don't cover it.
- Initial Since updated to support additional science packs. Remove the existing "labs" section then place the new version; there should be no conflicts. It includes a Landing Pad to receive Space Science packs though I expect it'll be moved later in the build. (Remember, keep the block on that side of IS open for future use.)

- Basic instructions are included in the Construction Site blueprint at the very head of the book. Once you have a location in mind, fit that block but don't place it -- just note where the construction Site needs to go. Then follow the instructions.

## v5.0.5

- Update to Red Mall support Space Age initial rocket. Super-force-place TWICE (ctrl-shift-left-click) to ensure it updates everything.
- New Space book with extension to the Red Mall that will build a few rockets and some basic parts.
- New Space Science (very simple) blueprint to apply to a new space platform for creating space science.

- Though the Mall extension produces scaffolding, crushers, and collectors, there are some other things needed to build the Space Science print. Collect those by hand and put them in the rocket cargo.

- It'll take multiple launches after the first one (that just places the space platform) to get everything up there. For the last launch, look at the requirements (shown by the space platform) to finish the build and make sure everything is present, especially enough scaffolding.

- It'll immediately start producing Space Science for return. Which I'll get to in the next release.

## v5.0.4

- New fueling station in Home block. (See up for how to apply it to existing builds.)
- Added BT:FuelIdle interrupts to all Special Trains. This prevents them getting stuck at fueling stations when their next stop isn't available. You can add this manually to your existing trains, available once any new special-train is placed.

## v5.0.3

- Fix IS provider stations that had green wires where they shouldn't be: (a) between the chests of different cars and (b) to the first "/" combinator on the 2-car and 4-car providers.

## v5.0.2

- Fix some small issues with Red Mall.
- Add Red Mall self-build framework. Just place this down, add the necessary trains, and let it go.
- Better pipe routing in IS. (very small change)

## v5.0.1

- Updated headers for all requester stations in IS. You'll have to remove the logic gates for requesters before applying.
- Moved IS 1-car stub stations that wouldn't let the train back out. Remove everything but the chests. Remove the green wire that goes across the track. Remove the 4 most-outside chests; the other 8 chests can remain with whatever contents they have. Remove the conflicting belts and move the pipe to its new position (or it'll feed the station by mistake). Apply the blueprint without conflict.
- Added the Red Mall! The basic structure to allow it to build itself isn't done -- later. I think I've updated all the recipes as required. A few require advanced materials now; they just have requester chests for that stuff.
- A number of new "Special Trains" have been added. Build and launch one of each (always fully fueling any backward-facing engine first). If you launched the ore ones to support IS, you don't need more of them.

## v5.0.0

Work in progress. Plenty of bugs. Maybe some breaking changes. Lots of fun.

v5 blueprints are for Factorio 2.x and the Space-Age expansion. It is wholly incompatible with all previous versions (and Factorio 1.x) but will join with track from Brian's Trains at the junctions.

Follow the original SBF instructions on how to place these. It hasn't been updated but the method should not have changed.

For trains, you'll need one 8-car BT train and 1 8-tank BT train, plus one each of the "special" trains in the SBF book. Start with the 8to1coal since that will fill the fuel station. Remember that they'll start moving as soon as they get fuel so supply a full stack and fill any backward-facing engine first.

And of course you'll need the full set of mines (coal, stone, iron ore, copper ore, oil) all using the 8-car provider blueprints from the BT book. Don't forget to connect red & green on those providers!

## v4.1.6

- Small updates to Red Mall self-build.

## v4.1.5

- Removed slots from loader chests in Red Mall.
- Fix reporting of amount by electric smelter.

## v4.1.4

- Restored Red-Mall recipes that Factorio itself somehow dropped from the blueprint.

## v4.1.3

- Added missing filters to some Blue Mall beacon storage chests.

## v4.1.2

- Remove bad inserters in Mall placing walls in the wrong chest.

## v4.1.1

- Another update to Blue Mall.
- Fixed credit for Red-Mall Self-Build.

## v4.1.0

- Updated malls to use storage chests instead of provider chests to provide better recycling. (credit: Thec-NiqueMan)
- Added Red-Mall Self-Build to "Construction" book. (credit: Merach)

## v4.0.3

- Re-captured Blue Mall as didn't include some expected 4.0.2 changes.

## v4.0.2

- Fixed request glitch when Construction Site is recycling.
- Fixed blue loader lubricant intake in Blue Mall.
- Fixed fast loader input of basic loader in Blue Mall.
- Fixed provide threshold in Advanced Circuits.

## v4.0.1

- Fixed light-oil pipe in Blue Mall.
- Moved combinator in Strong Defense that (sometimes) conflicts with rail.
- Prevented signals wires in Strong Defense from connecting between segments.

## v4.0.0

- Moved signal along block edge to fix deadlock potential when using quarter-blocks.

v4 blueprints are completely compatible with v3. If placed adjacent, there will be a couple extra rail signals along the straight edges but will still operate correctly. However, if you've already started with v3, there's no major reason (yet) to switch to v4.

## v3.5.13

- New "strong" perimeter defense!
- Added landfill under rail templates.

## v3.5.12

- Cleaned up some wiring in the Refinery.

## v3.5.11

- Fixed light-oil cracking in Refinery (removed extra UG pipe).
- Prioritized, somewhat, plastic production over others.

## v3.5.10

- Re-exported with all necessary mods installed.

## v3.5.9

- Fixed Construction Supply (was missing wire to account what had been loaded).
- Restored missing quarter-block rail template.

## v3.5.8

- Updated all station names to use embedded icons. (Thanks, nyurik!)

## v3.5.7

- Moved to GitHub under [brians-blueprints](https://github.com/bcwhite-code/brians-blueprints).

## v3.5.6

- Updated perimeter defense.

## v3.5.5

- Minor cleanups on Blue Mall
- Fixed steel provider train min-length in Initial Science
- Fixed loader directions in Aux Mine

## v3.5.4

- Removed extra blue chests from Depot Hub (logistics).
- Removed extra underground belts from tail of malls.
- Added missing signals to mine block's construction siding.
- Fixed number of centrifuges requested by 2.4GW block.

## v3.5.3

- Restored train-scaling combinator signals in HOME (lost in v3.5.1).

## v3.5.2

- Added standard "A" signal to the rail network with current accumulator level.
- Restored train-scaling stop in HOME (lost in v3.5.1).

## v3.5.1

- Fixed artillery outpost caching shells.
- Changed perimeter belt to red (1/2 the deployed inventory).
- Fixed an overload problem with multi-provider station.

## v3.5.0

- New quarter-block rail templates.
- New defense blueprints (not self-building).
- New "general construction" site that doesn't need programming (used for quarter-block construction).
- Fixed refinery item counts.
- Updated refinery stations to new standard (and set names).

## v3.4.16

- Restored station names in Red and Blue malls.

## v3.4.15

- Added chunk-alignment to landfill block.

## v3.4.14

- Fixed phase#4 of the Construction Site.

## v3.4.13

- Fixed 5-minute maximum time between train in Mall blueprints.

## v3.4.12

- Made it easier to find the fuel configuration in "fueled by logistics" hub.
- Removed extra rail segment in 1kSPM harness.

## v3.4.11

- Added missing belts to modules factory.

## v3.4.10

- Fixed provide threshold on Battery block requester stations.

## v3.4.9

- Fixed splitters in Processors block (red->blue).
- Removed some unused/leftover belt parts in Processors block..

## v3.4.8

- Fixed "not being produced" warning and 10-min delta calculation in HOME block.
- Restored missing flamethrower-ammunition recipe in Red Mall.

## v3.4.7

- Fixed power to roboports in malls.

## v3.4.6

- Fixed channel-3 output of solar parts availability (was going to train red wire).

## v3.4.5

- Fixed 1kSPM power for roboports on long side.

## v3.4.4

- Fixed 5-minute "call train" timer in Construction Supply station (including Red Mall and Blue Mall versions).

## v3.4.3

- Re-released because some assemblers in Starter Circuits and Processors were rotated by the export process.

## v3.4.2

- Extended landfill blueprints for new signals and Mine belts between rails.

## v3.4.1

- Fixed depots-full alert in Home

## v3.4.0

- Added support for automatic train building within Home block. (See doc for details.)

## v3.3.9

- Fixed Modules block publishing of prod module counts.
- Changed some accidental red belts back to yellow in Advanced Circuits block.

## v3.3.8

- Fixed Modules block build missing power path.

## v3.3.7

- Changed "Aux Mine" to support only len 6 & 11 trains. Otherwise it may try to fill engines and that can leave inserters holding ore.

## v3.3.6

- Restored missing combinators in "Aux Mine" for handling abundance of coal.
- Fixed ">60%" circuity in WIP "Home" for warning when depot hubs are getting full.

## v3.3.5

- Fixed mall Supply stations that wouldn't eject unwanted material while mall was still building.

## v3.3.4

- Fixed missing wires in Blue Mall from roboport to threshold circuits.
- Fixed Mine to be compatible with non-std cargo wagons.
- Removed old designs and test blueprints.

## v3.3.3

- Added "train limit" of 1 to all depot stops.
- Fixed belt chests in Blue Mall (requester->provider).

## v3.3.2

- Added missing rail segment in Depot Hub (train fuel).
- Restored missing efficiency modules in Blue Mall.
- Moved misbehaving rail signal in 1kSPM harness.

## v3.3.1

- Remove incorrect green wires in Mall provider stations between steel chests and the stack inserters that fill them.

## v3.3.0

- Publish info about trains waiting at LTN depots (Home & Hubs).
- Removed blocked slots in Personal Resupply trash chests.
- Greater perimeter coverage by roboports in Starter Circuits.

## v3.2.1

- Fixed red->green wire in Construction Chaining blueprint (to properly signal "done").

## v3.2.0

- Moved roboports in 1kSPM to better connect to ones in external blueprint.
- Cleaned up some constant combinator lines to match Factorio 1.1.

## v3.1.0

- Official release of new designs.

## v3.0.X (testing)

- Improved Construction Site & Supply.
- Added Manual Construction Site to allow building custom blueprints.
- Combed power lines of processor block.
- Added mixin blueprint to chain construction sites (start one when another finishes).
- Added "aux" Mine block for better UPS.
- Simpler control of Modules' circuit request sizes.
- Reduced module provider limit from 100 to 50 (1 stack).

## v2.2.5

- Fixed wiring to Construction Site speaker that caused it to no longer alert (now needs green wire between speaker and lamp).
- Available via this link.

## v2.2.4

- Fixed stack size on inserters of resupply station so they can't overfill and block other items from being loaded.

## v2.2.3

- Allow Construction Site to revert to "recycling" mode if more material arrives (perhaps from manually marking things to be removed).
- Improvements to personal train default schedule.

## v2.2.2

- Better home/resupply default schedule.

## v2.2.1

- Fixed some problems with the Resupply block.

## v2.2.0

- New personal train configuration in Home block (upgrade print in "Construction" book).
- New "resupply" block, found in the "Construction" book (can later be a Depot Hub).

## v2.1.0

- Official release of new designs.

## v2.0.X

- New rail signalling to fix deadlock problem.
- New rail templates for building new blocks.
- More iron from Initial Science & other small improvements.
- Minor improvements to Red Mall.
- Made Mine station safe during power brown-outs.
- New Construction Site.
- Added LTN ID to all stations following Brian's Trains v4.8.

## v1.7.7

- Added missing inserter in Initial Science processor production.

## v1.7.6

- Fixed red-belt item counts for Modules block.

## v1.7.5

- Fixed spent-fuel-cell requester station in 2.4GW reactor block.

## v1.7.4

- Removed extra green wine between medium power poles (for 1's material amount...

## v1.7.3

- Fixed water request amount on Oil Refinery.

## v1.7.2

- Removed extra red wire in solar parts block provider station.

## v1.7.1

- Fixed roboport power in coal-fired smelter.

## v1.7.0

- Added dedicated "battery" block (for bulk accumulator production).
- Changed 1kSPM harness to reduce train congestion.

## v1.6.3

- Added LTN Depot access from all four sides.
- Set "train limit" to 1 for all LTN depot stations.

## v1.6.2

- Restore 360spm block mistakenly overwritten with 1k SPM harness.

## v1.6.1

- Added missing red & green wires in Mine block. (again )

## v1.6.0

- Improvements to 1k SPM build.

## v1.5.3

- Added missing red & green wires in Mine block.

## v1.5.2

- Removed extraneous parts on outside of Mine block.

## v1.5.1

- Added missing power pole to coal-fired smelter.

## v1.5.0

- Updated mine to have actual stacker space for second train.
- Added harness for 1k SPM factory blueprint.
- Increased beacon storage of malls.

## v1.4.4

- Change #trains of mine from 1 to 2: Though there isn't actually a stacker for a second train, the buffer chests tend to fill faster than is unloaded by a single queued train. This can lead to a train blocking an intersection but trains should spend <10s loading anyway.
- Fixed number of yellow splitters in Refinery build orders.

## v1.4.3

- Added "Construction ON" blueprint for starting construction via map view.
- Removed accidental constant combinators from Modules block.
- Fixed positioning of concrete pad in "advanced circuits" block.

## v1.4.2

- Added missing wire in Red Mall module provider logic.

## v1.4.1

- Added ability to skip production of L1 and L2 modules in module block.
- Fixed providing of L3 modules from Red Mall.

## v1.4.0

- Added "basic circuit" block.
- Added more info to Home Base block.
- Added missing pipe in Blue Mall wood burning.
- Fixed depot hub requester-chest signal wiring.

## v1.3.1

- Fixed extra wire on solar-parts factory that caused LTN red light at provider.

## v1.3.0

- Clean up from Factorio bug that removed connections between power poles.

## v1.2.1

- Improved construction of rocket yard and refinery.
- Restored missing power poles in mine.
- Fixed battery feed in rocket yard (needs full belt).

## v1.2.0

- New "beaconized" smelter (16 blue belts) and foundry (4 blue belts) for less raw material.
- Improved provider station in mine to be fully balanced for all ores (fastest train loading).
- Fixed slow filling of chests in mines with a single ore type.
- Fixed potential stall of fuel stations in depot hubs.
- Fixed processor belts in module factory.

## v1.1.3

- Solar-parts block will now request steel from Initial Science (since it's impossible to build a Foundry without significant power).

## v1.1.2

- Fixed bad fix of refinery signals.

## v1.1.1

- Fixed production station in new Solar Parts block.
- Fixed required material and rail signals for refinery.

## v1.1.0

- New Advanced Solar mod support (see full instructions).
- Fixed problem where robots could get dumped into mining output.

## v1.0.3

- Fixed belting in Advanced Circuit block.

## v1.0.2

- Improvements to train-fueled depot hub.
- Connect refinery outputs to train circuit network.
- Added Train Programming Interface blueprint.

## v1.0.1

- Moved waterfill requests into separate combinator. (Factorio drops the entire item if it doesn't know an item within it.)
- Added settings to reduce warnings about un-filled trains leaving mines.

## v1.0.0

- First public release.

## v0.x

- Design and testing.
