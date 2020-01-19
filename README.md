# Portal News

system that captures news from other sites with web scraping performed with Django and Bootstrap.

## Getting Started

clone this repository and install the "requirements.txt" dependencies, after that run the news capture script as below.

```
./manage.py capturar_noticias
```

### Prerequisites

asgiref==3.2.3
astroid==2.3.3
autopep8==1.4.4
beautifulsoup4==4.8.2
bs4==0.0.1
certifi==2019.11.28
chardet==3.0.4
coreapi==2.3.3
coreschema==0.0.4
Django==3.0.2
django-crispy-forms==1.8.1
django-rest-swagger==2.2.0
djangorestframework==3.11.0
idna==2.8
isort==4.3.21
itypes==1.1.0
Jinja2==2.10.3
lazy-object-proxy==1.4.3
MarkupSafe==1.1.1
mccabe==0.6.1
openapi-codec==1.3.2
pycodestyle==2.5.0
pylint==2.4.4
pytz==2019.3
requests==2.22.0
selenium==3.141.0
simplejson==3.17.0
six==1.14.0
soupsieve==1.9.5
sqlparse==0.3.0
typed-ast==1.4.1
uritemplate==3.0.1
urllib3==1.25.7
wrapt==1.11.2



### Installing

first activate the application with the following command:

```
source venv/bin/activate
```

then run the django command, to run the web scraping script to get the news from the portal 'TecMundo' with the following command:

```
./manage.py capturar_noticias
```

## Deployment

now it's sor starts the server with the following command:

```
python manage.py runserver
```


## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - The web framework used
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used to Web scraping



## Contributing

Please read [CONTRIBUTING.md](https://github.com/jhonatheberson/news-portal/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) For the versions available, see the [tags on this repository](https://github.com/jhonatheberson/news-portal/tags).

## Authors

* **Jhonat Heberson** - *Initial work* - [jhonatheberson](https://github.com/jhonatheberson/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.



## Acknowledgments

* Adelardo Adelino Dantas de Memeiros
