# Base Crawler
![Base Crawler](/res/assets/logo.png "Base Crawler is your anytime crawler buddy.")

Base crawler is an Python based tool which that facilitates [Selenium Framework](https://github.com/SeleniumHQ/selenium "Selenium HQ Github project.") usage.

This project can be configured at src/conf.py file. You can add as many actions as you want inside actions_list variable.

### Running crawler
This program supports 2 args: browser and timeout.

- browser means which navigator will be instantiatated by Selenium (Google Chrome or Mozilla Firefox).

- timeout is the amount of seconds the Selenium webdriver will use as it's own timeout.

```bash
    python -m src.main browser timeout
```
