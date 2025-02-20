### Library Manag

manage library

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:


```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/Kasahun-Ab/Frappe-Library-Managment.git --branch main
bench install-app library_manag
```

###  Create site 
A site in Frappe is like a project that contains your database, configuration, and installed apps
```bash
cd $PATH_TO_YOUR_BENCH
bench new-site your-site-name
```
### Install the App on Your Site
 Run the following command to install the app you just pulled onto your site:

```bash
bench --site your-site-name install-app library_manag
```
### Run the server: 
After installing the app, you can start the development server to interact with the app.
```bash
bench start
```
This will start the server, and you can access your site at  http://localhost:8000.

### License

mit
