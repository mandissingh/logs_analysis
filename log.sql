-- Dropping views if already exists
DROP VIEW IF EXISTS view1 CASCADE;
DROP VIEW IF EXISTS view2 CASCADE;

-- Connecting to database
\c news;

-- Creating views
create view view1 as select time::timestamp::date, count(status) as total from log group by time::timestamp::date order by time::timestamp::date;
create view view2 as select time::timestamp::date, count(status) as fault from log where status = '404 NOT FOUND' group by time::timestamp::date;