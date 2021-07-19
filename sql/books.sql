-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema booksdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema booksdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `booksdb` DEFAULT CHARACTER SET utf8 ;
USE `booksdb` ;

-- -----------------------------------------------------
-- Table `booksdb`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `booksdb`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `booksdb`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `booksdb`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `title` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `booksdb`.`authors_books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `booksdb`.`authors_books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_authors_books_authors_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_authors_books_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_authors_books_authors`
    FOREIGN KEY (`author_id`)
    REFERENCES `booksdb`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_authors_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `booksdb`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `booksdb`.`authors_favorite_books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `booksdb`.`authors_favorite_books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_authors_favorite_books_authors1_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_authors_favorite_books_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_authors_favorite_books_authors1`
    FOREIGN KEY (`author_id`)
    REFERENCES `booksdb`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_authors_favorite_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `booksdb`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
