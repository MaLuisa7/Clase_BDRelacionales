USE profeco_db;
DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `test3`(  )
BEGIN
	SELECT 
	(sum(xmenosmean *ymenosmean)) / ( sqrt(sum(xmenosmeanCuadrado))* sqrt(sum(ymenosmeanCuadrado)) ) as correlacion
	FROM (
		SELECT 
			xy.x -  avg(xy.x) over () as xmenosmean , -- 1
			xy.y -  avg(xy.y) over () as ymenosmean , 
			( xy.x -  avg(xy.x) over () ) * ( xy.x -  avg(xy.x) over ()) as xmenosmeanCuadrado ,
			( xy.y -  avg(xy.y) over () ) * ( xy.y -  avg(xy.y) over ()) as ymenosmeanCuadrado 
		FROM xy	) as subq;
END;
DELIMITER //
call profeco_db.test3();
