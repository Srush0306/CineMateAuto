CREATE DATABASE cinemate;

USE cinemate;

CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50),
    duration INT
);

CREATE TABLE shows (
    show_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    show_time VARCHAR(50),
    screen VARCHAR(20),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    show_id INT,
    customer_name VARCHAR(100),
    seats_booked INT,
    FOREIGN KEY (show_id) REFERENCES shows(show_id)
);
-- Insert Movies
INSERT INTO movies (title, genre) VALUES
('Avengers', 'Action'),
('Barbie', 'Comedy'),
('Interstellar', 'Sci-Fi');

-- Insert Shows
INSERT INTO shows (movie_id, show_time, screen) VALUES
(1, '6:30 PM', 'A'),
(2, '9:00 PM', 'B'),
(3, '3:00 PM', 'C');

