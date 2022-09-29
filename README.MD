# DIM API MGMT GATEWAY MOCK
## Purpose
The purpose of this Mock is to simulate the BIT REST Gateway. It has 2 interfaces:
 1) GET /fromDIM
 2) POST /toDIM

Read the OpenAPI documentation on these interfaces after you have installed the mock --> http://127.0.0.1/8080/docs

## How the Mock is supposed to be used
For the GET /fromDIM the mock returns an aribtrary JSON array with event types - confirmed by Status Code 200. The JSON data is read from files in the /data/fromDIM directory. The Mock randomly chooses a JSON file from the available files. If one wants to return a dedicated event typely move move the others temporarily into the archive folder

The POST /toDIM is merely supposed to verify the format of the JSON data in the payload and return a Status Code 200. 

## Installation without Virtualization/Containerization

Install Python 3.9.14
https://www.python.org/downloads/release/python-3914/

### Create the Python Virtual Environment

Do the following steps only once (unless there is a code update that requires it)
Create the environment: `py -m venv .venv`
Install the python library requirementy: `python -m pip install -r .\requirements.txt`

### Run the server

Prerequisite: Python 3.9.14 installed
1) Switch to the root directory of the project
2) run the following command `uvicorn main:app --reload --port 8080`

## Installation with Virtualization/Containerization

### Build the image
`docker build --rm -t svabra/v-dim-api-gateway-mock .`

### Run the container
`docker run --rm -it --name v-dim-api-gateway-mock -p 8080:8080 svabra/v-dim-api-gateway-mock`

## The API Documentation and Tests

You can view and test the OpenAPI on http://127.0.0.1/8080/docs


