# Subdomain Discovery Tool

This Python script is designed to discover subdomains for a given target domain using a specified or custom wordlist. It utilizes the `requests` library to check the availability of discovered subdomains with 200 status code.

## Features

- **Subdomain Discovery:** Iterates through a wordlist and checks for subdomains of the target domain.
- **Custom Wordlist Support:** Allows the use of a custom wordlist file.

## Usage

### Requirements

- Python 
- `requests` library (install via `pip install requests`)

### Running the Script

1. Clone this repository or download the `subdomain_discovery.py` file.
2. Install the required dependencies (`requests` library).
   ```bash
   pip install requests
