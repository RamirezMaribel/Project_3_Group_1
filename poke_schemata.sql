-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- Quick Database Diagram ERD Code
-- https://pokeapi.co/api/v2/pokemon/?limit=1302
-- Ashley
CREATE TABLE "Pokemon" (
    "poke_id" int   NOT NULL,
    "poke_name" string   NOT NULL,
    "type" string   NOT NULL,
    "second_type" string   NOT NULL,
    "base_hp" int   NOT NULL,
    "base_att" int   NOT NULL,
    "base_sp_atk" int   NOT NULL,
    "base_def" int   NOT NULL,
    "base_sp_def" int   NOT NULL,
    "base_spd" int   NOT NULL,
    "evolution_chain" int   NOT NULL,
    CONSTRAINT "pk_Pokemon" PRIMARY KEY (
        "poke_id"
     )
);

-- https://pokeapi.co/api/v2/type/
-- add additional weak to/strong against calculation later
-- Maribel
CREATE TABLE "Type" (
    "type_name" string   NOT NULL,
    "weak_to" string   NOT NULL,
    "strong_against" string   NOT NULL,
    CONSTRAINT "pk_Type" PRIMARY KEY (
        "type_name"
     )
);

-- https://pokeapi.co/api/v2/ability?limit=367
-- Maribel
CREATE TABLE "Ability" (
    "ability_id" int   NOT NULL,
    "ability_name" string   NOT NULL,
    "effect" string   NOT NULL,
    "short_effect" string   NOT NULL,
    CONSTRAINT "pk_Ability" PRIMARY KEY (
        "ability_id"
     )
);

CREATE TABLE "pokeAbility" (
    "poke_id" int   NOT NULL,
    "ability_id" int   NOT NULL,
    CONSTRAINT "pk_pokeAbility" PRIMARY KEY (
        "poke_id","ability_id"
     )
);

-- Nikko
CREATE TABLE "Game" (
    "game_id" int   NOT NULL,
    "game_name" string   NOT NULL,
    CONSTRAINT "pk_Game" PRIMARY KEY (
        "game_id"
     )
);

CREATE TABLE "pokeGame" (
    "poke_id" int   NOT NULL,
    "game_id" int   NOT NULL,
    CONSTRAINT "pk_pokeGame" PRIMARY KEY (
        "poke_id","game_id"
     )
);

-- https://pokeapi.co/api/v2/move?limit=937
-- Kaitlyn
CREATE TABLE "Moves" (
    "move_id" int   NOT NULL,
    "move_name" string   NOT NULL,
    "move_power" int   NOT NULL,
    "move_pp" int   NOT NULL,
    "move_acc" int   NOT NULL,
    "move_type" string   NOT NULL,
    "dmg_class" string   NOT NULL,
    CONSTRAINT "pk_Moves" PRIMARY KEY (
        "move_id"
     )
);

CREATE TABLE "pokeMove" (
    "poke_id" int   NOT NULL,
    "move_id" int   NOT NULL,
    CONSTRAINT "pk_pokeMove" PRIMARY KEY (
        "poke_id","move_id"
     )
);

CREATE TABLE "pokeEvo" (
    "evolution_chain" int   NOT NULL,
    "stage_1" string   NOT NULL,
    "stage_2" string   NOT NULL,
    "stage_3" string   NOT NULL,
    CONSTRAINT "pk_pokeEvo" PRIMARY KEY (
        "evolution_chain"
     )
);

ALTER TABLE "Pokemon" ADD CONSTRAINT "fk_Pokemon_poke_id" FOREIGN KEY("poke_id")
REFERENCES "pokeMove" ("poke_id");

ALTER TABLE "Pokemon" ADD CONSTRAINT "fk_Pokemon_type" FOREIGN KEY("type")
REFERENCES "Type" ("type_name");

ALTER TABLE "Pokemon" ADD CONSTRAINT "fk_Pokemon_evolution_chain" FOREIGN KEY("evolution_chain")
REFERENCES "pokeEvo" ("evolution_chain");

ALTER TABLE "Type" ADD CONSTRAINT "fk_Type_type_name" FOREIGN KEY("type_name")
REFERENCES "Pokemon" ("second_type");

ALTER TABLE "pokeAbility" ADD CONSTRAINT "fk_pokeAbility_poke_id" FOREIGN KEY("poke_id")
REFERENCES "Pokemon" ("poke_id");

ALTER TABLE "pokeAbility" ADD CONSTRAINT "fk_pokeAbility_ability_id" FOREIGN KEY("ability_id")
REFERENCES "Ability" ("ability_id");

ALTER TABLE "pokeGame" ADD CONSTRAINT "fk_pokeGame_poke_id" FOREIGN KEY("poke_id")
REFERENCES "Pokemon" ("poke_id");

ALTER TABLE "pokeGame" ADD CONSTRAINT "fk_pokeGame_game_id" FOREIGN KEY("game_id")
REFERENCES "Game" ("game_id");

ALTER TABLE "pokeMove" ADD CONSTRAINT "fk_pokeMove_move_id" FOREIGN KEY("move_id")
REFERENCES "Moves" ("move_id");

CREATE INDEX "idx_Pokemon_poke_name"
ON "Pokemon" ("poke_name");

CREATE INDEX "idx_Ability_ability_name"
ON "Ability" ("ability_name");

CREATE INDEX "idx_Game_game_name"
ON "Game" ("game_name");

CREATE INDEX "idx_Moves_move_name"
ON "Moves" ("move_name");

