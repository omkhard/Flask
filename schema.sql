drop table if exists users;
    create table users (
    email text not null primary key,
    username text not null,
    password text not null
);