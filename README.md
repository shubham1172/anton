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
  
  ![screenshot](https://lh3.googleusercontent.com/g8ur4Pkfxe7TTKquCTF2i2A6h8b1pZKrG2tdTfXRry3htn7t3h9UxbVnT9qjLR_Yf9ryrs9-DGPW9GY-n8Sje8eH3hpJs7sJFuotC_fX13hJVdyV6vkFp4OyR8BY6QrMMCVvZDGf68u3p93iyaKBlwJTH_JBEu9sjFFS20tnQPzzM9XN5xOHwrwamHr0a23XehONGZ1F8JPNqxFbkGLXzKDi92V4hOGDOm8y-ESvY9HEfgzlKVY5jprfShRPLys-IPKUktxpU0JFNs7VKhu_pUQOli4_n72R7pJXrc9HCBYeHf5rKe1Sef9leRNwxG3X-2Y76Nfbf6oI8vyQQflHH6r61_7QzEDDVpyoii2foIqCsmyLfiDu0PSYmb5ZtNQHId-P0aeaFaktLWcsCuIAHFJoGuXrpmLcIYQ6DBuDRCaNLmqYsLSOghILdvujntmpZSiXiBEU-V40GPKOSJAZvLOKR4_zTvfjant-6XECS-UEMb5KWz_r5E8_n0hh8u-xO39-5_cOPQ9QtmVMJYU1utqaoMt18weO4fFKoVwa8o2ZDqBhWAs5HI3x_fwP0o7A4ZtZzs78RTLoZJyMPuxy6H-RODtQmFpe-XjWZA8=w1238-h637-no)

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
	 ![screenshot_func_dev](https://lh3.googleusercontent.com/-3-PFDuHKsvoPLewhaM76WlMG4kRVZV7MELhu7pKR7HkZVoXXYt655vVDELLwUhHrS_-6hHalNTHPTQQ9HXe93C5DLrL6yV80iHiHFA0MXa1vILcLQvU_cnn9O3ckFCNiZq33BcU4UK-2A9VoZd9fZaeFZP7PSjLw45j_M1l77FCaMdLKdZigfkh9X1fCin6B3efBTCaxi9kJx0pZD-31jlJ67j3gFv85kvzuSFUYdoSlbg-bZAndJ8JWPAcnlAstE_6sU9tJK2e7d2G2swmuB-mcXaEiHNnKfBm62QPxzv3y57O2E2uRYFtde0rv5SHDKkbnI7sbZNAeNttgvxQldxs0UiM-JgFAbLaWZ9K5aAFLHhetxboyAHpN04eMuJgTEXmC13bvXI_mWepWmLywJz4kP0l_27AuXYeC_K2RyoOo449mcaadHlBG2SmjjuL7FVz9RfgQ92lLt5YXPDZuDNxKkgJlyy0X4NvBWD7TaWdkiQ6WVMRDz0p_N-wDzYPmj-u42iY6VUPZMkB5GwHo4hg-Zbrx0gicXvPRr-cqjdZQMXRLhZvTk6NvImiFHbg740_D6sVL7U969zfkbXCqpnpZ-05sBRibk6msXI=w1026-h637-no)
- Anton for SQLphobic users
	- Anton provides a simple web interface to  interact with data. No more SQLing.
	- Easy to use UI makes life easy for Anton users.
![screenshot_func_users](https://lh3.googleusercontent.com/8jbpUCiYcFQZiOSOdWgzSqZaJF7SpB5_6MsZrWSPWBJJRxBo_M35w-44CDBNPeaaX7EqwUkBPdzYTy194uM2RQZaN2UDwCVl1Tp7OxueSX7MeXxNgMmyHs_5dH3eT06INsIw8GDflm4et9VY2THvwqevsCO2fmymG815zUuF3tBHiEiaGTzTl1_aRDLj9GfZYDNNOUoPY69Z7abD2LX-NBScXpWXAW5EL7VQUac2t3P_WLMIRNPLVLAMr1V06X3vjYa-xnFGGFff49V6ZOVwr5DrTByy4p8NVhKZXy4AXBtvc2il9Sd-mq22MCzyDA9aCEqzm0StgjJYtWPk8r5StS2H1orH2D4e_05DEPmEjrfypBnAZbdCNazLHVr1ZzNppDTs3h2KKmPnRsif8_zA78Ex4OJtuos7Ldn1Vrs6I_tXeB7DsAa8gkXBZgIqaBPpliIy_-z4e7BNSOARM50URT7LkUu05VD3pMK6WsOC7ydzRifbK69MkxQ9viGYW3KPABdw5VFIrP5SoKkQV4eN3OtlZh_Nq0YPC1ymwqaog_Cad8JZQxg6bia3Oc5FKCWRidzJI7L5T4_LH7T2tH2caGwdJPHobBej0RNkP5c=w1238-h637-no)

The complete list of features can be found in the [documentation](https://goo.gl/XbmUoK).

## License
Anton is licensed under the [GNU General Public License v2.0](https://github.com/shubham1172/anton/blob/master/LICENSE).
