-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : ven. 21 jan. 2022 à 02:07
-- Version du serveur : 10.3.29-MariaDB-0+deb10u1
-- Version de PHP : 8.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `python_poo`
--

-- --------------------------------------------------------

--
-- Structure de la table `candidat`
--

CREATE TABLE `candidat` (
  `id` int(11) NOT NULL,
  `numero_table` int(11) NOT NULL,
  `prenom_s` varchar(35) NOT NULL,
  `nom` varchar(35) NOT NULL,
  `date_naissance` date NOT NULL,
  `lieu_naissance` varchar(35) NOT NULL,
  `sexe` varchar(15) NOT NULL,
  `nationalite` varchar(35) NOT NULL,
  `choix_epr_facultative` tinyint(1) NOT NULL,
  `epreuve_facultative` varchar(35) NOT NULL,
  `aptitude_sportive` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `candidat`
--

INSERT INTO `candidat` (`id`, `numero_table`, `prenom_s`, `nom`, `date_naissance`, `lieu_naissance`, `sexe`, `nationalite`, `choix_epr_facultative`, `epreuve_facultative`, `aptitude_sportive`) VALUES
(1, 10202, 'lamine', 'beye', '2022-01-05', 'tambacounda', 'masculin', 'senegalaise', 1, 'musique', 0),
(5, 21458, 'test', 'test', '2022-01-05', 'THIES', 'Masculin', 'Malienne', 0, 'dessin', 1),
(6, 21458, 'test', 'test', '2022-01-05', 'THIES', 'Masculin', 'Malienne', 0, 'dessin', 1);

-- --------------------------------------------------------

--
-- Structure de la table `candidat_anonymat`
--

CREATE TABLE `candidat_anonymat` (
  `id` int(11) NOT NULL,
  `anonymat` int(11) NOT NULL,
  `id_candidat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `jury`
--

CREATE TABLE `jury` (
  `id` int(11) NOT NULL,
  `region` varchar(35) NOT NULL,
  `departement` varchar(35) NOT NULL,
  `localite` varchar(35) NOT NULL,
  `centre_examen` varchar(35) NOT NULL,
  `president` varchar(35) NOT NULL,
  `telephone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `jury`
--

INSERT INTO `jury` (`id`, `region`, `departement`, `localite`, `centre_examen`, `president`, `telephone`) VALUES
(1, 'Diourbel', 'Diourbel', 'Pont', 'LTAB', 'Soce Ndiaye', 774589621);

-- --------------------------------------------------------

--
-- Structure de la table `livret_scolaire`
--

CREATE TABLE `livret_scolaire` (
  `id` int(11) NOT NULL,
  `nombre_de_fois` int(11) NOT NULL,
  `moyenne_6e` decimal(10,0) NOT NULL,
  `moyenne_5e` decimal(10,0) NOT NULL,
  `moyenne_4e` decimal(10,0) NOT NULL,
  `moyenne_3e` decimal(10,0) NOT NULL,
  `moyenne_cycle` decimal(10,0) NOT NULL,
  `candidat_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `note`
--

CREATE TABLE `note` (
  `id` int(11) NOT NULL,
  `compo_franc` decimal(10,0) NOT NULL,
  `coef1` int(11) NOT NULL,
  `dictee` decimal(10,0) NOT NULL,
  `coef2` int(11) NOT NULL,
  `etude_de_texte` decimal(10,0) NOT NULL,
  `coef3` int(11) NOT NULL,
  `instruction_civique` decimal(10,0) NOT NULL,
  `coef4` int(11) NOT NULL,
  `histoire_geographie` decimal(10,0) NOT NULL,
  `coef5` int(11) NOT NULL,
  `mathematique` decimal(10,0) NOT NULL,
  `coef6` int(11) NOT NULL,
  `pc_lv2` decimal(10,0) NOT NULL,
  `coef7` int(11) NOT NULL,
  `svt` decimal(10,0) NOT NULL,
  `coef8` int(11) NOT NULL,
  `anglais1` decimal(10,0) NOT NULL,
  `coef9` int(11) NOT NULL,
  `anglais` decimal(10,0) NOT NULL,
  `coef10` int(11) NOT NULL,
  `eps` decimal(10,0) NOT NULL,
  `epreuve_facultative` decimal(10,0) NOT NULL,
  `candidat_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `candidat`
--
ALTER TABLE `candidat`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `candidat_anonymat`
--
ALTER TABLE `candidat_anonymat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_candidat` (`id_candidat`);

--
-- Index pour la table `jury`
--
ALTER TABLE `jury`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `livret_scolaire`
--
ALTER TABLE `livret_scolaire`
  ADD PRIMARY KEY (`id`),
  ADD KEY `candidat_id` (`candidat_id`);

--
-- Index pour la table `note`
--
ALTER TABLE `note`
  ADD PRIMARY KEY (`id`),
  ADD KEY `candidat_id` (`candidat_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `candidat`
--
ALTER TABLE `candidat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `candidat_anonymat`
--
ALTER TABLE `candidat_anonymat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `jury`
--
ALTER TABLE `jury`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `livret_scolaire`
--
ALTER TABLE `livret_scolaire`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `note`
--
ALTER TABLE `note`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `candidat_anonymat`
--
ALTER TABLE `candidat_anonymat`
  ADD CONSTRAINT `candidat_anonymat_ibfk_1` FOREIGN KEY (`id_candidat`) REFERENCES `candidat` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `livret_scolaire`
--
ALTER TABLE `livret_scolaire`
  ADD CONSTRAINT `livret_scolaire_ibfk_1` FOREIGN KEY (`candidat_id`) REFERENCES `candidat` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `note`
--
ALTER TABLE `note`
  ADD CONSTRAINT `note_ibfk_1` FOREIGN KEY (`candidat_id`) REFERENCES `candidat` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
