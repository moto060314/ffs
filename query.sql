create database ffs;

use ffs;

create table messages (
  id int auto_increment primary key,
  content text not null,
  created_at timestamp default current_timestamp
);

