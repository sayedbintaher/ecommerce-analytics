CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    parent_category_id INT
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    city VARCHAR(100),
    country VARCHAR(100),
    signup_date TIMESTAMP
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    cost DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_products_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP NOT NULL,
    status VARCHAR(50) NOT NULL,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE order_items(
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    
    CONSTRAINT fk_order_items_product
        FOREIGN KEY (order_id)
        REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id int PRIMARY KEY,
    order_id INT NOT NULL, 
    payment_date TIMESTAMP NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,

    CONSTRAINT fk_payments_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

CREATE TABLE shipments (
    shipment_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    ship_date TIMESTAMP, 
    delivery_date TIMESTAMP, 
    status VARCHAR(50) NOT NULL,

    CONSTRAINT fk_shipments_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);

SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'
ORDER by table_name