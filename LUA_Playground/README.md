# How to run lua scripts/projects on your personal computer

## Windows

### Installation

#### Install LUA

install and extract the LUA project from https://www.lua.org/ftp/
into the .env folder

#### Make sure you have gcc installed

download the top zip from https://winlibs.com/#download-release

extract in :C/

Add the /bin to PATH

#### Compile LUA

navigate to the lua-x.x.x directory in .env

run
```console
make mingw
```

### Running

you can now compile your code into compiled lua binaries.

To compile:

```console
.\.env\lua-5.4.7\src\luac -o <filename>.luac <filename>.lua
```

To run the code on the VM:

```console
.\.env\lua-5.4.7\src\lua <filename>.luac  
```

#### Mac

#TODO -mac user- fill this in.

# LUA Documentation


# Computer Craft specific Documentation

