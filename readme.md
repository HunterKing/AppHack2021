# Grocery Best Prices App
This app was developed by [Hunter King](https://github.com/HunterKing), [Troy Miller](https://github.com/troyjmiller), [John Hall](https://github.com/johnghall), and [Joe Story](https://github.com/storyjss) for [Apphack 2021](https://cs.appstate.edu/apphack/), where it won 1st prize. Our presentation slides for this project can be found [here](https://docs.google.com/presentation/d/1HXOBaX3WNNkv4py6IXLdHf-NTM4BLjQLUUM3xVDbnhQ/edit?usp=sharing).

## Intent
We developed this app in order to shop for prices on items at various retailers such as Walmart, Harris Teeter, Amazon Fresh, BJs, and more. We utilized web scraping software [Selenium](https://www.selenium.dev/) and HTML parsing from [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/) with python in order to fetch data from the sites, and tied them into an app created using [Expo](https://expo.io/) with React Native and Typescript. To connect the two, we utilized [Flask](https://flask.palletsprojects.com/en/1.1.x/) on DigitalOcean in order to run our queries server-side.

## Usage
Use `npm install` to install the requisite packages, then use `npm start` to run. Please note that we have a hard-coded ipv4 address which is used to tie into our server, so it will not be able to make server-side queries unless you create a flask instance.

## Flask Setup
The venv contained in the flask_server folder (myprojectenv) contains all the needed python dependencies. Install Google Chrome v89 on the Linux machine you are running the server from. Use `flask run` for a local development server or uwsgi for deployment.
