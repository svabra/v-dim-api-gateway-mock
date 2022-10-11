# DIM API MGMT GATEWAY MOCK
## Purpose
The purpose of this Mock is to simulate the BIT REST Gateway. It has 2 interfaces:
 1) GET /fromDIM
 2) POST /toDIM

Read the OpenAPI documentation on these interfaces after you have installed the mock --> http://127.0.0.1/8080/docs

## How the Mock is supposed to be used
For the GET /fromDIM/{event_type} the mock returns an aribtrary JSON array of the event_type passed by the GET URL - confirmed by Status Code 200. The JSON data is read from files in the /data/fromDIM directory. The Mock randomly chooses a JSON file from the available files selecting only files matching the event_type. One can have multiple files for the same event-type to quickly test multiple data-test-cases: e.g. msapersoncontactchange_1.json, msapersoncontactchange_2.json, etc.

The POST /toDIM is merely supposed to verify the format of the JSON data in the payload and return a Status Code 200. 

## Installation without Virtualization/Containerization

Install Python 3.9.14
https://www.python.org/downloads/release/python-3914/

### Create the Python Virtual Environment

Do the following steps only once (unless there is a code update that requires it)
1) Create the environment: `py -m venv .venv`
2) Activate the isolated python environment `.venv/Scripts/activate`
3) Install the python library requirementy: `python -m pip install -r .\requirements.txt`

### Run the server

Prerequisite: Python 3.9.14 installed
1) Switch to the root directory of the project
2) activate the isolated python environment `.venv/Scripts/activate`
3) run the following command `uvicorn main:app --reload --port 8080`

## Installation with Virtualization/Containerization

### Build the image
`docker build --rm -t svabra/v-dim-api-gateway-mock .`

### Run the container
`docker run --rm -it --name v-dim-api-gateway-mock -p 8080:8080 svabra/v-dim-api-gateway-mock`

## The API Documentation and Tests

You can view and test the OpenAPI on http://127.0.0.1/8080/docs


