-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema game_platform
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `game_platform` ;

-- -----------------------------------------------------
-- Schema game_platform
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `game_platform` DEFAULT CHARACTER SET utf8 ;
USE `game_platform` ;

-- -----------------------------------------------------
-- Table `game_platform`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `game_platform`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` CHAR(60) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `game_platform`.`games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `game_platform`.`games` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `genre` VARCHAR(45) NULL,
  `release_date` DATE NULL,
  `price` DECIMAL(4,2) NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `game_platform`.`users_games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `game_platform`.`users_games` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  `status` VARCHAR(8) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `user_id`, `game_id`),
  INDEX `fk_users_has_games_games1_idx` (`game_id` ASC) VISIBLE,
  INDEX `fk_users_has_games_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_games_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `game_platform`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_games_games1`
    FOREIGN KEY (`game_id`)
    REFERENCES `game_platform`.`games` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `game_platform`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `game_platform`.`friends` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `user_id`, `friend_id`),
  INDEX `fk_table1_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_table1_users2_idx` (`friend_id` ASC) VISIBLE,
  CONSTRAINT `fk_table1_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `game_platform`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_table1_users2`
    FOREIGN KEY (`friend_id`)
    REFERENCES `game_platform`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Forza Horizon 5", "Racing", "2021-11-04", 59.99, "Your Ultimate Horizon Adventure awaits! Explore the vibrant and ever-evolving open world landscapes of Mexico with limitless, fun driving action in hundreds of the world’s greatest cars.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Psychonauts 2", "3D Platformer", "2021-08-25", 59.99, "Razputin Aquato, trained acrobat and powerful young psychic, has realized his life long dream of joining the international psychic espionage organization known as the Psychonauts! But these psychic super spies are in trouble. Their leader hasn't been the same since he was kidnapped, and what's worse, there's a mole hiding in headquarters. Raz must use his powers to stop the mole before they execute their secret plan--to bring the murderous psychic villain, Maligula, back from the dead.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Mass Effect Legendary Edition", "Role-playing Game", "2021-05-14", 59.99, "The Mass Effect™ Legendary Edition includes single-player base content and over 40 DLC from the highly acclaimed Mass Effect, Mass Effect 2, and Mass Effect 3 games, including promo weapons, armors, and packs — remastered and optimized for 4K Ultra HD.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("It Takes Two", "Co-op", "2021-03-26", 39.99, "Bring your favorite co-op partner and together step into the shoes of May and Cody. As the couple is going through a divorce, through unknown means their minds are transported into two dolls which their daughter, Rose, made to represent them. Now they must reluctantly find a way to get back into their bodies, a quest which takes them through the most wild, unexpected and fantastical journey imaginable.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Final Fantasy VII Remake Intergrade", "Adventure", "2021-06-10", 69.99, "The new episode featuring Yuffie is a brand-new adventure in the world of FINAL FANTASY VII REMAKE INTERGRADE. Play as Wutai ninja Yuffie Kisaragi as she infiltrates Midgar and conspires with Avalanche HQ to steal the ultimate materia from the Shinra Electric Power Company.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Death's Door", "Action Role-playing Game", "2021-07-20", 19.99, "Reaping souls of the dead and punching a clock might get monotonous but it's honest work for a Crow. The job gets lively when your assigned soul is stolen and you must track down a desperate thief to a realm untouched by death - where creatures grow far past their expiry and overflow with greed and power.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Deathloop", "First Person Shooter", "2012-09-14", 59.99, "If at first you don't succeed Die, Die Again. From the team at Arkane Lyon comes an innovative take on first-person action. DEATHLOOP transports players to the lawless island of Blackreef in an eternal struggle between two extraordinary assassins. Explore stunning environments and meticulously designed levels in an immersive gameplay experience that lets you approach every situation any way you like. Hunt down targets all over the island in an effort to put an end to the cycle once and for all, and remember, if at first you don't succeed die, die again.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Ratchet & Clank: Rift Apart", "3D Platformer", "2021-06-11", 69.99, "Go dimension-hopping with Ratchet and Clank as they take on an evil emperor from another reality. Jump between action-packed worlds, and beyond at mind-blowing speeds – complete with dazzling visuals and an insane arsenal – as the intergalactic adventurers blast onto the PS5™ console.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Monster Hunter Rise", "Action Role-playing Game", "2021-03-26", 59.99, "Rise to the challenge and join the hunt. The action-RPG series returns to the Nintendo Switch! Set in the ninja-inspired land of Kamura Village, explore lush ecosystems and battle fearsome monsters to become the ultimate hunter. It's been half a century since the last calamity struck, but a terrifying new monster has reared its head and threatens to plunge the land into chaos once again.", NOW(), NOW());
INSERT INTO games (name, genre, release_date, price, description, created_at, updated_at)
VALUES ("Metroid Dread", "Metroidvania", "2021-10-08", 59.99, "Join intergalactic bounty hunter Samus Aran in her first new 2D Metroid™ story in 19 years. Samus’ story continues after the events of the Metroid™ Fusion game when she descends upon planet ZDR to investigate a mysterious transmission sent to the Galactic Federation. The remote planet has become overrun by vicious alien lifeforms and chilling mechanical menaces. Samus is more agile and capable than ever, but can she overcome the inhuman threat stalking the depths of ZDR?", NOW(), NOW());