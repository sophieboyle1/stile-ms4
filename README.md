# STILE - E-Commerce Web App.

### Code Institute - Final Milestone Project (4) - Full Stack Frameworks With Django.


STILE is a homeware boutique with hand picked items for you! Our collection ranges from furniture to home decor. The application focuses
on Interior Design, and also a blog page with DIY items you can do from your own home, and also comment and leave some tips for others.


![homepage](readme/images/hero-image.png)

The live website can be found [here](https://stile-boutique.herokuapp.com/)

## Table of Contents

* [Project Summary](#project-summary)
* [User Experience Design (UX)](#user-experience-design)
  * [The Strategy Plane](#the-strategy-plane)
    * [User Stories](#user-stories) 
  * [The Scope Plane](#the-scope-plane)
  * [The Structure Plane](#the-structure-plane)
  * [The Skeleton Plane](#the-skeleton-plane)
    * [Wireframes](#wireframes)
    * [Database Design](#database-design)
    * [Security](#security)
  * [The Surface Plane](#the-surface-plane)
* [Features](#features)
   * [Existing Features](#existing-features)
   * [Future Features](#future-features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
    * [AWS S3](#aws-s3)
    * [Heroku Deployment](#heroku)
    * [Local Deployment](#local-deployment)
* [Credits](#credits)

****

# Project Summary

Welcome to my Full Stack Frameworks with Django Project for Code Institute.

The goal of this project was to allow the user to create an account and make a purchase of products with Stripe. Although the majority of the admin activities is done through the Django admin site, the web app also provides more pleasant environment for common tasks such as adding, editing and deleting products or blog posts through the web app's UI.
I chose to develop an ecommerce shopping website as it is a complex and flexible application which challenged my understanding of the technologies involved. Given the sensitivity involved in handling customer details 
I had to approach development from a security conscious perspective.

# User Experience Design

## The Strategy Plane

Stile Homeware is a web-shop that represents a stored located in Dublin, Ireland. The customer can successfully purchase items and have them delivered to their home. For more user interaction, I created a blog with a comment section, and also a review option for all the products that is only available to logged in users.

## User Stories

As an e-commerce site owner...

* I want to offer a shopping journey that is informative and transparent so that the customers develop trust towards the marketplace.
* I want to have a marketplace offering more than just products so that the customers will have more reasons to come back to the site.
* I want to be able to make changes on the inventory myself so that I don't have to rely on external support when it comes to that.
* I want to be able to add, edit and adjust blog posts as I wish to do so.
* I want to offer a shopping journey that is informative and easy to navigate through.

As a customer...

* I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering.
* I want to easily navigate the site so that I can find content quickly with ease on any device.
* I want to view a list of products or look for an individual item by its category.
* I want to view individual product details and view the shipping and return policy.
* I want to easily view the total of my purchases at any time and have the option to update or delete.
* I want to successfully register for an account and proceed to log in.
* I want to easily access my previous orders.
* I want to be able to store my shipping details so that it’s easier for me to check out.
* I want to be able to contact the store of the website incase I have any issues or questons.
* I want to be able to easily recover my password incase I forget it.

## The Scope Plane 

In designing the page, I wanted for the user to have a positive experience and for the web-site to be simple to use. User can navigate through navigation bar that is always visible and by links in the footer. They can go from any part of the web-site to any other part. Simple to navigate and intuitive.

### Features planned:

* Responsive Design - Site should function on mobile, tablet and desktop/laptop devices.
* Mobile and desktop navigations.
* Website information clearly relayed upon entering the home page.
* Standard e-commerce feed of products with the option to sort products and filter them by category name. 
* Every product can be added to the cart immediately and links to a product page where the user can read more about it.
* About page to inform the user a information about the owners, with a testimonials section.
* Blog page containing blog posts all bout DIY projects to give the user inspiration for their own home.
* Contact information and form to easily contact the store.
* Options for the customers to leave a review on a product.

## The Structure Plane

When the user arrives on site, it will see the hero image and text which invokes the purpose of the site. Below there are three cards for new decor products we have in stock with the title and price. Each card is clickable to the product details. Navigation is always on top of the screen and the sites name acts as a link to Home page.On smaller devices there is a link in the hamburger menu. There is also a link for each section of the website. Also, I have placed main links of the web-site in the footer section as I've seen it in almost all web-sites I have visited.

Shop section is similar to every other web-shop. When they arrive at Shop, they will see all products available. I have put a drop down menu on the shop nav link to filter merchandise by four main categories. Products are presented as cards with images, name, short description and price. If user decides to view product, they willl see full name, full description, price and an option to add product to cart. If user adds to cart, they will see a message at the top of the page informing them that they have put that product with quantity X in their cart. I have included breadcrumbs to redirect the user back to all products page or home.

The about page explains a little about the owners of the website with a paragraph to left of the image of the owners. The testimonal section contains a carousel with a image, the comment and the auther and for now includes three different testimonals.

Blog page has an intro of the type of blogs the site will be submitting. Three images are placed below. Currently there are two blog posts which are in different categorys. The blogs contain a main image, a header, the date and time the blog was submitted and the information. The comment section below allows users to comment their thought on the blog and also give any tips they might want to add.

In a cart section, users can see all the items in their cart and when they change the quantity of it, it shows instantly. Once user is ready for checkout, they will see a form which they have to fill in order for the checkout to be completed. Once completed, the order will be stored in Account > Order History and user can see it anytime.

After every user input, submission, registration, login, comment, reply they are notified by a message from the web-site that briefly describes the action taken so that user knows their action was properly submitted.

## The Skeleton Plane

### Wireframes

Since this is a big project, I have decided to put wireframes in separate file.

You can access them [here]().

### Database Design

### Security

Using config variables in heroku, all SECRET access keys are stored safely to prevent unwanted connections to the database.

Django allauth was used to set up user registration and built in decorators allowed restricted access to certain features on the website that are not intended for regular users.

## The Surface Plane

### Colour Scheme

My inspiration for my site was taken from a colour pallett found on [Coloors](https://coolors.co/palettes/trending).

# Features

## Existing Features

## Future Features

# Technologies

The website is designed using following technologies:

## Programming languages

* HTML - the project used HTML to define structure and layout of the web page;
* CSS - the project used CSS stylesheets to specify style of the web document elements;
* JavaScript - the project used JavaScript to implement Stripe, EmailJS and custom Javascript.
* Python - the project back-end functions are written using Python.

## Libraries

* [Font Awesome](https://fontawesome.com/v4.7.0/) - Font Awesome icons were used throughout the web-site.
* [jQuery](https://jquery.com/) - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation.

## Frameworks & Extensions

* [Django](https://www.djangoproject.com/) – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Bootstrap](https://getbootstrap.com/) – Bootstrap is a web framework that focuses on simplifying the development of informative web pages.
* [EmailJS](https://www.emailjs.com/) – Service that helps sending emails using client side technologies only. It only requires to connect EmailJS to one of the supported email services, create an email template, and use their Javascript library to trigger an email.
* [Stripe](https://stripe.com/ie) – Allows individuals and businesses to make and receive payments over the Internet.

## Database
* [Heroku Postgres](https://www.heroku.com/postgres/) – PostgreSQL is one of the world's most popular relational database management systems.

## Others

* [GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git.
* [Gitpod](https://gitpod.io/workspaces/) - One-click ready-to-code development environments for GitHub.
* [Heroku](https://dashboard.heroku.com/) - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps.
* [AWS-S3](https://aws.amazon.com/s3/) – Object storage service that offers industry-leading scalability, data availability, security, and performance.

# Deployment

## AWS S3
Created a new Amazon account and connect to amazon service AWS3 account are cloud based serve where the project media and staicfiles will be stored unto. At first, we locate S3 on amazon service then we create a bucket. While creating the bucket on S3, the note that public access must be all switched off to allow access for users.

Once we've created the bucket, we now can now click on it's properties and enable the Static Website Hosting option, so it can serve the purpose of hosting our static files, you will need to imput an index.html and error.html before saving. Then we go into the created bucket Permissions and click into CORS configuration, this part already have a prefilled default config, All that is needed is just to write the default code and save the config.

Then we go into the bucket policy to allows access to the contents across all web and inside this we will put in here some code including arn address displayed at the top of the heading. Then we go into amazon IAM to allow identity and access management of our stored files and folder. In the IAM service, we add a new group for our application and then we set the policies to ALL Then it generates a downlaodable zip file containing ID and KEY for us to use for the newly added group. This ID and KEY as to be stored in an environment variable.

This then allows us to into our terminal window and install some settings Boto3 Django Storages

The Django Storages is passed into the installed apps in settings and also a custom_storage file is created to store credentials in environment variable. And once everything looks fine we can run python3 manage.py collectstatic. This will collect all the static files in our app including any changes that is made. N.B this command has to be run in the development(local) environment each time a change is been made in the static files/folder And your folder and files should display in your AWS S3 BUCKETS

## Heroku Deployment 

#### Create application:

1. Navigate to Heroku.com and login.
2. Click on the new button.
3. Select create new app.
4. Enter the app name.
5. Select region.

#### Set up connection to Github Repository:

1. Click the deploy tab and select GitHub - Connect to GitHub.
2. A prompt to find a github repository to connect to will then be displayed.
3. Enter the repository name for the project and click search.
4. Once the repo has been found, click the connect button.

#### Add PostgreSQL Database:

1. Click the resources tab.
2. Under Add-ons seach for Heroku Postgres and then click on it when it appears.
3. Select Plan name Hobby Dev - Free and then click Submit Order Form.

#### Set environment variables:

1. Click on the settings tab and then click reveal config vars.
2. Variables added: 
    * AWS_ACCESS_KEY_ID 
    * AWS_SECRET_ACCESS_KEY 
    * DATABASE_URL 
    * EMAIL_HOST_PASS 
    * EMAIL_HOST_USER
    * SECRET_KEY 
    * STRIPE_PRICE_ID 
    * STRIPE_PUBLIC_KEY 
    * STRIPE_SECRET_KEY 
    * STRIPE_WH_SECRET 
    * USE_AWS 

#### Enable automatic deployment:

1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

## Local Deployment

1. Navigate to the GitHub Repository.
2. Click the Code drop down menu.
3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
4. Open your developement editor of choice and open a terminal window in a directory of your choice.
5. Use the git clone command in terminal followed by the copied git URL.
6. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages: pip install -r requirements.txt

# Credits





