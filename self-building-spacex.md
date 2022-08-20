# Self-Building Space-Exploration

These blueprints are for Space Exploration games using the "self building factory" (SBF) system from my [self-building-factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD).

These cover a lot of the planetside work but the "space" aspect will generally be omitted because:
 - I don't want to spoil it.
 - I don't use automated construction trains in space.

Join the discussion [on Discord](https://discord.gg/eSt3Qd8D2e).

You'll want the following mods:
* [Space Exploration](https://mods.factorio.com/mod/space-exploration) (required)
* [Logistic Train Network](https://mods.factorio.com/mod/LogisticTrainNetwork) (required)
* [Loader Redux](https://mods.factorio.com/mod/LoaderRedux) (required)
* [Miniloader](https://mods.factorio.com/mod/miniloader) (required)
* [Merging Chests](https://mods.factorio.com/mod/WideChests) and [Unlimited](https://mods.factorio.com/mod/WideChestsUnlimited) (required)
* [Ghost Scanner](https://mods.factorio.com/mod/GhostScanner) (required)
* [Stack Combinator](https://mods.factorio.com/mod/stack-combinator) (required)
* [Auto Research](https://mods.factorio.com/mod/auto-research) (recommended)
* [Nanobots](https://mods.factorio.com/mod/Nanobots) (recommended)
* [Noxy's Waterfill](https://mods.factorio.com/mod/Noxys_Waterfill) (recommended)
* [Moar Radar](https://mods.factorio.com/mod/Moar-Radar) (suggested)

Install these using the in-game installer so that all the dependencies are also installed.

Yes, both "loader redux" and "miniloader" are required.  The former is the default loader for the train stations (being that it's by the same author an LTN) but there are a few cases where filters need to be set programatically and that is only possible with a "miniloader".

You'll need the following blueprint books:

**Import blueprint books only AFTER all mods are installed!** (Or things will be missing.)

* [Space Exploration](https://github.com/bcwhite-code/brians-blueprints/releases/tag/self-building-spacex)
* [Self-Building Factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD)
* [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW)
* [Brian's Trains (auxilliary)](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy)

## Configuration

During the creation of the initial ("Nauvis") world:

* Increase the size and richness of all ore/oil patches to maximum.
* Change the frequency of  copper and iron to 200%
* Reduce the amount of water, set it to the minimum, or turn it off completely (uncheck).
* Turn off all enemies.  Unless you want to manage that manually.
* Turn off pollution (less calculation == more UPS)
* Cliffs and trees are optional.  I tend to reduce the former and keep the latter.

In the Mod Settings for _Startup_:

* Merging Chests: Set "Mergable chest" [sic] to "Iron Chest".
* Set "Maximum chest width", "Maximum chest height", and "Maximum chest area" all to 150.
* Set "Inventory size limit" to 1000.
* Set "Whitelist of merged chests" to "1xN Nx1" (reduces memory consumption).
* Waterfill: Set "Waterfillable" to "Everything".

In the Mod Settings for the _Map_:

* LTN: Set "Stop timeout" to 300.  Enable "Schedule circuit conditions".  The designs still work without this but will sometimes have to wait for the stop-timeout.
* Ghost Scanner: Set "Update frequency" to 3600.  Set "Scan Result limit" to 0 (zero).

In the Mod Settings for the _Player_:

* Uncheck "Factorio Alerts".  Otherwise you'll get a lot of annoying warnings about trains with "missing cargo" and the like.  (It's intentional but the disable-warnings signal is not respected.)

## How to Build

See the [main SBF document for "The Build"](https://docs.google.com/document/d/1b7OT1-h5GWfey4rIVNbMCXX-dMkoWLmcURutqrliLYE/edit#heading=h.qqx59ll9md1) but note the following differences:

* Every rail station is an "[aux](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy)" station with merged chests.  Merging **must** be done **after** all chests and medium power poles are placed.  For full blocks, this is possible once phase#1 is complete (i.e. when construction is in phase#2 or later).  For quarter-blocks, wait until a delivery for LTN stations happens.  From map view, run the merge tool over the _entire block_ and not just obvious rail stations.  If merging is forgotten, stations will not function but won't "fail" either.  It's safe to merge chests even after deliveries begin.
* Quarter-block blueprints don't use the standard "Construction Site".  They use the "General Construction" version from the "Construction" sub-book of the SBF.  Just place that on the side to line up with the roboports there and turn it on as usual.  Removing it after construction is likely to remove the rail signal there, too, but there's an unconnected one just off from the track to show where it was.  Add it back and remove the unconnected one.

## Build Order

"Booting up" isn't covered but there are some blueprints in the book
to help out.  Place the Mall ghost before anything as it'll be taking
most of the product from the boostrap process.

Automate whatever is useful (yellow belts and red science, perhaps)
but also route some yellow belts of iron and copper plates to the Mall
inputs.  These will eventually run dry but by then it can be served by
trains.

Basic mines aren't included and the "Mine" block isn't suitable until
later.  Build them by hand using track from the SBF book and stations
from BT/aux book, adding more mines as necessary.  Be sure to connect
red & green wires from the big power pole to the rail power poles if
you want to have an accurate status report of available resources.

* [Mall](#mall)

That's pretty much it for now.  Nothing else is needed until it
launches a rocket.  While waiting for all the necessary research to
occur, lay down rail block ghosts (filling only the power poles) and
mines for all the ore types except uranium.  It's possible to have
provider stations be completed (including merged chests) except for
the rail and the LTN stop long before they're needed.  Later, the
rail, signals, etc. can be placed quickly.

* Home: Build beside Mall.
* Iron Smelter.
* Belts: This is a "quarter block" blueprint.  _Read blueprint comment!_
* Copper Smelter.
* Starter Circuits: _Read blueprint comment!_
* Basic Science: Place beside mall with factory side close.  Connect logistic networks.  Manually build out the station side.  Prioritize coal, stone, iron, & copper.
* Refinery: Will require a second placement once waterfill is down to place pumps.  No blue-belts yet so use planner to downgrade all blue to red and **turn on** the extra config combinator to add red belts to phase#2 of the construction.  Later, when blue belts do become available, reverse this.
* Steel (electric)

Since the refinery will soon export sulfuric acid, now would be a good time to build a uranium mine.

* Low-Density Structures: _Read blueprint comment!_  (It's like "Belts".)
* Nav Sats. Provides data about the solar system and allows space travel.





* Bricks & Glass.


* Depot Hub

If you haven't created a uranium mine, now would be a good time as power is
probably soon to become an issue.  The acid requester may need a higher
priority to be sure it gets fulfilled ahead of less important ones.

The self-building "Mine" block can be used from here as well but it's only
useful in a block with multiple large resources patches.

Start research of kovarex and nuclear power.  Re-place the Mall as research
happens so the parts start being built.

Also be sure the Starter Circuits block is fully filled out except for modules.

Going forward, many of the blueprints will be "quarter blocks" that attach only
at one of the four corners.  They build in a similar way except use the "General
Construction" blueprint on one side and don't have phases because they don't
have a configuration of materials.  _Do not merge chests until LTN Stations are
delivered._ Note that removing the construction station will generally also
remove a train signal that sits in that area.  There is an unattached
(blinking) one just off to the side that shows where it was; remove the
unattached one and place it on the side of the rail at the same level.  (Though
it sounds confusing, it'll be quite obvious when the time comes.)

* Kovarex/Nuclear (2.4GW)
* Speed Modules

There's a bit of a catch-22 here.  Module production needs red circuits and
processors.  Red circuits and processors need plastic.  Plastic production is
slow without modules.  There should be enough reserve to belt out a few hundred
prod-3 modules for the Refinery to help move things along.  Move a bunch by
hand if necessary.

* Production Modules

With both module types now available, the Starter Circuits can be completed
which will give more processors.

* Low-Density Structures

At this point, there's enough infrastructure to launch navigation satellites
which is very useful because it allows adjusting things at a distance.
However, two other things are more pressing: a shortage of circuits and,
possibly, a shortage of power due to an incoming CME.

* Nuclear (10GW): Build when necessary.  This will provide enough power for the rest of the game including defense against all incoming CME.  Note that it can take a long time for the Mall to create all the parts so start it a few hours early.
* Bricks & Glass
* Advanced Circuits
* Processors
* Basic Circuits


## Blocks

More detail on how to create/manage some blocks is below.

### Mall

_Read the blueprint notes!_

Use upgrade planner to change yellow chests to wooden.  Place them.
(Nanobots are awesome!)  Then reverse the upgrade and leave it
pending.  Do the same with red chests.  Later, bots will put
everything back in order.

Change the electric furnace to stone/steel furnace (with a
long-handled inserter to feed it sand).  Fuel it with a chest full of
coal.  Change it back later.

Set refinecy recipe to basic processing (output only methane) until
"advanced oil processing" is researched (requires blue science).

There are inputs from outside the block for various simple materials.
These will need to come from "bootstrap" factories around the starting
resource patches.  Some simple blueprints are available in the
"bootstrap" sub-book to help with this.

Only merge the the chests of the stations.  Running merge on the
entire block might catch a few side-by-side iron chests that should
_not_ be merged.

Aim research towards the "Rocket Silo" then "Construction Robotics",
inserting anything else you need/want ahead of it.

Blue and Black sciences are produced in reasonable numbers but aren't
routed to the labs.  You'll have to move them manually.

It will eventually launch a rocket with a satellite.  This unlocks
satellite navigation, provides telemetry for "rocket" (orange)
science, and most importantly, will reveal a "weapons cache" somewhere
on the map.  You need to get the items from that to complete the
Construction Supply station!

The single rocket launch eventually produces 800 orange science.  Use
them wisely.

Note: The Mall doesn't produce _everything_.  Some things will have to
be hand-crafted and dumped into the logistics network via "trash
slots" and others will have to be produced in space.


