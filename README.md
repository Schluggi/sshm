# sshm
[![donate](https://img.shields.io/badge/donate-PayPal-blue.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=KPG2MY37LCC24&source=url)
[![PyPI version](https://badge.fury.io/py/sshm.svg)](https://badge.fury.io/py/sshm)
[![release](https://img.shields.io/github/v/release/schluggi/sshm.svg)](https://github.com/Schluggi/sshm/releases/latest)
[![license](https://img.shields.io/badge/license-MIT-yellow.svg)](https://github.com/Schluggi/sshm/blob/master/LICENSE.txt)

A simple wiptail based ssh menu.

## Features
- Filter the hosts 
- Simple usage
    
## Requirements
- Python >= 3.6

## Installation
### pip (recommended)
1. Install sshm: `python3 -m pip install sshm`
2. Start the program: `sshm`
> **Upgrade**: `python3 -m pip install --upgrade sshm`

### whl / release
1. Download the latest [release](https://github.com/Schluggi/sshm/releases/latest)
2. Install the wheel-file: `python3 -m pip install sshm-X.X-py3-none-any.whl`
2. Start the program: `sshm`
> **Upgrade**: Simply install a newer release
 
### git
1. Clone this repo
2. Install the requirements by running `python3 -m pip install -r requirements.txt` 
3. Start the program:`./sshm --help` 
> **Upgrade**: `git pull`

## Usage
By running `sshm` without any arguments to get a menu with all hosts defined in your ~/.ssh/config.
```commandline
sshm
```

### Filter
You can filter the hosts by adding a string as first argument. The string will be used as a wildcard filter. 
```commandline
sshm cloud
```

### Custom config
By default sshm will load the ssh config from `~/.ssh/config`. You can change this by setting the environment variable
`SSHM_CONFIG_PATH`.
```commandline
SSHM_CONFIG_PATH=/opt/my_ssh_config sshm cloud
```


  
## Credits 
Created and maintained by Lukas Schulte-Tickmann / Schluggi.
