-- Drop if they already exist (makes the script idempotent)
DROP TABLE IF EXISTS progress_events;
DROP TABLE IF EXISTS orders;

-- Main order header table
CREATE TABLE orders (
  order_id         SERIAL PRIMARY KEY,          -- auto-increment
  customer_id      INT NOT NULL,
  material_grade   VARCHAR(30),
  quantity_ton     NUMERIC(10,2),
  order_date       DATE,
  promised_date    DATE,
  status           VARCHAR(15),
  last_update_ts   TIMESTAMP DEFAULT NOW()
);

-- History of status/location changes
CREATE TABLE progress_events (
  id               SERIAL PRIMARY KEY,
  order_id         INT REFERENCES orders(order_id) ON DELETE CASCADE,
  event_time       TIMESTAMP,
  location         VARCHAR(50),
  event            TEXT,
  notes            TEXT
);

-- Five mock orders
INSERT INTO orders (customer_id, material_grade, quantity_ton, order_date,
                    promised_date, status)
VALUES
 (101, 'IS2062 E250', 50, '2025-05-10', '2025-05-24', 'IN_PRODUCTION'),
 (102, 'API 5L X65',  80, '2025-05-12', '2025-05-26', 'DISPATCHED'),
 (103, 'IS2062 E350', 30, '2025-05-15', '2025-05-29', 'PLACED'),
 (104, 'ASTM A572',   60, '2025-05-14', '2025-05-28', 'DELIVERED'),
 (105, 'API 5CT K55', 40, '2025-05-11', '2025-05-25', 'CANCELLED');

-- Two progress events for order 1
INSERT INTO progress_events (order_id, event_time, location, event)
VALUES
 (1, '2025-05-15 09:30', 'Jamshedpur Mill', 'Slab casting complete'),
 (1, '2025-05-17 14:20', 'Jamshedpur Mill', 'Plate rolling complete');
