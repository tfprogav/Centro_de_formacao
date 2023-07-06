-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 06-Jul-2023 às 17:56
-- Versão do servidor: 8.0.31
-- versão do PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `tf_prog_av`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_alunos_cursos`
--

DROP TABLE IF EXISTS `q_alunos_cursos`;
CREATE TABLE IF NOT EXISTS `q_alunos_cursos` (
  `aluno_id` int DEFAULT NULL,
  `curso_id` int DEFAULT NULL,
  KEY `aluno_id` (`aluno_id`),
  KEY `curso_id` (`curso_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_alunos_cursos`
--

INSERT INTO `q_alunos_cursos` (`aluno_id`, `curso_id`) VALUES
(1, 1),
(3, 1),
(8, 1),
(12, 1),
(15, 1),
(19, 1),
(23, 1),
(27, 1),
(31, 2),
(35, 2),
(39, 2),
(2, 2),
(6, 2),
(9, 2),
(13, 2),
(16, 2),
(20, 3),
(24, 3),
(28, 3),
(32, 3),
(36, 3),
(40, 3),
(4, 3),
(7, 3),
(10, 4),
(14, 4),
(17, 4),
(21, 4),
(25, 4),
(29, 4),
(33, 4),
(37, 4),
(5, 5),
(11, 5),
(18, 5),
(22, 5),
(26, 5),
(30, 5),
(34, 5),
(38, 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_aulas`
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
  `aula_ausencias` varchar(100) NOT NULL,
  PRIMARY KEY (`aula_id`),
  KEY `aulas_curso_id` (`aulas_curso_id`),
  KEY `aula_prof_id` (`aula_prof_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_aulas`
--

INSERT INTO `q_aulas` (`aula_id`, `aulas_curso_id`, `aula_desc`, `aula_prof_id`, `aula_inicio`, `aula_termino`, `aula_sumarios`, `aula_ausencias`) VALUES
(1, 1, 'Introduction to Algebra', 47, '2023-07-05 09:00:00', '2023-07-05 10:30:00', 'Topics: Linear equations, Quadratic equations', ''),
(2, 1, 'Introduction to Algebra', 41, '2023-07-05 14:30:00', '2023-07-05 16:00:00', 'Topics: Linear equations, Quadratic equations', ''),
(3, 2, 'Grammar Rules', 42, '2023-07-05 11:00:00', '2023-07-05 12:00:00', 'Topics: Nouns, Verbs, Adjectives', ''),
(4, 2, 'Grammar Rules', 45, '2023-07-06 09:00:00', '2023-07-06 10:00:00', 'Topics: Nouns, Verbs, Adjectives', ''),
(5, 3, 'Chemical Reactions', 41, '2023-07-06 10:00:00', '2023-07-06 11:00:00', 'Topics: Balancing equations, Types of reactions', ''),
(6, 3, 'Chemical Reactions', 42, '2023-07-06 10:00:00', '2023-07-06 11:00:00', 'Topics: Balancing equations, Types of reactions', ''),
(7, 4, 'World War I', 49, '2023-07-06 14:30:00', '2023-07-06 16:00:00', 'Topics: Causes, Events, Consequences', ''),
(8, 4, 'World War I', 41, '2023-07-06 14:30:00', '2023-07-06 16:00:00', 'Topics: Causes, Events, Consequences', ''),
(9, 5, 'Continents and Oceans', 44, '2023-07-06 14:30:00', '2023-07-06 15:30:00', 'Topics: Names, Locations', '5,18,26'),
(12, 5, 'World War I', 43, '2023-06-27 23:00:00', '2023-06-28 00:00:00', 'Topics: Causes, Events, Consequences', '18'),
(13, 5, 'Revisão Teste', 42, '2023-06-28 01:00:00', '2023-06-28 02:00:00', 'Realização de Exercícios de preparação para a frequência.', ''),
(14, 5, 'Aula de Apresentação', 42, '2023-06-27 19:00:00', '2023-06-27 20:00:00', 'Aula de apresentação do docente e discentes', ''),
(15, 5, 'Primeira Aula', 48, '2023-06-27 23:00:00', '2023-06-28 00:00:00', 'Apresentação do curso aos alunos', ''),
(16, 1, 'Primeira Aula', 45, '2023-06-27 20:00:00', '2023-06-27 22:00:00', 'Apresentação da Matéria.', ''),
(20, 3, 'Teste', 42, '2023-06-29 19:00:00', '2023-06-29 20:00:00', 'Teste 12345', ''),
(21, 4, 'Teste 1236', 47, '2023-06-29 20:00:00', '2023-06-29 22:00:00', 'Teste', ''),
(22, 5, 'Teste', 49, '2023-06-29 14:00:00', '2023-06-29 15:00:00', 'Teste 12356', ''),
(23, 5, 'Teste', 46, '2023-06-29 12:00:00', '2023-06-29 13:00:00', 'Teste 12356', ''),
(24, 5, 'Teste', 48, '2023-06-29 07:00:00', '2023-06-29 08:00:00', 'Teste 12356', ''),
(25, 4, 'Teste', 44, '2023-06-29 10:00:00', '2023-06-29 12:00:00', 'Testees', ''),
(27, 4, 'Teste', 44, '2023-06-29 10:00:00', '2023-06-29 13:00:00', 'Testest asdfasdf', '21,33'),
(28, 2, 'Teste', 44, '2023-06-29 16:00:00', '2023-06-29 17:00:00', 'Teste', '2,9,13'),
(29, 5, 'Teste aula dia 30', 44, '2023-06-30 14:00:00', '2023-06-30 15:00:00', 'Teste dia 30', '18,26'),
(30, 3, 'TEste', 43, '2023-06-21 01:00:00', '2023-06-21 02:00:00', 'testsrdt', ''),
(32, 4, 'Teste', 42, '2023-06-29 15:00:00', '2023-06-29 15:00:00', 'TEstds', ''),
(34, 2, 'Teste', 44, '2023-06-30 08:30:00', '2023-06-30 09:30:00', 'TEstes', ''),
(35, 3, 'Teste', 43, '2023-07-12 16:30:00', '2023-07-12 17:30:00', 'Teste 123456456', '20,32,40,7');

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_avaliacoes`
--

DROP TABLE IF EXISTS `q_avaliacoes`;
CREATE TABLE IF NOT EXISTS `q_avaliacoes` (
  `avaliacao_id` int NOT NULL AUTO_INCREMENT,
  `avaliacao_aluno_id` int NOT NULL,
  `avaliacao_nota` decimal(4,2) NOT NULL,
  `avaliacao_data` date NOT NULL,
  `avaliacao_curso` int NOT NULL,
  `avaliacao_prof_id` int NOT NULL,
  PRIMARY KEY (`avaliacao_id`),
  KEY `avaliacao_aluno_id` (`avaliacao_aluno_id`),
  KEY `avaliacao_prof_id` (`avaliacao_prof_id`),
  KEY `avaliacao_aula` (`avaliacao_curso`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_avaliacoes`
--

INSERT INTO `q_avaliacoes` (`avaliacao_id`, `avaliacao_aluno_id`, `avaliacao_nota`, `avaliacao_data`, `avaliacao_curso`, `avaliacao_prof_id`) VALUES
(1, 1, '10.64', '2023-06-24', 1, 11),
(2, 2, '8.99', '2023-06-24', 1, 11),
(3, 3, '13.02', '2023-06-24', 2, 12),
(4, 4, '18.13', '2023-06-24', 5, 12),
(5, 5, '11.60', '2023-06-23', 4, 13),
(6, 6, '3.59', '2023-06-23', 4, 13),
(7, 7, '3.18', '2023-06-24', 3, 14),
(13, 1, '20.00', '2023-07-06', 1, 18);

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_cursos`
--

DROP TABLE IF EXISTS `q_cursos`;
CREATE TABLE IF NOT EXISTS `q_cursos` (
  `curso_id` int NOT NULL AUTO_INCREMENT,
  `curso_desc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `curso_horas` int NOT NULL,
  `curso_preco` int NOT NULL,
  PRIMARY KEY (`curso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_cursos`
--

INSERT INTO `q_cursos` (`curso_id`, `curso_desc`, `curso_horas`, `curso_preco`) VALUES
(1, 'Mathematics', 50, 350),
(2, 'English', 50, 250),
(3, 'Chemistry', 100, 700),
(4, 'History', 100, 500),
(5, 'Geography', 100, 500),
(14, 'Curso Teste 1', 50, 100);

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_pagamentos`
--

DROP TABLE IF EXISTS `q_pagamentos`;
CREATE TABLE IF NOT EXISTS `q_pagamentos` (
  `pagamento_id` int NOT NULL AUTO_INCREMENT,
  `pagamento_data` date NOT NULL,
  `pagamento_aluno_id` int NOT NULL,
  `pagamento_curso_id` int NOT NULL,
  `pagamento_valor` decimal(10,0) NOT NULL,
  `pagamento_metodo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `pagamento_pagou` tinyint(1) NOT NULL,
  PRIMARY KEY (`pagamento_id`),
  KEY `pagamento_aluno_id` (`pagamento_aluno_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_pagamentos`
--

INSERT INTO `q_pagamentos` (`pagamento_id`, `pagamento_data`, `pagamento_aluno_id`, `pagamento_curso_id`, `pagamento_valor`, `pagamento_metodo`, `pagamento_pagou`) VALUES
(1, '2023-06-24', 1, 0, '100', '', 0),
(2, '2023-06-24', 2, 0, '100', 'Credit Card', 1),
(3, '2023-06-24', 3, 0, '80', 'PayPal', 1),
(4, '2023-06-24', 4, 0, '80', '', 0),
(5, '2023-06-23', 5, 0, '90', 'Bank Transfer', 1),
(6, '2023-06-23', 6, 0, '90', '', 0),
(7, '2023-06-24', 7, 0, '75', '', 0),
(8, '2023-06-24', 8, 0, '75', 'Cash', 1),
(9, '2023-06-23', 9, 0, '70', '', 0),
(10, '2023-06-23', 10, 0, '70', 'Credit Card', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_perfis`
--

DROP TABLE IF EXISTS `q_perfis`;
CREATE TABLE IF NOT EXISTS `q_perfis` (
  `perfil_id` int NOT NULL AUTO_INCREMENT,
  `perfil_nome` varchar(100) NOT NULL,
  `perfil_estado` int NOT NULL,
  PRIMARY KEY (`perfil_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_perfis`
--

INSERT INTO `q_perfis` (`perfil_id`, `perfil_nome`, `perfil_estado`) VALUES
(1, 'Aluno', 1),
(2, 'Professor', 1),
(3, 'Administrador', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_utilizadores`
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
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_utilizadores`
--

INSERT INTO `q_utilizadores` (`utilizador_id`, `utilizador_nome`, `utilizador_email`, `utilizador_contacto`, `utilizador_morada`, `utilizador_localidade`, `utilizador_nascimento`, `utilizador_senha`, `utilizador_perfil`) VALUES
(1, 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St', 'City', '2000-01-01', 'password1', 1),
(2, 'Jane Smith', 'jane.smith@example.com', '9876543210', '456 Elm St', 'City', '1995-05-10', 'password2', 1),
(3, 'Mike Johnson', 'mike.johnson@example.com', '5555555555', '789 Oak St', 'City', '1998-08-15', 'password3', 1),
(4, 'Sarah Davis', 'sarah.davis@example.com', '1111111111', '321 Pine St', 'City', '2002-03-20', 'password4', 1),
(5, 'Emily Wilson', 'emily.wilson@example.com', '9999999999', '654 Birch St', 'City', '1997-11-25', 'password5', 1),
(6, 'David Brown', 'david.brown@example.com', '4444444444', '987 Maple St', 'City', '1999-06-05', 'password6', 1),
(7, 'Sophia Johnson', 'sophia.johnson@example.com', '2222222222', '567 Cedar St', 'City', '2001-09-12', 'password7', 1),
(8, 'Oliver Taylor', 'oliver.taylor@example.com', '6666666666', '234 Walnut St', 'City', '1996-02-28', 'password8', 1),
(9, 'Emma Wilson', 'emma.wilson@example.com', '8888888888', '876 Pineapple St', 'City', '2003-07-15', 'password9', 1),
(10, 'Daniel Anderson', 'daniel.anderson@example.com', '7777777777', '543 Orange St', 'City', '1994-04-09', 'password10', 1),
(11, 'Ava Martinez', 'ava.martinez@example.com', '3333333333', '765 Strawberry St', 'City', '1998-10-24', 'password11', 1),
(12, 'Alexander Davis', 'alexander.davis@example.com', '5555555555', '432 Grape St', 'City', '2000-05-05', 'password12', 1),
(13, 'Mia Miller', 'mia.miller@example.com', '1111111111', '678 Peach St', 'City', '1997-12-20', 'password13', 1),
(14, 'James Johnson', 'james.johnson@example.com', '9999999999', '321 Mango St', 'City', '2002-03-12', 'password14', 1),
(15, 'Evelyn Garcia', 'evelyn.garcia@example.com', '4444444444', '567 Kiwi St', 'City', '1996-08-06', 'password15', 1),
(16, 'Benjamin Wilson', 'benjamin.wilson@example.com', '2222222222', '876 Plum St', 'City', '2001-01-23', 'password16', 1),
(17, 'Liam Taylor', 'liam.taylor@example.com', '6666666666', '543 Lemon St', 'City', '1994-06-18', 'password17', 1),
(18, 'Amelia Anderson', 'amelia.anderson@example.com', '8888888888', '765 Watermelon St', 'City', '2003-11-05', 'password18', 2),
(19, 'Henry Martinez', 'henry.martinez@example.com', '7777777777', '432 Blueberry St', 'City', '1998-02-09', 'password19', 2),
(20, 'Charlotte Davis', 'charlotte.davis@example.com', '5555555555', '678 Raspberry St', 'City', '2000-07-24', 'password20', 2),
(21, 'William Wilson', 'william.wilson@example.com', '7777777777', '543 Cherry St', 'City', '1994-08-22', 'password21', 2),
(22, 'Sofia Anderson', 'sofia.anderson@example.com', '9999999999', '765 Blackberry St', 'City', '1998-01-06', 'password22', 2),
(23, 'Joseph Martinez', 'joseph.martinez@example.com', '4444444444', '432 Plum St', 'City', '2000-06-21', 'password23', 1),
(24, 'Avery Davis', 'avery.davis@example.com', '2222222222', '678 Strawberry St', 'City', '2001-11-07', 'password24', 1),
(25, 'Mia Taylor', 'mia.taylor@example.com', '6666666666', '876 Lemon St', 'City', '1996-04-02', 'password25', 1);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `q_alunos_cursos`
--
ALTER TABLE `q_alunos_cursos`
  ADD CONSTRAINT `q_alunos_cursos_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `q_alunos_cursos_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `q_cursos` (`curso_id`) ON UPDATE CASCADE;

--
-- Limitadores para a tabela `q_aulas`
--
ALTER TABLE `q_aulas`
  ADD CONSTRAINT `q_aulas_ibfk_1` FOREIGN KEY (`aula_prof_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `q_aulas_ibfk_2` FOREIGN KEY (`aulas_curso_id`) REFERENCES `q_cursos` (`curso_id`) ON UPDATE CASCADE;

--
-- Limitadores para a tabela `q_avaliacoes`
--
ALTER TABLE `q_avaliacoes`
  ADD CONSTRAINT `q_avaliacoes_ibfk_1` FOREIGN KEY (`avaliacao_aluno_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `q_avaliacoes_ibfk_2` FOREIGN KEY (`avaliacao_prof_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `q_avaliacoes_ibfk_3` FOREIGN KEY (`avaliacao_curso`) REFERENCES `q_cursos` (`curso_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `q_utilizadores`
--
ALTER TABLE `q_utilizadores`
  ADD CONSTRAINT `q_utilizadores_ibfk_1` FOREIGN KEY (`utilizador_perfil`) REFERENCES `q_perfis` (`perfil_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
