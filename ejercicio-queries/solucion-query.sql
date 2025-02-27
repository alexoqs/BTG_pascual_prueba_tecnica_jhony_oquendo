SELECT c.nombre FROM cliente AS c 
INNER JOIN inscripcion AS i ON i.id_cliente = c.id
INNER JOIN producto AS p ON i.id_producto = p.id
INNER JOIN disponibilidad AS d ON d.id_producto = p.id
INNER JOIN sucursal AS s ON s.id = d.id_sucursal
INNER JOIN visitan AS v ON v.id_sucursal = s.id AND v.id_cliente = c.id
