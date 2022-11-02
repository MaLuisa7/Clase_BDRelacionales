use profeco_db;
SELECT * FROM precio; -- ok cols(num_int, codigo_articulo, codigo_sucursal, descripcion, precio, fecha)
SELECT * FROM producto; -- ok  cols( num int, codigo, descripcion, precio_promedio)
SELECT * FROM tienda; -- ok cols(num_int, codigo, nombre,direccion, colonia, telefono, telefono2, estado, municipio,codigo_postal)
SELECT * FROM arbol; -- ok
SELECT * FROM zona;-- ok  

-- incluyan un join
CREATE VIEW precio_prod 
AS
SELECT precio.codigo_articulo , precio.codigo_sucursal, precio.descripcion, precio.precio/100, precio.fecha,
		producto.descripcion AS descrip , producto.codigo, producto.precio_promedio/100
FROM precio 
INNER JOIN producto
ON  precio.codigo_articulo = producto.codigo;

SELECT * FROM precio_prod;

-- incluyan un left join
CREATE VIEW precio_tienda
AS
SELECT precio.codigo_articulo, precio.codigo_sucursal, precio.descripcion, precio.precio, precio.fecha,
		tienda.num_int, tienda.codigo, tienda.nombre,tienda.direccion, tienda.colonia, tienda.estado, tienda.municipio 
FROM precio 
LEFT JOIN tienda
ON  precio.codigo_sucursal = tienda.codigo;
SELECT * FROM precio_tienda;

-- incluyan right join
CREATE VIEW precio_producto
AS
SELECT precio.codigo_articulo, precio.codigo_sucursal, precio.descripcion as precio_desc , precio.precio/100 as precio_precio, precio.fecha,
		producto.descripcion as prod_desc, producto.precio_promedio/100 as precio_prod
FROM precio 
RIGHT JOIN producto
ON  precio.codigo_articulo = producto.codigo;
SELECT * FROM precio_producto;

-- incluyan subconsulta
SELECT prod_desc
FROM
(
SELECT COUNT(precio_desc) as numero_desc ,precio_desc, ROUND(AVG(precio_precio),2) as avg_precio_precio, prod_desc, 
		ROUND(AVG(precio_prod ),2) as avg_precio_prod
FROM precio_producto
GROUP BY precio_desc
ORDER BY avg_precio_precio desc
) as subquery1;

-- investigar y crear al menos un disparador (TRIGGER) de inserción, actualización o eliminación.
-- se crea una tabla donde se llevará el registro de los triggers que se realicen

show tables; 
select * from zona;

-- create table contacts_audit (contact_id integer, 
--                             created_date date, 
--                             created_by varchar (30)); 
SELECT * FROM contacts_audit;

DELIMITER $$

CREATE TRIGGER after_newZone_insert1
AFTER INSERT
ON zona FOR EACH ROW
BEGIN
    IF NEW.estado IS NULL THEN
        INSERT INTO contacts_audit(contact_id,created_date, created_by)
        VALUES( 99999, sysdate(), 'user_crazy');
    END IF;
END$$

DELIMITER ;
             
insert into zona values ( 12345, 67890, "fifi" ); 
insert into zona values (963852, 6789770,    NULL); 
select *from contacts_audit;
select *from zona ;

    
