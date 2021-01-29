CREATE TABLE tblTrail_Trajectory (
    trajectory_ID INT GENERATED ALWAYS AS IDENTITY,
    trail_ID INT,
    lat float NOT NULL,
    lon float NOT NULL,
    elev float NOT NULL,
    PRIMARY KEY(trajectory_ID),
    CONSTRAINT fk_Trails
        FOREIGN KEY(trail_ID)
            REFERENCES tblTrails(trail_ID));
