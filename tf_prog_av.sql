-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 06-Jul-2023 às 08:58
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
  `aula_ausencias` varchar(10) NOT NULL,
  PRIMARY KEY (`aula_id`),
  KEY `aulas_curso_id` (`aulas_curso_id`),
  KEY `aula_prof_id` (`aula_prof_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_aulas`
--

INSERT INTO `q_aulas` (`aula_id`, `aulas_curso_id`, `aula_desc`, `aula_prof_id`, `aula_inicio`, `aula_termino`, `aula_sumarios`, `aula_ausencias`) VALUES
(1, 1, 'Introduction to Algebra', 11, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Linear equations, Quadratic equations', '0'),
(2, 1, 'Introduction to Algebra', 11, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Linear equations, Quadratic equations', '0'),
(3, 2, 'Grammar Rules', 12, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Nouns, Verbs, Adjectives', '0'),
(4, 2, 'Grammar Rules', 12, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Nouns, Verbs, Adjectives', '0'),
(5, 3, 'Chemical Reactions', 13, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Balancing equations, Types of reactions', '0'),
(6, 3, 'Chemical Reactions', 13, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Balancing equations, Types of reactions', '0'),
(7, 4, 'World War I', 14, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Causes, Events, Consequences', '0'),
(8, 4, 'World War I', 14, '2023-06-24 00:00:00', '2023-06-24 00:00:00', 'Topics: Causes, Events, Consequences', '0'),
(9, 5, 'Continents and Oceans', 15, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Names, Locations', '0'),
(10, 5, 'Continents and Oceans', 15, '2023-06-23 00:00:00', '2023-06-23 00:00:00', 'Topics: Names, Locations', '0'),
(12, 5, 'World War I', 6, '2023-06-27 14:00:00', '2023-06-27 16:00:00', 'Topics: Causes, Events, Consequences', ''),
(13, 5, 'World War I', 6, '2023-06-30 00:00:00', '2023-06-30 00:00:00', 'Topics: Causes, Events, Consequences', ''),
(14, 5, 'World War I', 6, '2023-06-30 00:00:00', '2023-06-30 00:00:00', 'Topics: Causes, Events, Consequences', ''),
(15, 5, 'World War I', 6, '2023-06-30 00:00:00', '2023-06-30 00:00:00', 'Topics: Causes, Events, Consequences', ''),
(16, 5, 'World War I', 6, '2023-06-30 00:00:00', '2023-06-30 03:00:00', 'Topics: Causes, Events, Consequences', '');

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
  KEY `avaliacao_curso` (`avaliacao_curso`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_avaliacoes`
--

INSERT INTO `q_avaliacoes` (`avaliacao_id`, `avaliacao_aluno_id`, `avaliacao_nota`, `avaliacao_data`, `avaliacao_curso`, `avaliacao_prof_id`) VALUES
(16, 1, '18.00', '2023-06-29', 1, 9),
(17, 1, '15.00', '2023-06-29', 1, 9),
(23, 2, '15.34', '2023-06-29', 1, 9),
(24, 2, '15.00', '2023-06-29', 2, 9),
(25, 2, '18.29', '2023-06-29', 2, 9),
(27, 3, '15.00', '2023-06-29', 4, 9),
(28, 4, '20.00', '2023-06-29', 1, 34),
(29, 4, '10.00', '2023-06-29', 2, 35),
(32, 1, '12.00', '2023-07-31', 1, 40),
(39, 1, '15.00', '2023-07-31', 1, 36),
(40, 1, '18.00', '2023-06-29', 1, 34),
(41, 1, '15.00', '2023-07-31', 1, 35);

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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_cursos`
--

INSERT INTO `q_cursos` (`curso_id`, `curso_desc`, `curso_horas`, `curso_preco`) VALUES
(1, 'Mathematics', 20, 100),
(2, 'English', 16, 80),
(3, 'Chemistry', 18, 90),
(4, 'History', 14, 75),
(5, 'Geography', 12, 70),
(6, 'Curso Teste', 400, 600),
(9, 'Curso teste 3', 50, 90),
(10, 'Teste 12345', 250, 400);

-- --------------------------------------------------------

--
-- Estrutura da tabela `q_pagamentos`
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
-- Extraindo dados da tabela `q_pagamentos`
--

INSERT INTO `q_pagamentos` (`pagamento_id`, `pagamento_data`, `pagamento_aluno_id`, `pagamento_valor`, `pagamento_metodo`) VALUES
(1, '2023-06-24', 1, '100', 'Credit Card'),
(2, '2023-06-24', 2, '100', 'Credit Card'),
(3, '2023-06-24', 3, '80', 'PayPal'),
(4, '2023-06-24', 4, '80', 'PayPal'),
(5, '2023-06-23', 5, '90', 'Bank Transfer'),
(6, '2023-06-23', 6, '90', 'Bank Transfer'),
(7, '2023-06-24', 7, '75', 'Cash'),
(8, '2023-06-24', 8, '75', 'Cash'),
(9, '2023-06-23', 9, '70', 'Credit Card'),
(10, '2023-06-23', 10, '70', 'Credit Card');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_perfis`
--

INSERT INTO `q_perfis` (`perfil_id`, `perfil_nome`, `perfil_estado`) VALUES
(1, 'Student', 1),
(2, 'Teacher', 1);

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
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `q_utilizadores`
--

INSERT INTO `q_utilizadores` (`utilizador_id`, `utilizador_nome`, `utilizador_email`, `utilizador_contacto`, `utilizador_morada`, `utilizador_localidade`, `utilizador_nascimento`, `utilizador_senha`, `utilizador_perfil`) VALUES
(1, 'John Doe', 'john@example.com', '123456789', '123 Main St', 'City', '2000-01-01', 'password', 1),
(2, 'Jane Smith', 'jane@example.com', '987654321', '456 Elm St', 'City', '2001-02-02', 'password', 1),
(3, 'Mike Johnson', 'mike@example.com', '555555555', '789 Oak St', 'City', '1999-03-03', 'password', 1),
(4, 'Sarah Davis', 'sarah@example.com', '111111111', '321 Pine St', 'City', '1998-04-04', 'password', 1),
(5, 'Emily Wilson', 'emily@example.com', '999999999', '654 Birch St', 'City', '2002-05-05', 'password', 1),
(6, 'Johnson', 'professor@example.com', '444444444', '111 Oak St', 'City', '1975-01-01', 'password', 2),
(7, 'Smith', 'professor2@example.com', '222222222', '222 Elm St', 'City', '1980-02-02', 'password', 2),
(8, 'Davis', 'professor3@example.com', '333333333', '333 Pine St', 'City', '1985-03-03', 'password', 2),
(9, 'Wilson', 'professor4@example.com', '666666666', '444 Birch St', 'City', '1990-04-04', 'password', 2),
(27, 'João Silva', 'joao@example.com', '912345678', 'Rua A, 123', 'Cidade X', '1980-01-01', 'senha123', 1),
(28, 'Maria Souza', 'maria@example.com', '923456789', 'Rua B, 456', 'Cidade Y', '1990-02-02', 'senha456', 1),
(29, 'Fernando Almeida', 'fernando@example.com', '934567890', 'Rua C, 789', 'Cidade Z', '1985-03-03', 'senha789', 1),
(30, 'Ana Santos', 'ana@example.com', '945678901', 'Rua D, 987', 'Cidade W', '1995-04-04', 'senha987', 1),
(31, 'Pedro Oliveira', 'pedro@example.com', '956789012', 'Rua E, 654', 'Cidade V', '1987-05-05', 'senha654', 1),
(32, 'Carla Pereira', 'carla@example.com', '967890123', 'Rua F, 321', 'Cidade U', '1992-06-06', 'senha321', 1),
(33, 'Miguel Costa', 'miguel@example.com', '978901234', 'Rua G, 654', 'Cidade T', '1984-07-07', 'senha654', 1),
(34, 'Sara Rodrigues', 'sara@example.com', '989012345', 'Rua H, 987', 'Cidade S', '1991-08-08', 'senha987', 2),
(35, 'Ricardo Sousa', 'ricardo@example.com', '900123456', 'Rua I, 321', 'Cidade R', '1983-09-09', 'senha321', 2),
(36, 'Beatriz Martins', 'beatriz@example.com', '911234567', 'Rua J, 654', 'Cidade Q', '1989-10-10', 'senha654', 2),
(37, 'André Ferreira', 'andre@example.com', '922345678', 'Rua K, 987', 'Cidade P', '1982-11-11', 'senha987', 1),
(38, 'Rita Gonçalves', 'rita@example.com', '933456789', 'Rua L, 321', 'Cidade O', '1993-12-12', 'senha321', 1),
(40, 'Inês Pereira', 'ines@example.com', '955678901', 'Rua N, 987', 'Cidade M', '1994-02-14', 'senha987', 2);

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
-- Limitadores para a tabela `q_pagamentos`
--
ALTER TABLE `q_pagamentos`
  ADD CONSTRAINT `q_pagamentos_ibfk_1` FOREIGN KEY (`pagamento_aluno_id`) REFERENCES `q_utilizadores` (`utilizador_id`) ON UPDATE CASCADE;

--
-- Limitadores para a tabela `q_utilizadores`
--
ALTER TABLE `q_utilizadores`
  ADD CONSTRAINT `q_utilizadores_ibfk_1` FOREIGN KEY (`utilizador_perfil`) REFERENCES `q_perfis` (`perfil_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
