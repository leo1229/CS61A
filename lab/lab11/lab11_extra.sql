.read lab11.sql

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  from students
  group by smallest
  having count(*) = 1;

CREATE TABLE sp20favpets AS
  SELECT pet, count(*) as total
  from students
  group by pet
  order by -count(*) limit 10;


CREATE TABLE sp20dog AS
  SELECT pet, total
  from sp20favpets
  where pet = 'dog';


create table helper as
  select seven, instructor
  from students where seven = '7';

CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) as total
  from helper
  group by instructor
  order by instructor;
