# Self-Building Space-Exploration

These blueprints are for Space Exploration games using the "self building factory" (SBF) system from my [self-building-factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD).

These cover a lot of the planetside work but the "space" aspect will
generally be omitted because:

* I don't want to spoil it.
* I don't use automated construction trains in space.
* The SE author specifically asks not to provide blueprints for too much.

Join the discussion [on Discord](https://discord.gg/eSt3Qd8D2e).

You'll want the following mods:
* [Space Exploration](https://mods.factorio.com/mod/space-exploration) (required)
* [Logistic Train Network](https://mods.factorio.com/mod/LogisticTrainNetwork) (required)
* [LTN Content Reader](https://mods.factorio.com/mod/LTN_Content_Reader) (required)
* [Space Exploration LTN integration](https://mods.factorio.com/mod/se-ltn-glue) (required for space elevator)
* [Loader Redux](https://mods.factorio.com/mod/LoaderRedux) (required)
* [Miniloader](https://mods.factorio.com/mod/miniloader) (required)
* [Merging Chests](https://mods.factorio.com/mod/WideChests) and [Unlimited](https://mods.factorio.com/mod/WideChestsUnlimited) (both required)
* [Ghost Scanner](https://mods.factorio.com/mod/GhostScanner) (required)
* [Stack Combinator](https://mods.factorio.com/mod/stack-combinator) (required)
* [Auto Research](https://mods.factorio.com/mod/auto-research) (recommended)
* [Nanobots](https://mods.factorio.com/mod/Nanobots) (recommended)
* [Noxy's Waterfill](https://mods.factorio.com/mod/Noxys_Waterfill) (suggested)
* [Moar Radar](https://mods.factorio.com/mod/Moar-Radar) (suggested)
* [Early Logistics System](https://mods.factorio.com/mod/wret-early-logi-system)  (suggested)

Install these using the in-game installer so that all the dependencies
are also installed.

Yes, both "loader redux" and "miniloader" are required.  The former is
the default loader for the train stations (being that it's by the same
author as LTN) but there are a few cases where filters need to be set
programatically and that is only possible with a "miniloader".

The "waterfill" mod was a requirement in my original designs (though
only for Nauvis) but I've been working on removing it.  There may
still be some blueprints here and there that still use it.

You'll need the following blueprint books:

**Import blueprint books only AFTER all mods are installed!** (Or things will be missing.)

* [Space Exploration](https://github.com/bcwhite-code/brians-blueprints/releases/tag/self-building-spacex): Most builds will come from this book.
* [Self-Building Factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD): Needed for general rail grid and station track from the "Rail Templates" sub-book.
* [Brian's Trains (auxilliary)](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy): Needed for train stations when manually building mines.
* [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW): Needed for fluid train stations when manually building oil fields and for building new trains.

## Configuration

In the Mod Settings for _Startup_:

* Merging Chests: Set "Mergable chest" [sic] to "Iron Chest".
* Set "Maximum chest width", "Maximum chest height", and "Maximum chest area" all to 150.
* Set "Inventory size limit" to 1000.
* Set "Whitelist of merged chests" to "1xN Nx1" (reduces memory consumption).
* Stack Combinator: Set the "Maximum signal capacity" to 100.
* Waterfill: Set "Waterfillable" to "Everything".

In the Mod Settings for the _Map_:

* LTN: Set "Stop timeout" to 300.  Enable "Schedule circuit conditions".  The designs still work without this but will sometimes have to wait for the stop-timeout.
* Ghost Scanner: Set "Update frequency" to 1800.  Set "Scan Result limit" to 0 (zero).
* Stack Combinator: Set "Signal update delay" to 20.

In the Mod Settings for the _Player_:

* Uncheck "Factorio Alerts".  Otherwise you'll get a lot of annoying warnings about trains with "missing cargo" and the like.  (It's intentional but the disable-warnings signal is not respected.)

During the creation of the initial ("Nauvis") world:

* Increase the size and richness of all ore/oil patches to maximum.
* Change the frequency of  copper and iron to 200%
* Reduce the amount of water, set it to the minimum, or turn it off completely (uncheck).
* Turn off all enemies.  Unless you want to manage that manually.
* Turn off pollution (less calculation == more UPS)
* Cliffs and trees are optional.  I tend to reduce the former and keep the latter.

## How to Build

See the [main SBF document for "The Build"](https://docs.google.com/document/d/1b7OT1-h5GWfey4rIVNbMCXX-dMkoWLmcURutqrliLYE/edit#heading=h.qqx59ll9md1) but note the following differences:

* Every rail station is an "[aux](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy)" station with merged chests.  Merging **must** be done **after** all chests and medium power poles are placed.  Both construction stations have a speaker alert for when it is time to do this.  When it rings, apply the "merge" tool over the (quarter) block and then use the destruction planner to remove the speaker providing the alert.  Both actions can be done from the "map" or "sat-nav" view so no need to travel to the actual site.
* Quarter-block blueprints have their own version of the Construction Site.  Note that removing the Site after construction is likely to remove a rail signal at the end but there's an unconnected one just off from the track to show where it was.  Add it back and remove the unconnected one.  This probably sounds confusing but it's quite obvious when you see it.


## Build Order

"Booting up" isn't covered but there are some blueprints in the book
to help out.  Place the Mall ghost before anything as it'll be taking
most of the product from the boostrap process.

Automate whatever is useful (yellow belts and red science, perhaps)
but also route some yellow belts of iron and copper plates to the Mall
inputs.  These will eventually run dry but by then it will be served by
trains.

Basic mines aren't included and the "Mine" block isn't suitable until
later.  Build them by hand using track from the SBF's "rail templates"
sub-book and stations from BT/aux book, adding more mines as necessary
throughout play.  Be sure to connect red & green wires from the big
power pole to the rail power poles if you want to have an accurate
status report of available resources.

And then build...

* [Mall](#mall)

That's pretty much it for now.  Nothing else is needed until it
launches a rocket.  While waiting for all the necessary research to
occur, lay down rail block ghosts (filling only the power poles) and
mines for all the ore types except uranium.  It's possible to have
provider stations be completed (including merged chests) except for
the rail and the LTN stop long before they're needed.  Later, the
rail, signals, etc. can be placed quickly.

* [Home](#home): Build beside Mall with personal train being directly adjacent.
* Iron Smelter: Temporarily turn off combinator near Mall station that disables supply of belts.
* Belts: This is a "quarter block" blueprint.  _Read blueprint comment!_
* Copper Smelter.

Re-enable the combinator in the Mall that disables the local supply of
belts since they're now being produced in greater quantities by the
dedicated block.

Many of the blocks include modules.  They'll run fine without them for
now but the Construction Site will not report "finished" until all the
modules are supplied... which will be a long time coming (on the order
of "days").  That's okay.  Just be sure that the full-block
construction areas don't overlap as that can lead to LTN station being
placed too soon and wreak all kinds of havoc.  Quarter-block areas
shouldn't have any such overlap so are safe to be adjacent within a
block.

* Starter Circuits: _Read blueprint comment!_
* Water.
* Basic Science: Place beside mall with factory side close.  Connect logistic networks.  Manually build out the station side.  Prioritize coal, stone, iron, & copper.
* Refinery: Will require a second placement once waterfill is down to place pumps.  No blue-belts yet so use planner to downgrade all blue to red and **turn on** the extra config combinator to add red belts to phase#2 of the construction.  Later, when blue belts do become available, reverse this. Re-place when Coal Liquefaction eventually becomes available.
* Steel (electric).
* Depot Hub: There are no requester chests so manually put fuel into the feeder chests so trains can be refueled.  (Or use the "Early Logistics System" mod to create perfectly usable requester chests for this application.)

Since the refinery will soon export sulfuric acid, now would be a good
time to build a uranium mine.

The self-building "Mine" block can be used from here as well but it's only
useful in a block with multiple large resources patches.

* Low-Density Structures: _Read blueprint comment!_  (It's like "Belts".)
* Nav Sats: Provides data about the solar system and allows space travel.
* Solar (128MW): (optional) The Mall should have sufficient batteries and glass to slowly fill this block.  Most useful is the accumulators as they provide a general buffer that helps the steam block adjust its output as needed.
* Rocket Sections: _Read blueprint comment!_
* Speed-1/2/3: This will have to be placed multiple times as research progresses.

At this point, Nav Sats should have produced enough telementry and
shipped it to Basic Science to finish researching nuclear power, cargo
rockets, and then every other non-space technology.  Re-place both the
Nav Sats and the Rocket Sections blueprints to ensure they have the
full assembler configuration.  Then do any downgrades to asm2 that are
necessary.

Nav-Sats can be temporarily disabled (turn the config combinator for
the station to "off") if it's drawing too many resources.

* Nuclear (480MW): There is no Kovarex in this block but it'll provide some power and nuclear fuel for later off-planet exploration.

The Mall has a personal cargo rocket silo that will begin to be built
and fueled but the assemblers that create the silo and landing pad
will need to be hand-fed some missing items until the logistics
network is researched.

At this point, connect the belts that bring the science packs to the
export station.

Load the rocket by dropping a pod into it (there will be some in the
Nav-Sats block) and turning on the combinators for "ORBT".  When
everything has been fetched to the warehouse, turn on the "LOAD"
combinator to move everything to the rocket.  It's possible to switch
back and forth between the "fetch" and "load" modes.  Just be sure,
upon returning from space, to **turn off** the combinators listing the
desired contents before switching out of "load" mode.

Once in orbit, there are a couple logistics chests that can be brought
back and placed in the Mall to falicitly automatic construction of
things instead of hand-feeding them.  Use wisely!

Use space science to research "Speed module 3", "Automation 3",
"Logistics 3", "Nuclear Fuel Reprocessing", "Condenser Turbine", 
"Production module 3", ...

Upon return to Nauvis, keep the Mall up-to-date with research and make
sure delivery capsules are getting the needed inputs.  Some others
will need hand-feeding (or "Early Logistics" mod requesters), too.

* Bricks & Glass.
* Heat Shields.
* Sulfur.
* Delivery Capsules.
* Concrete: Preparing for War.  Or if you want to pave over the world.
* War: Colonization of other planets will come soon, some of which have biters even if Nauvis does not.
* Prod-1/2/3.

Yellow assembers, blue belts, and speed-3 module production should be
in full swing by this point so it's time to revert all downgrades made to
earlier blocks.  Prod-3 requires vulcanite, and a lot of it, which comes
later.

Start the cargo rocket requesting the items for delivery canon core mining
(shown as a core miner, delivery canon, and "8H") to go do mining on another
planet; it has enough supplies to run for about eight hours.  The Mall's
production of delivery capsules isn't enough even if delivery canon capsules
have been running continuously since returning from orbit but the dedicated
block will speed things up.  While that is happening...

* Basic Cores (Nauvis).
* Cryonite Cores.
* Barrelling: There's no Construction Site for this one; it has to be built by hand, ideally near the refinery fluid outputs to minimize train travel.  If not using waterfill, will need water pumped in.
* Pyroflux Overflow.

When the delivery capsules are done and everything has been loaded
into the rocket but nuclear fuel cells, grab the necessary amount from
the reactor block.  Switch the rocket to "load" mode and find a good
cryonite planet/moon, ideally without any biters ("threat").  Set that
as the destination.  When the required liquid fuel has been loaded,
get in and launch.

Build a "Core Miner (cannon)" on top of a convenient fissure, sending
to the receiver in the Cryonite Cores block.  (See blueprint comment
for details on its setup.)  Then use the landing pod to return to
Nauvis via an "emergency burn"; it'll land some random place so be
prepared.

(If the cargo rocket still isn't ready, there are more blocks below
that can be built while waiting.)

* Cryonite: Set the provide threshold for rods to 10 stacks because of the limited input ore.
* Efficency-1/2/3.
* Data Substrates.
* Rocket Fuel.

With this, all the ingredients for making "utility" science packs are
available.  However, they have to be made in space and so it involves
another rocket configuration and some fetching of items by hand to be
able to produce a few thousand of them.

I don't provide blueprints for crafting this science pack, though!
Have fun with it but don't go overboard: A bigger science installation
will come later; this just needs a minimal build to get through the
basics. Some factory components necessary for this can only be
manufactured in space so remember to take the basic building blocks on
the rocket or in personal inventory as well.

The 4k of "space" science is likely gone so take more building blocks
for that along with an equal amount of the basic science packs.

Research "logistics system" first so that the factory can finally use
logistic bots to move material.

Once that is running and you're back on Nauvis, start loading another
"core" rocket, this time for vulcanite.

* Vulcanite Cores.
* Vulcanite: Set the provide threshold for cubes to 10 stacks because of the limited input ore.

Now find a Vulcanite planet and create a core miner there, too.

The crafting of Prod-3 modules is still some time off and even longer
before enough are producted to actually finish the myriad of
construction sites waiting for them.  Patience.

* Bots.
* [Bulk Receiver](#bulk-receiver).
* Scrap Recycling.

Back to space to create "production" science packs and start research
with them, too, beginning with "kovarex enrichment" (1500 science!), "effect
transmission" (75), and "coal liquefaction" (200).

Back to Nauvis...  Ensure that all the "module" blocks have the full
set of recipes.  Then:

* Kovarex/Nuclear (2.4GW).

The amount of cores sent by delivery canon can be enough to keep
science research going but not enough to catch up on all the builds
waiting for production modules.  It's time to make use of that bulk
receiver...

Add a second Vulcanite core miner but this time use the "rocket"
delivery mechanism going to one of the bulk receiver pads.  It'll
require the configuration of a pair of delivery canons in the Mall to
send the necessary fuel.  When the delivery-canon version runs dry,
replace that with another rocket version.

The same can be done for Cryonite if necessary but it doesn't have
much demand outside of science and making ice in the Mall.

Note that the delivery cannon pair for rocket-fuel will only send 500
capsules before stopping since there is no direct feedback as to when
the receiver is full.  When it's necessary to send more (there will be
a speaker alert), toggle the "RESET" combinator to start the count
again.

That's the basics, though more capacity will be needed for some
things...

* Smelter (Electric).
* Advanced Circuits.
* Processors.
* Basic Circuits.
* Capsules.

Now it's time to really colonize other planets in order to gather
large amounts of resources in a self-sustaining way.  Start with
Cryonite since rockets are bringing enough Vulcanite for the moment.

Create a cargo-rocket config for the "Colony Home" block (there's one
in the book) and start it loading.  Some things may need to be
hand-crafted or fetched from other blocks.

* [Off-World Supply](#off-world-supply): Start it building but don't configure it just yet.
* Recycling Pad: The pad's name doesn't get saved in the blueprint.  Change it to "Recycling" once placed.

No need to wait for these to finish before proceeding as they can be
configured via sat-nav view even if on another planet.

Once the rocket is ready, choose a Cryonite world, ideally with water
and no threat.  Using satellite view, be sure you can actually find a
good ore patch -- sometimes they won't be close or even common!  Go
there and build the [Colony Home](#colony-home) block in a convienent
place.

Using the sat-nav view, configure the [Off-World
Supply](#off-world-supply) for this new colony.  It'll start bringing
in material by rocket, including the things necessary to expand the
rail grid and build a Cryonite mine.

Build a mine for Cryonite ore.  Two efficiency-1 modules per large
miner will reduce power consumption by 80% which is a big help in a
power-starved colony.

Cryonite has stacks of only 20 but processed Cryonite rods has stacks
of 200.  Since rocket parts and rocket fuel has to be imported, it's
best to be as dense as possible and that means building a local
processing factory.

On Nauvis, configure two more pads of the Bulk Receiver for Cryonite
Rods and Glass.

On the new planet, build the following.  Note that construction is
done the same as on Nauvis.  The Home block will forward the request
and the Off-World Supply will fulfill it, though somewhat slower than
a Nauvis build.

* Cryonite.
* Bulk Launch System: Add a second rocket silo according to blueprint instructions.  Configure for Cryonite Rods and Glass with destinations in the Bulk Receiver.  Ensure everything, including fuel, can reach the second silo!  Since Cryonite processing has a 1-car train for glass, the min-length of trains needs to be reduced from 6 to 2.

The home block's reactor will support all this as long as the miners
have efficiency modules.

The petroleum gas "bulk" supply will need to be changed to heavy oil.
Just change every instance of the fluid and barrels around the head of
the station to be the new type.

Once all is running smoothly, head back to Nauvis.  Use either a
capsule's "emergency burn" or the personal cargo rocket.

* Water Ice.

Now repeat all that but on a Vulcanite world!

Instead of "bulk" heavy oil replacing petroleum gas, that stays but
sulfur needs to be added.  To do this, add a sulfur filter to the two
blue loaders off the red warehouses and the two red loaders off the
yellow warehouses (for cleaning up after crashed rockets).  Also add a
third rocket silo that transports enriched vulcanite to yet another
pad in the bulk receiver.

Nauvis will now be well supplied with both Cryonite and Vulcanite so
it's time to go to space and build a "space mall" for all the things
that can't be built on land.  Nauvis Orbit ("norbit") could host this
but it's better to move to Calidus Orbit because of the greatly
increased solar power available.

No "space mall" blueprint is included in the book but there are
blueprints to help move ingredients from Nauvis and return finished
products to Nauvis for inclusion in the general build system.

On Nauvis, you'll want...

* Off-World Supply.
* Bulk Launch System: For receiving large quantities of raw materials.  These can be brought by the off-world supply rocket but if a lot is needed, there is no beating dedicated rockets.
* Wood Recycling.

One of the biggest difficulties is that scaffolding can no longer be
made on the planet surface which means transporting 5x as many stacks
of material to space to produce the same amount, and you'll need a lot
(like tens of thousands) of scaffolding just for the space mall.

In this same space will be the main science factory so keep that in
mind as it will probably need *hundreds* of thousands of scaffolding to
complete.

Personally, I don't use trains or city blocks in space because
everything is planned to produce specific outputs but it can be done
that way.

At this point, it's probably best to return to Nauvis and beef up the
production there.

When ready, return to Calidus orbit and start building a real science
factory.  It'll likely require having a large amount of many resources
transported by bulk rocket with another bringing in the rest using another
Off-World Supply.  My personal factory has 12 bulk landing pads.

Other planets will have to be colonized to get Iridite, Holminite,
Beryl, and Vitamilange, also processed locally before being shipped to
Nauvis.  The Vulcanite and Cryonite words might need one or two more
processing blocks there, too (with added power to boot).

There are no blueprints for the processing of these new raw resources
-- they're part of the challenge that is Space Exploration.



## Blocks

More detail on how to create/manage some blocks is below.

### Bulk Receiver

A block for receiving large amounts of cargo by rocket from other
planets.

By default, none of the pads are configured.  To set up a receiver:

* Change the name of the pad.
* Set the expected item in the constant combinator with a large value (like 1000).
* Change the name of the LTN station.  (optional)

Then tell the rocket to go to the named pad (or any pad with that
name) when its cargo is full.

### Colony Home

A base of operations and material transport for colony words.

Start by using the configuration combinators to load a rocket with
everything that is needed then launch to the desired world.  Make sure
any personal roboport is turned _off_ so bots don't start cleaning up
the mess upon arrival.  Also turn off "personal logistics and
auto-trash" so that bots don't replenish you instead of building.

Find a good location (water beside the water provider station is very
helpful) and lay the blueprint.  Collect solar panels, accumulators,
power poles, roboports, and construction bots from the cargo pods then
stand in the middle of the solar array and build it.  Once there is
power and the beginning of a roboport network, you can transfer the
bots to that and start moving material to a storage chest so the rest
can be built automatically.

Once there is water in the reactor, it can be started by manually
dropping a single fuel cell into each one.

If pumping water from a local source, also pump it to the reactor but
use a local pump with the same condition as the ice-water one so it
doesn't overfill.  Then reduce the threshold slightly for the
ice-water in order to lower its priority.

Fix some defaults:

* Change the signal receiver to moniter the channel "Nauvis/Home".
* Change landing pad beside red warehouse chests to "(world)/Home", substituting the name of the world.
* Change the landing pad beside the green warehouse chest to "-Personal-".
* Change the recycling rocket beside the plain warehouse chest to have a destination of Nauvis/Recycling and to "launch on cargo full".
* Change the channel of the transmitter near the reactor to "(world)/Cannons".
* Change the channel of the transmitter near the landing pads to "(world)/Home".
* Merge chests (only once all chests and power poles have been placed).
* Set the trains to "automatic" and put some rocket fuel in the back engines of the two reversible ones.

Now finish configuring the [Off-World Supply](#off-world-supply).

There are some add-on blueprints that merged later.  The necessary
build items will be included in the next rocket delivery.

1. Personal Train: Local version of the Nauvis Home train.
2. More Meteor Defense: In case you're truely paranoid about a meteor getting through on a world where they spawn biters.
3. Solar Support: Applied to the power switch between the reactor and the main grid, it'll disconnect whenever an outside solar field is supplying significant power even at night.

There are three bulk provider stations: two fluid and one item.

One fluid is configured to fetch and provide Sulfulic Acid (typically
for mining purpores).  The other is set for Petroleum Gas but this can
be changed to any other fluid simply by changing the type everywhere
around the station.  Neither will fetch barrels of the set type until
the constant combinator with the "W" setting is turned on; this
prevents fetching those fluids enless they're actually needed.

Later on, if it's necessary to bring it material in significant
quantities, they can be configured in the "bulk" combinator (it
actually says "bulk" next to it).  Set the filters in the blue loaders
from the red warehouse chests to match and all this will be made
available via a rail provider station.  (Don't remove the existing
filter item -- burner miners -- because if the loader becomes
"unfiltered" then everything will get sent to the station.)

The personal rocket allows flying around with a full load of cargo,
making it available via logistics, and the re-loading a new rocket for
the next destination.  Enable it by setting the blue logistics chest
feeding the assembler with a request for 20 _packed_ cargo rocket
sections.  Then drop a capsule into the silo whenever you're ready to
leave; doing so will move all the items from the buffer warehouse into
the new rocket.


### Home

This basic block contains a starter depot hub, a place to build/park
trains, some useful logic to see the state of the factory,
communication to off-world sites, a warning system about low power,
and an umbrella.

The "fuel" station configuration combinator needs to have the desired
fuel request amount made negative to work.  It's done this way so that
re-placing the blueprint at a later time won't revert the request to
something obsolete (like coal) and pollute the belts.

The accumulator and speaker in one corner track power generation and
warn if it is insufficient.  However, it needs more than the single
accumulator to be accurate.  Typically, more get added in various
power blocks.  Just remove these two items for now if they're a
nuisance.

When the signal transmitter gets build **change its name** to "Nauvis/Home".

Near the signal transmitter is a combinator with some constants that
will need to be updated as the game progresses:

* **C**: The number of (packed) cargo rocket sections necessary for a return trip.  This starts at 18 and can be reduced with "reusability" research.  Note that the exact number of returned rocket sections is random so give at least 10% extra.
* **R**: Reliability (aka "safety") of the items loaded into a rocket.  This is actually a divisor for the amount of extra items required so a value of 100 will result in 1% extra.  The default is 10 for 10% extra.

There is a "personal train" that auto-loads with the things necessary
to expand the factory just by driving around and replenishing the
personal roboport with items from the train.  But honestly, jetpacks
and long-reach to replenish directly from the Mall is easier.

### Mall

_Read the blueprint notes!_

Use upgrade planner to change yellow chests to wooden.  Place them.
(Nanobots are awesome!)  Then reverse the upgrade and leave it
pending.  Do the same with red chests.  Later, bots will put
everything back in order.

The stone/steel furnace has a chest for coal.  Manually fill this.

Set refinecy recipe to basic processing (output only petroleum gas) until
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
science, and most importantly, reveals a "weapons cache" somewhere on
the map.  **You need to get the items from that to complete the
Construction Supply station!**

If you don't catch the notice about the weapons cache when it happens,
you can find a link to in under the "exploration journal" in the
InformaTron ("i" key).

There are a number of requester chests used.  Until that becomes
available (in v0.5, it was available much earlier), items will have to
moved by hand or the chests replaced with "Smol" versions from the
"Early Logistics System" mod.

The single rocket launch eventually produces 800 orange science.  Use
this to research "Advanced Electronics 2" to be able to produce
processors then work towards the Cargo Rocket Silo.

Note: The Mall doesn't produce _everything_.  Some things will have to
be hand-crafted and dumped into the logistics network via "trash
slots" and others will have to be produced in space.

The Mall is not "fire and forget".  It'll need manual updates as the
game progresses:

* Re-place the blueprint with shift-click as new technologies are researched.
* Upgrade assemblers and inserters for things that are in short supply.
* When lubricant is brought by train, reverse the pump where it is produced locally so the resources can be used for other things.
* Hand-feed life-support assemblers (including hand-crafting the lifesupport facilities) to create the necessary canisters.
* Change the furnace creating glass to an electric one.  The long-handled inserter can become a stack-inserter.

#### "Personal" Cargo Rocket

The included cargo rocket allows for travel to orbit and other planets
and is largely automated for the loading.  Apply a signal via green
wire to the substation, put a capsule in the silo (a couple can be
found in the nav-sats block), and it'll request everything by bots.
When it's full (the blue chest shows no outstanding requests), turn on
the "load" combinator to move it all to the rocket.  When that
finishes, get in and go.

There are a few combinators included that can be turned on for first
trips to orbit and to neighboring planets for the purpose of setting
up core mining.  The rest is left as an exercise to the player.

Obviously, some things aren't produced by the Mall.  You'll have to
find some way to bring them from where they are produced and drop them
in the big warehouse (extras will be removed and taken away by bots).

Upon returning, turn off the config combinators and the "load"
combinator before putting another capsule in the silo.

There are a few things on one side for loading capsules, barrels of
rocket fuel, and packed cargo sections for taking the supplies
necessary to create "return" rockets but in the beginning, it's
easiest and cheapest to use the "emergency burn" feature of the
capsule.


### Off-World Supply

A system for delivering supplies to places off-world.

Once built and there is a [Colony Home](#colony-home) waiting for
supplies, configure this block:

* Change the name of the 3 LTN stations to replace "(world)" with the actual world name.
* Change the channel of the dish near the delivery cannons to "(world)/Cannons".
* Change the channel of the dish near the rocket silo to "(world)/Home".
* Change the destination of the ice cannon to be the receiver chest next to the reactor and turn it on.
* Change the destination of the two rocket fuel cannons to be the receiver chest besider the station and turn them on.
* Change the destination of the rocket silo to be "(world)/Home" with a launch trigger of "launch on green signal or when cargo full".

This can also be used for "non home" bases such as in space.  Any
landing pad will do.  Signaling works like this:

* green wire: General request.  Everything here will be loaded "best effort" into the rocket.  Smaller requests may be deferred so as to not request too many trains.  Include the receiving pad's contents in the local availability so that everything is counted from the moment the rocket lands.
* red wire: Required items and control.  If items are sent this way, they will be prioritized in the request and the rocket will launch soon aftero all the required items are loaded.  The requirement **must not be greater than** the general request (i.e. green wire) or it will never be fulfilled.

The following signals on the red wire will affect the launch:

* red X: Don't launch unless full, regardless of the "required items" request.
* F: The allowed number of _empty_ slots that still counts as a "full" rocket.  (It's "F" because it is added to the rocket's natural "F" and compared to 500.)


### Space Launch System

**Read the blueprint comment!** There is a companion "SLS Orbit"
blueprint; read that blueprint comment as well.

LTN in orbit will be effectively disabled when the elevator cable is
not fully finished.  It does this by detecting (crudely) if power is
available and changing the LTN ID# if not.  These "disabled" requests
will appear as LTN errors saying that something is not "found in
networks 0x100".  Once power is restored, delivers will resume.

This block supports three different things:

* Orbital Rocket Launches

This moves  items into orbit for launching via rocket to the final
destination with about 40k to 50k _less_ rocket fuel, effectively
halving most launch costs in that regard.

To configure an item, place it in the constant combinator for the
given rocket with a value of 1.  Then set the rocket to for the
desired delivery, typically "any station with the name" so it can
provide to anywhere.  Set it to "launch when cargo full".

If 14 rockets isn't enough, allow longer merged chests and extend it.

* Local Deliveries

At the top of the "items" station is a large warehouse with a
combinator beside it.  Put an item (with value=1) in the combinator
and that item will be fetched and stored in the chest, keeping it
somewhere between 180 and 500 stacks.  This chest and its loaders can
be duplicated across to have up to 10 different items available.

* Ship Fluid Supply

This moves up to 3 fluids into orbit for transport via ship (since
rockets can't carry liquids).  One of these fluids is rocket fuel; the
other two can be anything so long as they're supply 8-tanker trains.
Water is a likely candidate for one of them.

To transport a fluid it, add it to the #1 or #2 combinators found near
the head of the orbital fluid station.

* Receiving Items from Ships

Receves items from ships and transports them to the ground, thus
avoiding the need for rocket engines to leave the planet surface.

There is room for up to 12 LTN provider stations; just duplicate the
one there to align with the other big power poles.  Each should
provide a different type of item.

There are six 8-car trains in the space depot hub for handling these
requests.  Smaller trains can be added if necessary.  **Don't set them
to "automatic" until fuel has been delivered!**
