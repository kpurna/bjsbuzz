**** select directory to create virtual environment ****
virtualenv credr

source venv/bin/activate -- To activate virtual environment

*** clone the Git Repository ******

git clone https://github.com/kpurna/credr.git

install the requirements.txt file for installing required packages

Changes the database setting of your own in the credrApp/settings.py file

*** select the database and run the command to create required tables ******

CREATE TABLE users (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(50) NOT NULL,
  firstname varchar(50) NOT NULL DEFAULT '',
  lastname varchar(50) DEFAULT '',
  email_id varchar(100) NOT NULL,
  password varchar(100) NOT NULL,
  dob date NOT NULL,
  gender varchar(10) NOT NULL DEFAULT 'male',
  hq_passout_year int(10) NOT NULL DEFAULT '0',
  hq_degree varchar(50) NOT NULL,
  current_location varchar(50) NOT NULL DEFAULT '',
  search_type varchar(50) NOT NULL DEFAULT 'fresher',
  domain varchar(100) NOT NULL DEFAULT '',
  company varchar(100) NOT NULL DEFAULT '',
  candidate_desc varchar(400) NOT NULL DEFAULT '',
  last_updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 COMMENT='latin1_swedish_ci'


CREATE TABLE users_comments (
  comment_id int(11) NOT NULL AUTO_INCREMENT,
  uid int(11) NOT NULL,
  user_comment text NOT NULL,
  answer text NOT NULL,
  is_answered tinyint(4) NOT NULL DEFAULT '0',
  last_updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (comment_id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COMMENT='latin1_swedish_ci'



python manage.py runserver -- To run project in local.


********Create a new record in db*****
method:POST
url: http://localhost:8000/v1/users/

{
  "username" : "purna",
  "firstname": "purna",
  "lastname" : "chandra",
  "email_id" : "kpurna543@gmail.com",
  "password" : "123456",
  "dob" : "1992-08-03",
  "gender" : "male",
  "hq_passout_year" :"2014",
  "hq_degree": "btech",
  "current_location": "banglore",
  "search_type":"fresher",
  "domain":"it",
  "company":"",
  "candidate_desc":"",
  "last_updated":"2018-01-25T08:39:00"
}

method:PATCH
url: http://localhost:8000/v1/users/
{
  "company":"any it",
  "candidate_desc":"php, python"
}

********add record to users comments from user end *****
method: POST
url: http://localhost:8000/v1/users-comments/

{
  "uid" : 2,
  "user_comment":"I need a institite for some it course"
}

********update users comments from admin end *****

method: PATCH
url: http://localhost:8000/v1/users-comments/1

{
  "uid" : 2,
  "answer":"hackandriod",
  "is_answered": 1
}


************ GET Record **************

http://localhost:8000/v0/user-details   ///////// get all the records from user table
http://localhost:8000/v0/users-comments/ /// get particluar reordc with id specified
