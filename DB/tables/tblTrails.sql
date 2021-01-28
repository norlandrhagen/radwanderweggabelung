-- trail metadata table

CREATE TABLE tblTrails (
    trail_ID INT GENERATED ALWAYS AS IDENTITY,
    trail_name varchar(50) NOT NULL,
    PRIMARY KEY(trail_ID)
);