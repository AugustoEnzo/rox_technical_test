/*
 A Query to identify the five days with worst sellings operations.
 With the result of the query we could identify that all of our worst days of selling operations have the same minimum ticket
*/

SELECT
  DATE(order_date) AS order_date,
  SUM(sales_value) AS total_sales_value
FROM
  `hazel-thunder-425017-p5.rox_partner.sales`
GROUP BY
  order_date
ORDER BY
  SUM(sales_value) ASC
LIMIT 5