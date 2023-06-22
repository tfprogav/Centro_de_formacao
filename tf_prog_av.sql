-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 21, 2023 at 08:36 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tf_prog_av`
--

-- --------------------------------------------------------

--
-- Table structure for table `q_alunos`
--

DROP TABLE IF EXISTS `q_alunos`;
CREATE TABLE IF NOT EXISTS `q_alunos` (
  `aluno_id` int NOT NULL AUTO_INCREMENT,
  `aluno_nome` varchar(100) NOT NULL,
  `aluno_telefone` int NOT NULL,
  `aluno_email` varchar(100) NOT NULL,
  PRIMARY KEY (`aluno_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_alunos`
--

INSERT INTO `q_alunos` (`aluno_id`, `aluno_nome`, `aluno_telefone`, `aluno_email`) VALUES
(1, 'John Doe', 1234567890, 'john.doe@example.com'),
(2, 'Jane Smith', 2147483647, 'jane.smith@example.com'),
(3, 'Michael Johnson', 2147483647, 'michael.johnson@example.com'),
(4, 'Emily Davis', 2147483647, 'emily.davis@example.com'),
(5, 'David Wilson', 1112223333, 'david.wilson@example.com');

-- --------------------------------------------------------

--
-- Table structure for table `q_alunos_cursos`
--

DROP TABLE IF EXISTS `q_alunos_cursos`;
CREATE TABLE IF NOT EXISTS `q_alunos_cursos` (
  `aluno_id` int DEFAULT NULL,
  `curso_id` int DEFAULT NULL,
  KEY `aluno_id` (`aluno_id`),
  KEY `curso_id` (`curso_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_alunos_cursos`
--

INSERT INTO `q_alunos_cursos` (`aluno_id`, `curso_id`) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 2),
(4, 1),
(5, 2),
(2, 2),
(3, 1),
(4, 2),
(5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `q_aulas`
--

DROP TABLE IF EXISTS `q_aulas`;
CREATE TABLE IF NOT EXISTS `q_aulas` (
  `aula_id` int NOT NULL AUTO_INCREMENT,
  `aulas_curso_id` int NOT NULL,
  `aula_desc` varchar(100) NOT NULL,
  `aula_prof_id` int NOT NULL,
  `aula_inicio` datetime NOT NULL,
  `aula_termino` datetime NOT NULL,
  `aula_sumarios` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `aula_ausencias` int NOT NULL,
  PRIMARY KEY (`aula_id`),
  KEY `aulas_curso_id` (`aulas_curso_id`),
  KEY `aula_prof_id` (`aula_prof_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_aulas`
--

INSERT INTO `q_aulas` (`aula_id`, `aulas_curso_id`, `aula_desc`, `aula_prof_id`, `aula_inicio`, `aula_termino`, `aula_sumarios`, `aula_ausencias`) VALUES
(1, 1, 'Introduction to Programming', 2, '2023-06-18 09:00:00', '2023-06-18 11:00:00', 'Summary of the first lecture', 0),
(2, 1, 'Data Structures', 2, '2023-06-19 09:00:00', '2023-06-19 11:00:00', 'Summary of the second lecture', 0),
(3, 2, 'Web Development', 2, '2023-06-20 09:00:00', '2023-06-20 11:00:00', 'Summary of the third lecture', 0),
(4, 1, 'Object-Oriented Programming', 2, '2023-06-21 09:00:00', '2023-06-21 11:00:00', 'Summary of the fourth lecture', 0),
(5, 2, 'Database Management', 2, '2023-06-22 09:00:00', '2023-06-22 11:00:00', 'Summary of the fifth lecture', 0);

-- --------------------------------------------------------

--
-- Table structure for table `q_avaliacoes`
--

DROP TABLE IF EXISTS `q_avaliacoes`;
CREATE TABLE IF NOT EXISTS `q_avaliacoes` (
  `avaliacao_id` int NOT NULL AUTO_INCREMENT,
  `avaliacao_aluno` varchar(100) NOT NULL,
  `avaliacao_data` date NOT NULL,
  `avaliacao_aula` varchar(100) NOT NULL,
  `avaliacao_prof_id` int NOT NULL,
  PRIMARY KEY (`avaliacao_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_avaliacoes`
--

INSERT INTO `q_avaliacoes` (`avaliacao_id`, `avaliacao_aluno`, `avaliacao_data`, `avaliacao_aula`, `avaliacao_prof_id`) VALUES
(1, 'John Doe', '2023-06-18', 'Introduction to Programming', 1),
(2, 'Jane Smith', '2023-06-19', 'Data Structures', 1),
(3, 'Michael Johnson', '2023-06-20', 'Web Development', 2),
(4, 'Emily Davis', '2023-06-21', 'Object-Oriented Programming', 3),
(5, 'David Wilson', '2023-06-22', 'Database Management', 3);

-- --------------------------------------------------------

--
-- Table structure for table `q_cursos`
--

DROP TABLE IF EXISTS `q_cursos`;
CREATE TABLE IF NOT EXISTS `q_cursos` (
  `curso_id` int NOT NULL AUTO_INCREMENT,
  `curso_desc` varchar(100) NOT NULL,
  `curso_horas` int NOT NULL,
  `curso_preco` int NOT NULL,
  `curso_alunos` int NOT NULL,
  PRIMARY KEY (`curso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_cursos`
--

INSERT INTO `q_cursos` (`curso_id`, `curso_desc`, `curso_horas`, `curso_preco`, `curso_alunos`) VALUES
(1, 'Programming Fundamentals', 40, 200, 20),
(2, 'Web Development Basics', 30, 150, 15),
(3, 'Database Management Essentials', 35, 180, 18),
(4, 'Mobile App Development', 45, 250, 25),
(5, 'Software Engineering Principles', 50, 300, 30),
(7, 'Teste 123', 50, 250, 0),
(8, 'Tteste 1415 7', 653, 12312, 0);

-- --------------------------------------------------------

--
-- Table structure for table `q_pagamentos`
--

DROP TABLE IF EXISTS `q_pagamentos`;
CREATE TABLE IF NOT EXISTS `q_pagamentos` (
  `pagamento_id` int NOT NULL AUTO_INCREMENT,
  `pagamento_data` date NOT NULL,
  `pagamento_aluno_id` int NOT NULL,
  `pagamento_valor` decimal(10,0) NOT NULL,
  `pagamento_metodo` varchar(100) NOT NULL,
  PRIMARY KEY (`pagamento_id`),
  KEY `pagamento_aluno_id` (`pagamento_aluno_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_pagamentos`
--

INSERT INTO `q_pagamentos` (`pagamento_id`, `pagamento_data`, `pagamento_aluno_id`, `pagamento_valor`, `pagamento_metodo`) VALUES
(1, '2023-06-18', 1, 100, 'Credit Card'),
(2, '2023-06-19', 2, 150, 'PayPal'),
(3, '2023-06-20', 3, 200, 'Bank Transfer'),
(4, '2023-06-21', 4, 250, 'Cash'),
(5, '2023-06-22', 5, 300, 'Credit Card');

-- --------------------------------------------------------

--
-- Table structure for table `q_perfis`
--

DROP TABLE IF EXISTS `q_perfis`;
CREATE TABLE IF NOT EXISTS `q_perfis` (
  `perfil_id` int NOT NULL AUTO_INCREMENT,
  `perfil_nome` varchar(100) NOT NULL,
  `perfil_estado` int NOT NULL,
  PRIMARY KEY (`perfil_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_perfis`
--

INSERT INTO `q_perfis` (`perfil_id`, `perfil_nome`, `perfil_estado`) VALUES
(1, 'Admin', 1),
(2, 'Instructor', 1),
(3, 'Student', 1),
(4, 'Staff', 1),
(5, 'Guest', 0);

-- --------------------------------------------------------

--
-- Table structure for table `q_utilizadores`
--

DROP TABLE IF EXISTS `q_utilizadores`;
CREATE TABLE IF NOT EXISTS `q_utilizadores` (
  `utilizador_id` int NOT NULL AUTO_INCREMENT,
  `utilizador_nome` varchar(100) NOT NULL,
  `utilizador_email` varchar(100) NOT NULL,
  `utilizador_endereco` varchar(100) NOT NULL,
  `utilizador_nascimento` date NOT NULL,
  `utilizador_senha` varchar(20) NOT NULL,
  `utilizador_perfil` int NOT NULL,
  PRIMARY KEY (`utilizador_id`),
  KEY `utilizador_perfil` (`utilizador_perfil`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_utilizadores`
--

INSERT INTO `q_utilizadores` (`utilizador_id`, `utilizador_nome`, `utilizador_email`, `utilizador_endereco`, `utilizador_nascimento`, `utilizador_senha`, `utilizador_perfil`) VALUES
(1, 'John Doe', 'john.doe@example.com', '123 Main St', '1990-05-15', 'password123', 1),
(2, 'Jane Smith', 'jane.smith@example.com', '456 Elm St', '1992-09-30', 'secret456', 2),
(3, 'Michael Johnson', 'michael.johnson@example.com', '789 Oak St', '1985-11-20', 'mypassword', 3),
(4, 'Emily Davis', 'emily.davis@example.com', '321 Maple Ave', '1993-07-12', '987654', 4),
(5, 'David Wilson', 'david.wilson@example.com', '567 Pine Rd', '1988-03-08', 'pass123', 5);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `q_alunos`
--
ALTER TABLE `q_alunos`
  ADD CONSTRAINT `q_alunos_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `q_alunos_cursos`
--
ALTER TABLE `q_alunos_cursos`
  ADD CONSTRAINT `q_alunos_cursos_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `q_alunos` (`aluno_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `q_alunos_cursos_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `q_cursos` (`curso_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `q_aulas`
--
ALTER TABLE `q_aulas`
  ADD CONSTRAINT `q_aulas_ibfk_1` FOREIGN KEY (`aula_prof_id`) REFERENCES `q_utilizadores` (`utilizador_id`),
  ADD CONSTRAINT `q_aulas_ibfk_2` FOREIGN KEY (`aula_id`) REFERENCES `q_cursos` (`curso_id`);

--
-- Constraints for table `q_pagamentos`
--
ALTER TABLE `q_pagamentos`
  ADD CONSTRAINT `q_pagamentos_ibfk_1` FOREIGN KEY (`pagamento_aluno_id`) REFERENCES `q_alunos` (`aluno_id`);

--
-- Constraints for table `q_utilizadores`
--
ALTER TABLE `q_utilizadores`
  ADD CONSTRAINT `q_utilizadores_ibfk_1` FOREIGN KEY (`utilizador_id`) REFERENCES `q_alunos` (`aluno_id`),
  ADD CONSTRAINT `q_utilizadores_ibfk_2` FOREIGN KEY (`utilizador_perfil`) REFERENCES `q_perfis` (`perfil_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
