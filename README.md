# UCI-RegCheck

UCI Registration Check is a program used for checking the registration status of courses at UCI. Since some courses do not have waitlists and spamming F5 is unreasonable, use this program to periodically check the [UCI schedule of classes](https://www.reg.uci.edu/perl/WebSoc) by using any course code for the current academic quarter.

Selenium and PhantomJS are used to scrape the above webpage for the current and max number of enrolled students in order to determine if the class is currently open or not.
