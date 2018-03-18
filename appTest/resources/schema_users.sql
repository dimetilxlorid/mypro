drop table if exists users;
create table users (
  id integer primary key autoincrement,
  nickname text not null,
  password text not null,
  role integer
);
drop table if exists pictures;
create table pictures (
  id integer primary key autoincrement,
  path text ,
  filename text not null,
  comment text,
  data text not null
);