INSERT INTO doctors (doctor_id, first_name, last_name) VALUES 
('123456789', 'Lauren', 'Sinclair'),
('234567891', 'Kym', 'Ladell'),
('345678912', 'Kieran', 'White'),
('456789123', 'William', 'Hawkes');

INSERT INTO licenses (license_id, doctor_id, license_number, issue_date, expiration_date) VALUES 
('987654321', '123456789', '100000000', '2000-01-01', '2010-01-01'),
('876543219', '234567891', '200000000', '2003-06-06', '2013-06-06'),
('765432198', '345678912', '300000000', '2009-12-12', '2019-12-12'),
('654321987', '456789123', '400000000', '2012-01-01', '2022-01-01');