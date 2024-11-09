# Brian's Trains (Auxiliary)

The main [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW) is intended to work on "vanilla" Factorio with no mods except the [LTN](https://mods.factorio.com/mod/LogisticTrainNetwork), and even that isn't strictly necessary.

There are certain optimizations, however, that can be done when other mods are installed, optimizations that are incredibly useful if you're building a train network for an Angel's & Bob's factory.

If you're willing to install:

- [Loader Redux](https://mods.factorio.com/mod/LoaderRedux)
- [Merging Chests](https://mods.factorio.com/mod/WideChests) + [Unlimited](https://mods.factorio.com/mod/WideChestsUnlimited)

then these extra blueprints will save a huge amount of resources and space as well as having much less impact on UPS. If you look at the image to the top-left, you can see a the vanilla blueprint for a single-car station on top and the optimized blueprint on the bottom. It's quite the improvement.

The narrower station design, even with extra logic and belting to keep the two sides balanced, is 1/2 the width which means it's possible to have about 2x as many stations in the same space. Included in the blueprint book are 7-station designs for 2, 4, and 8-car trains. I've also included double-width 17-station designs for 2-car and 4-car trains. (Yes, I've actually used those when bringing in materials for an Angel's & Bob's factory.)

## How to Use

For the "Merging Chests" mod, go to the "Startup" settings and change the "mergable chest" [sic] type to "iron". Also set the maximum height and width to at least 64. It's okay to lower the maximum chest area to keep memory-use down. I set that to 100.

Installing one of the new stations is fairly easy but does involve a few steps.

1. Choose a size. Personally, I plan around having a maximum of one blue-belt per car, preferably less. More than that can mean a lot of trains roaming around with the resulting contention. Later, if necessary, some stations can be upgraded to as much as two blue-belts per car and still be fully functional.
2. Place the station blueprint. Make sure you have the correct type: provider or requestor.
3. If you're using Bob's Mods, you'll probably want to use an upgrade-planner to change the chest inserters to whatever you can actually build. Once you have red stack inserters, that's probably as high as you need to go. If you add the side-balancer, change the belting to "basic".
4. Merge the chests by activating the tool and drawing a box around the entire station (or multiple stations). The merged chests can't be part of the blueprint without having separate horizontal and vertical prints. If you want it placed by bots from outside rather than a personal roboport, chest merging has to be done after all are placed.
5. Add loaders and belting. Use a matching provider/requester loader configuration on an end or on either side. You can easily connect as many belts as you want this way. Just remember that the trains still need to be able to keep the buffer chests full -- anything more than two blue-belts per car is impractical and even that works only if you have a stacker.
6. If it's a _provider_ station, block off most of the chest capacity. Open each (merged) chest, scroll to the bottom, click the red X, scroll back to the top, and block off all but 5, 10, or 25 rows for 1, 2, or 4/8 car stations. Each car being loaded will draw 20 stacks from each side so 5 rows from both can fill 2.5 cars. Storing more than a few rows just wastes resources.
