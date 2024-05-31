/*
 A Query to identify the top 5 days with more clients (Non-distinct).
 With the query result we could identify that there's no days with more clients than others
*/

SELECT
  DATE(order_date) AS order_date,
  COUNT(client_email) AS number_of_clients
FROM
  `hazel-thunder-425017-p5.rox_partner.sales`
GROUP BY
  order_date
ORDER BY
  COUNT(client_email) DESC
LIMIT 5
