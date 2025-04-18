create table if not exists  artists(
	id SERIAL primary key,
	art_name VARCHAR(60) not null
);

create table if not exists albums (
	id SERIAL primary key,
	album_name  VARCHAR(80) not null,
	release_year INTEGER not null
);

create table if not exists genres (
	id SERIAL primary key,
	genre_name VARCHAR(60) not null
);

create table if not exists tracks (
	id SERIAL primary key,
	track_name VARCHAR(80) not null,
	artists_id integer not null,
	albums_id integer not null,
	track_length integer,
	foreign key (artists_id) references artists (id),
	foreign key (albums_id) references  albums (id)
);

create table if not exists compilation  (
	id SERIAL primary key,
	compilation_name VARCHAR(60) not null,
	compilation_release_year INTEGER
); 

create table if not exists artists_genres (
	artists_id integer,
	genres_id integer,
	foreign key (artists_id) references artists (id),
	foreign key (genres_id) references genres (id)
);


create table if not exists artist_albums (
	artists_id integer,
	albums_id integer,
	foreign key (artists_id) references artists (id),
	foreign key (albums_id) references albums (id)
);

create table if not exists compilation_tracks (
	compilation_id integer,
	tracks_id integer,
	foreign key (compilation_id) references compilation (id),
	foreign key (tracks_id) references tracks (id)
);

-- Задание №1

INSERT INTO genres (genre_name) VALUES
	('Rap'),
	('Soul'),
	('DeepHouse');


INSERT INTO artists (art_name) VALUES
	('Ja Rule'),
	('50Cent'),
	('Adele'),
	('Tini');


insert into albums (album_name, release_year) values
	('Pain Is Love', 2001),
	('Get Rich or Die Tryin', 2003),
	('The Massacre', 2005),
	('19', 2008),
	('TINI', 2019);

insert into tracks (track_name, artists_id, albums_id, track_length) values
	('Livin It Up', 1, 1, 257),
	('Always On Time', 1, 1, 245),
	('In Da Club', 2, 2, 193),
	('21 Questions', 2, 2, 236),
	('Melt My Heart to Stone', 3, 3, 204),
	('Chasing Pavements', 3, 3, 210),
	('Great Escape', 4, 4, 247),
	('Got My Started', 4, 4, 211);

insert into compilation (compilation_name, compilation_release_year) values
	('Exodus', 2005),
	('Best of 50 Cent', 2017),
	('21', 2011),
	('Quiero Volver', 2019);


insert into artists_genres (artists_id, genres_id) values
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 3);

insert into artist_albums (artists_id, albums_id) values
	(1, 1),
	(2, 2),
	(2, 3),
	(3, 4),
	(4, 5);

insert into compilation_tracks (compilation_id, tracks_id) values
	(1, 1),
	(1, 2),
	(2, 3),
	(2, 4),
	(3, 5),
	(3, 6),
	(4, 7),
	(4, 8);


-- Задание №2

select track_name, track_length from tracks
order by track_length desc limit 1 

select track_name, track_length from tracks
where track_length >= 210

select * from compilation с
where compilation_release_year between 2018 and 2020

select art_name from artists
where art_name not like '% %'

select track_name from tracks t 
where lower(track_name) like '%МОЙ%' or lower(track_name) like '%my%'


--Задание №3

SELECT g.genre_name, COUNT(DISTINCT ag.artists_id) AS artist_count
FROM genres g
LEFT JOIN artists_genres ag ON g.id = ag.genres_id
GROUP BY g.id, g.genre_name
ORDER BY artist_count DESC;

SELECT * FROM albums WHERE release_year BETWEEN 2019 AND 2020;

SELECT a.album_name, 
       AVG(t.track_length) AS avg_track_length
FROM albums a
JOIN tracks t ON a.id = t.albums_id
GROUP BY a.album_name
ORDER BY a.album_name;

SELECT DISTINCT art.art_name
FROM artists art
WHERE art.id NOT IN (
    SELECT DISTINCT aa.artists_id
    FROM artist_albums aa
    JOIN albums alb ON aa.albums_id = alb.id
    WHERE alb.release_year = 2020
)
ORDER BY art.art_name;

SELECT DISTINCT c.compilation_name, a.art_name AS artist_name
FROM compilation c
JOIN compilation_tracks ct ON c.id = ct.compilation_id
JOIN tracks t ON ct.tracks_id = t.id
JOIN artists a ON t.artists_id = a.id
WHERE a.art_name = 'Ja Rule'
ORDER BY c.compilation_name, a.art_name;






