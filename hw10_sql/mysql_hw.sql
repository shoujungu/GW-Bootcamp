# 1a.
USE sakila;

SELECT first_name,last_name FROM sakila.actor;

# 1b.
USE sakila;

ALTER TABLE `sakila`.`actor` 
ADD COLUMN `Actor Name` VARCHAR(45) NULL AFTER `last_update`;

UPDATE actor
SET `Actor Name`=CONCAT(actor.first_name,' ', actor.last_name); 

# 2a.
USE sakila;

SELECT actor_id,first_name,last_name FROM sakila.actor
WHERE first_name='Joe';

# 2b.
USE sakila;

SELECT * FROM sakila.actor
WHERE first_name LIKE '%GEN%';

# 2c.
USE sakila;

SELECT * FROM sakila.actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name,first_name;

# 2d.
USE sakila;

SELECT country_id,country FROM sakila.country
WHERE country IN ('Afghanistan','Bangladesh','China');

# 3a.
USE sakila;

ALTER TABLE `sakila`.`actor` 
ADD COLUMN `middle_name` VARCHAR(45) NULL AFTER `first_name`;

# 3b.
USE sakila;

ALTER TABLE `sakila`.`actor` 
CHANGE COLUMN `middle_name` `middle_name` BLOB NULL DEFAULT NULL ;

# 3c.
USE sakila;

ALTER TABLE `sakila`.`actor` 
DROP COLUMN `middle_name`;

# 4a.
USE sakila;

SELECT DISTINCT last_name, COUNT(last_name)
FROM sakila.actor
GROUP BY last_name;

# 4b.
USE sakila;

SELECT DISTINCT last_name, COUNT(last_name)
FROM sakila.actor
GROUP BY last_name
HAVING COUNT(last_name)>1;

# 4c.
USE sakila;

UPDATE sakila.actor
SET first_name='HARPO'
WHERE actor_id=(SELECT actor_id FROM sakila.actor WHERE first_name='GROUCHO' AND last_name='WILLIAMS');

# 4d.
USE sakila;

UPDATE sakila.actor
SET first_name=IF(first_name='HARPO','GROUCHO','MUCHO GROUCHO')
WHERE actor_id=172;

# 5a.
USE sakila;

CREATE TABLE address;

# 6a.
USE sakila;

SELECT first_name,last_name,address
FROM address INNER JOIN staff 
ON address.address_id=staff.address_id;

# 6b.
USE sakila;

SELECT SUM(amount)
FROM staff INNER JOIN payment 
ON staff.staff_id=payment.staff_id
WHERE payment_date LIKE '2005-08%'
GROUP BY staff.staff_id;

# 6c.
USE sakila;

SELECT film.title,COUNT(film_actor.actor_id)
FROM film INNER JOIN film_actor 
ON film.film_id=film_actor.film_id
GROUP BY film.title;

# 6d.
USE sakila;

SELECT COUNT(inventory.store_id)
FROM film INNER JOIN inventory 
ON film.film_id=inventory.film_id
WHERE film.title='Hunchback Impossible';

# 6e.
USE sakila;

SELECT customer.last_name,SUM(payment.amount)
FROM payment INNER JOIN customer
ON payment.customer_id=customer.customer_id
GROUP BY customer.customer_id
ORDER BY customer.last_name;

# 7a.
USE sakila;

SELECT *
FROM film
WHERE (title LIKE 'K%') OR 
      (title LIKE 'Q%') AND 
      (language_id=(SELECT language_id FROM language WHERE name='English'));

# 7b.
USE sakila;

SELECT first_name,Last_name
FROM actor
WHERE actor_id IN (SELECT actor_id FROM film_actor WHERE film_id=(
                    SELECT film_id FROM film WHERE title='Alone Trip'
                      )
                );

# 7c.
USE sakila;

SELECT cu.first_name,cu.last_name,cu.email
FROM customer cu
INNER JOIN address ad ON cu.address_id=ad.address_id
INNER JOIN city ci ON ad.city_id=ci.city_id
INNER JOIN country co ON ci.country_id=co.country_id
WHERE co.country='Canada';

# 7d.
USE sakila;

SELECT f.title
FROM film f
INNER JOIN film_category fc ON f.film_id=fc.film_id
INNER JOIN category c ON fc.category_id=c.category_id
WHERE c.name='Family';

# 7e.
USE sakila;

SELECT f.title, COUNT(f.title)
FROM film f 
INNER JOIN inventory i ON f.film_id=i.film_id
INNER JOIN rental r ON i.inventory_id=r.inventory_id
GROUP BY f.title
ORDER BY COUNT(f.title) DESC;

# 7f.
USE sakila;

SELECT i.store_id, SUM(p.amount) AS Gross
FROM payment p
INNER JOIN rental r ON p.rental_id=r.rental_id
INNER JOIN inventory i ON r.inventory_id= i.inventory_id
GROUP BY i.store_id;

# 7g.
USE sakila;

SELECT s.store_id, ci.city, co.country
FROM store s
INNER JOIN address a ON s.address_id=a.address_id
INNER JOIN city ci ON a.city_id=ci.city_id
INNER JOIN country co ON ci.country_id=co.country_id;

# 7h.
USE sakila;

SELECT c.name,SUM(p.amount) AS 'gross revenue'
FROM payment p
INNER JOIN rental r ON p.rental_id=r.rental_id
INNER JOIN inventory i ON r.inventory_id=i.inventory_id
INNER JOIN film_category f ON i.film_id=f.film_id
INNER JOIN category c ON f.category_id=c.category_id 
GROUP BY c.name
ORDER BY SUM(p.amount) DESC
LIMIT 5;

# 8a.
USE sakila;

CREATE VIEW top_five_genres AS
SELECT c.name,SUM(p.amount) AS 'gross revenue'
FROM payment p
INNER JOIN rental r ON p.rental_id=r.rental_id
INNER JOIN inventory i ON r.inventory_id=i.inventory_id
INNER JOIN film_category f ON i.film_id=f.film_id
INNER JOIN category c ON f.category_id=c.category_id 
GROUP BY c.name
ORDER BY SUM(p.amount) DESC
LIMIT 5;

# 8b.
SELECT * FROM top_five_genres;

# 8c.
DROP VIEW top_five_genres;


