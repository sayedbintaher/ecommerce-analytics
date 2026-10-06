COPY categories
FROM '/home/sayed/CodePractice/Python/ecommerce-analytics/data/cleaned/categories.csv'
WITH (
    FORMAT csv,
    HEADER 
);