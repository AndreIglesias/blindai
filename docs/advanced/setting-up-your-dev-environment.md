# Setting up your dev environment

## Using remote container extension on vs-code 🐳

Clone the repo and open it in vs-code. If you do not have the remote container extension, vs-code should prompt you to install it. 

Open the green menu at the bottom-left of the vs-code 

![](../assets/Screenshot-vscode.png)

Choose: "Open folder in container". It will build for you the image described in [this Dockerfile](https://github.com/mithril-security/blindai/blob/master/server/docker/build.dockerfile) with the dev-env target. It installs Ubuntu18-04 and all the dependencies and drivers the project needs as well as the Rust analyzer, python-intellisense and jupyter-notebook vs-code extensions.

To get started on the project you should create a python virtual environment like this :
```
virtualenv ~/python3.9-dev-env
source ~/python3.9-dev-env/bin/activate
```

Then you can install the python client sdk in editable mode with :
```
cd client
python setup.py install
pip install -e .
```

And check that everything is working fine by running the integration tests :
```
export BLINDAI_TEST_NO_HW=1
cd ../tests
pip install -r requirements.txt
python -m unittest .
```

## Without Docker

If you don't want to use docker, you will need to install the following:

* Intel SGX DCAP **1.41** Driver
* Intel SGX SDK v2.15.1
* Intel SGX PSW (version 2.15.101.1 for the PSW librairies and 1.12.101.1 for the PSW-DCAP librairies)
* Rust nightly-2021-11-01 with Xargo

You can find the [installation guides](https://download.01.org/intel-sgx/sgx-linux/2.9/docs/) for Intel SGX software on the 01.org website.

Note: if you are running on a machine without SGX support, you will need the simulation versions of the Intel PSW and SDK.