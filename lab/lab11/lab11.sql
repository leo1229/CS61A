.read sp20data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 order by smallest limit 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color,b.color
  from students as a, students as b
  where a.time < b.time and a.pet = b.pet and a.song = b.song
  order by a.time;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;


  CREATE TABLE stacks_helper(dogs, stack_height, last_height);
  insert into stacks_helper select name, height, height from dogs;
  insert into stacks_helper
    select dogs || ', ' || name, height+stack_height, height
    from dogs, stacks_helper
    where name != dogs and last_height < height;
  insert into stacks_helper
    select dogs || ', ' || name, height+stack_height, height
    from dogs, stacks_helper
    where name != dogs and last_height < height;
  insert into stacks_helper
    select dogs || ', ' || name, height+stack_height, height
    from dogs, stacks_helper
    where name != dogs and last_height < height;


  CREATE TABLE stacks AS
    SELECT dogs, stack_height
    from stacks_helper
    where stack_height > 170
    order by stack_height;
