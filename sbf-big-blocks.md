# Self-Building-Factory: Big-Blocks

_Go big, or go home!_

This expansion can be started any time after the first
[SBF](https://github.com/bcwhite-code/brians-blueprints/releases/tag/self-building-factory)
Refinery is built though it is probably best to get through "More
Plates" at the end of Phase 4 but **skip the Modules block**.  But if
you haven't yet done a complete play-through of the SBF, I don't
recommend attempting this.

This requires the same extra mods as the "aux" blueprints of the
original:

* [Loader Redux](https://mods.factorio.com/mod/LoaderRedux) (required)
* [Merging Chests](https://mods.factorio.com/mod/WideChests) and [Unlimited](https://mods.factorio.com/mod/WideChestsUnlimited) (both required)

The blocks of this book are **25x** the size of those in the original,
or 5x as long on each side.  Each blueprint is a _half_ block and
though there is typically a lot of empty space in the middle, it's
important for all four sides to be long enough for a single train in
order to eliminate the possibility of deadlock.

Yes, it takes a length 5x as long to fit _one_ train!  The trains that
supply these blocks are **100 cars** long that, pulled by **20
engines**, reach full speed in about 7.5 seconds when powered by
nuclear fuel.

The blocks are composed if identical "slices" of a factory, replecated
to draw from 100 train cars.  Each slice is independent but the train
cars obviously are not.  The upshot is that if the slices get out of
sync, then one slice may block causing the train not to fully unload
causing the train to wait causing other slices to starve etc. etc.
It's deadlock and it's permanent.  Only the mines and fluid providers
are immune to this.  **Never add or remove items manually or otherwise
adjust production.**

There's no power supply block here.  The standard SBF blocks will
suffice but expect to consume between 30GW and 50GW for one set of
7200 SPM.  "Elite" or "ultimate" solar is probably the way to go.  Be
**very careful** not to run short of power.  Glitching circuits or
slow inserters can cause an unbalance in train loading which will then
prapogate.

With the "Moar-Radar" mod, setting the "Nearby revealed range" to 20
in "startup" settings will make the entire map visible when radars are
placed in the corners.

## Construction

Each blueprint is a 1/2 block.  When the long track is at the bottom,
the entrance is on the right and the exit is on the left.  Orientation
and relative position to a block's source items can improve train
efficiency.

Factorio sometimes does not do cliff conflicts correctly and will not
create destruction plans for them which prevents bots from placing the
overlapping item.  If cliffs were not turned off when creating the
world, they can be removed using the command-line:

```
/c for k, cliff in pairs(game.player.surface.find_entities_filtered{type="cliff"}) do cliff.destroy() end
```

Construction will take a lot longer than the SBF blocks because the
new blocks are so big.  They're so big that Factorio may pause for a
number of seconds just dropping the blueprint.

Construction is handled by base SBF system.  Each half-block blueprint
has a spot for a construction station 1/2 way along its long side.
Build as normal (i.e. Construction Site first) with the following
exceptions:

### Grid

Construction does not build rail grid though it will build the block's
connections to it.  The rail grid needs to be built manually before
dropping construction site and the block blueprint.

### Bypass

There is a "bypass" through the middle and down the exit side of each
block that allows exiting trains to use either corner, somewhat
reducing traffic on the main grid.  This is **not** built by automated
construction.  If desired, it'll have to be built manually.

### Modules

Because all the "slices" must operate with identical throughput,
modules cannot be populated incrementally.  They must be all or
nothing.  Until the modules big-block is running, it won't be feasible
to populate modules in the blocks being built.  This is okay as they
can run at a lower capacity without modules for the time being.

**If the Modules block has been built...**

Construct as normal but _under no circumstances_ launch any trains
until construction is complete.

**If the Modlues block has _not_ been built...**

After placing the block blueprint (which is after the Construction
Site has been built):

* Go into the third constant combinator and _delete_ the signals for Prod-3 and Speed-3.
* Go into the constant combinator immediately beside the Ghost Scanner (it has rrocket fuel and nuclear fuel signals) and similarly add Prod-3 and Speed-3 with values of -50000 (i.e. _negative_ fifty thousand).

Start construction.

Under no circumstances allow any modules to enter the block as that
will break the syncronization between the slices.  That means **do not
re-place the blueprint as that will undo the changes made above.**

When construction is complete, launch the trains even though no modules have been fetched or placed.  Do _not_ remove the Construction Site!

Later on, once the Modules block _is_ running, come back to this site
and do the following:

* Be **absolutely sure** that the Modules block has enough of _both_ module types buffered in the provider station.  Check the local Ghost Scanner to see how many are needed.  The block being updated will be offline for the duration of the update and will not be able to provide material certainly necessary to the crafting of more modules.
* Remove the rail piece _after_ the stacker but _before_ the factory.
* Wait for all crafting to come to a _complete_ stop.  It is essential that absolutely no assemblers, furnaces, whatever are running.
* Remove the -50000 entries in the constant combinator beside the Ghost Scanner. Construction will reset and begin fetching the necessary modules.
* Once construction is again complete, replace the removed rail piece.

The block is now complete and the Construction Site as well as all
construction roboports (those without check-marks beside them) can be
removed.

### Train Fuel

The standard fueling station requests nuclear fuel for the trains.  If
none is available (the 2.4GW block creates it) the request can be
changed to -500 rocket fuel instead.

### Merge

Merge all chests in the block by selecting the "merge" tool and
dragging it over the _entire_ half-block.  It may take a few seconds
to run.

### Launch

Blocks don't start automatically.  When construction is complete, all
of the trains at the factory stations need to be set to automatic;
this is the minimum operating limit.  The other trains in the stacker
can be launched at any time, either when needed or immediately to
allow the factory to "work ahead"; this is the maximum operating limit.

Don't worry that the trains show that some kind of fuel is missing.
They request both nuclear fuel and rocket fuel but only need one or
the other.  As long as the fueling station is working, there will be
some fuel in the trains.

In addition, all of the trains can be found in the "Trains" sub-book.
If a block cannot get input material fast enough for constant
operation, more trains can be launched (from anywhere).  Also increase
the train-limit on the station receiving those trains if it is not
automatically controlled.  Extend the stacker if it becomes necessary.

### Enable

At the corner where the heads of all trains stop is a combinator with
signals for every output of the block.  Turn it on.

## Build Order

Building these blocks tends to be slow going but luckily there are not
that many of them.  Of course, in order to fulfill all the requests of
the eventual **7200 science-per-minute** block(s), more than one of
some blocks will certainly be needed.  This is left as an exercise to
the reader but note that deadlock can happen if there isn't enough
supply as the stacker fills up and trains start waiting on the main
track.

Placement/ordering of the blocks is important.  The junctions do not
allow U-turns (trains hit their own tails if they do) so while having
inputs being adjacent (short-side) to their source materials output is
very efficient and having them on the opposite half of the bloock is
reasonably efficient, having them across the tracks (long-side) is the
very _inefficient_.  For circuits, having the output of a lower teir
next to the input of the next higher teir is most efficient.

Have a plan before starting.  For example: Smelter at the top of a
block. Green Circuts at the bottom of the same block. Refinery above
the Smelter. Red Circuits to the left of that (also at the
bottom). Blue Circuits to the left of that. Modules to the left of
that.

* Connection

Use the "SBF/BB Connection" to create a link between the existing
factory and where the new blocks will go.  The two block types cannot
sit directly adjacent.  If the big blocks surround the small-block
factory, which would normally be the case, multiple of these can be
used to provide additional access points for construction and fuel.

* Controller

There needs to be exactly one "BB Controller" set somewhere.  It fits
inside any junction of the main SBF overlapping the big power pole in
the center.

* Mines

Mines will be needed for the four main ore types but not uranium.
There is no self-building for these because there is no standard
layout for ore patches and a generic layout would be massive simply
because of the size of these blocks.  Multi-ore support is also
unavailable because these are not LTN trains.  Mines have to be built
manually but don't bother going beyond seven blue belts per mine as
that's the fastest they can load trains.

It's best to go build mines whenever waiting for a block to build.
Iron and copper are the most used with coal and stone being a far
third and distant fourth.

To build a mine, start with the "base" block.  When ready, apply the
appropritate "overlay" to the stations and logic to turn it into a
mine of the proper type.  Also merge the chests.  Then start laying
down miners and belting it to the station, using the "Provider Chest
Loader" blueprints from the Brian's Trains "aux" book to fill the
merged chests.

Start with iron and copper mines as they're needed by the Smelter.
Coal will be required for the Refinery and stone (eventually) for
science.

* Smelter

* Electronic Circuits

* Fluids

These are very similar to Mines: build the "base" then apply the
desired "overlay".  Fill the outer tanks from with many feeds as
evenly spaced as practical, including the very ends.

* Refinery

Make sure "coal liquefaction" is researched before placing the
blueprint.

* Advanced Circuits

* Processors

* Modules

This block produces Prod-3 and Speed-3 modules both at a rate of 4/s
and provides them to the standard construction network.  This
alleviates the need of the Modules block of the SBF (and all it's
support) plus crafts them much more quickly... a good thing because
some big blocks can require upwards of 20,000 of _each_.

Since this block produces modules, it doesn't request any.  It will
populate its own modules once it starts running in order to run even
faster.  It can do this only because it has no _productivity_ modules
and thus the amount of output for a given input is constant even if
some slices may run a bit faster when only partually populated.

* Foundry

* Low-Density Structures

* Science 4

Best to start with this "final" block simply because it can take a
long time to craft the 50 rocket silos it needs.  The trains can also
run ahead and pick up all the necessary science packs as the other
blocks are built.

Placing them so that 1 through 4 are in a single line allows the
"packs" train to simply run from one to the next.  (Take note of the
entrace and exit corners so as to not reverse the order.)

* Science 1

* Science 2

* Science 3

That's it.  Start researching those infinite techs, probably starting
with Mining Productivity.

If science is able to remain fully fed, build another set of them.
Then another.  Let me know when the UPS gets below 1.0.

## Miscellaneous

Just some notes that don't really belong anywhere...

* Though this book uses quad-rail, there can be a lot of trains going through a relatively few number of junctions, often doing left turns or u-turns, which results in congestion.  Arranging the blocks so trains can travel in relatively straight lines is useful but hard to accomplish.  There is an (experimental) "congestion control" mix-in inside the Brian's Trains book that can be added.
