# Brian's Trains (Auxiliary)

The main [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW) is intended to work on "vanilla" Factorio with no mods except the [LTN](https://mods.factorio.com/mod/LogisticTrainNetwork), and even that isn't strictly necessary.

There are certain optimizations, however, that can be done when other mods are installed, optimizations that are incredibly useful if you're building a train network for an Angel's & Bob's factory.

If you're willing to install:
 * [Loader Redux](https://mods.factorio.com/mod/LoaderRedux)
 * [Merging Chests](https://mods.factorio.com/mod/WideChests) + [Unlimited](https://mods.factorio.com/mod/WideChestsUnlimited)

then these extra blueprints will save a huge amount of resources and space as well as having much less impact on UPS.  If you look at the image to the top-left, you can see a the vanilla blueprint for a single-car station on top and the optimized blueprint on the bottom.  It's quite the improvement.

The narrower station design, even with extra logic and belting to keep the two sides balanced, is 1/2 the width which means it's possible to have about 2x as many stations in the same space.  Included in the blueprint book are 7-station designs for 2, 4, and 8-car trains.  I've also included double-width 17-station designs for 2-car and 4-car trains.  (Yes, I've actually used those when bringing in materials for an Angel's & Bob's factory.)

## How to Use

For the "Merging Chests" mod, go to the "Startup" settings and change the "mergable chest" [sic] type to "iron".  Also set the maximum height and width to at least 64.  It's okay to lower the maximum chest area to keep memory-use down.  I set that to 100.

Installing one of the new stations is fairly easy but does involve a few steps.

1. Choose a size. Personally, I plan around having a maximum of one blue-belt per car, preferably less.  More than that can mean a lot of trains roaming around with the resulting contention.  Later, if necessary, some stations can be upgraded to as much as two blue-belts per car and still be fully functional.
1. Place the station blueprint.  Make sure you have the correct type: provider or requestor.
1. If you're using Bob's Mods, you'll probably want to use an upgrade-planner to change the chest inserters to whatever you can actually build.  Once you have red stack inserters, that's probably as high as you need to go.  If you add the side-balancer, change the belting to "basic". 
1. Merge the chests by activating the tool and drawing a box around the entire station (or multiple stations). The merged chests can't be part of the blueprint without having separate horizontal and vertical prints.  If you want it placed by bots from outside rather than a personal roboport, chest merging has to be done after all are placed.
1. Add loaders and belting.  Use a matching provider/requester loader configuration on an end or on either side.  You can easily connect as many belts as you want this way.  Just remember that the trains still need to be able to keep the buffer chests full -- anything more than two blue-belts per car is impractical and even that works only if you have a stacker.
1. If it's a _provider_ station, block off most of the chest capacity.  Open each (merged) chest, scroll to the bottom, click the red X, scroll back to the top, and block off all but 5, 10, or 25 rows for 1, 2, or 4/8 car stations.  Each car being loaded will draw 20 stacks from each side so 5 rows from both can fill 2.5 cars.  Storing more than a few rows just wastes resources.

# Blueprint Changelog

History, in brief...

## V4.9
* Fixed default LTN thresholds in multi-provider.

## V4.8
* Fixed problems with multi-provider due to unbalanced sides.
* New side-balancer supporting multiple items.

## V4.7
* Added "multi" provide/request stations.
* Added negative channel "0" amounts for wanted items.

## V4.6
* Removed extra red wire in 1-car provider station.

## V4.5
* Apply 4.4 fixes in requester stations, too!
* Added signal wire to train stop on requester stations to be compatible with LTN "use signals" option.

## V4.4
* Added red+green along rows of chests so LTN won't go crazy if merging gets forgotten.
* Removed front balancers from all stations since it's not generally needed.  Can always merge the "Chest Balancer" blueprint on any of them if needed.

## V4.3
* Set LTN network IDs to match main Brian's Trains so other networks can co-exist.
* Combed power wires.

## V4.2
* Changed to use #stacks instead of #items in station configs.

## V4.0
* Updated to match main V4 blueprints.

## V3.1
* added missing chain signal on 18-station loops

## V3.0
* updated to match main V3 blueprints library
* _do not use_ on a base built with the V2 blueprints

## V1.0

* launched a rocket under Angel's and Bob's mods with these
* first public release
* for use with V2 of Brian's Trains blueprints _only_

## V0.X

* initial designs and testing
