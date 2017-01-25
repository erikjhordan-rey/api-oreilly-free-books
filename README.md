# O'Reilly free programming books - Web API

This project was inspired in [erikcaffrey's](https://github.com/erikcaffrey/api-oreilly-free-books/tree/api-oreilly-free-v1) web application project
used for expose [O'Reilly free programming ebooks](http://www.oreilly.com/programming/free/) via a web API.

## How does it works?

It is written in Python 2.7 using webapp2 and it's designed to be executed on [**Google App Engine**](https://cloud.google.com/appengine/).
It also make use of [**Google Cloud Datastore**](https://cloud.google.com/datastore/) to persist books data and a there is
a [**cron job**](https://cloud.google.com/appengine/docs/python/config/cron) scheduled to run every 1 hour to go to O'Reilly's website
and update books data by doing web scrapping.

That's basically it.

## About the API

It is hosted on [https://oreilly-api.appspot.com/](https://oreilly-api.appspot.com/) and the main resource is
[**/books**](https://oreilly-api.appspot.com/books) which after a GET request will expose you a
JSON list with all available books. Each list element will look this:

| Field       | Type        | Description                                                       |
|-------------|-------------|-------------------------------------------------------------------|
| title       | String      | Book title                                                        |
| url         | String      | Book details URL                                                  |
| thumbnail   | String      | Book thumbnail URL                                                |
| description | String      | Book description                                                  |
| category    | String      | Book category                                                     |
| subcategory | String/null | Book subcategory. This can be either the subcategory name or null |
| pdf         | String/null | Download URL (PDF). This can be either null or a URL              |
| mobi        | String/null | Download URL (MOBI). This can be either null or a URL             |
| epub        | String/null | Download URL (ePub). This can be either null or a URL             |

## Usage
These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes. See deployment for notes on how to deploy the project on a live system.

1. Install Google App Engine SDK for Python from [https://cloud.google.com/appengine/downloads](https://cloud.google.com/appengine/downloads)
2. Install lxml your local environment with: `$ pip install lxml==2.3
3. Run with: `$ dev_appserver.py .`

## Deployment
Once you have set up your gcloud CLI in your local environment as well as your project in Google App Engine's console,
you can simply run this for deployment.

```
$ glcoud app deploy
```

# Built with

* [lxml](http://lxml.de/): Used for HTML processing
* [webapp2](http://lxml.de/): Python Web micro-framework.

## Contributors
* [erikcaffrey](https://github.com/erikcaffrey)(Erik Jhordan Rey)
* [pablotrinidad](https://github.com/pablotrinidad) (Pablo Trinidad)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
