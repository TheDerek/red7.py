BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "game" (
    "id" INTEGER NOT NULL UNIQUE,
    "token" TEXT NOT NULL UNIQUE,
    "current_position" INTEGER NOT NULL,
    "deck" TEXT NOT NULL,
    "canvas" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "player" (
    "id" INTEGER NOT NULL UNIQUE,
    "token" TEXT NOT NULL UNIQUE,
    "game_id" INTEGER NOT NULL,
    "position" INTEGER NOT NULL,
    "hand" TEXT NOT NULL,
    "palette" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    UNIQUE("position","game_id"),
    FOREIGN KEY("game_id") REFERENCES "game"("id")
);
COMMIT;
