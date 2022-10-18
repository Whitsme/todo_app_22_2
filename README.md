# Assignment 2 - TODO Application

## Author

Aaron Whitaker

## Description

Create a Django Web Application with a single model to hold TODOs and a single home / index page that will list out all of the TODOs that have been entered via the admin. The home page should extend a base template even though there is only one page. Once created, you will add testing to make sure the model and all pages work correctly. Lastly, host it on Heroku.

The main non-admin page will be a list of all the TODOs and the date that they should be completed by. Additionally there should be some buttons (as links) for add, edit, and delete that will take the user to the corresponding admin page for that functionality. You can see a screenshot of what I am expecting below in the screenshots section.

Tests for the site should be similar to the ones we wrote in class. I am expecting three in total. Just like what we did in the in-class.

Publish the site on Heroku and submit the URL for the site to Canvas as the submission for this assignment as well as have your most recent commit pushed up to GitHub.

In general, the program should allow the following functionality:

1. Created Django Project and App for static pages.
2. Base template that other templates will extend from.
3. TODO Model.
4. Home URL/View/Template listing all TODOs.
5. Superuser can do CRUD operations in the admin.
6. Basic Bootstrap styling.
7. Three Tests for the project which include:
   1. Model Content. Be sure to test all fields.
   2. URL exists at correct location.
   3. Homepage.
      1. Assert response code.
      2. Assert correct template used.
      3. Assert response contains correct content (Name and Date).
8. Published to Heroku and URL submitted to Canvas as Assignment Submission.

Documentation should include the following for this, and all future assignments:
* Comments at the top of each file that you add source code to with the following:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. Use the """ (triple quote) doc string method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

### Database Requirements
I have included an ERD (Entity Relationship Diagram) that shows the database tables. You should be able to use this diagram to know how to structure your models. Additionally, I tend to include the User (and sometimes related) tables in the ERD. You will never need to create these user models as they are included by Django. However, by including them in the ERD you can see the relationships between users and other tables. In the case of this assignment, there is no relationship between users and TODOs. But, in future assignments, there will be. Consider this a primer into being able to create models from an ERD.

In the case of this assignment and the TODO model that you will need to create, it will contain the following fields:
* Name
* Complete By

![Database Entity Relationship Diagram](http://barnesbrothers.net/cis218/assignment_images/assignment_2/cis218_assignment_2_erd.png "Database Entity Relationship Diagram")

### Screenshots
I am not expecting that your site will necessarily look exactly like mine, but I am expecting that you will use Bootstrap and that you will try your best to match the screenshot. Since you don't know exactly how I did it though, it's fine if there are differences. Think of the screenshot as a general guide.

![Todo Page Screenshot](http://barnesbrothers.net/cis218/assignment_images/assignment_2/cis218_assignment_2_screenshot.png "Todo Page Screenshot")

### Solution Requirements
* Created Django Project and App for static pages.
* Base template that other templates will extend from.
* TODO Model.
* Home URL/View/Template listing all TODOs.
* Superuser can do CRUD operations in the admin.
* Basic Bootstrap styling.
* 3 Tests for the project which include:
* Published to Heroku and URL submitted to Canvas as Assignment Submission.

### Notes
In order to render out the number of TODOs in the template, you can reference the following link. It shows how to use what is called a template filter. This linked page contains all sorts of template tags and filters that can be used inside templates to do things. This is an invaluable resource that I reference constantly. We will explore template tags and filters more in later chapters / assignments. But knowing about it now does not hurt. In fact, you can see tags that we have already used such as the url one.

https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#length

In order to be able to link to certain pages within the admin, you can look at the following page:

https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls

In it, you can see that reversing a url for an admin page follows the format:

```
{{ app_label }}_{{ model_name }}_{{ action }}
```

So, assuming an app named `todo` and a model named `todo` you would use the following for getting to the change link:

```
todo_todo_change
```

And since the url template tag takes a url name, you can get to admin ones by prefixing the url name with the app label (more on this later too). In the case of the admin, the app label is admin. So, the full name that can be reversed would be:

```python
'admin:todo_todo_change'
```

So, doing this in the template would look something like:

```htmldjango
{% url 'admin:todo_todo_change' %}
```

If you have more questions regarding this, don't hesitate to ask.

## Grading
| Feature                                  | Points |
|------------------------------------------|--------|
| Create Django Project and App            | 10     |
| Base Template                            | 10     |
| TODO Model                               | 15     |
| Home Url/View/Template                   | 15     |
| Superuser can do CRUD in admin           | 15     |
| Bootstrap Styling                        | 10     |
| Automated Tests                          | 10     |
| Heroku Deployment                        |  5     |
| Documentation                            |  5     |
| Readme                                   |  5     |
| **Total**                                | **100**|

## Outside Resources Used



## Known Problems, Issues, And/Or Errors in the Program


