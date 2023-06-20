-- phpMyAdmin SQL Dump
-- version 4.9.11
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 17, 2023 at 07:37 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  `aula_inicio` date NOT NULL,
  `aula_termino` date NOT NULL,
  `aula_sumarios` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `aula_ausencias` int NOT NULL,
  PRIMARY KEY (`aula_id`),
  KEY `aulas_curso_id` (`aulas_curso_id`),
  KEY `aula_prof_id` (`aula_prof_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  ADD CONSTRAINT `q_alunos_cursos_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `q_alunos` (`aluno_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `q_alunos_cursos_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `q_cursos` (`curso_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `q_cursos`
--
ALTER TABLE `q_cursos`
  ADD CONSTRAINT `q_cursos_ibfk_1` FOREIGN KEY (`curso_id`) REFERENCES `q_aulas` (`aulas_curso_id`);

--
-- Constraints for table `q_pagamentos`
--
ALTER TABLE `q_pagamentos`
  ADD CONSTRAINT `q_pagamentos_ibfk_1` FOREIGN KEY (`pagamento_aluno_id`) REFERENCES `q_alunos` (`aluno_id`);

--
-- Constraints for table `q_perfis`
--
ALTER TABLE `q_perfis`
  ADD CONSTRAINT `q_perfis_ibfk_1` FOREIGN KEY (`perfil_id`) REFERENCES `q_utilizadores` (`utilizador_perfil`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `q_utilizadores`
--
ALTER TABLE `q_utilizadores`
  ADD CONSTRAINT `q_utilizadores_ibfk_1` FOREIGN KEY (`utilizador_id`) REFERENCES `q_aulas` (`aula_prof_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
