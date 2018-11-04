# DES-visualizer

This project came about as I wanted to have a debug output for a differential power analysis of DES.
It builds on the pyDes implementation and generates a LaTeX file with a Tikz drawing for each round.

## Usage

It is suggested to use a virtual environment to run the software and operate within this:
```bash
$ virtualenv env
$ source ./env/bin/activate
```

Install the requirements:

```bash
$ pip install -r requirements.txt
```

If you want, modify the data and key in `des-visualizer.py`. They are stored in lists of 1's and 0's.

Generate the TeX code:

```bash
$ python des-visualizer.py
```

Compile the TeX:

```bash
$ cd pdf && latex out.tex && cd ..
```

The final PDF can be viewed at `pdf/out.pdf`


## Credits

Many Thanks go to:
 - Todd Whiteman https://github.com/toddw-as/pyDes
 - Orlin Grabbe http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm