# UCI-RegCheck

UCI Registration Check is a program used for checking the registration status of courses at UCI. Since some courses do not have waitlists and spamming F5 is unreasonable, use this program to periodically check the [UCI schedule of classes](https://www.reg.uci.edu/perl/WebSoc) by using any course code for the current academic quarter.

Selenium and PhantomJS are used to scrape the above webpage for the current and max number of enrolled students in order to determine if the class is currently open or not.

## Getting Started

The following sections provide instructions to get a copy of the project set up and running on your local machine.

### Prerequisites

- This project uses Python 3.6.2 (although it _should_ work with any recent 3.x version... _no promises!_)

### Installing

- You will need to download [PhantomJS](http://phantomjs.org/releases.html) version 2.1 and add it to your system PATH.
- Next, run the following pip commands to download the remaining packages:

```
pip install selenium
pip install win10toast
```
With that, you have everything you need to run the project on your machine.

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details

## Acknowledgements

Shamelessly copied [PurpleBooth's lovely readme template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
