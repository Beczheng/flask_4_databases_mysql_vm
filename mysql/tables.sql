CREATE TABLE doctors (
	doctor_id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE licenses (
    license_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_id INT,
    license_number INT,
    issue_date DATE,
    expiration_date DATE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) 
);