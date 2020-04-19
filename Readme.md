# Firework Module

Welcome to my work, In this work I built a python module
to use in your __RaspberryPi__ and __SenseHat__!

## Hardware

For you use this module you need:
- RaspberryPi
- SenseHat

If you don't have a RaspberryPi or SenseHat, you can use a SenseHat
emulator, for exemple: [Trinket](https://trinket.io/sense-hat)

## How to use?

1. You need install 3 modules:
    1. time
    2. random
    3. sensehat
2. Download the _FireWorkModule.py_
3. Add the module in your program
4. Run :)

## Command

```
import FireWorkModule

FireWorkModule.fire()
FireWorkModule.explosion()
FireWorkModule.stick()
```
***
Params for `FireWorkModule.fire()` and `FireWorkModule.stick()`
* Length
* Color
* Limit
* Ground
* Background
* Velocity
***
Params for `FireWorkModule.explosion()`
* Point
* Color
* Velocity
* Background
* Length


## Contributing

Pull requests are welcome in this work, For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
