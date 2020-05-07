## Contents
- [Getting Started](#Getting-Started)
- [Additional Arguments](#Additional-Arguments)
  * [Size](#Size)
  * [Generations](#Generations)
  * [Seeds](#Seeds)

## Getting Started
The script is dependent on three libraries: `numpy`, `matplotlib` and `argparse`. These dependencies can be installed through `pip`.

```
pip install numpy matplotlib argparse
```

Download `GameofLife.py` and `SeedDict.py`, and store them in a directory you're comfortable with. Then, navigate to them in command prompt. For example, if the files are stored within `/Downloads`, simply feed this into command prompt.

```
cd C:\Users\<Name>\Downloads
```

You're close to getting some sick gifs. Simply, put this into command prompt.

```
python GameofLife.py
```

Bang. By default, the script produces 100 states of a 100 by 100, randomly intialized world.

## Additional Arguments
The world can be seeded, and it's size along with the number of states to compute can be modified. These can be defined in command prompt.

```
python GameofLife.py [-h] [-size SIZE] [-generations GENERATIONS] [-seed SEED]
```

### Size
If you wish to define a World size of your choice, feed in its lenght and width seperated by a comma. Both should be integers.

```
python GameofLife.py -size 30,30
```

Here, 100 generations of a randomly initialized world will be produced.

### Generations
The number of generations to compute. Again, this has to be an integer.

```
python GameofLife.py -size 30,30 -generations 25
```

Since we have defined the generations, 25 instead of 100 generations will be produced.

### Seeds
There are a number of Seeds to choose from: Glider, Glider Gun, Toad, Blinker, Pulsar, Beacon, Penta-Decathalon, Diehard, Boat, Acorn, Spaceship and Block Switch Engine. Some examples:
 
|Glider             |Pulsar              |Spaceship              |Beacon              |Acorn              |
:------------------:|:------------------:|:---------------------:|:------------------:|:-----------------:|
![](Gifs/Glider.gif)|![](Gifs/Pulsar.gif)|![](Gifs/Spaceship.gif)|![](Gifs/Beacon.gif)|![](Gifs/save3.gif)|

To feed a Pulsar, place it within double quotes.

```
python GameofLife.py -size 30,30 -generations 25 -seed "Pulsar"
```

This will produce 10 generations of Pulsar, placed at the center of a 30 by 30 world of zeros.
