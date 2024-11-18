CREATE TABLE `payments`(
    `payment_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_id` BIGINT NOT NULL,
    `payment_date` DATE NOT NULL,
    `total` DECIMAL(8, 2) NOT NULL,
    `payment_method` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `payments` ADD INDEX `payments_invoice_id_index`(`invoice_id`);
CREATE TABLE `clients`(
    `client_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `company_id` BIGINT NOT NULL,
    `client_rib` VARCHAR(255) NOT NULL,
    `client_company` VARCHAR(255) NULL,
    `name` VARCHAR(255) NULL,
    `last_name` VARCHAR(255) NULL,
    `email` VARCHAR(255) NOT NULL,
    `phone` VARCHAR(255) NOT NULL,
    `address` TEXT NOT NULL,
    `created_at` TIMESTAMP NOT NULL
);
ALTER TABLE
    `clients` ADD INDEX `clients_company_id_index`(`company_id`);
CREATE TABLE `contracts`(
    `contract_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `client_id` BIGINT NOT NULL,
    `company_id` BIGINT NOT NULL,
    `description` TEXT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE NOT NULL,
    `amount` DECIMAL(8, 2) NOT NULL,
    `status` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `contracts` ADD INDEX `contracts_client_id_index`(`client_id`);
ALTER TABLE
    `contracts` ADD INDEX `contracts_company_id_index`(`company_id`);
CREATE TABLE `users`(
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
);
CREATE TABLE `companies`(
    `company_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` BIGINT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `address` TEXT NOT NULL,
    `created_at` TIMESTAMP NOT NULL
);
CREATE TABLE `invoices`(
    `invoice_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `company_id` BIGINT NOT NULL,
    `client_id` BIGINT NOT NULL,
    `total` DECIMAL(8, 2) NOT NULL,
    `status` VARCHAR(255) NOT NULL,
    `issue_date` DATE NOT NULL,
    `due_date` DATE NULL
);
ALTER TABLE
    `invoices` ADD INDEX `invoices_company_id_index`(`company_id`);
ALTER TABLE
    `invoices` ADD INDEX `invoices_client_id_index`(`client_id`);
ALTER TABLE
    `payments` ADD CONSTRAINT `payments_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `invoices`(`invoice_id`);
ALTER TABLE
    `companies` ADD CONSTRAINT `companies_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `users`(`user_id`);
ALTER TABLE
    `clients` ADD CONSTRAINT `clients_company_id_foreign` FOREIGN KEY(`company_id`) REFERENCES `companies`(`company_id`);
ALTER TABLE
    `contracts` ADD CONSTRAINT `contracts_company_id_foreign` FOREIGN KEY(`company_id`) REFERENCES `companies`(`company_id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_company_id_foreign` FOREIGN KEY(`company_id`) REFERENCES `companies`(`company_id`);
ALTER TABLE
    `contracts` ADD CONSTRAINT `contracts_client_id_foreign` FOREIGN KEY(`client_id`) REFERENCES `clients`(`client_id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_client_id_foreign` FOREIGN KEY(`client_id`) REFERENCES `clients`(`client_id`);


INSERT INTO users (name, last_name, email, password) VALUES ('John', 'Doe', 'john.doe@example.com', 'hashed_password');
INSERT INTO companies (user_id, name, address, created_at) VALUES (1, 'Tech Solutions', '1234 Tech Ave', NOW());
