INSERT INTO coaches (first_name, last_name, email, password) values ("Bill", "Coachman", "bill@gmail.com", "Bill"),("Bob", "Coacher", "bill@gmail.com", "Bob");

INSERT INTO events (name) values ("Boys 100m Dash"),("Boys 200m Dash"),("Boys 400m Dash"),("Boys 800m Dash"),("Boys 4x100m Relay"),("Boys 4x200m Relay"),("Boys 4x400m Relay"),("Boys 4x800m Relay"),("Boys 100m Hurdles"),("Boys 300m Hurdles"),("Boys 1600m Run"),("Boys 3200m Run");
INSERT INTO events (name) values ("Girls 100m Dash"),("Girls 200m Dash"),("Girls 400m Dash"),("Girls 800m Dash"),("Girls 4x100m Relay"),("Girls 4x200m Relay"),("Girls 4x400m Relay"),("Girls 4x800m Relay"),("Girls 100m Hurdles"),("Girls 300m Hurdles"),("Girls 1600m Run"),("Girls 3200m Run");
INSERT INTO comment_content (content) values ("Nice time!"),( "What a run!"),("Keep training, you got this!"),("NEW RECORD!!!");
INSERT INTO times (time, date, coach_id,athlete_id,event_id) values(123,NOW(),1,1,1);