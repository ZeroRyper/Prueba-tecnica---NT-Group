CREATE TABLE companies (
    company_id VARCHAR(24) PRIMARY KEY,
    company_name VARCHAR(130)
);

CREATE TABLE charges (
    id VARCHAR(24) PRIMARY KEY,
    company_id VARCHAR(24),
    amount DECIMAL(16,2),
    status VARCHAR(30),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
