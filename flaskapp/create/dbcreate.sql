-- (A) FEEDBACK
CREATE TABLE  if not exists `feedback` (
id int,userName varchar(255) NOT NULL,curDate varchar(40),userType varchar(255) NOT NULL,changes Text,brief Text,PRIMARY KEY (id)
);
CREATE TABLE  if not exists `user` (
id int,email varchar(100),role varchar(100),password varchar(255),PRIMARY KEY (id)
);