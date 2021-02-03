-- trail metadata table

CREATE TABLE tblTrails (
    trail_ID INTEGER PRIMARY KEY,
    trail_name varchar(50) NOT NULL,
    UNIQUE (trail_name)

)