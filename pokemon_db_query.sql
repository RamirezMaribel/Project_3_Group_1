-- Quick Database Diagram ERD Code
-- https://pokeapi.co/api/v2/pokemon/?limit=1302
-- Ashley
CREATE TABLE Pokemon (
    poke_id int NOT NULL,
    poke_name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    second_type VARCHAR(50),
    base_hp int NOT NULL,
    base_att int NOT NULL,
    base_sp_atk int NOT NULL,
    base_def int NOT NULL,
    base_sp_def int NOT NULL,
    base_spd int NOT NULL,
    evolution_chain int NOT NULL,
    PRIMARY KEY (poke_id)
);
-- https://pokeapi.co/api/v2/type/
-- add additional weak to/strong against calculation later
-- Maribel
CREATE TABLE Type (
    type_name VARCHAR(50) NOT NULL,
    weak_to VARCHAR(50) NOT NULL,
    strong_against VARCHAR(50) NOT NULL,
    PRIMARY KEY (type_name)
);
-- https://pokeapi.co/api/v2/ability?limit=367
-- Maribel
CREATE TABLE Ability (
    ability_id int NOT NULL,
    ability_name VARCHAR(255) NOT NULL,
    effect VARCHAR(255) NOT NULL,
    short_effect VARCHAR(255) NOT NULL,
    PRIMARY KEY (ability_id),
	UNIQUE (ability_name)
);
CREATE TABLE pokeAbility (
    poke_id int NOT NULL,
    ability_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (poke_id,ability_name),
    FOREIGN KEY (poke_id) REFERENCES Pokemon (poke_id),
    FOREIGN KEY (ability_name) REFERENCES Ability (ability_name)
);
-- Nikko
CREATE TABLE Game (
    game_id int NOT NULL,
    game_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (game_id)
);
CREATE TABLE pokeGame (
    poke_id int NOT NULL,
    game_id int NOT NULL,
    PRIMARY KEY (poke_id, game_id),
    FOREIGN KEY (poke_id) REFERENCES Pokemon (poke_id),
    FOREIGN KEY (game_id) REFERENCES Game (game_id)
);
-- https://pokeapi.co/api/v2/move/
-- Kaitlyn
CREATE TABLE Move (
    move_id int NOT NULL,
    move_name VARCHAR(255) NOT NULL,
    move_effect VARCHAR(255) NOT NULL,
    move_power int NOT NULL,
    move_pp int NOT NULL,
    move_acc int NOT NULL,
    move_type VARCHAR(50) NOT NULL,
    dmg_class VARCHAR(50) NOT NULL,
    PRIMARY KEY (move_id)
);
CREATE TABLE pokeMove (
    poke_id int NOT NULL,
    move_id int NOT NULL,
    PRIMARY KEY (poke_id, move_id),
    FOREIGN KEY (poke_id) REFERENCES Pokemon (poke_id),
    FOREIGN KEY (move_id) REFERENCES Move (move_id)
);
CREATE TABLE pokeEvo (
    evolution_chain int NOT NULL,
    stage_1 VARCHAR(50) NOT NULL,
    stage_2 VARCHAR(50),
    stage_3 VARCHAR(50),
    PRIMARY KEY (evolution_chain)
);
ALTER TABLE Pokemon
ADD CONSTRAINT fk_Pokemon_type FOREIGN KEY (type)
REFERENCES Type (type_name);
ALTER TABLE Pokemon
ADD CONSTRAINT fk_Pokemon_second_type FOREIGN KEY (second_type)
REFERENCES Type (type_name);
CREATE INDEX idx_Pokemon_poke_name
ON Pokemon (poke_name);
CREATE INDEX idx_Ability_ability_name
ON Ability (ability_name);
CREATE INDEX idx_Game_game_name
ON Game (game_name);
CREATE INDEX idx_Move_move_name
ON Move (move_name);