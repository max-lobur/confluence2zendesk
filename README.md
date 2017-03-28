# Migrate Confluence wiki article to Zendesk help center

A tool to migrate articles. It does not fully handle Confluence markup.

## Requirements
* python 3

## Installation
Get source and dependencies:
```
git clone https://github.com/max-lobur/confluence2zendesk.git && cd confluence2zendesk
virtualenv --python=`which python3` venv && source ./venv/bin/activate  # optional
pip3 install -r requirements.txt
```
Create and fill your local config file:
```
cp ./conf.sample ~/confl2zend.rc
vi ~/confl2zend.rc
source ~/confl2zend.rc
```
NOTE: Login/Password are required in config. If you use OAuth you still can add a 
password to your account through "I forgot password" form.

## Usage
##### Migrate article
```
./migrate.py <confluence_article_id> <target_zendesk_section_id>
```
* To get Confluence article id click `````"..." -> "Page Information"````` and 
get the id from the url. Or use ```search.py```
* To get Zendesk section id open the section you need and copy id from the 
url (it will look like 115000735929-FAQ)
##### Find confluence article by title/content
```
./search.py "<search text>"
```