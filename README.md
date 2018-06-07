<h1 align="center">  
    Anton  
</h1>  
  
<h4 align="center">A database management tool built on top of <a href="http://flask.pocoo.org/" target="_blank">Flask</a>.</h4>
 
 <p align ="center">
<a href="https://goo.gl/BG4WQy">Abstract</a> | 
<a href="https://goo.gl/XbmUoK"> Documentation |
<a href="#getting-started">Getting started</a> |
<a href="#features">Features</a> |
<a href="#license">License</a>
</p>
  
  ![screenshot](https://lh5.googleusercontent.com/gpLU1QmimKPGWipvBaVcr03Z2grPblOV3fXJ6HUqBe3eQy2HRP4Pxop9OF83I9_xHSDizrHXWrCrRfgJSFzF=w760-h637-rw)

## Getting started

### Prerequisites
* python3
* postgresql (>=9.5 required) 

### Installation  
```sh  
$ git clone https://github.com/shubham1172/anton/  
$ cd anton  
$ pip3 install -r requirements.txt  
```

### Running
```sh
$ python3 app.py
```
The default port is 80. If you want to run it on a different port,
```sh
$ python3 app.py -p [port]
```

## Features
Anton helps you manage databases easily. It supports only PostgreSQL for now.  The functionality is broadly divided into two	use cases:

 - Anton for developers
	 - Anton helps developers use databases in their apps without any hassles.
	 - With the rich API, any developer can get started with using a postgres database.
	 ![screenshot_func_dev](https://lh3.googleusercontent.com/yKu2zHcTfBRByJKKoulQv58wO-nP_OKNAt3sqOjlewQ-LEdrxcwPJnSsQODUGWWfgugcXnL_xIorvpI-tGMQ=w760-h637-rw)
- Anton for SQLphobic users
	- Anton provides a simple web interface to  interact with data. No more SQLing.
	- Easy to use UI makes life easy for Anton users.
![screenshot_func_users](https://lh6.googleusercontent.com/fZofcNx4sTgn4C6HiaPvc_EdFOBv4O25GAex6p1r2SiK45VfK16ucCMBw5b4Mgv4Jq490b6iIAKphVdK5Vlp=w760-h637-rw)

The complete list of features can be found in the [documentation](https://goo.gl/XbmUoK).

## License
Anton is licensed under the [GNU General Public License v2.0](https://github.com/shubham1172/anton/blob/master/LICENSE).