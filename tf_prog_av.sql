-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 23, 2023 at 05:39 PM
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
(1, 3),
(2, 2),
(2, 4),
(2, 5),
(3, 3),
(3, 4),
(4, 1),
(4, 3),
(5, 2),
(5, 4),
(5, 5);

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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_aulas`
--

INSERT INTO `q_aulas` (`aula_id`, `aulas_curso_id`, `aula_desc`, `aula_prof_id`, `aula_inicio`, `aula_termino`, `aula_sumarios`, `aula_ausencias`) VALUES
(1, 1, 'Introduction to Algebra', 11, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Linear equations, Quadratic equations', 0),
(2, 1, 'Introduction to Algebra', 11, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Linear equations, Quadratic equations', 0),
(3, 2, 'Grammar Rules', 12, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Nouns, Verbs, Adjectives', 0),
(4, 2, 'Grammar Rules', 12, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Nouns, Verbs, Adjectives', 0),
(5, 3, 'Chemical Reactions', 13, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Balancing equations, Types of reactions', 0),
(6, 3, 'Chemical Reactions', 13, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Balancing equations, Types of reactions', 0),
(7, 4, 'World War I', 14, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Causes, Events, Consequences', 0),
(8, 4, 'World War I', 14, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Causes, Events, Consequences', 0),
(9, 5, 'Continents and Oceans', 15, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Names, Locations', 0),
(10, 5, 'Continents and Oceans', 15, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Names, Locations', 0);

-- --------------------------------------------------------

--
-- Table structure for table `q_avaliacoes`
--

DROP TABLE IF EXISTS `q_avaliacoes`;
CREATE TABLE IF NOT EXISTS `q_avaliacoes` (
  `avaliacao_id` int NOT NULL AUTO_INCREMENT,
  `avaliacao_aluno_id` int NOT NULL,
  `avaliacao_data` date NOT NULL,
  `avaliacao_aula` varchar(100) NOT NULL,
  `avaliacao_prof_id` int NOT NULL,
  PRIMARY KEY (`avaliacao_id`),
  KEY `avaliacao_aluno_id` (`avaliacao_aluno_id`),
  KEY `avaliacao_prof_id` (`avaliacao_prof_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_avaliacoes`
--

INSERT INTO `q_avaliacoes` (`avaliacao_id`, `avaliacao_aluno_id`, `avaliacao_data`, `avaliacao_aula`, `avaliacao_prof_id`) VALUES
(1, 1, '2023-06-24', 'Introduction to Algebra', 11),
(2, 2, '2023-06-24', 'Introduction to Algebra', 11),
(3, 3, '2023-06-24', 'Grammar Rules', 12),
(4, 4, '2023-06-24', 'Grammar Rules', 12),
(5, 5, '2023-06-23', 'Chemical Reactions', 13),
(6, 6, '2023-06-23', 'Chemical Reactions', 13),
(7, 7, '2023-06-24', 'World War I', 14),
(8, 8, '2023-06-24', 'World War I', 14),
(9, 9, '2023-06-23', 'Continents and Oceans', 15),
(10, 10, '2023-06-23', 'Continents and Oceans', 15);

-- --------------------------------------------------------

--
-- Table structure for table `q_cursos`
--

DROP TABLE IF EXISTS `q_cursos`;
CREATE TABLE IF NOT EXISTS `q_cursos` (
  `curso_id` int NOT NULL AUTO_INCREMENT,
  `curso_desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `curso_horas` int NOT NULL,
  `curso_preco` int NOT NULL,
  PRIMARY KEY (`curso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_cursos`
--

INSERT INTO `q_cursos` (`curso_id`, `curso_desc`, `curso_horas`, `curso_preco`) VALUES
(1, 'Mathematics', 20, 100),
(2, 'English', 16, 80),
(3, 'Chemistry', 18, 90),
(4, 'History', 14, 75),
(5, 'Geography', 12, 70),
(6, 'Curso Teste', 400, 600);

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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_pagamentos`
--

INSERT INTO `q_pagamentos` (`pagamento_id`, `pagamento_data`, `pagamento_aluno_id`, `pagamento_valor`, `pagamento_metodo`) VALUES
(1, '2023-06-24', 1, 100, 'Credit Card'),
(2, '2023-06-24', 2, 100, 'Credit Card'),
(3, '2023-06-24', 3, 80, 'PayPal'),
(4, '2023-06-24', 4, 80, 'PayPal'),
(5, '2023-06-23', 5, 90, 'Bank Transfer'),
(6, '2023-06-23', 6, 90, 'Bank Transfer'),
(7, '2023-06-24', 7, 75, 'Cash'),
(8, '2023-06-24', 8, 75, 'Cash'),
(9, '2023-06-23', 9, 70, 'Credit Card'),
(10, '2023-06-23', 10, 70, 'Credit Card');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_perfis`
--

INSERT INTO `q_perfis` (`perfil_id`, `perfil_nome`, `perfil_estado`) VALUES
(1, 'Student', 1),
(2, 'Teacher', 1);

-- --------------------------------------------------------

--
-- Table structure for table `q_utilizadores`
--

DROP TABLE IF EXISTS `q_utilizadores`;
CREATE TABLE IF NOT EXISTS `q_utilizadores` (
  `utilizador_id` int NOT NULL AUTO_INCREMENT,
  `utilizador_nome` varchar(100) NOT NULL,
  `utilizador_email` varchar(100) NOT NULL,
  `utilizador_contacto` varchar(14) NOT NULL,
  `utilizador_morada` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `utilizador_localidade` varchar(100) NOT NULL,
  `utilizador_nascimento` date NOT NULL,
  `utilizador_senha` varchar(20) NOT NULL,
  `utilizador_perfil` int NOT NULL,
  PRIMARY KEY (`utilizador_id`),
  KEY `utilizador_perfil` (`utilizador_perfil`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `q_utilizadores`
--

INSERT INTO `q_utilizadores` (`utilizador_id`, `utilizador_nome`, `utilizador_email`, `utilizador_contacto`, `utilizador_morada`, `utilizador_localidade`, `utilizador_nascimento`, `utilizador_senha`, `utilizador_perfil`) VALUES
(1, 'John Doe', 'john@example.com', '123456789', '123 Main St', 'City', '2000-01-01', 'password', 1),
(2, 'Jane Smith', 'jane@example.com', '987654321', '456 Elm St', 'City', '2001-02-02', 'password', 1),
(3, 'Mike Johnson', 'mike@example.com', '555555555', '789 Oak St', 'City', '1999-03-03', 'password', 1),
(4, 'Sarah Davis', 'sarah@example.com', '111111111', '321 Pine St', 'City', '1998-04-04', 'password', 1),
(5, 'Emily Wilson', 'emily@example.com', '999999999', '654 Birch St', 'City', '2002-05-05', 'password', 1),
(6, 'Professor Johnson', 'professor@example.com', '444444444', '111 Oak St', 'City', '1975-01-01', 'password', 2),
(7, 'Professor Smith', 'professor2@example.com', '222222222', '222 Elm St', 'City', '1980-02-02', 'password', 2),
(8, 'Professor Davis', 'professor3@example.com', '333333333', '333 Pine St', 'City', '1985-03-03', 'password', 2),
(9, 'Professor Wilson', 'professor4@example.com', '666666666', '444 Birch St', 'City', '1990-04-04', 'password', 2);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `q_alunos_cursos`
--
ALTER TABLE `q_alunos_cursos`
  ADD CONSTRAINT `q_alunos_cursos_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `q_alunos_cursos_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `q_cursos` (`curso_id`) ON UPDATE CASCADE;

--
-- Constraints for table `q_aulas`
--
ALTER TABLE `q_aulas`
  ADD CONSTRAINT `q_aulas_ibfk_1` FOREIGN KEY (`aula_prof_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `q_aulas_ibfk_2` FOREIGN KEY (`aulas_curso_id`) REFERENCES `q_cursos` (`curso_id`) ON UPDATE CASCADE;

--
-- Constraints for table `q_avaliacoes`
--
ALTER TABLE `q_avaliacoes`
  ADD CONSTRAINT `q_avaliacoes_ibfk_1` FOREIGN KEY (`avaliacao_aluno_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `q_avaliacoes_ibfk_2` FOREIGN KEY (`avaliacao_prof_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE;

--
-- Constraints for table `q_pagamentos`
--
ALTER TABLE `q_pagamentos`
  ADD CONSTRAINT `q_pagamentos_ibfk_1` FOREIGN KEY (`pagamento_aluno_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE;

--
-- Constraints for table `q_utilizadores`
--
ALTER TABLE `q_utilizadores`
  ADD CONSTRAINT `q_utilizadores_ibfk_1` FOREIGN KEY (`utilizador_perfil`) REFERENCES `q_perfis` (`perfil_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
