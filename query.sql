create table users(id integer primary key autoincrement, name text, not null, password text, email text, joined timestamp default (datetime('now', 'localtime')));
create table events(id integer primary key autoincrement, name text, not null, date timestamp default (datetime('now', 'localtime')), user_id integer, foreign key(user_id) references users(id), description text);



insert into users(name, password, email) values('Shmuli', '1234', 'shmulikeller@gmail.com');
INSERT INTO events(name, user_id, description, date) values('test', 2, 'test', '2020-02-01');
INSERT INTO events(name, user_id, description, date) values('test2', 1, 'test2', '2020-01-01');


SELECT * FROM users;
SELECT * FROM events where date = '2020-01-01';


-- get all events for a user by name
select * from events where user_id = (select id from users where name = "Shmuli");


-- get all events for a user by id
select * from events where user_id = 1;


--get user events by date (id)
select * from events where date = '2020-01-01' and user_id = 1;



--get user events by date (name)
select * from events where date = '2020-01-01' and user_id = (select id from users where name = "Shmuli");


