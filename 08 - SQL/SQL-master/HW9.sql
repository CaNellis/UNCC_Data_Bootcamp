USE sakila;

-- ----------------- SECTION 1 --------------------
-- 1a. Display the first and last names of all actors from the table actor.
SELECT actor.first_name, actor.last_name FROM actor;
-- 1b. Display first and last name of actor in single column in upper case letters. Name the column Actor Name.
ALTER TABLE actor ADD COLUMN actor_name VARCHAR(80);
SET SQL_SAFE_UPDATES = 0;
UPDATE actor SET actor_name = CONCAT(first_name, " ", last_name) WHERE actor_id;

-- ----------------- SECTION 2 --------------------
-- 2a. find ID nu, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT * FROM actor WHERE first_name = "Joe";
-- 2b. Find all actors whose last name contain the letters GEN:
SELECT * FROM actor WHERE last_name LIKE '%GEN%';
-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT * FROM actor WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name DESC;
-- 2d. Using IN, display country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country.country_id, country.country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- ----------------- SECTION 3 --------------------
-- 3a. You want to keep a description of each actor. don't think will need to query so can use data type BLOB; research difference between BLOB and VARCHAR are significant).
ALTER TABLE actor ADD COLUMN actor_description BLOB;
-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER TABLE actor DROP COLUMN actor_description;

-- ----------------- SECTION 4 --------------------
-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(last_name) FROM actor GROUP BY last_name;
-- 4b. List last names and number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, COUNT(last_name) FROM actor GROUP BY last_name HAVING COUNT(last_name) >= 2;
-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor SET first_name = "HARPO", last_name = "WILLIAMS", actor_name = "HARPO WILLIAMS" WHERE actor_name = "GROUCHO WILLIAMS";
-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor SET first_name = "GROUCHO" WHERE actor_name = "HARPO WILLIAMS";

-- ----------------- SECTION 5 --------------------
-- 5a. You cant locate the schema of the address table. Which query would you use to re-create it?
-- Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html
SHOW CREATE TABLE address; 

-- ----------------- SECTION 6 --------------------
-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT s.first_name, s.last_name, a.address FROM staff as s 
INNER JOIN address as a ON s.address_id = a.address_id;
-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT s.first_name, s.last_name, SUM(p.amount) FROM staff as s 
INNER JOIN payment as p ON s.staff_id = p.staff_id 
WHERE p.payment_date >= '2005-08-00' AND p.payment_date < '2005-09-00' 
GROUP BY s.last_name; 
-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT f.title, count(a.actor_id) FROM film_actor AS a 
INNER JOIN film AS f ON a.film_id = f.film_id 
GROUP BY a.film_id;
-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT f.title, count(f.title) FROM film AS f 
WHERE f.title LIKE 'Hunchback Impossible%';
-- 6e. Using tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT c.first_name, c.last_name, SUM(p.amount) as 'Total Amount Paid' FROM customer AS c 
INNER JOIN payment AS p ON c.customer_id = p.customer_id GROUP BY c.last_name, c.first_name;

-- ----------------- SECTION 7 --------------------
-- 7a. in films table, use subqueries to display titles of movies starting with letters K and Q whose language is English.
SELECT title FROM film AS f 
WHERE title IN (SELECT title FROM film AS f WHERE title LIKE 'K%' OR 'Q%') 
AND language_id = 1;
-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name FROM actor 
WHERE actor_id IN (SELECT actor_id FROM film_actor WHERE film_id IN 
(SELECT film_id FROM film WHERE title = 'ALONE TRIP'));
-- 7c. use (inner) joins to get names and email addresses of all Canadian customers 
SELECT cu.first_name, cu.last_name, cu.email FROM customer AS cu 
INNER JOIN address AS ad ON cu.address_id = ad.address_id
INNER JOIN city AS ci ON ad.city_id = ci.city_id 
WHERE ci.country_id = 20;
-- 7d. Identify all movies categorized as family films.
SELECT f.title FROM film AS f
INNER JOIN film_category AS fca ON f.film_id = fca.film_id
INNER JOIN category AS ca ON ca.category_id = fca.category_id
WHERE ca.category_id = 8;
-- 7e. Display the most frequently rented movies in descending order.
SELECT f.title as 'Movie Title', count(f.title) as 'Number of Times Title was Rented' FROM film AS f
INNER JOIN inventory AS iv ON f.film_id = iv.film_id
INNER JOIN rental AS re ON iv.inventory_id = re.inventory_id
GROUP BY f.title
ORDER BY count(f.title) DESC;
-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT inv.store_id, SUM(pa.amount) as 'Gross Revenue in $' FROM payment AS pa
INNER JOIN rental AS re ON pa.customer_id = re.customer_id
INNER JOIN inventory AS inv ON re.inventory_id = inv.inventory_id
GROUP BY inv.store_id;
-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT st.store_id, ci.city, co.country FROM store AS st
INNER JOIN address AS ad ON st.address_id = ad.address_id 
INNER JOIN city AS ci ON ad.city_id = ci.city_id
INNER JOIN country AS co ON ci.country_id = co.country_id;
-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT ca.name AS 'Genre', sum(pa.amount) AS 'Gross Revenue in $' FROM category AS ca
INNER JOIN film_category AS fca ON ca.category_id = fca.category_id
INNER JOIN inventory AS inv ON fca.film_id = inv.film_id
INNER JOIN rental AS re ON inv.inventory_id = re.inventory_id
INNER JOIN payment AS pa ON re.rental_id = pa.payment_id
GROUP BY ca.name
ORDER BY sum(pa.amount) DESC
LIMIT 5;

-- ----------------- SECTION 8 --------------------
-- 8a. use 7h solution to create a view to easily see the Top five genres by gross revenue. 
CREATE OR REPLACE VIEW top_five_genres 
AS SELECT ca.name AS 'Genre', sum(pa.amount) AS 'Gross Revenue in $' FROM category AS ca
INNER JOIN film_category AS fca ON ca.category_id = fca.category_id
INNER JOIN inventory AS inv ON fca.film_id = inv.film_id
INNER JOIN rental AS re ON inv.inventory_id = re.inventory_id
INNER JOIN payment AS pa ON re.rental_id = pa.payment_id
GROUP BY ca.name
ORDER BY sum(pa.amount) DESC
LIMIT 5;
-- 8b. How would you display the view that you created in 8a?
SELECT * FROM top_five_genres;
-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW top_five_genres;