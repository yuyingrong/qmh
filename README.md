# Quakers and Mental Health
http://qmh.haverford.edu/

The Quakers & Mental Health portal launched in the summer of 2015 as an interactive website to hold scholarship about the history of mental health in Philadelphia, in the 19th and 20 centuries, and in particular of Friends Hospital, the first private mental health institution in the United States. This multi-year project combines archival research and writing with digital scholarship to create and support scholarship on the history of mental health, to analyze data and create visualizations from that research. The Friends Hospital records, which are on loan to Haverford College Quaker & Special Collections, offer a wealth of information on Quakerism, the treatment of the mentally ill, and the development of American psychiatric hospitals in the 19th and 20th centuries.

This project consists of basic static pages built on Django, and uses Plotly to create interactive data visualizations.


## Local Development

### Install the requirements

`pip install virtualenv`

`python3 -m venv env`

`source env/bin/activate`

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`


### Set up a local server

`python myAsylum/manage.py migrate`

`python myAsylum/manage.py runserver`

View local server at: http://127.0.0.1:8000/

*Additional notes: see "tutorials" and "instructions" in "Summer 2019/Yuying Rong/" in Friends Asylum Google Drive.*


## Deploying

Start by ssh-ing into the server (`ssh USER@IP_ADDRESS`). (To deploy to production, you must be on the [Haverford VPN](https://iitskb.sites.haverford.edu/knowledge-base/installing-the-vpn-client/) first. Request credentials from IT if you don't have them.) Once you are on the server, you can use sudo to get elevated privileges for anything requiring them. The project directory with the live code is located in "/srv/qmh-v2".

`cd /srv/qmh-v2`

`git pull origin master`

On prod you'll need to run git with sudo: `sudo git pull origin master` (then enter password)

The web server itself is a 2-tiered application stack; Nginx runs the HTTP port advertisement and proxies all requests to a local socket owned by uWSGI. The configuration for Nginx lives in "/etc/nginx/sites-enabled/qmh-v2". The configuration for uWSGI lives in "/etc/uwsgi/apps-enabled/qmh-v2.ini". If you make any changes to the configuration, you can use "systemctl restart servicename" (uwsgi or nginx) to restart the appropriate service. You will need to restart uWSGI for any changes to the application's code to be live, as the uWSGI socket points to a version living in RAM and restarting the application container is the only way to update it with new code.

`sudo systemctl restart uwsgi`

## Adding new images
In the repo, add images to this directory [/myAsylum/qmh/static/images](https://github.com/HCDigitalScholarship/qmh-v2/tree/master/myAsylum/qmh/static/images). The static image mounting does not appear to be correctly set up. This needs to be fixed in the future. In the meantime, you can manually copy the image from the upload directly to the static folder it wants to be in:

Example:
`cd /srv/qmh-v2/myAsylum/static/images`

`cp /srv/qmh-v2/myAsylum/qmh/static/images/GenderDeath.png GenderDeath.png`


## Adding New Essays

1. Upload the PDF to [this static folder](https://github.com/HCDigitalScholarship/qmh-v2/tree/master/myAsylum/static/essays) (note: there are two static folders, we don't know why. `/myAsylum/static/essays` in the correct one). 
2. Create the html template in `/myAsylum/qmh/templates/` (you can mostly duplicate an existing essay template)
3. Add the page to the `views.py` [here](https://github.com/HCDigitalScholarship/qmh-v2/blob/master/myAsylum/qmh/views.py)
4. Add the page in `urls.py` [here](https://github.com/HCDigitalScholarship/qmh-v2/blob/master/myAsylum/qmh/urls.py)
5. Update the table in `essays.html` [here](https://github.com/HCDigitalScholarship/qmh-v2/blob/master/myAsylum/qmh/templates/essays.html) to include the link to your new essay page
6. Commit & merge your changes 
7. Deploy your changes to the server and restart the server (see above)


## Updates in 2019 summer:

- Templates: adopted most website pages to conciser, cleaner template scripts.
- Data visualizations: migrated some graphs through copy-pasting; re-wrote all Bokeh graphs with Plotly JS; created one new graph with HTML/CSS.
  - The new HTML/CSS graph has visible issues (extra lines), and is not responsive.
  - The D3.js graphs copy-pasted as-were are not responsive, either because of their nature or the units, such as px, that scale the graphs.
- Static images: the "images" folder in "static/images" (i.e. static/images/images/) contains potentially useful images which are NOT in use in the website; images in the outer "images" folder contain all and only images in use.
- The project: re-structured the directory hierarchy to the regular structure; the "my" in naming, e.g. "myqmh", "myAsylum", was used to distinguish the new project I was working on with the old "FriendsAsylum" project name on the server. Feel free to change.
- Stylesheets: "base.css" styles mostly just what is in "base.html"; repetitive features, such as "buttons", in almost all pages, are styled in "elements.css".

REMAINING TASKS
- All copy-pasted d3 graphs had fixed dimension which would not display properly on smaller screens; I thought they all needed to be remade.
- In-text glossary fetching is not enabled on every page. I only knew to add the same code under every function in "views.py" so every page could load "glossary_dict" which the get_item custom tag would grab glossary info from. I believed that a smarter way for all functions to inherit these lines must exist.
- I wanted to add all bibliography as an object to Models, but bib info was not full and I did not have the time. Once added, I would like to create another custom tag to grab info from the database, and then enable an topple-show feature for clickable citations. However, it still needs to be consulted whether to carry out these steps.
