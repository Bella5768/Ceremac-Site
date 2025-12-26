-- Base de données CEREMAC
CREATE DATABASE IF NOT EXISTS ceremac_db CHARACTER SET utf8 COLLATE utf8_general_ci;
USE ceremac_db;

-- Table des utilisateurs
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    full_name VARCHAR(100),
    role ENUM('admin', 'member') DEFAULT 'member',
    can_validate TINYINT(1) DEFAULT 0,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Table des actualités
CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    image VARCHAR(255),
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    date_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Table des projets
CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    image VARCHAR(255),
    file_path VARCHAR(255),
    status ENUM('current', 'past') DEFAULT 'current',
    date_start DATE,
    date_end DATE,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Table des publications
CREATE TABLE IF NOT EXISTS publications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    description TEXT,
    file_path VARCHAR(255),
    publication_date DATE,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Table des partenaires
CREATE TABLE IF NOT EXISTS partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    logo VARCHAR(255),
    website VARCHAR(255),
    type ENUM('national', 'international') DEFAULT 'national',
    description TEXT,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Table des messages de contact
CREATE TABLE IF NOT EXISTS contact_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Table des abonnés à la newsletter
CREATE TABLE IF NOT EXISTS newsletter_subscribers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_subscribed DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Insertion d'un utilisateur admin par défaut (mot de passe: admin123)
-- À changer après la première connexion!
INSERT INTO users (username, password, email, full_name, role) VALUES 
('admin', '$2y$10$vFuo4AEb7AoQ9JSrxZF0F.PvHUa42038W2pcS0UKF8Ylk1ABrONxa', 'admin@ceremac.gn', 'Administrateur', 'admin');

-- Données d'exemple pour les actualités
INSERT INTO news (title, content, date_created) VALUES 
('Bienvenue sur le site du CEREMAC', 'Le Centre de Recherche en Océanographie, Environnement Marin et Côtier est heureux de vous accueillir sur son nouveau site web.', NOW()),
('Nouveau projet de recherche', 'Le CEREMAC lance un nouveau projet de recherche sur l\'impact du changement climatique sur les écosystèmes marins côtiers.', NOW()),
('Publication scientifique', 'Notre équipe a publié un article important sur la biodiversité marine en Guinée dans une revue internationale.', NOW());

-- Données d'exemple pour les projets
INSERT INTO projects (title, description, status, date_start) VALUES 
('Étude de la biodiversité marine', 'Projet de recherche approfondie sur la biodiversité des écosystèmes marins de la côte guinéenne.', 'current', CURDATE()),
('Protection des mangroves', 'Programme de protection et de restauration des mangroves côtières.', 'current', CURDATE()),
('Projet de recherche océanographique', 'Étude des courants marins et de leur impact sur l\'écosystème côtier.', 'past', DATE_SUB(CURDATE(), INTERVAL 1 YEAR));

-- Données d'exemple pour les publications
INSERT INTO publications (title, author, description, publication_date) VALUES 
('Biodiversité marine en Guinée', 'Dr. Alpha Diallo', 'Étude complète sur la biodiversité marine des côtes guinéennes.', CURDATE()),
('Impact du changement climatique', 'Dr. Fatoumata Bah', 'Analyse de l\'impact du changement climatique sur les écosystèmes marins.', DATE_SUB(CURDATE(), INTERVAL 6 MONTH)),
('Océanographie côtière', 'Dr. Mamadou Camara', 'Recherche sur les caractéristiques océanographiques de la zone côtière.', DATE_SUB(CURDATE(), INTERVAL 1 YEAR));

-- Données d'exemple pour les partenaires
INSERT INTO partners (name, type, website) VALUES 
('Ministère de l\'Environnement', 'national', 'https://example.com'),
('Université de Conakry', 'national', 'https://example.com'),
('Institut de Recherche Océanographique', 'international', 'https://example.com'),
('Organisation Maritime Internationale', 'international', 'https://example.com');

