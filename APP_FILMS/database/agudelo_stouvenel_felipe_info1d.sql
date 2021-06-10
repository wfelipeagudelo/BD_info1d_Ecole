-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 18 Mars 2021 à 06:51
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `agudelo_stouvenel_felipe_info1d`
--

DROP DATABASE IF EXISTS agudelo_stouvenel_felipe_info1d;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS agudelo_stouvenel_felipe_info1d;

-- Utilisation de cette base de donnée

USE `agudelo_stouvenel_felipe_info1d`;

-- --------------------------------------------------------

--
-- Structure de la table `t_appartenance`
--

CREATE TABLE `t_appartenance` (
  `id_appartenancce` int(11) NOT NULL,
  `appartenance` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_avs`
--

CREATE TABLE `t_avs` (
  `id_avs` int(11) NOT NULL,
  `avs` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_banque`
--

CREATE TABLE `t_banque` (
  `id_banque` int(11) NOT NULL,
  `nom_banque` varchar(100) NOT NULL,
  `num_compte` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_classe`
--

CREATE TABLE `t_classe` (
  `id_classe` int(11) NOT NULL,
  `nom_classe` text NOT NULL,
  `temps` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_instrument`
--

CREATE TABLE `t_instrument` (
  `id_instrument` int(11) NOT NULL,
  `nom_instrument` varchar(63) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_mail`
--

CREATE TABLE `t_mail` (
  `id_mail` int(11) NOT NULL,
  `mail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_niveaux`
--

CREATE TABLE `t_niveaux` (
  `id_niveaux` int(11) NOT NULL,
  `niveaux` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_personne`
--

CREATE TABLE `t_personne` (
  `id_personne` int(11) NOT NULL,
  `nom_pers` varchar(42) NOT NULL,
  `prenom_pers` varchar(21) NOT NULL,
  `date_nais_pers` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_appartenance`
--

CREATE TABLE `t_pers_appartenance` (
  `id_pers_appartenance` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_appartenance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_avs`
--

CREATE TABLE `t_pers_avs` (
  `id_pers_avs` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_avs` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_banque`
--

CREATE TABLE `t_pers_banque` (
  `id_pers_banque` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_banque` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_classe`
--

CREATE TABLE `t_pers_classe` (
  `id_pers_classe` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_classe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_instrument`
--

CREATE TABLE `t_pers_instrument` (
  `id_pers_instrument` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_instrument` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_mail`
--

CREATE TABLE `t_pers_mail` (
  `id_pers_mail` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_mail` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_niveaux`
--

CREATE TABLE `t_pers_niveaux` (
  `id_pers_niveaux` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_niveaux` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_prix`
--

CREATE TABLE `t_pers_prix` (
  `id_pers_prix` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_prix` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_telephone`
--

CREATE TABLE `t_pers_telephone` (
  `id_pers_telephone` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_telephone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_ville`
--

CREATE TABLE `t_pers_ville` (
  `id_pers_ville` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_ville` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_prix`
--

CREATE TABLE `t_prix` (
  `id_prix` int(11) NOT NULL,
  `prix` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_telephone`
--

CREATE TABLE `t_telephone` (
  `id_telephone` int(11) NOT NULL,
  `num_telephone` int(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_adresse`
--

CREATE TABLE `t_adresse` (
  `id_adresse` int(11) NOT NULL,
  `adresse ` varchar(250) NOT NULL,
  `ville` varchar(100) NOT NULL,
  `NPA` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_appartenance`
--
ALTER TABLE `t_appartenance`
  ADD PRIMARY KEY (`id_appartenancce`);

--
-- Index pour la table `t_avs`
--
ALTER TABLE `t_avs`
  ADD PRIMARY KEY (`id_avs`);

--
-- Index pour la table `t_banque`
--
ALTER TABLE `t_banque`
  ADD PRIMARY KEY (`id_banque`);

--
-- Index pour la table `t_classe`
--
ALTER TABLE `t_classe`
  ADD PRIMARY KEY (`id_classe`);

--
-- Index pour la table `t_instrument`
--
ALTER TABLE `t_instrument`
  ADD PRIMARY KEY (`id_instrument`);

--
-- Index pour la table `t_mail`
--
ALTER TABLE `t_mail`
  ADD PRIMARY KEY (`id_mail`);

--
-- Index pour la table `t_niveaux`
--
ALTER TABLE `t_niveaux`
  ADD PRIMARY KEY (`id_niveaux`);

--
-- Index pour la table `t_personne`
--
ALTER TABLE `t_personne`
  ADD PRIMARY KEY (`id_personne`);

--
-- Index pour la table `t_pers_appartenance`
--
ALTER TABLE `t_pers_appartenance`
  ADD PRIMARY KEY (`id_pers_appartenance`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`,`fk_appartenance`),
  ADD KEY `fk_appartenance` (`fk_appartenance`);

--
-- Index pour la table `t_pers_avs`
--
ALTER TABLE `t_pers_avs`
  ADD PRIMARY KEY (`id_pers_avs`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`,`fk_avs`),
  ADD KEY `fk_avs` (`fk_avs`);

--
-- Index pour la table `t_pers_banque`
--
ALTER TABLE `t_pers_banque`
  ADD PRIMARY KEY (`id_pers_banque`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`,`fk_banque`),
  ADD KEY `fk_banque` (`fk_banque`);

--
-- Index pour la table `t_pers_classe`
--
ALTER TABLE `t_pers_classe`
  ADD PRIMARY KEY (`id_pers_classe`),
  ADD KEY `fk_personne` (`fk_personne`,`fk_classe`),
  ADD KEY `fk_classe` (`fk_classe`);

--
-- Index pour la table `t_pers_instrument`
--
ALTER TABLE `t_pers_instrument`
  ADD PRIMARY KEY (`id_pers_instrument`),
  ADD KEY `fk_personne` (`fk_personne`),
  ADD KEY `fk_tracteur` (`fk_instrument`);

--
-- Index pour la table `t_pers_mail`
--
ALTER TABLE `t_pers_mail`
  ADD PRIMARY KEY (`id_pers_mail`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`),
  ADD UNIQUE KEY `fk_mail` (`fk_mail`);

--
-- Index pour la table `t_pers_niveaux`
--
ALTER TABLE `t_pers_niveaux`
  ADD PRIMARY KEY (`id_pers_niveaux`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`),
  ADD UNIQUE KEY `fk_niveaux` (`fk_niveaux`);

--
-- Index pour la table `t_pers_prix`
--
ALTER TABLE `t_pers_prix`
  ADD PRIMARY KEY (`id_pers_prix`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`,`fk_prix`),
  ADD KEY `fk_prix` (`fk_prix`);

--
-- Index pour la table `t_pers_telephone`
--
ALTER TABLE `t_pers_telephone`
  ADD PRIMARY KEY (`id_pers_telephone`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`,`fk_telephone`),
  ADD KEY `fk_telephone` (`fk_telephone`);

--
-- Index pour la table `t_pers_ville`
--
ALTER TABLE `t_pers_ville`
  ADD PRIMARY KEY (`id_pers_ville`),
  ADD UNIQUE KEY `fk_personne` (`fk_personne`,`fk_ville`),
  ADD KEY `fk_ville` (`fk_ville`);

--
-- Index pour la table `t_prix`
--
ALTER TABLE `t_prix`
  ADD PRIMARY KEY (`id_prix`);

--
-- Index pour la table `t_telephone`
--
ALTER TABLE `t_telephone`
  ADD PRIMARY KEY (`id_telephone`);

--
-- Index pour la table `t_adresse`
--
ALTER TABLE `t_adresse`
  ADD PRIMARY KEY (`id_adresse`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_appartenance`
--
ALTER TABLE `t_appartenance`
  MODIFY `id_appartenancce` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_avs`
--
ALTER TABLE `t_avs`
  MODIFY `id_avs` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_banque`
--
ALTER TABLE `t_banque`
  MODIFY `id_banque` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_classe`
--
ALTER TABLE `t_classe`
  MODIFY `id_classe` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_instrument`
--
ALTER TABLE `t_instrument`
  MODIFY `id_instrument` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_mail`
--
ALTER TABLE `t_mail`
  MODIFY `id_mail` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_niveaux`
--
ALTER TABLE `t_niveaux`
  MODIFY `id_niveaux` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_personne`
--
ALTER TABLE `t_personne`
  MODIFY `id_personne` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_appartenance`
--
ALTER TABLE `t_pers_appartenance`
  MODIFY `id_pers_appartenance` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_avs`
--
ALTER TABLE `t_pers_avs`
  MODIFY `id_pers_avs` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_banque`
--
ALTER TABLE `t_pers_banque`
  MODIFY `id_pers_banque` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_classe`
--
ALTER TABLE `t_pers_classe`
  MODIFY `id_pers_classe` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_instrument`
--
ALTER TABLE `t_pers_instrument`
  MODIFY `id_pers_instrument` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_mail`
--
ALTER TABLE `t_pers_mail`
  MODIFY `id_pers_mail` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_niveaux`
--
ALTER TABLE `t_pers_niveaux`
  MODIFY `id_pers_niveaux` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_prix`
--
ALTER TABLE `t_pers_prix`
  MODIFY `id_pers_prix` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_telephone`
--
ALTER TABLE `t_pers_telephone`
  MODIFY `id_pers_telephone` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_pers_ville`
--
ALTER TABLE `t_pers_ville`
  MODIFY `id_pers_ville` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_prix`
--
ALTER TABLE `t_prix`
  MODIFY `id_prix` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_telephone`
--
ALTER TABLE `t_telephone`
  MODIFY `id_telephone` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_adresse`
--
ALTER TABLE `t_adresse`
  MODIFY `id_adresse` int(11) NOT NULL AUTO_INCREMENT;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_pers_appartenance`
--
ALTER TABLE `t_pers_appartenance`
  ADD CONSTRAINT `t_pers_appartenance_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_appartenance_ibfk_2` FOREIGN KEY (`fk_appartenance`) REFERENCES `t_appartenance` (`id_appartenancce`);

--
-- Contraintes pour la table `t_pers_avs`
--
ALTER TABLE `t_pers_avs`
  ADD CONSTRAINT `t_pers_avs_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_avs_ibfk_2` FOREIGN KEY (`fk_avs`) REFERENCES `t_avs` (`id_avs`);

--
-- Contraintes pour la table `t_pers_banque`
--
ALTER TABLE `t_pers_banque`
  ADD CONSTRAINT `t_pers_banque_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_banque_ibfk_2` FOREIGN KEY (`fk_banque`) REFERENCES `t_banque` (`id_banque`);

--
-- Contraintes pour la table `t_pers_classe`
--
ALTER TABLE `t_pers_classe`
  ADD CONSTRAINT `t_pers_classe_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_classe_ibfk_2` FOREIGN KEY (`fk_classe`) REFERENCES `t_classe` (`id_classe`);

--
-- Contraintes pour la table `t_pers_instrument`
--
ALTER TABLE `t_pers_instrument`
  ADD CONSTRAINT `t_pers_instrument_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_instrument_ibfk_2` FOREIGN KEY (`fk_instrument`) REFERENCES `t_instrument` (`id_instrument`);

--
-- Contraintes pour la table `t_pers_mail`
--
ALTER TABLE `t_pers_mail`
  ADD CONSTRAINT `t_pers_mail_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_mail_ibfk_2` FOREIGN KEY (`fk_mail`) REFERENCES `t_mail` (`id_mail`);

--
-- Contraintes pour la table `t_pers_niveaux`
--
ALTER TABLE `t_pers_niveaux`
  ADD CONSTRAINT `t_pers_niveaux_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_niveaux_ibfk_2` FOREIGN KEY (`fk_niveaux`) REFERENCES `t_niveaux` (`id_niveaux`);

--
-- Contraintes pour la table `t_pers_prix`
--
ALTER TABLE `t_pers_prix`
  ADD CONSTRAINT `t_pers_prix_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_prix_ibfk_2` FOREIGN KEY (`fk_prix`) REFERENCES `t_prix` (`id_prix`);

--
-- Contraintes pour la table `t_pers_telephone`
--
ALTER TABLE `t_pers_telephone`
  ADD CONSTRAINT `t_pers_telephone_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_telephone_ibfk_2` FOREIGN KEY (`fk_telephone`) REFERENCES `t_telephone` (`id_telephone`);

--
-- Contraintes pour la table `t_pers_ville`
--
ALTER TABLE `t_pers_ville`
  ADD CONSTRAINT `t_pers_ville_ibfk_1` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`),
  ADD CONSTRAINT `t_pers_ville_ibfk_2` FOREIGN KEY (`fk_ville`) REFERENCES `t_adresse` (`id_adresse`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
