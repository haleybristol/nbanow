# NBA now - A live scoreboard for the NBA

This website is live at [http://nbanow-207513.appspot.com/](http://nbanow-207513.appspot.com/), check it out.

***

## Setting up a local environment for development

Here are the steps you have to take to run nbanow on your localhost.

#### Step 1 - Install Anaconda

NBA now runs flask on the backend which is a python based web framework. You can [read more about flask here](http://flask.pocoo.org/).

In order to run flask, you'll have to have python installed. Anaconda is a distribution of python that simplifies package installation and management.

**[Download Anaconda here](https://www.anaconda.com/download/)**.

Once Anaconda is downloaded, run the installer. You'll have to add anaconda to your path so that you can use the command line tool named conda. The installer should do this for you automatically.

Test that you have conda installed and on your path by opening your terminal (mac users) or command prompt (windows users) and typing `conda --version`. If you have conda on your path, you will get an output like `conda 4.3.30`.

#### Step 2 - Clone the repository

Clone the nbanow repository onto your computer by running the following in your terminal:
```
git clone https://github.com/haleybristol/nbanow.git
```

Once you've cloned the repository, change directory into the project:
```
cd nbanow
```

#### Step 3 - Create a virtual environment & install the required libraries

Next you should create a conda environment for the project and install the libraries necessary to run the app locally.

```
conda create -n env-nbanow python=2.7
```

This line will create a virtual environment with the name env-nbanow. The `python=2.7` tells conda you want to run python version 2.7 in your environment.

Your console should output something like this, prompting you to reply yes or no to proceed:

```
Fetching package metadata .............
Solving package specifications: .

Package plan for installation in environment C:\Users\user\Anaconda3\envs\env-nbanow:

The following NEW packages will be INSTALLED:

    certifi:        2018.4.16-py27_0
    pip:            10.0.1-py27_0
    python:         2.7.15-he216670_0
    setuptools:     39.2.0-py27_0
    vc:             9-h7299396_1
    vs2008_runtime: 9.00.30729.1-hfaea7d5_1
    wheel:          0.31.1-py27_0
    wincertstore:   0.2-py27hf04cefb_0

Proceed ([y]/n)?
```

Once you answer with `y`, the environment will be created with those packages installed.

Now that the environment has been created, run this to activate it:
```
activate env-nbanow
```
You are now working from inside your environment.

Next, you will have to install the rest of the packages nbanow requires to run. We keep a list of these packages in the `requirements.txt` file inside the repository.

Run `pip install -r requirements.txt` to install these libraries in your environment.

#### Step 4 - Run the app

Once all the libraries are in your environment, you can execute the `run.py` script inside the project to run the app on localhost:
```
python run.py
```

The app should start running on port 5000 so if you open a web browser and visit `localhost:5000` you ought to see the website.

***

If you want to run the app again in the future, the only things you should have to do is navigate to the project directory, activate the virtual environment and execute the run.py script:
``````
cd nbanow
activate env-nbanow
python run.py
```

***

If you have any trouble with any of the above, or any issues with the app, lodge an issue on the repository & @haleybristol or @efbbrown will reply as soon as possible.