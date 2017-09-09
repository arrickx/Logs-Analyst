# Logs-Analyst
* This is an internal reporting tool that will use information from the database to discover the answer of these following questions.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started
* You can *[clone](https://github.com/arrickx/Logs-Analyst.git)* or *[download](https://github.com/arrickx/Logs-Analyst.git)* this project via [GitHub](https://github.com) to your local machine.

### Prerequisites
You will need to install these following application in order to make this code work.
* Unix-style terminal(Windows user please download and use [Git Bash terminal](https://git-scm.com/downloads))
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

You will also need to download these following files to make it work.
* [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
* [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Installing

* Unzip the **VM configuration** and you will find a vagrant folder
* Use the **Terminal** to get into the vagrant folder from **VM configuration**
* run the following command
```sh
$ vagrant up
```
* This will cause Vagrant to download the Linux operating system and install it.
* After it finished and after the shell prompt comes back, you can run this command
```sh
$ vagrant ssh
```
* And this will let you login to the Linux VM.

### Setting up the enviroment

* First you need to move the **newsdata.py** from this project and **newsdata.sql** from the newsdata files into the vagrant folder in your local machince (not the Linux VM).
* To load the data, use the following command in the Terminal(make sure you are in the **Linux VM**)
```sh
psql -d news -f newsdata.sql
```
* Once you have the data loaded into your database, connect to your database using this command
```sh
psql -d news
```
* After you sucessfully connect to the database. Please create the following view by typing it in the psql
```sh
create view view_by_date  as
select time::date as date, count(*) as views
from log
group by date;
```
* and
```sh
create view error_by_date  as
select time::date as date, count(*) as errors
from log where status != '200 OK'
group by date
order by date;
```
* when you finish creating these two view. You can quit the PostgreSQL enviroment by this command
```sh
\q
```
* Now you can run this following code to find out those question's answer.
```sh
$ python newsdata.py
```

## License

* This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
* [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) was provided by [udacity](https://www.udacity.com).
* [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) was provided by [udacity](https://www.udacity.com).
