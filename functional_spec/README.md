# Functional Suite

`functional_spec/` contains the Rspec/Aruba based automated testing suite that will validate the correctness of your program for the sample input and output.

Please to add specs as needed when building your solution.

We do not support Windows at this point in time. If you don't have access to an OSX or Linux machine, we recommend  setting up a Linux machine you can develop against using something like [VirtualBox](https://www.virtualbox.org/) or [Docker](https://docs.docker.com/docker-for-windows/#test-your-installation).

This needs [Ruby to be installed](https://www.ruby-lang.org/en/documentation/installation/), followed by some libraries. The steps are listed below.

## Setup

First, install [Python3.x](https://www.python.org/downloads/). Then run the following commands under the `functional_spec` dir.

```
functional_spec $ python -version # confirm Python present
Python 3.x

```

## Usage

You can run the full suite from `parking_lot` by doing
```
parking_lot $ bin/run_functional_specs
```

You can run the full suite directly from `parking_lot/functional_spec` by doing
```
parking_lot/functional_spec $ bundle exec rake spec:functional
```

You can run a specific test from `parking_lot/functional_spec` by providing the spec file and line number. In this example we're running the `can create a parking lot` test.
```
parking_lot/functional_spec $ PATH=$PATH:../bin bundle exec rspec spec/parking_lot_spec.rb:5
```
