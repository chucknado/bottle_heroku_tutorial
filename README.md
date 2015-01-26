## Deploying a Bottle web app on Heroku

This tutorial shows how to set up and deploy a Bottle web app on Heroku. [Bottle](http://bottlepy.org/docs/dev/) is a Python micro web framework that's easy to learn and use.

Steps covered in this tutorial:

1. [What you need](#reqs)
3. [Get a free Heroku account](#heroku)
4. [Get the sample Bottle app](#bottle)
4. [Deploy the Bottle app on Heroku](#deploy)
5. [Push updates to Heroku](#push)

### [What you need](id:reqs)

You need a text editor and a command-line interface like the command prompt in Windows or the Terminal on the Mac.

You also need to install Python and a few libraries, as described next.

#### Install Python

Install version 3 of Python on your computer if you don't already have it. Visit the [Python website](http://www.python.org/about/) to learn more. To download and install it, see <http://www.python.org/download/>.

When copying the examples in this tutorial, make sure to indent lines exactly as shown. Indentation matters in Python.

#### Install pip

After installing Python, install [pip](https://pip.pypa.io/en/latest/index.html), a simple tool for installing and managing Python packages.

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
$ pip install bottle
```

If you have any problems, see the [Bottle instructions](http://bottlepy.org/docs/dev/tutorial.html#installation).

#### Install Git

You'll use [Git](http://git-scm.com), the popular version control system, to push files to the remote server on Heroku.

<div class="note note"><span class="notetitle">Note: </span>If you already have Git, update it to the latest version.</div>

Download and run one of the following installers:

* Windows - <http://git-scm.com/download/win>
* Mac - <http://git-scm.com/download/mac>


### [Get a free Heroku account](id:heroku)

Sign up for a free Heroku account to deploy your Bottle apps on the web.

<div class="note note"><span class="notetitle">Note: </span>If you already have a Heroku account and know how to deploy apps to it, you can skip this section.</div>

1. Sign up to Heroku at <https://signup.heroku.com/dc>.

    Enter your name and email, pick Python as your development language, then click **Create Free Account**. Check your email to confirm your account. When prompted, set up a password.

    After setting up a password, you'll be taken to the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) tutorial.

    When you're ready, click the **I'm Ready to Start** button.

1. Perform the **Set up** step.

    Install the Heroku Toolbelt and authenticate your Heroku account by logging in at the command line.

    When you're done, click **I have installed the Toolbelt**.

2. Perform the **Prepare an app** step.

    Download the sample app from Heroku using git. The sample app is used in the next step to test your setup.

    When you're done, click **My app is ready**.

3. Perform the **Deploy the app** step.

    Follow the instructions to deploy the sample app. When you're done, you should be able to open the app -- a simple page with the line "Hello from Python!" -- in a browser. You successfully deployed your first web app on Heroku.

If you like, you can go through the rest of the Heroku steps to learn more about how Heroku works, but it's not required for this tutorial.

### [Get the sample Bottle app](id:bottle)

Because this isn't a Bottle tutorial, a set of starter files is provided.

* [Download the app files](#download)
* [Bottle basics](#basics)
* [Run the app locally](#localhost)


#### [Download the app files](id:download)

1. If you don't already have one, create a tutorials folder and navigate to it with your command-line interface.

2. Run the following command to download the app files:

    ```
    git clone https://github.com/chucknado/bottle_heroku_tutorial.git
    ```

    A git repository is created containing the application starter files. See the next section to learn more about the files.

#### [Bottle basics](id:basics)

To keep things simple, the sample app simulates an API request that gets the name and role of a user.

Navigate to the **bottle_heroku_tutorial** folder in a file browser. The app consists of the following folders and files:

```
/bottle_heroku_tutorial
    /static
        /css
            main.css
        /images
            logo.png
        /js
            scripts.js
    /views
        details.tpl
        home.tpl
        error.tpl

    Procfile
    README.md
    requirements.txt
    runtime.txt
    sample_app.py
```

The **sample_app.py** file is the app's nerve center. Open it in a text editor to take a look. Here's a link to the file in this repository:

* <a target="blank" href="https://github.com/chucknado/bottle_heroku_tutorial/blob/master/sample_app.py">sample_app.py</a>

The file consist of *routes* that map HTTP requests to functions. The return value of each function is sent in the HTTP response.

For example, when a browser requests the page at the `/home` relative URL, the app looks up the **/home** route and runs the `show_home()` custom function:

```
@route('/home')
def show_home():
    return template('home')
```

The `show_home()` function returns the results of the framework's `template()` function in the HTTP response. The `template()` function renders a template named 'home' in HTML. Templates are located in the **views** folder and have **.tpl** file extensions.

Here's the **home.tpl** template:

```
<html>
  <head>
    <title>Sample App Home</title>
    <link href="/css/main.css" rel="stylesheet">
  </head>
  <body>
      <h2>Sample app</h2>
      <p>Welcome to the Bottle sample app.</p>
      <p>Get the user's <a href="profile">profile info</a>.</p>
  </body>
</html>
```

The home template includes a link to a "profile" page, which is handled by the **/profile** route in the **sample_app.py** file:

```
@route('/profile')
def make_request():
    # make an API request here
    profile_data = {'name': 'Marcel Hellkamp', 'role': 'developer'}
    return template('details', data=profile_data)
```

The `template()` function passes the information contained in the **profile_data** variable to the template using the **data** keyword argument. The argument name is arbitrary. For now, the function sends dummy data until you add the request code later.

The argument values are inserted at placeholders in the **details.tpl** template:

```
  <ul>
    <li>Name: {{data['name']}}</li>
    <li>Role: {{data['role']}}</li>
  </ul>
```

The `{{}}` placeholders contain standard Python expressions for reading data in a dictionary.

The home template also includes a link to a css file, `"/css/main.css"`, which is handled by the **/css/\<filename\>** route:

```
@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')
```

The term `<filename>` is a wildcard that lets the route handle requests for *any* file in the css folder. It saves you from defining a different route for every CSS file used in the app. This kind of route is especially useful for image files. The framework's `static_file()` function serves static files like image, CSS, and JavaScript files from the app's **static** folder.

Finally, the **sample_app.py** file calls the framework's `run()` function to run the app on a local web server or on Heroku:

```
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
```

The sample app checks for the APP_LOCATION environment variable to decide which statement to run. You'll set the variable later.

The Bottle framework includes a built-in development server that you can use to test your changes locally before deploying them to a remote server.

To learn more about the framework, see the excellent tutorial on the [Bottle website](http://bottlepy.org/docs/dev/tutorial.html).

#### [Run the app locally](id:localhost)

1. In your command-line interface, navigate to the **sample_tutorial_app** folder.

2. Run the following command to start the local server:

    ```
    $ python3 sample_app.py
    ```

3. In a browser, go to `http://localhost:8080/home`.

    You should see the sample app's admittedly plain home page.

4. Run some tests.

    Try clicking the link on the home page. Try opening `http://localhost:8080/`.

5. When you're done, switch to your command-line interface and press Ctrl+C to shut down the server.

You're ready to deploy the app on Heroku for the first time.


### [Deploy the Bottle app on Heroku](id:deploy)

In this step, you'll deploy the app to Heroku for the first time.

When deploying, the following configuration files need to be included in the app's root directory:

* Procfile
* requirements.txt
* runtime.txt

All 3 are text files. The files ensure Heroku runs your app in the same runtime environment you use locally to develop and test the app. The remote environment should match your local environment as much as possible to prevent unexpected bugs caused by different software versions.

1. In a text editor, open the **Profile** file and make sure it contains the following line:

    ```
    web: python sample_app.py
    ```

    A Procfile lists the app's process types and the commands to start each process. The Bottle sample app runs a single web process, which is started by executing the `python sample_app.py` command.

2. Open the **runtime.txt** file and update the Python version number, if necessary.

    The **runtime.txt** file tells Heroku what Python version to use for your app:

    ```
    python-3.3.2
    ```

    The find out the version you're using locally, run the following command at the command line:

    ```
    $ python3 --version
    ```

2. Open the **requirements.txt** file and make sure it lists all the external libraries the app needs to run. Update the version number of each library, if necessary. The sample app needs just one external library:

    ```
    bottle==0.12.8
    ```

    Update the version number to the version installed on your computer. To find out the version, run the following commands:

    ```
    $ pip show bottle
    ```

3. Commit the changes to your local git repository:

    ```
    $ git commit -a -m "Update Heroku config files"
    ```

4. Login to Heroku on the command line and enter your Heroku email and password when prompted:

    ```
    $ heroku login
    ```

5.  Create the app:

    ```
    $ heroku create
    ```

    This is a one-time-only requirement. Heroku creates a remote git repository called `heroku` associated with your local git repository. This lets you use a simple `git push` command to deploy your app to the server.

    Heroku generates a random name for the app. Mine is murmuring-beyond-5480. You can rename it later in your Heroku dashboard at <https://dashboard.heroku.com/apps>. Look under the Settings tab for the app.

6. Deploy the app:

    ```
    $ git push heroku master
    ```

    The command uploads the app files to the remote git repository on Heroku. Heroku then builds the app and deploys it.

7. Set the following configuration variable on Heroku:

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

8. Open and test the app in a browser:

    ```
    heroku open
    ```

If something goes wrong, go back to your command-line interface and enter `heroku logs --tail`. Check the entries for clues of what went wrong.

Bookmark the URL of your app.


### [Push updates to Heroku](id:push)

You can start tweaking or adding to the app. See the [Bottle tutorial](http://bottlepy.org/docs/dev/tutorial.html). Test your changes locally before pushing the changes to Heroku, as described next.

<div class="note note"><span class="notetitle">Note: </span>If you make changes to the <strong>sample_app.py</strong> file while the local server is running, you have to stop and restart the server to see the changes. You don't have to restart the server if you make changes to static files like the templates or css. Just refresh the page in the browser.</div>

**To push updates to Heroku:**

1. In your command-line interface, navigate to your app folder.

2. Commit all the changes in Git:

    ```
    git commit -a -m "Various updates"
    ```

3. Log in to Heroku on the command line and enter your Heroku email and password when prompted:

    ```
    heroku login
    ```

4. Push the files:

    ```
    git push heroku master
    ```

5. Open and test the app in a browser:

    ```
    heroku open
    ```

