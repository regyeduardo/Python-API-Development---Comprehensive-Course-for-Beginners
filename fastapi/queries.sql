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

-- ORDER BY: Ordera uma coluna (por padrao em ordem crescente)
SELECT * FROM products ORDER BY price; -- Todos os itens mas ordenado em ordem crescente (padrao)

-- ASC: Ordem crescente
SELECT * FROM products ORDER BY price ASC; -- Mesmo resultado da query anterior

-- DESC: Ordem decrescente
SELECT * FROM products ORDER BY price DESC; -- Todos os itens mas ordenado em ordem decrescente

SELECT * FROM products ORDER BY inventory DESC, price; -- Itens com a coluna inventory em ordem decrescente e tambem com a columa price em ordem crescente (padrao)
-- Caso o valor de um item seja zero em inventory entao sera ordenado pela segunda opcao que e price

-- LIMIT: Limita a quantidade de itens retornados
SELECT * FROM products LIMIT 10; -- Retorna os 10 primeiros id's

SELECT * FROM products WHERE price > 10 LIMIT 10; -- Retorna os 10 primeiros itens ordenados por id onde price e maior do que 10

-- OFFSET: Pula/Ignora os primeiros resultados
SELECT * FROM products ORDER BY id LIMIT 5 OFFSET 5; -- Retorna 5 itens ordenados por id pelando os 5 primeiros resultados, ou seja, comecando pelo id com valor 6

-- INSERT INTO https://youtu.be/0sOvCWFmrtA?t=13183
-- INSERTO INTO: Insere dados na tabela
INSERT INTO products (name, price, inventory) VALUES ('tortilla', 4, 1000); -- Cria uma nova linha na tabela definindo as colunas name, price e inventory 
-- E preciso definir em quais colunas irao ser preenchidas em uma sequencia e a sequencia de values precisa seguir essa seguencia para os valores de suas respectivas colunas

INSERT INTO products (price, name, inventory) VALUES (4, 'tortilla', 1000); -- O mesmo resultado da query anterior mas alterando a ordem de price e name

-- returning *: Retorna todas as colunas apos uma acao (CREATE, DELETE, UPDATE) 
INSERT INTO products (name, price, inventory) VALUES ('Car', 10000, 1000) returning *; -- Insere um item na tabela e depois o retorna
-- Se for retornar apenas uma coluna substitua "*" pela coluna

INSERT INTO products (name, price, inventory) VALUES ('Blue Car', 10000, 1000), ('Red Card', 20000, 500), ('Black Car', 500, 100) returning *; -- Adicionando tres linhas simultaneamente na tabela products

-- DELETE https://youtu.be/0sOvCWFmrtA?t=13632
-- DELETE: Deleta algo na tabela (nao se pode esquece de usar WHERE se nao ira deletar todos os dados)
DELETE FROM products WHERE id = 10; -- Deleta o item que possui o id 10

DELETE FROM products WHERE id = 11 RETURNING *; -- Deleta o item que possui o id 10 e retornando todas as colunas dessa linha

DELETE FROM products WHERE inventory = 0; -- Deleta os itens onde inventory e igual a 0