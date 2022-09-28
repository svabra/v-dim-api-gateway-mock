# DIM API MGMT GATEWAY MOCK
## Purpose
The purpose of this Mock is to simulate the BIT REST Gateway. It has 2 interfaces:
 1) GET /fromDIM
 2) POST /toDIM

## How it Mock is supposed to work
For the GET /fromDIM the mock returns an aribtrary JSON array with event types - confirmed by Status Code 200. The JSON data is read from files in the /data directory. The Mock randomly chooses a JSON file for the available files. If one wants to return a dedicated file, simply move the other files into the archive.

The POST /toDIM will only verify the format of the JSON data in the payload and return a Status Code 200. 

## Installation

Install Python 3.9.14
https://www.python.org/downloads/release/python-3914/

## Run the server

Prerequisite: Pyston 3.9.14 installed
1) Switch to the root directory of the project
2) run the following command `uvicorn src.main.py --reload --port 8080`



