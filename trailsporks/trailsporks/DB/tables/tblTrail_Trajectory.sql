CREATE TABLE tblTrail_Trajectory (
    trail_ID INT NOT NULL,
    lat float NOT NULL,
    lon float NOT NULL,
    elev float NOT NULL,
    PRIMARY KEY(trail_ID));


ALTER TABLE tblTrail_Trajectory   ADD CONSTRAINT FK_tblTrail_Trajectory_tblTrails FOREIGN KEY(trail_ID)
REFERENCES tblTrails (trail_ID);



