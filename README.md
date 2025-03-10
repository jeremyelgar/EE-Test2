### Docker Build Solution

To create a docker image for the solution use the following docker build command in the root of the project

``docker build -t <image name>:<tag> .``

where tag is optional (latest used if not supplied)

e.g. ``docker build -t candiate-solution .``

To run the docker image use

``docker run -it --rm -p <port to connect to>:8080 <image name>''

e.g.  ``docker run -it --rm -p 8080:8080 candiate-solution''

Then point a Web Browser or http client to "http://localhost:8080/<github user>


### Docker Build Tests

The test can also be run in docker

#### Build

docker build -t ee-tests -f Dockerfile-tests  .

#### Run

 docker run -it --rm  ee-tests


### To run without docker.

Create a virtual enviroment inside the root of the project. [Creation of virtual environments](https://docs.python.org/3/library/venv.html)
e.g
``python -m venv venv ``
``activate venv/bin/activate``

The modules can be installed inside the virtual evnviroment using pip.
e.g
`` pip3 install -r requirements-tests.txt ``

The Test can be run by executing

pytest in the root of the project
e.g.
``pytest``


### Missing
Paging and caching not implimented (time contraints) solution returns 100 results.
Configutation of runtime logging / url paths not include for brevity

### Testing.

I normally prefer component / system style tests rather than mocking out the HTTP calls
for this type of API, this involves creating a mock server to use and deploy along side the soluton server.
But includes a unit test as requested.
