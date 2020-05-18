# Base Crawler
![Base Crawler](/res/assets/logo.png "Base Crawler is youy anytime crawler buddy.")

Base crawler is an Python based tool which that facilitates [Selenium Framework](https://github.com/SeleniumHQ/selenium "Selenium HQ Github project."). usage.
This project can be configured through src/conf.py file.
Add as many any actions as you want inside actions_list variable.

### Running crawler
This program supports 2 args: browser and timeout.

browser means which navigator will be instantiatated by Selenium (Google Chrome or Mozilla Firefox).

timeout is the amount of seconds the Selenium webdriver will use as it's own timeout.

```bash
    python -m src.main browser timeout
```
