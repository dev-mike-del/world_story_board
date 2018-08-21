# Story Board

This is a social media application. A user can post (publish) stories that they write. A story is anything that a user wants to write in a post. It is called a story to differentiate it from other social media apps.

A user can anonymously publish a story (without ever creating an account) or they can create an account and publish a story with their username as the author. A username in a story 'by line' will link to the user's profile page. 

After creating an account, a user can choose to follow another author. To do this, a user must navigate to another user's profile page. On that page, they can press the 'follow' button to follow the author or 'unfollow' to un-follow the author. They can view the stories form the author's that they follow in the 'following' page link (found in the nav bar). 

Additionally, stories can be recalled and edited by the original author. Soon, you will be able to delete a story as well. 

Please visit the app to test it out for yourself: https://worldstoryboard.com/ 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project is live and hosted on AWS Elastic Beanstalk. The requirements.txt lists many packages but most are related to the AWS cli and other required packages associated with it. They are not required to run this project your local environment. 

As with all python projects, using a virtual environment is recommended.  
 
If you do not wish to download all the packages listed in the requirements.txt, you will need to make sure to at least install Django. This project is using Django==2.0.7.

```
pip install Django==2.0.7
```

### Installing

Download the project from this repository .

In your terminal, run the python development server

```
python your-local-path-to-the-project/storyboard/manage.py runserver
```

Follow the link that the development provides to view the app in your browser 

You can now create an account and publish a story. 

<!-- ## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
``` -->

## Deployment

This application is deployed on AWS Elastic Beanstalk. 

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [venv](https://docs.python.org/3/library/venv.html) - Dependency Management
* [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) - Frontend styling
* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) - Deployment 

<!-- ## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  -->

## Authors

* **Michael Delgado** - *Initial work* - [dev\_mike\_del](https://github.com/dev-mike-del)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Tutorial: Adding https to a custom domain on Elastic Beanstalk](https://medium.com/in-development/tutorial-adding-https-to-a-custom-domain-on-elastic-beanstalk-29a5617b8842) - A tutorial by [James Beswick](https://medium.com/@jbesw)
* [Automatically generating unique slugs in Django](https://keyerror.com/blog/automatically-generating-unique-slugs-in-django) - A tutorial by [KeyError: Blog](https://keyerror.com/blog)
* [README-Template.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) - A template to make good README.md by [Billie Thompson](https://github.com/PurpleBooth)

