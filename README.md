## Deploying a Bottle web app on Heroku

This tutorial shows how to set up and deploy a Bottle web app on Heroku. [Bottle](http://bottlepy.org/docs/dev/) is a Python micro web framework that's easy to learn and use.

Steps covered in this tutorial:

1. [What you need](#reqs)
2. [Get the sample Bottle app](#bottle)
4. [Deploy the Bottle app on Heroku](#deploy)
5. [Push updates to Heroku](#push)


<h3 id="reqs">What you need</h3>

You need a text editor and a command-line interface like the command prompt in Windows or the Terminal on the Mac.

You also need to install Python and a few libraries, as described next.

#### Install Python

Install version 3 of Python on your computer if you don't already have it. Visit the [Python website](http://www.python.org/about/) to learn more. To download and install it, see <http://www.python.org/download/>.

When copying the examples in this tutorial, make sure to indent lines exactly as shown. Indentation matters in Python.

#### Install pip (Python 3.3 or earlier)

After installing Python, install [pip](https://pip.pypa.io/en/latest/index.html), a simple tool for installing and managing Python packages.

Note: If you have Python 3.4 or better, you already have pip. Skip ahead.

1. Right-click [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and download the file.
2. In your command-line interface, navigate to the folder containing the **get-pip.py** file.
3. Run the following command:

    ```
    $ python3 get-pip.py
    ```

     <div class="note note"><span class="notetitle">Note: </span>In Windows, the prompt is <strong>C:\></strong> instead of <strong>$</strong>.</div>

If you have any trouble, see the [pip instructions](https://pip.pypa.io/en/latest/installing.html#install-pip).

#### Install Bottle

After installing pip, use the following pip command to download and install Bottle.

```
$ pip3 install bottle
```

If you have Python 3.3 or earlier and you installed pip separately, use `pip` instead of `pip3` on the command line.

If you have any problems, see the [Bottle instructions](http://bottlepy.org/docs/dev/tutorial.html#installation).

#### Install Git

You'll use [Git](http://git-scm.com), the popular version control system, to push files to the remote server on Heroku.

<div class="note note"><span class="notetitle">Note: </span>If you already have Git, update it to the latest version.</div>

Download and run one of the following installers:

* Windows - <http://git-scm.com/download/win>
* Mac - <http://git-scm.com/download/mac>


<h3 id="bottle">Get the sample Bottle app</h3>

Because this isn't a Bottle tutorial, a set of starter files is provided. Click the following link to download it from Github:

<https://github.com/chucknado/bottle_heroku_tutorial/archive/master.zip>


#### Bottle basics

To keep things simple, the sample app simulates an API request that gets the name and role of a user.

Navigate to the **bottle\_heroku\_tutorial** folder in a file browser. The **sample_app.py** file is the app's nerve center. Open it in a text editor to take a look. Here's a link to the file in this repository:

* <a target="blank" href="https://github.com/chucknado/bottle_heroku_tutorial/blob/master/sample_app.py">sample_app.py</a>

The file consist of *routes* that map HTTP requests to functions. The return value of each function is sent in the HTTP response. To learn more, see [Request Routing](http://bottlepy.org/docs/dev/tutorial.html#request-routing) in the Bottle docs.

Routes typically specify templates to render for the response. To learn more, see [Templates](http://bottlepy.org/docs/dev/tutorial.html#templates) in the Bottle docs.

The **sample_app.py** file calls the framework's `run()` function to run the app on a local web server or on Heroku:

```
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
```

The sample app checks for the APP_LOCATION environment variable to decide which statement to run. You'll set the variable later.

The Bottle framework includes a built-in development server that you can use to test your changes locally before deploying them to a remote server.

You can run the sample app locally as follows:

1. In your command-line interface, navigate to the app folder that contains the **sample_app.py** file.

2. Run the following command to start the local server:

    ```
    $ python3 sample_app.py
    ```

3. In a browser, go to `http://localhost:8080/home`.

    You should see the sample app's admittedly plain home page.

4. Run some tests.

    Try clicking the link on the home page.

5. When you're done, switch to your command-line interface and press Ctrl+C to shut down the server.



<h3 id="deploy">Deploy the Bottle app on Heroku</h3>

Deploying a Bottle app for the first time consists of the following steps:

* [Get a free Heroku account](#heroku)
* [Create a remote Git repo for your app on Heroku](#create)
* [Create a local Git repo](#git)
* [Prepare the app files for deployment](#prep)
* [Push the app to Heroku](#push)


<h4 id="heroku">Get a free Heroku account</h4>

If you don't already have an Heroku account, you can sign up for a free one.

<div class="note note"><span class="notetitle">Note: </span>If you already have an account and have installed the Heroku Command Line Interface (CLI), you can skip this section.</div>

1. Go to <https://signup.heroku.com/dc>, then enter your information, pick Python as your primary development language, then click **Create Free Account**.

2. Check your email to confirm your account. When prompted, set up a password.

    After setting up a password, you'll be taken to a welcome page.

3. Install the Heroku Command Line Interface. To download and install it, see [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) in the Heroku docs.

	As the doc suggests, you should login at the command line immediately after installing the tool.


<h4 id="create">Create a remote Git repo for your app on Heroku</h4>

After you push your app to the repo, Heroku will serve the app from there.

1. If not already done, login to Heroku in your command-line interface:

	```
	$ heroku login
	```

2. Run the following command:

	```
	$ heroku create your-app-name
	```

	Change "your-app-name" to whatever you want to name your app. You can expect that common names like “my-app” or “tutorial” will already be taken. You can omit the name and let Heroku generate a random name that you can change it later. Example:

	```
	$ heroku create
	```

	Example response:

	```
	Creating app... done, ⬢ fast-sierra-15737
	https://fast-sierra-15737.herokuapp.com/ | https://git.heroku.com/fast-sierra-15737.git
	```

This is a one-time-only requirement. Heroku creates a remote git repository that you'll link to a local Git repo in the next section. This setup will let you use a simple git `push` command to deploy your app to the server.

<h4 id="git">Create a local Git repo</h4>

Before you start, make sure you installed Git. See Install Git above for instructions.

1. In your command-line interface, navigate to the folder that contains the files of your Bottle app.

	If you copied the sample app, it should be the folder that contains the **sample_app.py** file.

2. Run the following 3 commands one after the other:

	```
	$ git init
	$ git add .
    $ git commit -m "my first commit"
	```

	This creates a local Git repository and adds you files to it. You'll connect this local repo to a remote repository on Heroku in the next step.

3. Make sure you're logged in to Heroku (`$ heroku login`), then run the following command to set your Heroku app repo as the remote repo of your local repo:

	```
	$ heroku git:remote -a your-app-name
	```

	**Important**: Change "your-app-name" to whatever is the name of your app. Example:

	```
	$ heroku git:remote -a fast-sierra-15737
	```

4.	To verify you set the remote repo, run:

	```
	$ git remote -v
	```


<h4 id="prep">Prepare the app files for deployment</h4>

When deploying, the following configuration files need to be included in the web app's root directory:

* Procfile
* runtime.txt
* requirements.txt

1. In a text editor, create a file named **Procfile** and make sure it contains the following line:

    ```
    web: python sample_app.py
    ```

    A Procfile lists the app's process types and the commands to start each process. The Bottle app runs a single web process, which is started by executing the `python sample_app.py` command.

2. Create a file named **runtime.txt** and make sure it contains the following line, adjusted for your version number:

    ```
    python-3.5.2
   	```

    The **runtime.txt** file tells Heroku what Python version to use for your app. The setting ensures Heroku runs your app in the same runtime environment you used locally to develop and test the app.

    To find out the version you're using locally, run the following command at the command line:

    ```
    $ python3 --version
    ```

3. Create a file named **requirements.txt** and make sure it lists the following libraries:

    ```
    bottle==0.12.13
    requests==2.12.4
    ```

	The file lists all the external libraries the app needs to run. Update the version number of each library, if necessary. To find out the version, run the following commands:

    ```
    $ pip3 show bottle
    ```

	or

    ```
    $ pip3 show requests
    ```

4. Add the new config files to your local repo:

	```
	$ git add .
	$ git commit -a -m "Add config files"
	```


<h4 id="push">Push the app to Heroku</h4>

In this step, you deploy the app to Heroku for the first time.

1. If not already done, login to Heroku and enter your Heroku email and password when prompted:

    ```
    $ heroku login
    ```

2. Deploy the app:

    ```
    $ git push heroku master
    ```

    The command uploads the app files to the remote git repository on Heroku. Heroku then builds and deploys the app.

3. Set the following APP_LOCATION environment variable in Heroku:

    ```
    $ heroku config:set APP_LOCATION=heroku
    ```

    This is a one-time-only requirement. The code in **sample_app.py** has two different run statements: one for the local server and one for the Heroku server. At runtime, the app checks for the APP_LOCATION environment variable to decide which one to run:

    ```
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
    ```

5. Open and test the app in a browser:

	```
	$ heroku open
	```

If something goes wrong, go back to your command-line interface and enter `heroku logs --tail`. Check the entries for clues of what went wrong.

Bookmark the URL of your app.


<h3 id="push">Push updates to Heroku</h3>

You can start tweaking or adding to the app. See the [Bottle tutorial](http://bottlepy.org/docs/dev/tutorial.html). Test your changes locally before pushing the changes to Heroku, as described next.

**Note**: If you make changes to the **sample_app.py** file while the local server is running, you have to stop and restart the server to see the changes. You don't have to restart the server if you make changes to static files like the templates or css. Just refresh the page in the browser.

**To push updates to Heroku**

1. In your command-line interface, navigate to your app folder.

2. Commit all the changes in Git:

    ```
    $ git commit -a -m "Various updates"
    ```

3. If not already done, log in to Heroku and enter your Heroku email and password when prompted:

    ```
    $ heroku login
    ```

4. Push the files:

    ```
    $ git push heroku master
    ```

5. Open and test the app in a browser.

	```
	$ heroku open
	```

