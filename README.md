# Read Receipts
Web API built with Flask. Contains 1 GET request to fetch an image of a blank pixel used to obtain read receipt information in the mass email campaign.

## Deployment
The API is deployed at [readreceipts.net](http://readreceipts-env.eba-pciprdij.us-east-2.elasticbeanstalk.com/), which is an alias for the actual Elastic Beanstalk link.

## Testing
In the terminal / cmd, follow the following steps if you're using a Windows machine.
```
set FLASK_APP=application
flask run
```
The API will run on [http://localhost:5000/](http://localhost:5000/).