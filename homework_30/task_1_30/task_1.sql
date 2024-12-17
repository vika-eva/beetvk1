CREATE TABLE contacts (
	id serial,
	name varchar(25) NOT NULL,
	phone_numb integer NOT NULL UNIQUE,
	last_name varchar(30),
	city varchar,
	bith_date date,
	creared_at timestamp DEFAULT now(),
	PRIMARY KEY (id)
)

-------

INTO contacts (name, phone_numb, last_name, city) VALUES ('tom', 0986665324, 'fov', 'paris')

INSERT INTO contacts (name, phone_numb, last_name, city) VALUES
('ann', 0987895324, 'ivachenko', 'london'),
('dan', 0955565324, 'alt', 'amsterdam'),
('joni', 0984459324, 'frolov', 'spain');

-----
ALTER TABLE contacts RENAME TO my_contacts

UPDATE contacts SET bith_date = '1995-12-12' WHERE name = 'tom'

UPDATE contacts SET bith_date = '03-03-1998' WHERE name = 'dan'

UPDATE contacts SET phone_numb = 0994567822 WHERE name = 'ann'

ALTER TABLE my_contacts ADD pets VARCHAR(20)

UPDATE contacts SET name = 'toom' WHERE name = 'tom'

DELETE FROM contacts WHERE name = 'toom'