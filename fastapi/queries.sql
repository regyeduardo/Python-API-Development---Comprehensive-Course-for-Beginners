-- SELECT * FROM: Retorna todos as colunas da tabela
SELECT * FROM products; -- Retorna todos os itens

-- WHERE: Executa determinada condicao
SELECT * FROM products WHERE price > 20; -- Itens onde price e maior que 20
-- WHERE price <> 20; preco diferente de 20

-- AND: Operador logico "e"
SELECT * FROM products WHERE inventory > 0 AND price > 20; -- Itens onde inventorio maior que 0 e tambem price maior que 0

-- OR: Operador logico "ou"
SELECT * FROM products WHERE price > 100 OR price < 20; -- Itens onde price e maior que 100 ou price e menor que 20

SELECT * FROM products WHERE id = 1 OR id = 2 OR id = 3; -- Itens onde o id e 1, 2 ou 3

-- IN: Verifica uma lista de valores
SELECT * FROM products WHERE id IN (1,2,3); -- O mesmo resultado da query acima

-- LIKE: Retorna algo se o valor satisfazer determinada string 
SELECT * FROM products WHERE name LIKE 'Laptop%'; -- Itens onde name comeca com "Laptop"
-- % significa "qualquer coisa", ou seja, qualquer coisa apos de "Laptop" (case-sensitive)

SELECT * FROM products WHERE name LIKE '%n'; -- Itens que terminam com a letra n name

SELECT * FROM products WHERE name LIKE '%n%'; -- Qualquer item que possua pelo menos uma letra "n" na coluna name

-- NOT: Inverte o comando a seguir
SELECT * FROM products WHERE name NOT LIKE 'en%'; -- Itens que nao comecam com "en"