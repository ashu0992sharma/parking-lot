## Setup

First, install [Python3.x](https://www.python.org/downloads/). Then run the following commands under the `functional_spec` dir.

```
functional_spec $ python -version # confirm Python present
Python 3.x

```

## Usage

run application from `parking_lot` by doing


```
parking_lot $ bin/parking_lot
```
this will open a shell prompt which has commands like

```
create_parking_lot 6
park KA-01-HH-1234 White
park KA-01-HH-9999 White
park KA-01-BB-0001 Black
park KA-01-HH-7777 Red
park KA-01-HH-2701 Blue
park KA-01-HH-3141 Black
leave 4
status
park KA-01-P-333 White
park DL-12-AA-9999 White
registration_numbers_for_cars_with_colour White
slot_numbers_for_cars_with_colour White
slot_number_for_registration_number KA-01-HH-3141
slot_number_for_registration_number MH-04-AY-1111
```
also application can be given a file as input which should be present
 in parking_lot/fixtures directory
 
 ```
parking_lot $ bin/parking_lot file_input.txt
```


## Tests


run all tests from `parking_lot` by doing
```
parking_lot $ bin/setup
```

run a single test from `parking_lot` by giving a system argument 
e.g in below case we want to test for leaving a parking slot

```
parking_lot $ bin/setup test_leave
```

